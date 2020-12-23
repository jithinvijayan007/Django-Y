from django.contrib import admin
from cust_app.models import Customer, Services, SalesData
# Register your models here.
admin.site.register(Customer)
admin.site.register(Services)
admin.site.register(SalesData)
