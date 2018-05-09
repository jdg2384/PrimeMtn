from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from pet.models import Woof

urlpatterns = [ 
                url(r'^$', ListView.as_view(queryset=Woof.objects.all(),
                                            template_name="pet/pet.html")),
                
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Woof,
                                                         template_name = 'pet/post.html')),
            ]


