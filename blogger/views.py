from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from blogger.models import Post




class Home(TemplateView):
    template_name = 'blogger/home.html'

class Listpost(ListView):
    template_name = 'blogger/post.html'
    model = Post
class detailpost(DetailView):
    template_name =  'blogger/detail.html'
    model = Post

class IndexPost(ListView):
    template_name =  'blogger/intro.html'
    model =  Post

class FieldPost(DetailView):
    template_name = 'blogger/field.html'
    model = Post

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)



