# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

from animals.models import Animals
from animals.forms import AnimalSelectionForm


def AnimalSelection(request, template_name='index.html'):
    title = "Animal Voting Form"
    form = AnimalSelectionForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['add_animal'] != '':
            name = form.cleaned_data['add_animal']
        else:
            name = form.cleaned_data['choose_animal']
        animal, created = Animals.objects.get_or_create(
            name=name,
        )
        if animal.votes > 0:
            animal.votes += 1
        else:
            animal.votes = 1
        animal.save()
        messages.add_message(
            request, messages.INFO,
            'You registered a vote for ' + animal.name + '!'
        )
    # get animal list
    animal_list = Animals.objects.all()
    return render_to_response(template_name, {
        'title': title,
        'form': form,
        'animal_list': animal_list
    }, RequestContext(request))
