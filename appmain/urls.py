from . import views
from django.urls import path
app_name = "appmain"
urlpatterns = [
    path('', views.index_page, name="homepage"),
    path('<int:pk>/',views.buspage, name="heaasd"),
    path('ad/driveside/', views.homepage_admin, name="main"),
    path('driveside/<str:route>/', views.send_stops, name="mainstop"),
    path('driveside/<str:route>/<str:stop>/', views.update_stops, name="mainupdate"),
]