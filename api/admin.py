from dataclasses import fields
from django.contrib import admin
from .models import*



admin.site.register(Video)
admin.site.register(Personne)
admin.site.register(Information)


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

    list_display=('projet','image_preview')
    list_display_links=('projet','image_preview')
    search_fields=['projet__nom']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'image'
    image_preview.allow_tags = True



admin.site.register(Theme, CouvertureAdmin)
admin.site.register(Projet,ProjetAdmin)
admin.site.register(Image,ImageAdmin)




admin.site.site_header = "Hedia Photography Administration"
admin.site.site_title = "Hedia Photography Administration"
admin.site.index_title = "Hedia Photography Administration"
admin.site.site_url=None

