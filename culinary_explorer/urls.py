from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from culinary_explorer_api.views import register_user, check_user, CategoriesView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoriesView, 'categories')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]