from django.conf.urls import include,url
from . import views

urlpatterns = [
   url(r'^$',views.home),
   url(r'^sucursal/new/$', views.sucursal_new, name='sucursal_new'),
   url(r'^sucursal/$',views.sucursal_list, name='sucursal_list'),
   url(r'^empleado/new/$',views.empleado_new, name='empleado_new'),
   url(r'^empleados/$',views.empleado_list, name='empleado_list'),
   url(r'^empleado/(?P<pk>[0-9]+)/edit/$',views.empleado_edit,name='empleado_edit'),
   url(r'^sucursal/(?P<pk>[0-9]+)/edit/$',views.sucursal_edit, name='sucursal_edit'),
   url('^signup/$',views.signup,name='signup'),

]
