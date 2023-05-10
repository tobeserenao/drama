import openai
from django.conf import settings

openai.api_key = settings.OPENAI_KEY


class ChatCompletionService:
    @classmethod
    def get_chat_completion(cls, model, conversation):
        completions = openai.ChatCompletion.create(model=model, messages=conversation)
        response = {'text': completions["choices"][0]["message"]["content"]}

        return response
