from django.urls import path

from .views import MetricsExporterView, CustomMetricsExporterView

urlpatterns = [
    path("", MetricsExporterView.as_view(), name="metrics-exporter"),
    path("custom/", CustomMetricsExporterView.as_view(), name="metrics-exporter-custom")
]
