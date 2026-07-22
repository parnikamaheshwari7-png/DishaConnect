from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required(login_url='login')
def my_profile(request):
    return render(request, 'dashboard/profile.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def guide_dashboard(request):

    if request.user.role != "GUIDE":
        return redirect("home")

    guide_profile = request.user.guide_profile

    context = {
        "guide_profile": guide_profile,
    }

    return render(
        request,
        "dashboard/guide_dashboard.html",
        context
    )