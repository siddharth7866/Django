from django.conf.urls import url

from register import views

app_name='basic_app'

urlpatterns = [

    url(r'^index', views.index, name='index'),
    url(r'^user/', views.user, name='user'),

]
