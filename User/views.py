from .serializers import UserInformationserializer
from .models import UserInformation
from rest_framework import viewsets

class UserInformationViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationserializer