from django.conf.urls import url

from . import views
urlpatterns = [url(r'^$',views.index, name = 'index'),
			url(r'^login',views.login_view, name = 'login'),
			url(r'^signUp', views.signup_view , name = 'signup'),
			url(r'^wikiview',views.wiki_view, name = 'wikiview'),
			url(r'^homepage',views.home_page, name='homepage'),
			url(r'^del/(?P<id>(\d+))/(?P<userid>(\d+))/$',views.delete_content, name='del'),
			url(r'^edit/(?P<id>(\d+))/(?P<userid>(\d+))/$',views.edit_content,name='edit'),
			url(r'^update_view',views.update_content, name = 'update_view'),
]
