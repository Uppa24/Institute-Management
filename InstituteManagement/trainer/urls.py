from django.urls import path

from trainer import views

urlpatterns = [
    path('',views.trainer_home),
    path('login/',views.login_fun,name='login'),
    path('signup/',views.signup_fun,name='signup'),
    path('addnewstudent/',views.add_fun,name='add'),
    path('display/',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
    path('logout/',views.logout_fun,name='logout'),

]