from django.urls import path

from users.views import AccountUpdateView, LoginFormView, RegisterView, confirm_email

app_name = 'users'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginFormView.as_view(), name="login"),
    # path("logout/", RegisterView.as_view(), name="logout"),
    path("account/", AccountUpdateView.as_view(), name="account"),
    # path("update/password/", RegisterView.as_view(), name="register"),
    # path("forget/password/", RegisterView.as_view(), name="register"),
    # path("verification/recent/", RegisterView.as_view(), name="register"),
    path("verification/<int:uid>/<str:token>/", confirm_email, name="confirm-email"),
]
