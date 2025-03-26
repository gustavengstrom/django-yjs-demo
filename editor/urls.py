from django.urls import path
from . import views

app_name = "editor"

urlpatterns = [
    path("", views.DocumentListView.as_view(), name="document_list"),
    path("editor/", views.EditorView.as_view(), name="editor"),
]
