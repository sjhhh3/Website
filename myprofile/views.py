from django.views import generic
from .models import Profilepost

# Create your views here.

class ProfilePostView(generic.DetailView):
    model = Profilepost
    template_name = 'myprofile/profilepost.html'