from django.urls import path
from final_app import views

# Templates Tagging
app_name = 'final_app'

urlpatterns = [
    path('', views.user,name='user'),
    path('login', views.user_login,name='user_login'),
    path('logout', views.user_logout,name='logout'),

]
