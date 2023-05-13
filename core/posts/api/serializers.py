from rest_framework import serializers
from posts.models import Forum



class ForumSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)
    author = serializers.CharField()
    title = serializers.CharField()
    
    content = serializers.CharField()

    active = serializers.BooleanField()

    created = serializers.DateTimeField(read_only = True)
    updated = serializers.DateTimeField(read_only = True)

    def create(self,validated_data):
        Forum.objects.create(
            **validated_data
        )

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.active = validated_data.get('active',instance.active)

        instance.save()

        return instance
    