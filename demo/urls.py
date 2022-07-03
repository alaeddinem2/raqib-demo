from django.urls import path


from . import views
urlpatterns = [
    path('',views.login_demo,name="login-demo"),
    path('login',views.user_login, name='login'),
    path('home',views.home_demo, name='home'),
    path('logout',views.user_logout, name='logout'),
    path('add_vehicle',views.add_vehicle, name='add-vehicle'),
    path('add_vehicle_save',views.add_vehicle_save, name='add-vehicle-save'),
    path('manage_vehicle',views.manage_vehicle, name='manage-vehicle'),
    path('vehicle_logs/<int:id>',views.vehicle_logs, name='manage-vehicle'),
    path('add_driver',views.add_driver, name='add-driver'),
    path('add_driver_save',views.add_driver_save, name='add-driver-save'),
    path('manage_drivers',views.manage_drivers, name='manage-drivers'),
    path('edit_drivers/<int:id>',views.edit_drivers, name='edit-drivers'),
    path('edit_driver_save',views.edit_driver_save, name='edit-drivers-save'),
    
   
]