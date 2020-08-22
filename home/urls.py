from . import views
from django.urls import path


urlpatterns=[
    path('index/',views.index,name='index'),
    path('about-us/',views.about_us,name='about_us'),
    path('loans/',views.loans,name='loans'),
    path('index/elements/',views.elements,name='elements'),
    path('contact/',views.contact,name='contatt'),
    path('news/',views.news,name='news'),
    path('details/',views.details,name='details'),
    path('predict/',views.predict,name='predict'),
    
]