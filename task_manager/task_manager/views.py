# from django.shortcuts import render
from multiprocessing import context
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['who'] = 'World'
        return context
# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })



