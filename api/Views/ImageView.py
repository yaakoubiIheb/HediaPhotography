from ..serializers import ImageSerializer
from ..models import Image
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def ImageByProject(request, pk):


    if request.method == 'GET':
        images = Image.objects.filter(projet=pk)
        serializer = ImageSerializer(images,many=True)
        res={"images":[]}
        for image in serializer.data:
             url=request.META['HTTP_HOST']+image["image"] 


             res["images"].append({"id": image["id"],
             "projet":image["projet"],
             "priorite":image["priorite"],
            "image":url})

        
        return JsonResponse(res, safe=False)






