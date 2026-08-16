
from platform import python_version
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Person
from .serializers import PeopleSerializer
from rest_framework.views  import APIView


class PersonApi(APIView):
    def get(self,request):
        return Response({'message': 'Get request successful'})
    def post(self,request):
        return Response({'message': 'Post request successful'})
    def put(self,request):
        return Response({'message': 'Put request successful'})
    def patch(self,request):
        return Response({'message': 'Patch request successful'})
    def delete(self,request):
        return Response({'message': 'Delete request successful'})
     
@api_view(['GET','POST','PUT',"PATCH"])
def index(request):
    courses={'Python':'Python course',
        'learn':['PYthon','DJango','DRF','Tornado','FastAPI']}
    if request.method=='GET':
        print("GET request")
        
    elif request.method=='POST':
        data=request.data
        print('******')
        print(data)
        print('******')
        print("POST request")
    return Response(courses)


@api_view(["GET","POST","PUT","PATCH","DELETE"])
def person(request):
    if request.method=='GET':

        obj=Person.objects.all()
        serializers=PeopleSerializer(obj,many=True)
        return Response(serializers.data)
    
    elif request.method=='PUT':
        data=request.data
        id=request.data.get("id")
        person = Person.objects.get(id=id)
        serializer=PeopleSerializer(person,data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors)

    
    elif request.method=='PATCH':
        data=request.data
        id=request.data.get("id")
        person = Person.objects.get(id=id)
        serializer=PeopleSerializer(person,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors)

    elif request.method=="DELETE":  
        data=request.data
        obj=Person.objects.get(id=data["id"])
        obj.delete()
        return Response({"message":"Person deleted"})
        
    else :
        data=request.data
        serializer=PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors)

