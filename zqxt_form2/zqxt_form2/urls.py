from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zqxt_form2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','tools.views.index',name='index'),
    #url(r'^$','tools.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
