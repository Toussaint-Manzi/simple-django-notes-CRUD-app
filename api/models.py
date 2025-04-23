import uuid
from django.db import models


class Note(models.Model):
    # Enum values for note types
    class NoteType(models.TextChoices):
        PERSONAL = "personal", "Personal"
        WORK = "work", "Work"
        FINANCES = "finances", "Finances"
        OTHERS = "others", "Others"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(
        max_length=10,
        choices=NoteType.choices,
        default=NoteType.PERSONAL,
        error_messages={
            "invalid_choice": "Type must be one of: personal, work, finances, others"
        },
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
