from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import todolistserializer

#APIView를 상속받은 클래스 안에서 request method 함수를 정의하여 사용
class UserTodoList(APIView):
    def post(self, request):
        print("UserTodoList_request", request)
        tdserializer = todolistserializer(data=request.data)

        if tdserializer.is_valid():
            tdserializer.save()
            return Response({"message":"등록되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${tdserializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)