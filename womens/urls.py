from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from womens.models import Wost

urlpatterns = [ 
                url(r'^$', ListView.as_view(queryset=Wost.objects.all(),
                                            template_name="womens/womens.html")),
                
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Wost,
                                                         template_name = 'womens/post.html')),
            ]


