from django.conf.urls import url

from . import views

urlpatterns = [
    uurl(r'^pdf-generator/$', views.pdf_generator, name='pdf-generator')
]