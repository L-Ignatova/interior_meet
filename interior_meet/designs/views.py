from django.shortcuts import render

from interior_meet.core.utils import get_designs


def list_designs(request):
    all_designs = get_designs()
    category = request.GET.get('type')
    if category:
        all_designs = all_designs.filter(type=category)

    context = {
        'designs': all_designs,
    }
    return render(request, 'catalogue.html', context)

#
# def list_designs_by_category(request, category):
#     filtered_designs = get_designs().filter(type=category)
#     context = {
#         'designs': filtered_designs,
#     }
#     return render(request, 'catalogue.html', context)


# temporary
def add_page(req):
    return render(req, 'add.html')