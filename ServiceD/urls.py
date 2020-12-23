"""ServiceD URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from cust_app import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'customers', views.CustomerViewset)
# router.register(r'services', views.ServicesViewset)
# router.register(r'sales', views.SalesDataViewset)

urlpatterns = [
    url(r'^api/customer$',views.customer_list),
    url(r'^api/service$', views.service_list),
    url(r'^api/data$', views.data_list),
    url('admin/', admin.site.urls),
    url(r'^api/details$', views.data_detail),



]
