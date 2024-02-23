from django.urls import path

from apps.users.views import UserLoginView, UserRegisterView, UserLogoutView, AddAuthorView, AddBookView

app_name = "users"
urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login-page"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('register/', UserRegisterView.as_view(), name="register-page"),
    path('add-author/', AddAuthorView.as_view(), name="addauthor-page"),
    path('add-book/', AddBookView.as_view(), name="addbook-page"),
]
