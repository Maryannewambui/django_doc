from django.urls import path
from . import views
# from mini import views


#url config
urlpatterns = [
    path('hello/', views.say_hello),
    path('check_age/', views.check_age),
    path('loop/', views.loop)
]