from .auth import check_user, register_user
from rest_framework.decorators import action
from .categories_views import CategoriesView
from .food_log_views import FoodLogView
from .dish_views import DishView
from .restaurants_views import RestaurantView