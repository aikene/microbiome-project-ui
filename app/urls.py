from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import ResetPasswordView


urlpatterns = [
    path('', views.home, name='home'),
    # path('admin/', admin.site.urls),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>/", views.user_profile, name="profile"),
    path("profile/<str:username>/<int:page>/", views.user_profile, name="profile"),
    path("profile/<str:username>/<int:page>/<int:show_history>/", views.user_profile, name="profile"),
    path("editprofile/<str:field>", views.edit_profile, name="edit_profile"),
    path("generate_visualization/", views.generate_visualization, name="generate_visualization"),
    path("feature_table_summary/<str:uuid>", views.feature_table_summary, name="feature_table_summary"),
    path("taxonomic_bar_plots/<str:uuid>", views.taxonomic_bar_plots, name="taxonomic_bar_plots"),
    path("demo_table_view/", views.demo_table_view, name="demo_table_view"),
    path("api/check_run_status/<str:runId>",views.check_run_status, name="check_run_status"),
    path("table/", include(("filter_table.urls", "filter_table"), namespace="tables")),
    path("select2/", include("django_select2.urls")),
    path("change_password", views.change_password, name='change_password'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset_sent_email/', views.password_reset_sent_email, name='password_reset_sent_email'),
    path("status/<str:username>/", views.status, name="status"),
    path("status/<str:username>/<int:page>/", views.status, name="status"),
    path("delete_account_confirm/<str:username>/", views.delete_account_confirm, name="delete_account_confirm"),
    path("delete_account/<str:username>/", views.delete_account, name="delete_account"),
    # path("featuretable/", views.featuretable, name="featuretable"),
    # path("taxonomy/overview/<str:uuid>", views.taxonomy_overview, name="taxonomy_overview"),
    # path("featuretable/overview/<str:uuid>", views.featuretable_overview, name="featuretable_overview"),
    # path("featuretable/interactive/<str:uuid>", views.featuretable_interactive, name="featuretable_interactive"),
    # path('example/', ExampleView.as_view(), name='example'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)