from rest_framework import BasePermission

class CreateBoardPermission(BasePermission):
    def has_permission(self, request, view):
        return True