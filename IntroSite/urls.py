
from django.contrib import admin
from django.urls import path
from base.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_text', update_text, name='update_text'),
    path('get_text', get_text, name='get_text'),
    path('anim', anim, name='anim'),
    path('', interface_with_text, name='interface_with_text'),
    path('interface_with_text', interface_with_text, name='interface_with_text'),
    path('interface_with_button', interface_with_button, name='interface_with_button'),


    
]
from django.conf.urls.static import static
from IntroSite import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)