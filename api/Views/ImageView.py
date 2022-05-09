from ..serializers import ImageSerializer
from ..models import Image
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def ImageByProject(request):


    if request.method == 'POST':
        images = Image.objects.filter(projet=request.POST.get("projet"))
        serializer = ImageSerializer(images,many=True)
        res={"images":[]}
        for image in serializer.data:
             if image["priorite"]==2:
                 url=request.META['HTTP_HOST']+image["image"] 


                 res["images"].append({"id": image["id"],
                "projet":image["projet"],
                "priorite":image["priorite"],
                "image":url})


        for image in serializer.data:
             if image["priorite"]==1:
                 url=request.META['HTTP_HOST']+image["image"] 


                 res["images"].append({"id": image["id"],
                "projet":image["projet"],
                "priorite":image["priorite"],
                "image":url})



        for image in serializer.data:
             if image["priorite"]==0:
                 url=request.META['HTTP_HOST']+image["image"] 


                 res["images"].append({"id": image["id"],
                "projet":image["projet"],
                "priorite":image["priorite"],
                "image":url})


             
        
        return JsonResponse(res, safe=False)






