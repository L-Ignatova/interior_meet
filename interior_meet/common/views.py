from django.shortcuts import render


def landing_page(req):
    return render(req, 'home_page.html')