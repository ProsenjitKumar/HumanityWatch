from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm, LoginForm, LastDonationChangeForm, DonorForm
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError



def home(request):
    return render(request, 'accounts/home.html')


@csrf_protect
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        #user.active = False
        if user is not None:
            # Is the account active? It could have been disabled.
            # user.is_active = False
            if user.is_active:
                login(request, user)
                return render(request, 'accounts/profile.html')
                #return HttpResponseRedirect("/profile/")
            else:
                return HttpResponse("You have to Wait for admin approval.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'accounts/pass_admin_approval_wrong.html')
    else:
        return render(request, 'accounts/login.html', context)


User = get_user_model()
@csrf_protect
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return render(request, 'accounts/register_success.html')
    return render(request, 'accounts/register.html', context)


@csrf_protect
def donor_page(request):
    form = DonorForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return render(request, 'donor_form_success.html')
    return render(request, 'donor_form.html', context)


@login_required
def profile(request):
    args = {"user": request.user }

    return render(request, 'accounts/profile.html', args)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


def contact_us(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def mission_vision(request):
    return render(request, 'mission_vision.html')


def organization(request):
    return render(request, 'organization.html')


def photo_gallery(request):
    return render(request, 'photo_gallery.html')


def available_donor(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            match = User.objects.filter(
                Q(full_name__startswith=search) |
                Q(email__icontains=search) |
                Q(blood__startswith=search) |
                Q(first_address__icontains=search)
            )
            if match:
                return render(request, 'available_donor.html', {"match": match})
            else:
                messages.error(request, "No result found")
        else:
            return HttpResponseRedirect('/')

    args = {
        "users": User.objects.all(),
    }
    return render(request, 'all_donor_list.html', args)


# def base(request):
#     return render(request, 'index.html')

def last_donation_date(request):
    if request.method == 'POST':
        form = LastDonationChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'accounts/blood_donation_update_siccess.html')
    else:
        form = LastDonationChangeForm(instance=request.user)
        context = {
            "form": form,
        }
        return render(request, 'accounts/last_donation_date.html', context)



#******************************************** Blood Group List Mehod **********************

def a_positive(request):

    match = User.objects.filter(blood__startswith='a+')
    if match:
        return render(request, 'blood_type/a_positive.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')


def a_negative(request):

    match = User.objects.filter(blood__startswith='a-')
    if match:
        return render(request, 'blood_type/a_negative.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')


def b_positive(request):

    match = User.objects.filter(blood__startswith='b+')
    if match:
        return render(request, 'blood_type/b_positive.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')


def b_negative(request):

    match = User.objects.filter(blood__startswith='b-')
    if match:
        return render(request, 'blood_type/b_negative.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')


def ab_positive(request):

    match = User.objects.filter(blood__startswith='ab+')
    if match:
        return render(request, 'blood_type/ab_positive.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')


def ab_negative(request):

    match = User.objects.filter(blood__startswith='ab-')
    if match:
        return render(request, 'blood_type/ab_negative.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')


def o_positive(request):

    match = User.objects.filter(blood__startswith='o+')
    if match:
        return render(request, 'blood_type/o+positive.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')


def o_negative(request):

    match = User.objects.filter(blood__startswith='o-')
    if match:
        return render(request, 'blood_type/o_negative.html', {"match": match})
    else:
        messages.error(request, "No result found")

    return render(request, 'blood_type/not_found.html')






