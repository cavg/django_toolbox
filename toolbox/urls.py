from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pdf-generator/$', views.pdf_generator, name='pdf-generator')
]