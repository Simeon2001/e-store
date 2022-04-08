from rest_framework import serializers

# from .models import profile,Social_Media,site_links,feedback
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


UserModel = get_user_model()


# profile serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        new_token = Token.objects.create(user=user)
        return user

    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password"]
