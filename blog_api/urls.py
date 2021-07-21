from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from apps.blog.views import CategoryListAPIView, BlogListAPIView


router = routers.DefaultRouter()
router.register('category-list', CategoryListAPIView)
router.register('blog-list', BlogListAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    
  path('api/v1/auth/', include('rest_auth.urls')),
  path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title='documentacion DRF', public=True)),
]

