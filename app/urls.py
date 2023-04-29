from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.user_profile, name="profile"),
    path("import_data", views.import_data, name="import_data"),   # <- added by nlandi
    path("visualization/", views.visualization, name="visualization"),
]
