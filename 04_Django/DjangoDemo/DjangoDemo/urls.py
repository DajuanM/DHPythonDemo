from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', tv.do_normalmap),
    url(r'^withparams/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])', tv.withparams),
    url('^teacher/', include(teacher_urls)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),
    url(r'^name/$', tv.extremParam, {"name": "Aiden"}),
    url(r'^abcdname/', tv.revParse, name="askname"),
    url(r'^v_exception', tv.v_exception),
    url(r'^v10_1/', tv.v10_1),
    url(r'^v10_2/', tv.v10_2),
    url(r'^v11/', tv.v11, name="v11"),
    url(r'^v8/', tv.v8_get),
    url(r'v9_get/', tv.v9_get),
    url(r'v9_post/', tv.v9_post),
    url(r'^render_test', tv.render_test),
    url(r'^render2_test', tv.render2_test),
    url(r'^render3_test', tv.render3_test),
    url(r'^get404', tv.get404)
]
