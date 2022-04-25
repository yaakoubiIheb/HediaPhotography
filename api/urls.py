from django.urls import path
from .Views.ThemeView import*
from .Views.ProjetView import*


urlpatterns = [

#theme paths
path('theme/',Theme_list),
path('theme/<slug:pk>/',Theme_detail),



#project paths
path('projet/<slug:pk>/',ProjetByTheme),
]

