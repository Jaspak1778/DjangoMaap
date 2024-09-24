#urls.py
#path: E:\Koodi\DJANGO\kauppatoriapp\kauppatoriapp\urls.py

from .views import home, create_ad, my_ads, edit_ad, delete_ad

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  
    path("accounts/", include("django.contrib.auth.urls")),  
    path("", home, name="home"),  
    path('create-ad/', create_ad, name='create_ad'),
    path('my-ads/', my_ads, name='my_ads'),
    path('my-ads/', my_ads, name='my_ads'),
    path('edit-ad/<int:ad_id>/', edit_ad, name='edit_ad'),
    path('delete-ad/<int:ad_id>/', delete_ad, name='delete_ad'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #kuvan lataus
 

