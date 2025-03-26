import uuid
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Document


class EditorView(TemplateView):
    """View for collaborative editor"""

    template_name = "editor/editor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("hej editor")
        # Get room name from query parameters or use a default
        room_name = self.request.GET.get("room", "default")
        # Generate a random client ID
        client_id = str(uuid.uuid4())[:8]
        print(Document.objects.filter(name=room_name).first())
        context.update(
            {
                "room_name": room_name,
                "client_id": client_id,
                # Get document if it exists
                "document": Document.objects.filter(name=room_name).first(),
            }
        )
        return context


class DocumentListView(ListView):
    """View for listing available documents"""

    model = Document
    template_name = "editor/document_list.html"
    context_object_name = "documents"
