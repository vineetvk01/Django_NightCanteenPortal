from django.conf.urls import url
from . import views

urlpatterns = [
    # /order/
    url(r'^$', views.index, name='index'),
    # /order/makeorder/
    url(r'^makeorder/', views.makeorder, name='makeorder'),
    # /order/payorder/
    url(r'^payorder/', views.payorder, name='payorder'),
    # /order/doneorder/
    url(r'^doneorder/', views.doneorder, name='doneorder'),
]
