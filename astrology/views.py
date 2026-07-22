from django.shortcuts import render, redirect, get_object_or_404
from . models import AstrologyQuestion, BirthChart
# Create your views here.

def astrology_home(request):
    popular_questions=AstrologyQuestion.objects.filter(
        is_active=True
    )[:5]

    context={
        "popular_questions": popular_questions
    }

    return render(request, "astrology/home.html", context)

def generate_kundali(request):

    if request.method == "POST":

        chart = BirthChart.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=request.POST.get('full_name'),
            date_of_birth=request.POST.get('date_of_birth'),
            time_of_birth=request.POST.get('time_of_birth'),
            place_of_birth=request.POST.get('place_of_birth'),
            gender=request.POST.get('gender')
        )

        return redirect(
            'kundali_result',
            chart_id=chart.id
        )

    return render(
        request,
        'astrology/generate_kundali.html'
    )


def kundali_result(request, chart_id):

    chart = get_object_or_404(
        BirthChart,
        id=chart_id
    )

    context = {
        'chart': chart
    }

    return render(
        request,
        'astrology/kundali_result.html',
        context
    )

#Today's Panchang
from django.shortcuts import render
from datetime import date

def today_panchang(request):

    context = {
        'today': date.today(),
        'tithi': 'Shukla Paksha Panchami',
        'nakshatra': 'Rohini',
        'yoga': 'Siddhi',
        'karana': 'Bava',
        'sunrise': '05:28 AM',
        'sunset': '07:18 PM',
        'rahu_kaal': '10:30 AM - 12:00 PM',
        'abhijit_muhurat': '11:55 AM - 12:45 PM',
    }

    return render(
        request,
        'astrology/panchang.html',
        context
    )

from django.shortcuts import render
#Kundali Matching
def kundali_matching(request):

    if request.method == "POST":

        context = {
            "score": 28,
            "total_score": 36,
            "compatibility": "Excellent Match",
            "communication": "Very Good",
            "emotional_bond": "Excellent",
            "financial_compatibility": "Good",
            "marriage_outlook": "Highly Favorable",
            "show_result": True,
        }

        return render(
            request,
            "astrology/kundali_matching.html",
            context
        )

    return render(
        request,
        "astrology/kundali_matching.html"
    )