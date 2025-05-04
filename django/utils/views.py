from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    action_permissions = {}
    action_serializers = {}

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)

    def get_permissions(self):
        permissions = self.action_permissions.get(self.action, self.permission_classes)
        return (permission() for permission in permissions)
