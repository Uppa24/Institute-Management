from django.urls import path
from Student import views


urlpatterns = [
    path('',views.student_home),
    path('login/',views.studentlogin,name='login'),
    path('signup/',views.studentsignup),
    path('filldata/',views.student_filldata),
    path('getqr/',views.studentqrgenerate),

    # path('register/',views.studentreg),
]
