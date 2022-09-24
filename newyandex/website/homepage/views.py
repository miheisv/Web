from django.views.generic.base import TemplateView

# Create your views here.

class HomePage(TemplateView):

    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['img'] = '/my_img.jpg'
        return context