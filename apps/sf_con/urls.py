from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'user/(?P<user_id>\d+)$', views.user_page, name='user_page'),

]
