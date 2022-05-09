from ..serializers import ViedoSerializer
from ..models import Video
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def VideoByProject(request):


    if request.method == 'POST':
        videos = Video.objects.filter(projet=request.POST.get("projet"))
        serializer = ViedoSerializer(videos,many=True)
        
        return JsonResponse(serializer.data, safe=False)






