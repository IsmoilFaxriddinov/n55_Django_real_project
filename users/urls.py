from django.urls import path

from users.views import RegisterView

app_name = 'users'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # path("login/", RegisterView.as_view(), name="login"),
    # path("logout/", RegisterView.as_view(), name="logout"),
    # path("account/", RegisterView.as_view(), name="account"),
    # path("update/password/", RegisterView.as_view(), name="register"),
    # path("forget/password/", RegisterView.as_view(), name="register"),
    # path("verification/recent/", RegisterView.as_view(), name="register"),
    path("verification/", verify_email, name="confirm_email"),
]
