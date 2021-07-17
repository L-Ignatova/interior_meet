from django.shortcuts import render


# temporary
def landing_page(req):
    return render(req, 'home_page.html')


# temporary
def add_page(req):
    return render(req, 'add.html')