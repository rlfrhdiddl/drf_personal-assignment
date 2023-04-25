from rest_framework import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def sign_up(request):
    return Response("가입되었습니다!")