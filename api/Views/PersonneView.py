from ..serializers import PersonneSerializer
from ..models import Personne
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def Personne_List(request):


    if request.method == 'GET':
        personnes = Personne.objects.all()
        serializer = PersonneSerializer(personnes,many=True)
        
        return JsonResponse(serializer.data, safe=False)