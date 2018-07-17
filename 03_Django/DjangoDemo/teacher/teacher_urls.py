from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^doapp/', views.do_app),
]
