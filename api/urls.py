from django.urls import path


from .Views.ThemeView import*
from .Views.ProjetView import*
from .Views.ImageView import*
from .Views.VideoView import*
from .Views.PersonneView import*
from .Views.InformationView import*


urlpatterns = [

#theme paths
path('theme/',Theme_list),
path('themeById/',Theme_detail),



#project paths
path('projet/',ProjetByTheme),
path('projetById/',ProjetById),




#image paths
path('image/',ImageByProject),


#video paths
path('video/',VideoByProject),



#personne paths
path('personne/',Personne_List),




#information paths
path('information/',Information_List),
]



