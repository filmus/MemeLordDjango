from django.conf.urls.static import static
from django.urls import path

from memelord import settings
from memelordapp.views import add_post_view
from . import views

urlpatterns = [
    path('addpost/', add_post_view, name='addpost'),
    path('', views.home, name='memelordapp-home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
