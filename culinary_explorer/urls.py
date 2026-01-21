from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from culinary_explorer_api.views import register_user, check_user, CategoriesView, FoodLogView, DishView, RestaurantView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoriesView, 'categories')
router.register(r'food_log', FoodLogView, 'food_log')
router.register(r'dish', DishView, 'dish')
router.register(r'culinary_explorer_api_restaurants', RestaurantView, 'restaurants')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register_user', register_user),
    path('checkuser', check_user),
]
