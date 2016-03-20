"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from user_promission.views import index,q_code,q_name,u_add,u_updata,u_delete,u_query,u_q

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user_permission/query_code/$',q_code, name='q_code'),
    url(r'^user_permission/query_name/$',q_name, name='q_name'),
    url(r'^user_permission/add/$',u_add, name='u_add'),
    url(r'^user_permission/updata/$',u_updata, name='u_updata'),
    url(r'^user_permission/delete/$',u_delete, name='u_delete'),
    url(r'^query/$',u_query, name='u_query'),
    url(r'^u_q/$',u_q, name='u_q'),
    url(r'^index/$',index, name='index'),
]
