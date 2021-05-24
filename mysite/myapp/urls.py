from django.conf.urls import url                                                                                                                              
from . import views

urlpatterns = [ 

    url(r'', views.default_map, name="default"),
]

handler404="views.error_404_view"
handler500="views.error_505_view"