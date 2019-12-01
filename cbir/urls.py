from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from cbirApp.views import *

urlpatterns = [
    path("images/", image_list, name="image_list"),
    path('image_search', dest_image_view, name='image_search'),
    path('success', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
