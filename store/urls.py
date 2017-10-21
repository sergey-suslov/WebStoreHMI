"""WebStoreHMI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from store.views import store_main, add_to_bucket, login_manager, goto_login, sign_up, sign_in, sign_out

urlpatterns = [
    url(r'^store/$', store_main, name='store'),
    url(r'^$', login_manager, name='login_manager'),
    url(r'^login/$', goto_login, name='login'),
    url(r'^logout/$', sign_out, name='sign_out'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^sign_in/$', sign_in, name='sign_in'),
    url(r'^add_item/$', add_to_bucket, name='add_item'),
]
