from django.db import models
from django.utils.html import mark_safe




class Theme(models.Model):
    nom = models.CharField(max_length=50,blank=False,primary_key=True )
    description= models.TextField(blank=False)
    couverture=models.ImageField(upload_to ='ThemeImages/',blank=False)
    def __str__(self):
        return self.nom
    @property
    def couverture_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.couverture.url,))
    





class Projet(models.Model):
    nom = models.CharField(max_length=50,primary_key=True)
    description= models.TextField()
    couverture=models.ImageField(upload_to ='ProjectImages/',blank=False)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE,blank=False)
    def __str__(self):
        return self.nom
    @property
    def couverture_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.couverture.url,))






class ThingPriority(models.IntegerChoices):
    LOW = 0, 'Low'
    NORMAL = 1, 'Normal'
    HIGH = 2, 'High'


class Image(models.Model):
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE,blank=False)
    image =models.ImageField(blank=False)
    priorite=models.IntegerField(default=ThingPriority.LOW,choices=ThingPriority.choices)
    @property
    def image_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.image.url,))








class Video(models.Model):
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE,blank=False)
    url=models.TextField(blank=False)
    def __str__(self):
        return "project video"

    @property
    def video_preview(self):
        return mark_safe('{url}'.format(url=self.url,))

        







class Personne(models.Model):
    nom = models.CharField(max_length=50,blank=False)
    prenom = models.CharField(max_length=50,blank=False)
    image =models.ImageField(upload_to ='Images/PersonneImages')
    description=models.TextField(blank=False)
    def __str__(self):
        return self.prenom

    @property
    def image_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.image.url,))
    






class Information(models.Model):
    telephone=models.CharField(max_length=12,blank=False)
    email=models.EmailField(blank=False)
    adresse=models.CharField(max_length=200,blank=False)
    def __str__(self):
        return self.email





