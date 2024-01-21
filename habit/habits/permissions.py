from rest_framework.permissions import BasePermission




class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class CustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
            if request.user != obj.user:
                if obj.is_public:
                    return True
                return False
            return True

