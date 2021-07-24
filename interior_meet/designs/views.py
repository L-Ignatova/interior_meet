from django.shortcuts import render, redirect

from interior_meet.core.utils import get_designs
from interior_meet.designs.forms import CreateDesignForm, EditDesignForm
from interior_meet.designs.models import Design


def list_designs(request):
    all_designs = get_designs()
    category = request.GET.get('type')
    if category:
        all_designs = all_designs.filter(type=category)

    context = {
        'designs': all_designs,
    }
    return render(request, 'catalogue.html', context)


def create_design(request):
    if request.method == 'POST':
        form = CreateDesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all designs')
    else:
        form = CreateDesignForm()

    context = {
        'form': form,
    }

    return render(request, 'add.html', context)


def edit_design(request, pk):
    design = Design.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditDesignForm(request.POST, request.FILES, instance=design)
        if form.is_valid():
            form.save()
            return redirect('design details', pk)
    else:
        form = EditDesignForm(instance=design)

    context = {
        'form': form,
        'design': design,
    }

    return render(request, 'edit.html', context)


def design_details(request, pk):
    design = Design.objects.get(pk=pk)
    likes = design.like_set.count()

    context = {
        'design': design,
        'likes': likes,
    }
    return render(request, 'details.html', context)