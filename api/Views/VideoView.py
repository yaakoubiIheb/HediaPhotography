from ..serializers import ViedoSerializer
from ..models import Video
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def VideoByProject(request, pk):


    if request.method == 'GET':
        videos = Video.objects.filter(projet=pk)
        serializer = ViedoSerializer(videos,many=True)
        
        return JsonResponse(serializer.data, safe=False)






