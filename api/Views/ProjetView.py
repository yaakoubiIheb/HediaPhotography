
import json
from ..serializers import ProjetSerializer,ImageSerializer,ViedoSerializer
from ..models import Projet,Image,Video
from django.http import JsonResponse
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
        images = Image.objects.filter(projet=pk)
        imageSerializer = ImageSerializer(images,many=True)
        videos = Video.objects.filter(projet=pk)
        videoSerializer = ViedoSerializer(videos,many=True)



        res={"projet":[],
        "images":[],
        "videos":[]
        }

        
        for video in videoSerializer.data:
            
            res["videos"].append({"id": video["id"],
                "url":video["url"],
                })
        


        for image in imageSerializer.data:
             if image["priorite"]==2:
                 url=request.META['HTTP_HOST']+image["image"] 


                 res["images"].append({"id": image["id"],
                "projet":image["projet"],
                "priorite":image["priorite"],
                "image":url})


        for image in imageSerializer.data:
             if image["priorite"]==1:
                 url=request.META['HTTP_HOST']+image["image"] 


                 res["images"].append({"id": image["id"],
                "projet":image["projet"],
                "priorite":image["priorite"],
                "image":url})



        for image in imageSerializer.data:
             if image["priorite"]==0:
                 url=request.META['HTTP_HOST']+image["image"] 


                 res["images"].append({"id": image["id"],
                "projet":image["projet"],
                "priorite":image["priorite"],
                "image":url})

    
        url=request.META['HTTP_HOST']+serializer.data["couverture"]   
        res["projet"].append({"nom": serializer.data["nom"],
             "description":serializer.data["description"],
             "theme":serializer.data["theme"],
            "couverture":url})

        
     

        
        return JsonResponse(res, safe=False)






