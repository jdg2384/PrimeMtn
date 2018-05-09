from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from access.models import Item

urlpatterns = [ 
                url(r'^$', ListView.as_view(queryset=Item.objects.all(),
                                            template_name="access/access.html")),
                
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Item,
                                                         template_name = 'access/post.html')),
            ]


