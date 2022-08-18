from .import views
from django.urls import path
urlpatterns=[
    path('tv/',views.testView,name='home'),
    path('av/',views.addorderView,name='addorder'),
    path('sv/',views.showordersView,name='showorder'),
    path('abv/',views.AboutUsView,name='aboutus'),
    path('cnv/',views.ContactUsView,name='contactus'),

    path('uv<int:id_from_fe>/',views.updateorderView,name='update'),
    path('dv<int:id_from_fe>/',views.deleteorderView,name='delete')
]