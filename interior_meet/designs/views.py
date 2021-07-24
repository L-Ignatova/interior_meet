from django.shortcuts import render


# temporary
def add_page(req):
    return render(req, 'add.html')