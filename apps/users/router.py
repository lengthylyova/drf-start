from rest_framework.routers import DefaultRouter
from .views.users import UserCreateViewSet, UserViewSet



router = DefaultRouter()
router.register("users", UserViewSet)
router.register("users", UserCreateViewSet)