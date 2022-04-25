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






