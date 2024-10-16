from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from server.views import ServerListViewSet
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter ()
router.register("api/server/select", ServerListViewSet,basename='server')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)