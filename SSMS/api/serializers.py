from rest_framework import serializers
from .models import Custom_User, Subject, Mark
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ['id', 'username', 'email', 'role', 'password']

    def get_fields(self):
        fields = super(UserSerializer, self).get_fields()
        fields['password'].write_only = True
        return fields

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).update(instance, validated_data)

    

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subname','teacher']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id', 'student', 'subject', 'marks_obtained']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            return data
        raise serializers.ValidationError("Must include 'username' and 'password'.")