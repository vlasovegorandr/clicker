from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='home'),
    url(r'^index/$', views.main_menu, name='main_menu'),
    url(r'^about/$', views.about, name='about'),
    url(r'^game/', include('game.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
