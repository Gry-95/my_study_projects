from django.urls import path
from . import views

urlpatterns = [
    path('get_rectangle_area/<int:width>/<int:height>', views.redirect),
    path('get_square_area/<int:width>', views.redirect),
    path('get_circle_area/<int:radius>', views.redirect),
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='redirect-rectangle'),
    path('square/<int:width>', views.get_square_area, name='redirect-square'),
    path('circle/<int:radius>', views.get_circle_area, name='redirect-circle'),
]
