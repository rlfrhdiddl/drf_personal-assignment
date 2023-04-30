from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from users.serializers import CustomTokenObtainPairSerializer, Userserializer, UserDetailSerializer
from .models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)


class UserSignup(APIView):
    def post(self, request):
        print("UserSignup_request", request)
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        

        
#너무 많은 시행착오를 겪었던 UserDetail....!!!
class UserDetail(APIView):
    def put(self, request):
        user_id = get_object_or_404(User, email=request.data["email"]) # models.User를 인자로 가져오고, request.data의 "email"을 email로 지정,     # 값이 없으면 404오류표시
        user_id.set_password(request.data["password"]) # 여기가 삽질 엄청 하다가 찾아낸 부분. 해시될 비밀번호는 request한 "password"여야 함.. 당연한데 왜 자꾸 여기서 직접 지정하려고 했을까..
        data = {"email": request.data["email"], "password": user_id.password, "username": request.data["username"],"gender": request.data["gender"] ,"age": request.data["age"], "introduction": request.data["introduction"]} # data라는 변수로 회원정보 딕셔너리를 만들었다. 이유는 아래 data=data부분때문에!
        serializer = UserDetailSerializer(user_id, data=data) # data=data를 data=request.data로 했었다. 그 때는 data dic를 해주지 않아서 request.data를 집어넣었는데, 결론적으로 set_password를 해놓고 다시 request.data의 password를 저장해버리니 바뀔리가 있나..
        print("데이터", request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정완료."})
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"message":"삭제완료."}, status=status.HTTP_204_NO_CONTENT)


class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response("aa")
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer