
from rest_framework.decorators import api_view
from rest_framework.response import Response 

# Create your views here.


@api_view(['GET','POST'])
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