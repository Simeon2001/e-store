from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [JSONParser]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


@api_view(["post"])
def authrtoken(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            log = authenticate(username=username, password=password)
            login = str(Token.objects.get(user_id=log.id))
            

            return Response(
                {"status": True, "token": login},
                status=status.HTTP_202_ACCEPTED,
            )
           

        except AttributeError:
            return Response(
                {
                    "status": False,
                    "message": "Please enter the correct username and password",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

    else:
        return Response(
            {"status": False, "MESSAGE": "I DONT ACCEPT GET REQUEST"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
