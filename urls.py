from django.urls import path
from .import views
app_name = 'Profile'
urlpatterns = [
    path('' , views.profile_list , name = 'Profile') ,
    path('<int:id>' , views.profile_detail , name = 'detail'),
    path('' , views.del_profile , name = 'delete')
]
