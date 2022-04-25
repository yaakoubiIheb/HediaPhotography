from ..serializers import InformationSerializer
from ..models import Information
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def Information_List(request):


    if request.method == 'GET':
        informations = Information.objects.all()
        serializer = InformationSerializer(informations,many=True)
        
        return JsonResponse(serializer.data, safe=False)