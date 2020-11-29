from django.urls import path, include
from .views import some, readBlood, createBlood, editBlood, deleteBlood
urlpatterns = [
    path('', some, name="some"),
    path('readblood/', readBlood, name="readblood"),
    path('createblood/', createBlood, name="createblood"),
    path('editblood/<int:id>/', editBlood, name="editblood"),
    path("deleteblood/<int:id>/", deleteBlood, name="deleteBlood")
]