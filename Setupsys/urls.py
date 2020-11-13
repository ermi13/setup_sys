from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from homepage import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('services/', include('services.urls')),
    path('price/', include('price.urls'), name='price')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
