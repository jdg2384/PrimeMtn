from django.conf.urls import url
from . import views
# from django.views.generic import ListView, DetailView
# from head.models import Post

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', ListView.as_view(queryset=Post.objects.all(),
    #                             template_name="beers.html")),
]
