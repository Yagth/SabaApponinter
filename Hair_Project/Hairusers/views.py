import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignupForm, UserUpdateForm, HostPageUpdateForm, CustomerPageUpdateForm
from Hairapp.models import HairSalon, Reservations, Services
from .models import UserPage, YourReserv


def signup(request):

    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You are now able to login')
            messages.info(
                request, 'After logging in, update your profile with more information to make your account iligible')
            return redirect('login')

    else:
        form = UserSignupForm()
    context = {
        'form': form
    }
    return render(request, 'tempreg.html', context)


@login_required
def User_page(request):

    if request.method == "POST":
        prev_sal = request.user.userpage.hairsalon
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if request.user.userpage.status == 'HOST':
            hp_form = HostPageUpdateForm(
                request.POST, request.FILES, instance=request.user.userpage)
            if u_form.is_valid() and hp_form.is_valid():
                u_form.save()
                hp_form.save()
                salon = hp_form.cleaned_data.get('hairsalon')
                messages.success(
                    request, f'Your account has been updated successfully!')
                if not salon == prev_sal:
                    messages.success(
                        request, f'{request.user.userpage.hairsalon} has been created successfully! We will add it to customers\'s list after we contact you about the details')
                return redirect('Userhome')
        else:
            cp_form = CustomerPageUpdateForm(
                request.POST, request.FILES, instance=request.user.userpage)
            if u_form.is_valid() and cp_form.is_valid():
                u_form.save()
                cp_form.save()
                status = cp_form.cleaned_data.get('status')
                messages.success(
                    request, f'Your account has been updated successfully!')
                if status == 'HOST':
                    return redirect('UserPage')
                else:
                    return redirect('Userhome')
    else:
        u_form = UserUpdateForm(instance=request.user)
        if request.user.userpage.status == 'HOST':
            hp_form = HostPageUpdateForm(instance=request.user.userpage)
        else:
            cp_form = CustomerPageUpdateForm(instance=request.user.userpage)

    if request.user.userpage.status == 'HOST':
        context = {
            'u_form': u_form, 'hp_form': hp_form
        }
    else:
        context = {
            'u_form': u_form, 'cp_form': cp_form,
        'salons': HairSalon.objects.all()
        }
    return render(request, 'Userpage.html', context)

def reservation(request):
    user = request.user
    salon = HairSalon.pk
    reserve = YourReserv.objects.create(user = request.user, salon = salon, price = Services.request )

    #     username = request.POST['username']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']
    #     phone_number = request.POST['number']
    #     status = request.POST['status']
    #     email = request.POST['email']

    #     if User.objects.filter(username = username).exists():
    #         messages.info(request, 'Username already userd')
    #         return redirect('signup')
    #     elif email != '':
    #         if User.objects.filter(email = email).exists():
    #             messages.info(request, 'Email already userd')
    #             return redirect(request, 'signup')
    #     elif len(password)<8:
    #         messages.info(request, 'Password too short')
    #         return redirect('signup')
    #     elif password != password2:
    #         messages.info(request, "Passwords don't match")
    #         return redirect('signup')
    #     else :
    #         messages.success(request,f'Account successfuly created for {username}! login below!')
    #         user = User.objects.create_user(username = username, password = password, email = email)
    #         user.save()
    #         return redirect('login')

    # else:
    #     return render(request, 'signup.html')
