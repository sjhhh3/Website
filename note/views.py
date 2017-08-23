from django.views import generic
from .models import Notepost
from django.shortcuts import render

# Create your views here.
class NoteView(generic.ListView):
    template_name = "note/note.html"
    context_object_name = "all_notepost"

    def get_queryset(self):
        return Notepost.objects.all().order_by("-date")[:25]

class NotepostView(generic.DetailView):
    model = Notepost
    template_name = 'note/notepost.html'

def NoteNone(request):
    return render(request, 'note/None.html')