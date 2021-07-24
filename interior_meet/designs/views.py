from django.shortcuts import render

from interior_meet.core.utils import get_designs


def list_designs(request):
    all_designs = get_designs()
    context = {
        'designs': all_designs,
    }
    return render(request, 'catalogue.html', context)


# temporary
def add_page(req):
    return render(req, 'add.html')