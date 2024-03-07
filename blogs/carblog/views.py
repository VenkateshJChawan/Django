from django.shortcuts import render
from django.views import View

# Create your views here.
# Function Based View
def template_view(request):
    context = {'name': 'Venkatesh'}
    return render(request, 'template.html', context)

# Class based View
class TemplateView(View):
    def get(self, request):
        return render(request, 'template.html')