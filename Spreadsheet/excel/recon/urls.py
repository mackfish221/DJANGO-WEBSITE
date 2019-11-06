from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.reconciliations),
    url(r'form/', views.upload),
    #url(r'data/', views.upload),
    url(r'messages',views.messages),
]

