from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "role",
            "password",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "is_active"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def validate_email(self, value):
        user = self.context.get("request").user if self.context.get("request") else None
        queryset = User.objects.filter(email=value)

        # If updating existing user, exclude self from uniqueness check
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Email is already in use.")

        # Email format validation
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")

        return value

    def validate_username(self, value):
        queryset = User.objects.filter(username=value)

        # Exclude current user when updating
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Username is already in use.")
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
