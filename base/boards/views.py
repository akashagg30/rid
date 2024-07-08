from base.boards.permissions import CreateBoardPermission
from rest_framework import status, generics

class CreateBoardView(generics.CreateAPIView):
    permission_classes = (CreateBoardPermission,)
    