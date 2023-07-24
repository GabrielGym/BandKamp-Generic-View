from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator( queryset=User.objects.all(), message="A user with that username already exists.",)],)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())],)
    
    class Meta:
        model = User
        fields = ["id", "email", "full_name", "artistic_name", "username", "password"]
        extra_kwargs = {
            "full_name": {"allow_null": True, "default": None},
            "password": {"write_only":True}
        }

        def create(self, validated_data: dict) -> User:
            return User.objects.create_user(**validated_data)

        def update(self, instance: User, validated_data: dict) -> User:
            for key, value in validated_data.items(): 
                setattr(instance, key, value)
                
            instance.set_password(validated_data["password"]) 

            return instance
