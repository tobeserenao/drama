from rest_framework import serializers


class ChatCompletionRequestSerializer(serializers.Serializer):
    model = serializers.CharField()
    conversation = serializers.ListField()
