from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("editor/", include("editor.urls")),
    path("", RedirectView.as_view(pattern_name="editor:document_list"), name="home"),
]
