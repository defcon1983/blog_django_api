from django.contrib import admin
from django.urls import path, include
from apps.blog.views import CategoryListAPIView

from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()

router.register('category-list', CategoryListAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='documentacion DRF', public=True)),
]
