

# # Register your models here.
# admin.site.site_header="Clicker|Admin"
# #admin.site.register(Contact)

# class ContactAdmin(admin.ModelAdmin):
#     list_display=['id','name','email','number','message','added_on','is_approve']
# admin.site.register(Contact,ContactAdmin)

from django.utils.html import format_html
from django.contrib import admin
from myapp.models import Contact, About,Portfolio,LatestNews,OurGallery,Testimonial

# Register your models here.
admin.site.site_header = "Clicker|Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'number', 'message', 'added_on', 'is_approve']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'display_image1', 'display_image2']

    def display_image1(self, obj):
        return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.image1.url))

    def display_image2(self, obj):
        return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.image2.url))

    display_image1.short_description = 'Image 1'
    display_image2.short_description = 'Image 2'

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'link', 'description']

class LatestNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'news_heading', 'news_description', 'display_image']

    def display_image(self, obj):
        return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.news_image.url))

    display_image.short_description = 'News Image'

class OurGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'gallery_link', 'gallery_description', 'display_image']

    def display_image(self, obj):
        return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.gallery_image.url))

    display_image.short_description = 'Gallery Image'

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'testimonial_heading', 'testimonial_description', 'display_image']

    def display_image(self, obj):
        return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.testimonial_image.url))

    display_image.short_description = 'Testimonial Image'

admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(LatestNews, LatestNewsAdmin)
admin.site.register(OurGallery, OurGalleryAdmin)
admin.site.register(Testimonial, TestimonialAdmin)




