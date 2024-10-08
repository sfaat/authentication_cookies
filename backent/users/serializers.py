from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import get_user_model
User=get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("firstname",'lastname', 'email','password')

    def validate(self, data):
        user=User(**data)
        password=data.get('password')
        try:
            validate_password(password, user)

        except exceptions.ValidationError as e:
            serializer_errors=serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {
                    "password":serializer_errors['non_field_errors']
                }
            )
        return data


    def create(self, validated_data):
        user=User.objects.create_user(
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("firstname",'lastname', 'email',)


