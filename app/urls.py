from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.user_profile, name="profile"),
    path("generate_visualization/", views.generate_visualization, name="generate_visualization"),
    path("feature_table_summary/<str:uuid>", views.feature_table_summary, name="feature_table_summary"),
    path("taxonomic_bar_plots/<str:uuid>", views.taxonomic_bar_plots, name="taxonomic_bar_plots"),
    path("demo_table_view/", views.demo_table_view, name="demo_table_view"),
    path("api/check_run_status/<str:runId>",views.check_run_status, name="check_run_status"),
    path("table/", include(("filter_table.urls", "filter_table"), namespace="tables")),
    path("select2/", include("django_select2.urls")),
    # path("featuretable/", views.featuretable, name="featuretable"),
    # path("taxonomy/overview/<str:uuid>", views.taxonomy_overview, name="taxonomy_overview"),
    # path("featuretable/overview/<str:uuid>", views.featuretable_overview, name="featuretable_overview"),
    # path("featuretable/interactive/<str:uuid>", views.featuretable_interactive, name="featuretable_interactive"),
    # path('example/', ExampleView.as_view(), name='example'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)