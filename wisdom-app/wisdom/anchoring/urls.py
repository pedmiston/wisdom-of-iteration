from django.conf.urls import url, include

import anchoring.views as anchoring


urlpatterns = [
    url(r'^$', anchoring.Home.as_view(), name='home'),
    url(r'^new/$', anchoring.NewGame.as_view(), name='new'),
]
