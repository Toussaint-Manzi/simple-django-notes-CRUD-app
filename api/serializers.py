from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "type", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long"
            )
        return value.strip()

    def validate_type(self, value):
        valid_types = ["personal", "work", "finances", "others"]
        if value.lower() not in valid_types:
            raise serializers.ValidationError(
                f"Type must be one of: {', '.join(valid_types)}"
            )
        return value.lower()

    def validate_content(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Content must be at least 10 characters long"
            )
        return value.strip()

    def validate(self, data):
        # Object-level validation
        if "title" in data and "content" in data:
            if data["title"].lower() == data["content"].lower():
                raise serializers.ValidationError(
                    "Title and content cannot be identical"
                )
        return data
