from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('contact/',views.contact_us, name="contact"),
    path('about/',views.about, name="about"),
    path('portfolio/',views.portfolio, name="portfolio")
]



# Add the following lines at the end of your urls.py file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.ABOUT_IMAGES_URL, document_root=settings.ABOUT_IMAGES_ROOT)
