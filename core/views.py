from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello World'}
        return Response(content)

#### python manage.py drf_create_token <username>.
#### pip install httpie.
####http http://127.0.0.1:8000/hello/  "Authorization: Token 8d6c8894404ea48d17186c85cb0547e980b966b6"


