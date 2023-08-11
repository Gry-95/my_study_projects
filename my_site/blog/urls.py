from django.urls import path
from . import views

urlpatterns = [
    path('1', views.view_first_blog),
    path('2', views.get_guinness_world_records),
    path('<int:number_post>', views.num_of_post),
    path('', views.posts),
    path('<name_post>', views.dinam_rout),
]