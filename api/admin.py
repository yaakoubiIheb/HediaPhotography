from dataclasses import fields
from django.contrib import admin
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth.models import Group








class CouvertureAdmin(admin.ModelAdmin):

    list_display=('nom','description',)
    list_display_links=('nom','description',)
    readonly_fields = ('couverture_preview',)

    def couverture_preview(self, obj):
        return obj.couverture_preview

    couverture_preview.short_description = 'image de couverture'
    couverture_preview.allow_tags = True




class ProjetAdmin(admin.ModelAdmin):

    list_display=('nom','description','theme')
    list_display_links=('nom','description','theme')
    list_filter=['theme']
    search_fields=['nom','theme__nom']
    readonly_fields = ('couverture_preview',)

    def couverture_preview(self, obj):
        return obj.couverture_preview

    couverture_preview.short_description = 'image de couverture'
    couverture_preview.allow_tags = True





class ImageAdmin(admin.ModelAdmin):

    list_display=('projet','image_preview','priorite',)
    list_display_links=('projet','image_preview','priorite',)
    search_fields=['projet__nom']
    readonly_fields = ('image_preview',)
    list_filter=['projet','priorite']

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'image'
    image_preview.allow_tags = True








class PersonneAdmin(admin.ModelAdmin):

    list_display=('nom','prenom','description',)
    list_display_links=('nom','prenom','description',)
    readonly_fields = ('image_preview',)
    

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'image'
    image_preview.allow_tags = True









class InformationAdmin(admin.ModelAdmin):

    list_display=('email','telephone','adresse','instagram','facebook','description',)
    list_display_links=('email','telephone','adresse','instagram','facebook','description',)








class VideoAdmin(admin.ModelAdmin):

    list_display=('projet','url',)
    list_display_links=('projet','url',)
    list_filter=['projet']
    search_fields=['url']
    readonly_fields = ('video_preview',)


    def video_preview(self, obj):
        return obj.video_preview

    video_preview.short_description = 'video'
    video_preview.allow_tags = True






admin.site.register(Theme, CouvertureAdmin)
admin.site.register(Projet,ProjetAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Personne,PersonneAdmin)
admin.site.register(Information,InformationAdmin)



admin.site.site_header = "Hedia Photography Administration"
admin.site.site_title = "Hedia Photography Administration"
admin.site.index_title = "Hedia Photography Administration"
admin.site.site_url=None




admin.site.unregister(User)
admin.site.unregister(Group)

