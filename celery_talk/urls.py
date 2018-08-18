from django.conf.urls import url
from django.contrib import admin

from core import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register_user, name='register_user'),
]
