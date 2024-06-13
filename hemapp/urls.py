from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('login/', login_view, name='login'),
    path('logout/', Logout, name='logout'),
    path('viewdata/',viewdata,name="viewdata"),
    path('edit/<int:id>/', edit_view, name='edit'),
    path('delete/<int:id>/', delete_view, name='delete'),
    path('work_completed/', work_completed, name='work_completed'),
    path('lpo_received/', lpo_received, name='lpo_received'),
    path('not_invoiced_tasks/', not_invoiced_tasks, name='not_invoiced_tasks'),
    path('invoiced_tasks/', invoiced_tasks, name='invoiced_tasks'),
    path('download_filtered_data/', download_filtered_data, name='download_filtered_data'),
]

