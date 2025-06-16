from django.shortcuts import render, redirect
from .forms import LandingDataForm
from .models import LandingData

def landing_view(request):
    if request.method == "POST":
        form = LandingDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("landing_result")
    else:
        form = LandingDataForm()
    return render(request, "landing/landing_form.html", {"form": form})

def landing_result_view(request):
    data = LandingData.objects.last()
    return render(request, "landing/landing_result.html", {"data": data})
