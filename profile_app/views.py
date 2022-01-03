from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_app import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        an_apiview=[
            'Uses HTTP methods as function(get,put,patch,delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control logic view',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello! {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})


class HelloViewSets(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        a_viewset=["ibad","shaikh","Mohammad","shakeel"]
        return Response({"a_viewset":a_viewset})
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            age=serializer.validated_data.get('age')
            msg=f'Hello! {name} of age {age}'
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        return Response({'method':'Retrieve'})
    def update(self,request,pk=None):
        return Response({'method':'update'})
    def partial_update(self,request,pk=None):
        return Response({'method':'Partial update'})
    def destroy(self,request,pk=None):
        return Response({'method':'destroy'})
