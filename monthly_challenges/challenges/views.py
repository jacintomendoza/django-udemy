from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": "Write in a journal every day"
}

# Create your views here.

def index_whatever(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalize_month = month.capitalize() # ex: janurary -> Janurary
        month_path = reverse("month-challenge", args=[month])
        print(month_path) # ex: challanges/december
        list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"

    # After for loop: <li><a href="...">January</a></li><li><a href="...">February</a></li...>

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



def monthly_challenge_by_number( request, month ):
    months = list(monthly_challenges.keys()) # keys retrieves first col

    if month > len(months):
        return HttpResponseNotFound("Invalid month") 

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/args
    return HttpResponseRedirect(redirect_path)



def monthly_challenge( request, month ):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Error this month DNE!")