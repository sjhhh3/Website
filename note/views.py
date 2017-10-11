from django.views import generic
from .models import Notepost
from django.shortcuts import render
import datetime

today = datetime.date.today()
# Create your views here.
class NoteView(generic.ListView):
    template_name = "note/note.html"
    context_object_name = "all_notepost"
    def get_queryset(self):
        return Notepost.objects.filter(date__year=today.year, date__month=today.month).order_by("-date")[:25]

def MonthView(request, year, month):
    all_posts = Notepost.objects.filter(date__year=int(year), date__month=int(month)).order_by("-date")[:25]
    if all_posts.exists():
        context = {'all_posts': all_posts}
        return render(request, "note/note.html",context)
    return render(request,'note/None.html')

class NotepostView(generic.DetailView):
    model = Notepost
    template_name = 'note/notepost.html'

def NoteNone(request):
    return render(request, 'note/None.html')