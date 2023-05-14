from rest_framework import serializers
from posts.models import Forum
from datetime import datetime
from django.utils.timesince import timesince


class ForumSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()

    class Meta:
        model = Forum
        fields = '__all__'
        read_only_fields = ['id','created','updated']




'''
class ManuelForumSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)
    author = serializers.CharField()
    title = serializers.CharField()
    
    content = serializers.CharField()

    active = serializers.BooleanField()

    created = serializers.DateTimeField(read_only = True)
    updated = serializers.DateTimeField(read_only = True)

    def create(self,validated_data):
        forum = Forum.objects.create(
            **validated_data
        )

        return forum

    def update(self,instance,validated_data):
        instance.author = validated_data.get('author')
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.active = validated_data.get('active',instance.active)

        instance.save()

        return instance
    
    def validate(self,data):
        if data['title'] == data['content']:
            raise serializers.ValidationError('Title and content not be same')
        
        return data        
    
    def validate_title(self,value):

        if (len(value) < 10):
            raise serializers.ValidationError('Title mut be shorter than 10 characters')
        
        return value
    
'''