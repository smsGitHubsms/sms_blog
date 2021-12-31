from django.urls import path
from . import views
urlpatterns = [
    path('',views.func,name='func'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('login/logout/',views.logout,name='logout Me'),
    path('logout/',views.logout,name='logout'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('login/NewBlog/',views.add_blogs,name='New Blog'),

]
