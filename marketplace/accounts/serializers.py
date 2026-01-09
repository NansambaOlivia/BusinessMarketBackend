from rest_framework import serializers
from .models import User, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'can_create_product', 'can_edit_product',
                  'can_approve_product', 'can_delete_product', 'can_manage_users']

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)  # nested role info
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), write_only=True, source='role'
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'role_id', 'business', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'business': {'read_only': True}  
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        # Assign the same business as the request user
        user.business = self.context['request'].user.business
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
