from django.conf.urls import url,patterns
from account import views
from django.conf import settings
urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^register/$',views.register,name = 'register'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^portfolio/$',views.portfolio,name='portfolio'),
    url(r'^features/$',views.features,name='features'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root':settings.STATIC_ROOT }),

)