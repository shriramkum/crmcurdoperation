
from .models import Customer
from.serializers import Customerserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET'])
def customerlist(request):
    customer=Customer.objects.all()
    serializer_class=Customerserializer(customer,many=True)
    try:
        return Response(serializer_class.data,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def customerDetail(request,pk):
    customer=Customer.objects.get(id=pk)
    serializers_class=Customerserializer(customer)

    return Response(serializers_class.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def customercreate(request):
    serializer_class=Customerserializer(data=request.data)


    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)

@api_view(['PUT'])
def customerupdate(request,pk):
    customer=Customer.objects.get(id=pk)
    serializer_class=Customerserializer(instance=customer,data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)

@api_view(['DELETE'])
def customerdelete(request,pk):
    empolyee=Customer.objects.get(id=pk)
    empolyee.delete()
    return Response('deleted succesfully ')



class Customercall(APIView):
    def get(self,request):
        customer=Customer.objects.all()
        if 'first_name' in request.GET:
            first_name=request.GET['first_name']
            customer=Customer.objects.filter(first_name__icontains=first_name)
        elif 'last_name' in request.GET:
            last_name=request.GET['last_name']
            customer=Customer.objects.filter(last_name__icontains=last_name)
        serializer=Customerserializer(customer,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)



