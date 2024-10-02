
from django.contrib import admin
from django.urls import path, include
from  django.conf import settings

from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path('', include('Myapp.urls')),
    path('chat/', include('chat.urls')),
    path('Blog/', include('Blog.urls')),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    
    
