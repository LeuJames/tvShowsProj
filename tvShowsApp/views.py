from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages
from datetime import datetime


def index(request):
    return redirect('/shows')

def new(request):
    return render(request, 'newShow.html')

def shows(request):
    context = {
        'shows' : Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def create(request):
    errors = Show.objects.new_show_validator(request.POST)
    if len(errors) > 0:
        request.session['show'] = request.POST
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        if 'show' in request.session:
            del request.session['show']
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
        id = Show.objects.last().id
        print(id)
        return redirect(f'/shows/{id}')

def details(request, id):
    context = {
        'show' : Show.objects.get(id=id),
    }
    return render(request, 'showDetails.html', context)

def edit(request, id):
    context = {
        'show' : Show.objects.get(id=id),
    }
    return render(request, 'editShow.html', context)

def update(request, id):
    errors = Show.objects.update_show_validator(request.POST)
    if len(errors) > 0:
        request.session['showToUpdate'] = request.POST
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        print(request.session)
        if 'showToUpdate' in request.session:
            del request.session['showToUpdate']
        showToUpdate = Show.objects.get(id=id)
        showToUpdate.title = request.POST['title']
        showToUpdate.network = request.POST['network']
        showToUpdate.release_date = request.POST['release_date']
        showToUpdate.desc = request.POST['desc']
        showToUpdate.save()
        return redirect(f'/shows/{id}')

def delete(request, id):
    showToDelete = Show.objects.get(id=id)
    showToDelete.delete()
    return redirect('/shows')