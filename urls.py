from django.conf.urls.defaults import patterns, url, include
from main import views
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wdys.views.home', name='home'),
    # url(r'^wdys/', include('wdys.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main),
    url(r'^make/$', views.make),
    url(r'^comment/$', views.comment),
    url(r'^upload/$', views.upload),
    url(r'^upload_images/$', views.upload_images),
    url(r'^step2/$', views.step2),
    url(r'^step3/$', views.step3),
    url(r'^publish/$', views.publish),
    url(r'^background_list/$', views.background_list),
    url(r'^delete_background_image/(\d+)/$', views.delete_background_image),
    url(r'^edit_background_image/(\d+)/$', views.edit_background_image),
    
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
