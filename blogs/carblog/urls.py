from django.urls import path
from .views import *

urlpatterns = [
    path('fbv_template/', template_view, name='fbv'),
    path('cbv_template/', TemplateView.as_view(), name='cbv')
]