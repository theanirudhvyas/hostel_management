from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from hostel.forms import UserForm, DiffForm, StudentForm, RoomForm
from hostel.models import Diff, Student, Room, Change, Swap
from django.contrib.auth.models import User

@login_required
def index(request):
    diff = Diff.objects.get(user = request.user)
    return render(request, 'hostel/index.html', {'diff': diff, })

# Create your views here.
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and DiffForm.
        user_form = UserForm(data=request.POST)
        diff_form = DiffForm(data=request.POST)
        student_form = StudentForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and diff_form.is_valid() and student_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            diff = diff_form.save(commit=False)
            diff.user = user

            # Now we save the Diff model instance.
            diff.save()

            student = student_form.save(commit=False)
            student.roll_no = user
            student.save()


            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, diff_form.errors, student_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        diff_form = DiffForm()
        student_form = StudentForm()

    # Render the template depending on the context.
    return render(request,
            'hostel/register.html',
            {'user_form': user_form, 'diff_form': diff_form, 'student_form': student_form, 'registered': registered})


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/hostel/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponseRedirect("/hostel/login")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request,'hostel/login.html', {})

@login_required
def student_details(request):
    student = Student.objects.get(roll_no = request.user)
    room = Room.objects.get(room_no = student.room.room_no)
    return render(request, 'hostel/student_details.html', {'student': student,'room1': room, })


def allocate(request):

    if request.method == 'POST':

        roll_no = request.POST['roll_no']
        room_no = request.POST['room_no']

        student_roll_no = User.objects.get(username=roll_no)

        student = Student.objects.get(roll_no=student_roll_no)

        #try:
        room_new = Room.objects.get(room_no=room_no)
       # except:
        #    HttpResponse('Room does not exist! Try some Valid entry.')
# Add exception condition for case where room does not exist
        if room_new.vacancy:
            student.room = room_new
            room_new.vacancy -= 1
            student.save()
            room_new.save()
            return HttpResponseRedirect('/hostel/')
        else:
            html = "<html><body>Sorry, The room is Full.</body></html>"
            HttpResponse(html)

    else:
        return render(request, 'hostel/student_allocate.html', {})


def swap(request):

    if request.method == 'POST':

        roll_no1 = request.POST['roll_no1']
       # room_no1 = request.POST['room_no1']

        roll_no2 = request.POST['roll_no2']
        #room_no2 = request.POST['room_no2']

        user1 = User.objects.get(username=roll_no1)
        student1 = Student.objects.get(roll_no=user1)

        user2 = User.objects.get(username=roll_no2)
        student2 = Student.objects.get(roll_no=user2)

        room1 = student1.room
        room2 = student2.room

        student1.room = room2
        student2.room = room1

        student1.save()
        student2.save()

        html = '<html><body> Room Swapped Successfully</body><html>'

        return HttpResponse(html)


    else:
        return render(request, 'hostel/swap.html', {})


def change(request):

    if request.method == 'POST':

        roll_no = request.POST['roll_no']

        room_no = request.POST['room_no']

        user = User.objects.get(username=roll_no)
        student = Student.objects.get(roll_no=user)

        room_new = Room.objects.get(room_no=room_no)

       # room_old = Student.room

        if room_new.vacancy:
            student.room.vacancy += 1
            student.room = room_new
            room_new.vacancy -= 1
            student.room.save()
            student.save()
            room_new.save()
            #room_old.save()
            return HttpResponseRedirect('/hostel/')
        else:
            html = "<html><body>Sorry, The new room is Full.</body></html>"
            return HttpResponse(html)


    else:
        return render(request, 'hostel/change.html', {})


def change_request(request):
    #address duplicate requests

    if request.method == 'POST':

        reason = request.POST['reason']
        flag = request.POST['flag']
        student = Student.objects.get(roll_no=request.user)

        if flag:
            request = Change.objects.create(student=student, reason=reason)
            #request.save()

        else:
            return HttpResponseRedirect('/hostel/')

        return HttpResponse('<html><body> Success! </body></html>')

    else:
        return render(request, 'hostel/change_req.html', {})


def swap_request(request):
    #address duplicate requests

    if request.method == 'POST':

        stud2 = request.POST['stud2']
        flag = request.POST['flag']
        reason = request.POST['reason']
        user = User.objects.get(username=stud2)
        student2 = Student.objects.get(roll_no=user)
        student1= Student.objects.get(roll_no = request.user)

        if flag and student2.room.room_no:
            Swap.objects.create(student1 = student1, student2=student2, reason=reason )

        else:
            return HttpResponseRedirect('/hostel/')

        return HttpResponse('<html><body> Success! </body></html>')

    else:
        return render(request, 'hostel/swap_request.html', {})


def swap(request):
    #works for only one swap request, have to make it work for more or have different pages for all requests

    req = Swap.objects.get(id=1)
    reqs=Swap.objects.all()

    stud1=req.student1
    user=User.objects.get(username=req.student2)
    stud2=Student.objects.get(roll_no=user)

    if request.method == 'POST':

        if '_accept' in request.POST:
            room = stud1.room
            stud1.room=stud2.room
            stud2.room=room
            stud1.save()
            stud2.save()
            request.delete()

        elif '_decline' in request.POST:
            request.delete()


    else:
        return render(request, 'hostel/swap.html', {'requests':reqs, })


def swap_ack(request):
    #works for only one swap request, have to make it work for more or have different pages for all requests

    req = Swap.objects.get(student2=request.user.username)

    if request.method == 'POST':

        if '_accept' in request.POST:
            req.accept = 1
            req.save()

        if '_decline' in request.POST:
            req.delete()
        return HttpResponseRedirect('/hostel/')
    else:
        return render(request, 'hostel/swap_ack.html', {'request':req, })















