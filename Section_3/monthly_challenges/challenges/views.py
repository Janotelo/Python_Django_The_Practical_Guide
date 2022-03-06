from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january" : "Eat no meat for the entire month!",
    "february" : "Walk for at least 20 minutes every day!",
    "march" : "Learn Django for at least 20 minutes every day!",
    "april" : "Mommy's birth month",
    "may" : "Papu's birth month",
    "june" : "JB's birth month",
    "july" : "This month is remembered",
    "august" : "Kathryn's birth month",
    "september" : "Jimbi's birth month",
    "october" : "My birth month",
    "november" : "Jerricho's birth month",
    "december" : "Christmas"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys()) #Getting the keys of the dictionary and using it as a list.
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/<str:month>
    return HttpResponseRedirect(redirect_path) #Redirect

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")