from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Todo.models import TdList
from .serializers import todolistserializer
from rest_framework.generics import get_object_or_404

#APIView를 상속받은 클래스 안에서 request method 함수를 정의하여 사용
class UserTodoList(APIView):
    def post(self, request):
        tdserializer = todolistserializer(data=request.data)

        if tdserializer.is_valid():
            tdserializer.save()
            return Response({"message":"등록되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${tdserializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request):
        TodoList_id = get_object_or_404(TdList, user_id= ['user_id_id'])
        TodoList_id.data = request.data
        tdserializer = todolistserializer(data=request.data)

    def get(self, request):
        showing = TdList.objects.all()
        swserializer = todolistserializer(showing, many=True)
        return Response(swserializer.data)
    
    # def delete(self, request, pk):
    #     remove = TdList.objects.get(pk)
    #     remove.delete()
    #     return Response("삭제완료.")
    
    def get_object(self, pk):
        try:
            return TdList.objects.get(pk=pk)
        except TdList.DoesNotExist:
            raise Http404
    
    def delete(self, request, pk, format=None):
        TdList = self.get_object(pk)
        TdList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)