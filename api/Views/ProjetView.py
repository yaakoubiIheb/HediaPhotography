from ..serializers import ProjetSerializer
from ..models import Projet
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def ProjetByTheme(request, pk):


    if request.method == 'GET':
        projets = Projet.objects.filter(theme=pk)
        serializer = ProjetSerializer(projets,many=True)
        res={"projets":[]}
        for projet in serializer.data:
             url=request.META['HTTP_HOST']+projet["couverture"]   
             res["projets"].append({"nom": projet["nom"],
             "description":projet["description"],
             "theme":projet["theme"],
            "couverture":url})

        
        return JsonResponse(res, safe=False)





@csrf_exempt
def ProjetByName(request, pk):


    if request.method == 'GET':
        projets = Projet.objects.get(pk=pk)
        serializer = ProjetSerializer(projets)
        res={"projet":[]}
        
    
        url=request.META['HTTP_HOST']+serializer.data["couverture"]   
        res["projet"].append({"nom": serializer.data["nom"],
             "description":serializer.data["description"],
             "theme":serializer.data["theme"],
            "couverture":url})

        
        return JsonResponse(res, safe=False)






