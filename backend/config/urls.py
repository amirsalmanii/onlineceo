from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('categories.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('threed.urls')),
    path('api/v1/', include('discount.urls')),
    path('api/v1/', include('mark.urls')),
    path('api/v1/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
