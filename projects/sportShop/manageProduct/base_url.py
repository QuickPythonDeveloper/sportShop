from django.urls import path

from .views.base import BaseView


urlpatterns = [

    path('', BaseView.as_view()),
]
