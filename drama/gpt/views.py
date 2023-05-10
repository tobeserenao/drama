from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drama.gpt.serializers import ChatCompletionRequestSerializer
from drama.gpt.services import ChatCompletionService


class GPTIndexView(LoginRequiredMixin, TemplateView):
    template_name = "gpt/index.html"


class ChatCompletionView(APIView):
    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ChatCompletionRequestSerializer(data=request.data)
        if serializer.is_valid():
            response_data = ChatCompletionService.get_chat_completion(
                model=serializer.validated_data['model'],
                conversation=serializer.validated_data['conversation']
            )
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


gpt_index_view = GPTIndexView.as_view()
gpt_chat_completion_view = ChatCompletionView.as_view()
