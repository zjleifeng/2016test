from django.conf.urls import patterns, include, url

from django.contrib import admin
from learn import views as learn_views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zqxt_tmpl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',learn_views.home,name='home'),
    url(r'^add/(\d+)/(\d+)/$',learn_views.add,name='add'),
    url(r'^admin/', include(admin.site.urls)),
)
