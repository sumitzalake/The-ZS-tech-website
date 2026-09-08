from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.course_list,
        name='course_list'
    ),

    path(
        'add/',
        views.course_create,
        name='course_create'
    ),

    path(
        '<int:pk>/',
        views.course_detail,
        name='course_detail'
    ),

]