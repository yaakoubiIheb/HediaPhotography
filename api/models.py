from django.db import models
from django.utils.html import mark_safe



#the theme model
class Theme(models.Model):
    nom = models.CharField(max_length=50,blank=False)
    description= models.TextField(blank=False)
    couverture=models.ImageField(upload_to ='ThemeImages/',blank=False)
    def __str__(self):
        return self.nom
#this is for displaying the image as a field in django admin
    @property
    def couverture_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.couverture.url,))
    





#the project model
class Projet(models.Model):
    nom = models.CharField(max_length=50,blank=False)
    description= models.TextField()
    couverture=models.ImageField(upload_to ='ProjectImages/',blank=False)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE,blank=False)
    def __str__(self):
        return self.nom
    @property
    def couverture_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.couverture.url,))












#the image model
class Image(models.Model):
    STATUS = (
      (0,  ('LOW')),
      (1, ('MEDUIM')),
      (2, ('HIGH')),
   )
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE,blank=False)
    image =models.ImageField(blank=False,upload_to ='Images/')
    priorite=models.IntegerField(default=1,choices=STATUS)
    @property
    def image_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.image.url,))







#this is the video model
class Video(models.Model):
    projet = models.ForeignKey(Projet,on_delete=models.CASCADE,blank=False)
    url=models.TextField(blank=False)
    def __str__(self):
        return "project video"


#this is for displaying the youtube video in django admin
    @property
    def video_preview(self):
        #this is for giving the position of a string in another string
        def find_str(s, char):
            index = 0

            if char in s:
                c = char[0]
                for ch in s:
                    if ch == c:
                        if s[index:index+len(char)] == char:
                            return index

                    index += 1

            return -1

        pos1=find_str(self.url,"width")

        pos2=find_str(self.url,"height")
        pos3=find_str(self.url,"src")
        #this is for replacing the default width and height by 800*600 to adapt to the window width
        width = self.url[self.url.find('width'):pos2-1]
        print(len(width))
       # width=self.url[pos1:pos2-1]
        height=self.url[pos2:pos3]

        res=self.url.replace(width,'width="100%"')
        #res=res.replace(height,'height="600"')



        return mark_safe('{url}'.format(url=res,))

        








#the personne model
class Personne(models.Model):
    nom = models.CharField(max_length=50,blank=False)
    prenom = models.CharField(max_length=50,blank=False)
    image =models.ImageField(upload_to ='PersonneImages/')
    description=models.TextField(blank=False)
    def __str__(self):
        return self.prenom

    @property
    def image_preview(self):
        return mark_safe('<img src="{}" width=300 height=300 />'.format(self.image.url,))
    







#the information model
class Information(models.Model):
    telephone=models.CharField(max_length=12,blank=False)
    email=models.EmailField(blank=False)
    adresse=models.CharField(max_length=200,blank=False)
    instagram=models.CharField(max_length=200,blank=True)
    facebook=models.CharField(max_length=200,blank=True)
    linkedIn=models.CharField(max_length=200,blank=True)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.email








