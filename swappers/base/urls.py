from django.conf.urls import url
from base import views
from django.urls import include, path
from rest_framework import routers
# from .views import (
#     PostListView, 
#     PostDetailView, 
#     PostCreateView,
#     PostDeleteView,
#     TravelListView, 
#     TravelDetailView, 
#     TravelCreateView,
#     TravelDeleteView
# )

# urlpatterns = [
#     url('', views.home),
#     # url('', views.gallery)
# ]

app_name = 'base'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('rest', include(router.urls)),
    path('home/', views.home, name='base-home'),
    path('travel/', views.TravelListView.as_view(), name='base-travel'),
    path('travel/new/', views.TravelCreateView.as_view(), name='travel-create'),
    path('travel/post/<int:pk>/delete', views.TravelDeleteView.as_view(), name='travel-delete'),
    path('travel/post/<int:pk>/update', views.TravelUpdateView.as_view(), name='travel-update'),
    path('travel/post/<int:pk>/', views.TravelDetailView.as_view(), name='travel-detail'),
    path('gallery', views.PostListView.as_view(), name='base-gallery'),
    path('gallery/post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('gallery/new/', views.PostCreateView.as_view(), name='post-create'),
    path('gallery/post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('gallery/post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('food/', views.FoodListView.as_view(), name='base-food'),
    path('food/new/', views.FoodCreateView.as_view(), name='food-create'),
    path('food/post/<int:pk>/delete', views.FoodDeleteView.as_view(), name='food-delete'),
    path('food/post/<int:pk>/update', views.FoodUpdateView.as_view(), name='food-update'),
    path('food/post/<int:pk>/', views.FoodDetailView.as_view(), name='food-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]