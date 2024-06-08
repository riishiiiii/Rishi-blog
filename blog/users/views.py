from django.contrib.auth.decorators import login_required
import random
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from .models import profileModel
from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.mail import send_mail

# Create your views here.


def signup(request: object) -> object:
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.mobile = request.mobile
            instance.save()
            return redirect("user-login")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "users/signup.html", context)


@login_required
def profile(request: object) -> object:
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST or None,
            request.FILES or None,
            instance=request.user.profilemodel,
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("/profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "users/profile.html", context)


def register(request: object) -> object:
    form = SignupForm(request.POST)
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            username = request.POST.get("username")
            check_user = User.objects.filter(email=email).first()
            check_profile = profileModel.objects.filter(mobile=mobile).first()
            if check_user or check_profile:
                context = {
                    "message": "User already exists",
                    "class": "danger",
                    "form": form,
                }
                return render(request, "users/signup.html", context)
            user = User(username=username, email=email)
            user.save()
            otp = str(random.randint(1000, 9999))
            profile = profileModel(
                user=user,
                mobile=mobile,
                otp=otp,
                exp_time=timezone.now() + datetime.timedelta(seconds=60),
            )
            profile.save()
            request.session["mobile"] = mobile
            return redirect("user-login")
    context = {"form": form}
    return render(request, "users/signup.html", context)


def login_attempt(request: object) -> object:
    if request.method == "POST":
        email = request.POST.get("email")

        user = User.objects.filter(email=email).first()
        profile = profileModel.objects.filter(user=user).first()
        if user is None:
            context = {"message": "User not found", "class": "danger"}
            return render(request, "users/login.html", context)
        otp = str(random.randint(1000, 9999))
        profile.otp = otp
        profile.exp_time = timezone.now() + datetime.timedelta(seconds=60)
        profile.save()
        send_mail(
            subject="YOUR OTP",
            message=f"Here is your otp: {otp}. This will expire in 5 minutes",
            from_email="rishu9510@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )
        request.session["email"] = email
        return redirect("user-login-otp")
    return render(request, "users/login.html")


def login_otp(request: object) -> object:
    email = request.session["email"]
    context = {"mobile": email}
    if request.method == "POST":
        otp = request.POST.get("otp")
        user = User.objects.filter(email=email).first()
        profile = profileModel.objects.filter(user=user).first()
        if otp == "":
            context = {"message": "Enter valid OTP", "class": "danger", "mobile": email}
            return render(request, "users/login_otp.html", context)
        if otp == profile.otp and profile.exp_time > timezone.now():
            user = User.objects.get(id=profile.user.id)
            login(request, user)
            profile.otp = None
            profile.save()
            return redirect("blog-index")
        if otp != profile.otp:
            context = {"message": "Wrong OTP", "class": "danger", "mobile": email}
            return render(request, "users/login_otp.html", context)
        else:
            profile.otp = None
            profile.save()
            context = {"message": "expired OTP", "class": "danger", "mobile": email}
            return render(request, "users/login_otp.html", context)

    return render(request, "users/login_otp.html", context)


def resend_otp(request: object) -> object:
    email = request.session["email"]
    user = User.objects.filter(email=email).first()
    profile = profileModel.objects.filter(user=user).first()
    if user is None:
        context = {"message": "User not found", "class": "danger"}
        return render(request, "users/login.html", context)
    otp = str(random.randint(1000, 9999))
    profile.otp = otp
    profile.exp_time = timezone.now() + datetime.timedelta(seconds=60)
    profile.save()
    send_mail(
        "your otp",
        f"Here is your otp: {otp}.",
        "rishu9510@gmail.com",
        [email],
        fail_silently=False,
    )
    request.session["email"] = email
    return redirect("user-login-otp")
