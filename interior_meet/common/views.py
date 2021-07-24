from django.shortcuts import render

# Create your views here.
def landing_page(req):
    return render(req, 'home_page.html')