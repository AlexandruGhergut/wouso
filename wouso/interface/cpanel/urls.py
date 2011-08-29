from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'wouso.interface.cpanel.views.dashboard', name='dashboard'),
    url(r'^customization/$', 'wouso.interface.cpanel.views.customization', name='customization'),
    url(r'^qpool/$', 'wouso.interface.cpanel.views.qpool_home', name='qpool_home'),
    url(r'^qpool/edit/(?P<id>\d*)/$', 'wouso.interface.cpanel.views.question_edit', name='question_edit'),
    url(r'^qpool/importer/$', 'wouso.interface.cpanel.views.importer', name='importer'),
    url(r'^qpool/importer/send$', 'wouso.interface.cpanel.views.import_from_upload', name='importer_send'),

    url(r'^artifact/set/(?P<id>\d*)/$', 'wouso.interface.cpanel.views.artifactset', name='artifact_set')
)
