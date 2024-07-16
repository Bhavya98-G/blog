from django.urls import path , include

from home import views 
urlpatterns = [
    path('register/', views.register , name= 'register'),
    path('patient_register/',views.patient_register.as_view(), name='patient_register'),
    path('doctor_register/',views.doctor_register.as_view(), name='doctor_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('post/', views.view_posts, name='view_posts'),
]

