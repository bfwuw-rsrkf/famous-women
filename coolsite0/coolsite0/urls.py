from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from coolsite0 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
