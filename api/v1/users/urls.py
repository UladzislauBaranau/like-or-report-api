from api.v1.users.views import (
    ChangeUserPasswordView,
    MyObtainTokenPairView,
    RegisterView,
    UpdateUserProfileView,
)

from django.urls import path

from django_rest_passwordreset.views import (
    ResetPasswordConfirmViewSet,
    ResetPasswordRequestTokenViewSet,
    ResetPasswordValidateTokenViewSet,
)

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter()

router.register(
    r"register",
    RegisterView,
    basename="register",
)
router.register(
    r"update-profile",
    UpdateUserProfileView,
    basename="update-profile",
)
router.register(
    r"password-change",
    ChangeUserPasswordView,
    basename="change-password",
)
router.register(
    r"password-reset/validate-token",
    ResetPasswordValidateTokenViewSet,
    basename="reset-password-validate",
)
router.register(
    r"password-reset/confirm",
    ResetPasswordConfirmViewSet,
    basename="reset-password-confirm",
)
router.register(
    r"password-reset",
    ResetPasswordRequestTokenViewSet,
    basename="reset-password-request",
)

urlpatterns = [
    path("login/", MyObtainTokenPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
]

urlpatterns += router.urls
