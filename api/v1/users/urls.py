from api.v1.users.views import MyObtainTokenPairView, RegisterView

from django.urls import path

from rest_framework import routers


from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter()
router.register(r"register", RegisterView, basename="register")

urlpatterns = [
    path("login/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += router.urls
