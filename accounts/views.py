from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import CustomUser, GuideProfile


# -----------------------------
# Registration
# -----------------------------
def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            role = form.cleaned_data.get("role")

            user.role = role

            # -----------------------------
            # Normal User Registration
            # -----------------------------
            if role == CustomUser.Roles.USER:

                user.is_approved = True
                user.approval_status = (
                    CustomUser.ApprovalStatus.APPROVED
                )

                user.save()

                login(request, user)

                messages.success(
                    request,
                    "Registration successful!"
                )

                return redirect("home")

            # -----------------------------
            # Guide Registration
            # -----------------------------
            elif role == CustomUser.Roles.GUIDE:

                user.is_approved = False
                user.approval_status = (
                    CustomUser.ApprovalStatus.PENDING
                )

                user.save()

                guide_profile = GuideProfile.objects.create(
                    user=user,
                    qualification=form.cleaned_data.get(
                        "qualification"
                    ),
                    experience_years=form.cleaned_data.get(
                        "experience_years"
                    ) or 0,
                    bio=form.cleaned_data.get(
                        "bio"
                    ),
                    languages_known=form.cleaned_data.get(
                        "languages_known"
                    ),
                    linkedin_url=form.cleaned_data.get(
                        "linkedin_url"
                    )
                )

                guide_profile.expertise.set(
                    form.cleaned_data.get("expertise")
                )

                messages.success(
                    request,
                    "Guide application submitted successfully. "
                    "Please wait for admin approval."
                )

                return redirect("login")

        else:
            messages.error(
                request,
                "Please correct the errors below."
            )

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


# -----------------------------
# Login
# -----------------------------under review."

def user_login(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            if user.role == "GUIDE" and not user.is_approved:
                messages.error(
                    request,
                    "Your guide account is waiting for admin approval."
                )
                return redirect("login")

            login(request, user)

            messages.success(
                request,
                "Login Successful"
            )

            if user.role == "ADMIN":
                return redirect("/admin/")

            elif user.role == "GUIDE":
                return redirect("guide_dashboard")

            return redirect("home")

        else:
            messages.error(
                request,
                "Invalid email or password"
            )

    return render(
        request,
        "accounts/login.html"
    )
# -----------------------------
# Logout
# -----------------------------
def user_logout(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("home")