from rest_framework import serializers
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user']




class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
    
        account = User.objects.create(username = username, email = email)
        account.set_password(password)
        account.save()
        return account
    

class UserLoginSerializer(serializers.Serializer):
    username =serializers.CharField(required = True)
    password =serializers.CharField(required = True)