from typing import Any, Dict
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "ひろき"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_service"] = "12345"
        ctxt["skills"] = [
            "Git",
            "Docker",
            "Python",
            "Numpy",
            "VB.net",
        ]
        return ctxt