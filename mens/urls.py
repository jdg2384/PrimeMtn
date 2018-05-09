from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from mens.models import Most

urlpatterns = [ 
                url(r'^$', ListView.as_view(queryset=Most.objects.all(),
                                            template_name="mens/mens.html")),
                
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Most,
                                                         template_name = 'mens/post.html')),
            ]


