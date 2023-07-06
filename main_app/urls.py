from django.urls import path
from . import views

# this is like app.use() in express
urlpatterns = [
    path('', views.SeaAnimals.as_view(), name="seaanimals"),
    # new paths here
    # path('shrimp/', views.ShrimpHome.as_view(), name="shrimphome"),
    # path('cephalopods/', views.CephaloHome.as_view(), name="cephalohome"),
    # path('cephalopods/add/', views.CreateCephalopod.as_view(), name="create_cephalopod"),
    # path('cephalopods/<int:pk>', views.CephalopodDetail.as_view(), name="cephalopod_detail"),
    # path('cephalopods/<int:pk>/update', views.UpdateCephalopod.as_view(), name="cephalopod_update"),
    # path('cephalopods/<int:pk>/delete', views.CephalopodDeleteConfirmation.as_view(), name="cephalopod_delete"),
    path('seaanimal/new/', views.CreateSeaAnimal.as_view(), name="create_seaanimal"),
    path('seaanimal/<int:pk>', views.SeaAnimalDetails.as_view(), name="seaanimal_detail"),
    path('seaanimal/<int:pk>/animal/new/', views.CreateAnimal.as_view(), name="create_animal"),
    path('seaanimal/<int:pk>/delete', views.AnimalDeleteConfirmation.as_view(), name="animal_delete"),
    path('seaanimal/<int:pk>/update', views.UpdateAnimal.as_view(), name="animal_update"),
    path('seaanimal/<int:pk>/speciesdelete', views.SpeciesDeleteConfirmation.as_view(), name="species_delete"),

]