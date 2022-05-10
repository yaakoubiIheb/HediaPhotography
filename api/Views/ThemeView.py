from ..serializers import ThemeSerializer
from ..models import Theme
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def Theme_list(request):

    if request.method == 'GET':
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        res={"themes":[]}
        for theme in serializer.data:
             url=request.META['HTTP_HOST']+theme["couverture"]   
             res["themes"].append({"id":theme['id'],
                 "nom": theme["nom"],
             "description":theme["description"],
            "couverture":url})

        
        return JsonResponse(res, safe=False)




@csrf_exempt
def Theme_detail(request):
  
    try:
        theme = Theme.objects.get(pk=request.POST.get('id'))

        
    except Theme.DoesNotExist:
        return HttpResponse("Theme not found",status=404)

    if request.method == 'POST':

        serializer = ThemeSerializer(theme)
        url=request.META['HTTP_HOST']+serializer.data["couverture"]
        return JsonResponse({"id":theme['id'],"nom": serializer.data["nom"],
             "description":serializer.data["description"],
            "couverture":url})




