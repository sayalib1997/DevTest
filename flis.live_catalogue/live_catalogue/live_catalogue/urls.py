from django.conf.urls import patterns, include, url
from django.contrib import admin
from live_catalogue import views
from live_catalogue.auth import login_required


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'live_catalogue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', login_required(views.HomeView.as_view()), name='home'),
    url(r'^api/keywords$', login_required(views.ApiKeywords.as_view()), name='api_keywords'),
    url(r'^need/add$', login_required(views.NeedEdit.as_view()), name='need_edit'),
    url(r'^need/(?P<pk>[\w\-]+)/edit$', login_required(views.NeedEdit.as_view()), name='need_edit'),
    url(r'^admin/', include(admin.site.urls)),
)
