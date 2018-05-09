from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from special.models import Enter

urlpatterns = [ 
                url(r'^$', ListView.as_view(queryset=Enter.objects.all(),
                                            template_name="special/postspecial.html")),
                
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Enter,
                                                         template_name = 'special/special.html')),
            ]


