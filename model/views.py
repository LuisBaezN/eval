from django.views.generic import ListView, DetailView, TemplateView


from .models import Productos

class HomeView(ListView):
    model = Productos
    context_object_name = "prod"
    template_name = 'model/home.html'