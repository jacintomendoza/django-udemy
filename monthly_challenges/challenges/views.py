from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "No caffeine for 28 days",
    "march": "Read one book a week",
    "april": "Run 5 miles every week",
    "may": "No social media for 31 days",
    "june": "Meditate for 10 minutes daily",
    "july": "Drink 8 glasses of water a day",
    "august": "Wake up at 5 AM every day",
    "september": "Learn a new skill or hobby",
    "october": "Take a 30-minute walk daily",
    "november": "Do 50 push-ups every day",
    "december": None
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })



def monthly_challenge_by_number( request, month ):
    months = list(monthly_challenges.keys()) # keys retrieves first col

    if month > len(months):
        return HttpResponseNotFound("Invalid month") 

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/args
    return HttpResponseRedirect(redirect_path)



def monthly_challenge( request, month ): # month = 1 = janurary
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404() # will look for 404 file (put 404 in root templates)