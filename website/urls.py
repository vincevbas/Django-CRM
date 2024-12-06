from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('song/<int:pk>', views.loona_song, name='song'),
    path('delete_song/<int:pk>', views.delete_song, name='delete_song'),
    path('add_song/', views.add_song, name='add_song'),
    path('update_song/<int:pk>', views.update_song, name='update_song'),

]