from posts.models import Forum
from posts.api.serializers import ForumSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def forum_list_create_view(request):

    if request.method == 'GET':

        queryset = Forum.objects.filter(active= True)

        serialized_data = ForumSerializer(instance = queryset,many= True).data

        return Response(data=serialized_data,status=200)

    if request.method == 'POST':
        
        serializer = ForumSerializer(data=request.data)
    