from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from outdoor.models import Post

urlpatterns = [ 
                url(r'^$', ListView.as_view(queryset=Post.objects.all(),
                                            template_name="outdoor/outdoor.html")),
                
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                                         template_name = 'outdoor/post.html')),
            ]


