from django.shortcuts import render

from django.views.generic import TemplateView


class GPTIndexView(TemplateView):
    template_name = "gpt/index.html"


gpt_index_view = GPTIndexView.as_view()
