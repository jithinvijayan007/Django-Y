from django.shortcuts import render
from cust_app.models import Customer, Services, SalesData
from cust_app.serializer import CustomerSerializer, ServicesSerializer, SalesDataSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from cust_app.models import SalesData,Customer,Services
from django.http import JsonResponse
from rest_framework import serializers

# Create your views here.

@api_view(['GET','POST'])
def customer_list(request):
    if request.method=="GET":
        ins_salesdata=SalesData.objects.all()
        print(ins_salesdata)
        # serializer=DemoSerializer(ins_user,many=True)
        # return Response(serializer.data)
        return Response(ins_salesdata)
    elif request.method=="POST":
        print("Inside POST",request.data)
        # dict_salesdata=request.data
        dat_serv_sale=request.data['dat_sale']
        # dat_serv_sale=dat_serv_sale[:10]
        print(" ",dat_serv_sale)
        dbl_serv_amount=request.data['dbl_amount']
        dbl_serv_service_charge=request.data['dbl_service_charge']
        dbl_serv_total=request.data['dbl_total']
        int_serv_paid_status=request.data['int_paid_status']
        int_serv_status=request.data['int_status']

        vchr_serv_ref_no=request.data['vchr_ref_no']

        vchr_service=request.data['vchr_service_name']


        ins_service = Services.objects.get(pk_bint_id=vchr_service)
        print(" ",ins_service)
        print(dat_serv_sale)


        if((request.data['vchr_name']=="") and (request.data['bint_mobile']=="")):
            ins_sales = SalesData.objects.create(
                                            fk_service_id=ins_service.pk_bint_id,dbl_amount=dbl_serv_amount,
                                            dbl_service_charge=dbl_serv_service_charge,
                                            dbl_total=dbl_serv_total,int_paid_status=int_serv_paid_status,
                                            int_status=int_serv_status,vchr_ref_no=vchr_serv_ref_no)







        else:
            vchr_cust_name=request.data['vchr_name']
            bint_cust_mobile = request.data['bint_mobile']
            if(Customer.objects.filter(bint_mobile=bint_cust_mobile).exists()):
                print("Customer exists!")
                ins_customer = Customer.objects.get(bint_mobile=bint_cust_mobile)

            else:
                ins_customer = Customer.objects.create(vchr_name=vchr_cust_name,bint_mobile=bint_cust_mobile)
                print("Customer Added!")




            print(" ",ins_service,ins_customer)
            ins_sales = SalesData.objects.create(fk_customer_id=ins_customer.pk_bint_id,
                                            fk_service_id=ins_service.pk_bint_id,dbl_amount=dbl_serv_amount,
                                            dbl_service_charge=dbl_serv_service_charge,
                                            dbl_total=dbl_serv_total,int_paid_status=int_serv_paid_status,
                                            int_status=int_serv_status,vchr_ref_no=vchr_serv_ref_no)
        if ins_sales:
            print("Details Added")
            str_data="Details Added"
        else:
            print("Error occured!")
            str_data="Details already exists!"







        return Response(str_data)


@api_view(['GET','POST'])
def service_list(request):
    if request.method == 'GET':
        print("getaaa")
        ins_service = Services.objects.all()
        serializer=ServicesSerializer(ins_service,many=True)
        return Response({'data':serializer.data})

@api_view(['GET','POST'])
def data_list(request):
    if request.method == 'POST':
        print(request.data)
        start_date = request.data['dat_from']
        end_date = request.data['dat_to']
        int_status = int(request.data['int_status'])
        int_paid_status = int(request.data['int_paid_status'])
        if ((int_paid_status ==2) and (int_status ==2)):
            ins_data = list(SalesData.objects.filter(dat_sale__range=[start_date, end_date]).values("dat_sale","dbl_amount","dbl_service_charge","dbl_total","fk_customer__bint_mobile","fk_service__vchr_name","int_paid_status","pk_bint_id"))
        elif (int_paid_status ==2):
            ins_data = list(SalesData.objects.filter(dat_sale__range=[start_date, end_date],int_status=int_status).values("dat_sale","dbl_amount","dbl_service_charge","dbl_total","fk_customer__bint_mobile","fk_service__vchr_name","int_paid_status","pk_bint_id"))
        elif (int_status ==2):
            ins_data = list(SalesData.objects.filter(dat_sale__range=[start_date, end_date],int_paid_status=int_paid_status).values("dat_sale","dbl_amount","dbl_service_charge","dbl_total","fk_customer__bint_mobile","fk_service__vchr_name","int_paid_status","pk_bint_id"))




        # response = {}
        # response['ins_data'] = serializers.serialize("json", SalesData.objects.filter(dat_sale__range=[start_date, end_date], int_status=int_status, int_paid_status=int_paid_status))
        # return HttpResponse(response, content_type="application/json")
        # import pdb; pdb.set_trace()
        else:
            ins_data = list(SalesData.objects.filter(dat_sale__range=[start_date, end_date],int_paid_status=int_paid_status, int_status=int_status).values("dat_sale","dbl_amount","dbl_service_charge","dbl_total","fk_customer__bint_mobile","fk_service__vchr_name","int_paid_status","pk_bint_id"))
        print(ins_data)
        return JsonResponse(ins_data, safe=False)

@api_view(['PUT','POST'])
def data_detail(request):
    if request.method == 'POST':
        int_id = request.data
        ins_data = list(SalesData.objects.filter(pk_bint_id=int_id).values("dat_sale","dbl_amount","dbl_service_charge","dbl_total","fk_customer__bint_mobile","fk_service__pk_bint_id","int_paid_status","fk_customer__vchr_name","fk_service__vchr_name","vchr_ref_no","int_status","pk_bint_id"))
        return JsonResponse(ins_data, safe = False)
    elif request.method == 'PUT':
         # import pdb; pdb.set_trace()
         print("inside PUT", request.data)
         pk_bint_id = request.data['pk_bint_id']
         dbl_amount = request.data['dbl_amount']
         dbl_service_charge = request.data['dbl_service_charge']
         dbl_total = request.data['dbl_total']
         int_paid_status = request.data['int_paid_status']
         int_status = request.data['int_status']
         int_service_id = request.data['fk_service__pk_bint_id']
         ins_service = Services.objects.get(pk_bint_id = int_service_id)
         ins_sales = SalesData.objects.get(pk_bint_id = pk_bint_id)

         
         ins_sales.dbl_amount = dbl_amount
         ins_sales.dbl_service_charge = dbl_service_charge
         ins_sales.dbl_total = dbl_total
         ins_sales.int_paid_status = int_paid_status
         ins_sales.int_status = int_status
         ins_sales.fk_service = ins_service
         ins_sales.save()
         # print("Updated")
         if request.data['fk_customer__bint_mobile']:
            bint_phone = request.data['fk_customer__bint_mobile']
            ins_customer = Customer.objects.get(bint_mobile=bint_phone)
            ins_customer.vchr_customer_name=request.data['fk_customer__vchr_name']
            ins_customer.save()
            print(ins_customer.vchr_customer_name)
            print("Name Updated")
            return Response("Updated Successfully")

         # if request.data['vchr_name']:
         #     str_name = request.data['vchr_name']
         #    bint_phone = request.data['bint_mobile']
         #    ins_customer = Customer.objects.get(bint_mobile=bint_phone)
         #    ins_customer.vchr_name=str_name
         #    ins_customer.save()
         #    print(ins_customer.vchr_customer_name)
         #    print("Name Updated")
         #    return Response("Updated Successfully")
