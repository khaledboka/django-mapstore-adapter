from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = [
    url(r"^o/", include("mapstore2_adapter.urls", namespace="mapstore2_adapter")),
]


urlpatterns += [url(r"^admin/", admin.site.urls)]
