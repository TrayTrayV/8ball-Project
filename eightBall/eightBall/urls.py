
from django.contrib import admin
from django.urls import path

from eightVue import views as eightVue_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', eightVue_views.index),
    path('',eightVue_views.index),
    path('eight-ball-responses/', eightVue_views.get_eight_ball_responses, name='eight_ball_responses'),
]
