from posts.models import Forum
from posts.api.serializers import ForumSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView



class ForumListCreateAPIView(APIView):
    
    def get(self,request):
        queryset = Forum.objects.filter(active= True)

        serialized_data = ForumSerializer(queryset,many= True).data

        return Response(data=serialized_data,status=status.HTTP_200_OK)



    def post(self,request):
        serializer = ForumSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        if not serializer.is_valid():
            return Response({'errors' : serializer.errors },status= status.HTTP_400_BAD_REQUEST)
        

class ForumDetailAPIView(APIView):

    def get_obj(self,pk):
        obj = get_object_or_404(Forum, pk = pk)

        return obj

    def get(self,request,pk):
        forum = self.get_obj(pk=pk)
        serializer = ForumSerializer(instance= forum)

        return Response(serializer.data , status=status.HTTP_200_OK)

    def put(self,request,pk):
        forum = self.get_obj(pk=pk)
        serializer = ForumSerializer(instance=forum , data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response({'errors' : serializer.errors },status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        forum = self.get_obj(pk=pk)

        forum.delete() 
        return Response({'message':'content successfully deleted.'},status=status.HTTP_204_NO_CONTENT)



'''
@api_view(['GET','POST'])
def forum_list_create_view(request):

    if request.method == 'GET':

        queryset = Forum.objects.filter(active= True)

        serialized_data = ForumSerializer(instance = queryset,many= True).data

        return Response(data=serialized_data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        
        serializer = ForumSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        if not serializer.is_valid():
            return Response(status= status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def get_forum_page_view(request,id):

    
    try:
        obj = Forum.objects.get(id= id)
    except Forum.DoesNotExist:
        return Response({
            'error' : 'Forum is not found'
        },status= status.HTTP_404_NOT_FOUND)

    if obj.active == False:
        return Response({
            'error' : 'this forum object is hidden.'
        },status=status.HTTP_401_UNAUTHORIZED)
    
    

    
    
    if request.method == 'GET':
        serializer = ForumSerializer(obj, many = False)
        return Response(serializer.data , status= status.HTTP_200_OK)


    if request.method == 'PUT':
        serializer = ForumSerializer(instance=obj , data= request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data , status = status.HTTP_200_OK)

        if not serializer.is_valid():
            return Response(status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        obj.delete()
        return Response({
            'code' : 204,
            'message' : 'Object deleted.' 
        },status=status.HTTP_204_NO_CONTENT)
    

    
'''