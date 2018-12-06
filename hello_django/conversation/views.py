from django.views.generic import View
from django.http import JsonResponse


class NCCOView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            [{"action": "talk", "text": "Hello World from Django"}], safe=False
        )
