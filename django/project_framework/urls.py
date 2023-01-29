"""project_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import traceback
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django import get_version
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    # Docorized django homepage - You can delete this line if you don't want to use it.
    urlpatterns += [
        path('', TemplateView.as_view(template_name="dockerized_django_home.html"), name='dockerized_django_home', kwargs={'version': get_version()[:-3]}),

    ]
    # Media url
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Debug toolbar
    if settings.ENABLE_DEBUG_TOOLBAR:
        urlpatterns += [
            path('__debug__/', include('debug_toolbar.urls')),
        ]

# Custom apps urls.
if settings.CUSTOM_APPS:
    for app, base_url in settings.CUSTOM_APPS.items():
        try:
            urlpatterns.append(
                path(base_url + '/', include(app + '.urls')),
            )
        except Exception as e:
            print(f"{app} urls module not found.")
            traceback.print_exc()
