from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_type = serializers.ReadOnlyField(source='content_type.model')

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_type', 
                 'object_id', 'is_read', 'created_at']