from django.shortcuts import render
from django.views import View
# view class to handle requests

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect

from .models import Cephalopod, Species, Animal

from django.http import HttpResponse 
# a class to handle sending a type of response

# Create your views here.

# these are basic views that can't use templates
# class Home(View):

#     # this method will be ran when dealing with a GET request
#     def get(self, request):
#         # generic response
#         # similar to response.send()
#         return HttpResponse("ShrimpyHouse")
    
# class About(View):

#     def get(self, request):
#         return HttpResponse("ViewScreen")
    
# home page

class SeaAnimals(TemplateView):

    template_name = 'seaanimals.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["seaanimals"] = Species.objects.all()
        return context

# class ShrimpHome(TemplateView):

#     template_name = 'view.html'

# class CephaloHome(TemplateView):

#     template_name = 'cephalohome.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         name = self.request.GET.get("name")
#         if name != None:
#             context["cephalopods"] = Cephalopod.objects.filter(name__icontains=name)
#             context["header"] = f"Searching for {name}"
#         else:
#             context["cephalopods"] = Cephalopod.objects.all()
#             context["header"] = 'Cephalopods'

#         return context

# # index view
# class ViewCephalopod:

#     def __init__(self, name, image, description):
#         self.name = name
#         self.image = image
#         self.description = description

# class CreateCephalopod(CreateView):
#     model = Cephalopod
#     fields = ['name', 'image', 'description', 'animal']
#     template_name = 'create_cephalopod.html'

#     def get_success_url(self):
#         return reverse("cephalopod_detail", kwargs={"pk":self.object.pk})

# class CephalopodDetail(DetailView):
#     model = Cephalopod
#     template_name = "cephalopod_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cephalopods = Cephalopod.objects.all()
#         print(cephalopods)
#         # context["cephalopod"] = Cephalopod.objects.all()
#         return context
    
# class UpdateCephalopod(UpdateView):
#     model = Cephalopod
#     fields = ['name', 'image', 'description']
#     template_name = "cephalopod_update.html"
    
#     def get_success_url(self):
#         return reverse("cephalopod_detail", kwargs={"pk":self.object.pk})
    
class UpdateAnimal(UpdateView):
    model = Animal
    fields = ['name', 'image', 'description']
    template_name = "animal_update.html"
    success_url = '/'
    

# class CephalopodDeleteConfirmation(DeleteView):
#     model = Cephalopod
#     template_name = 'cephalopod_delete.html'
#     success_url = '/cephalopods/'

class AnimalDeleteConfirmation(DeleteView):
    model = Animal
    template_name = 'animal_delete.html'
    success_url = '/'

class SpeciesDeleteConfirmation(DeleteView):
    model = Species
    template_name = 'species_delete.html'
    success_url = '/'

class CreateSeaAnimal(CreateView):
    model = Species
    fields = ['name', 'image']
    template_name = 'create_seaanimal.html'
    success_url = '/'

class SeaAnimalDetails(DetailView):
    model = Species
    template_name = "seaanimal_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seaanimals'] = Species.objects.all()
        return context
    
class CreateAnimal(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        description = request.POST.get("description")
        species = Species.objects.get(pk=pk)
        Animal.objects.create(name=name, image=image, description=description, species=species)
        return redirect('seaanimal_detail', pk=pk)