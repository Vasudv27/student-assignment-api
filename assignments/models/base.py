import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from assignments.middlewares import get_current_user
from django.db.models import Max

User = get_user_model()

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class DeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    auto_id = models.PositiveIntegerField(unique=True, editable=False, null=True, blank=True)

    creator = models.ForeignKey(
        User, related_name="created_%(class)s_objects",
        on_delete=models.SET_NULL, null=True, blank=True
    )
    updater = models.ForeignKey(
        User, related_name="updated_%(class)s_objects",
        on_delete=models.SET_NULL, null=True, blank=True
    )
    deleter = models.ForeignKey(
        User, related_name="deleted_%(class)s_objects",
        on_delete=models.SET_NULL, null=True, blank=True
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    objects = models.Manager()
    active_objects = ActiveManager()
    deleted_objects = DeletedManager()

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_deleted = True
        user = get_current_user()
        if user and user.is_authenticated:
            self.deleter = user
        self.save()

    def save(self, *args, **kwargs):
        user = get_current_user()

        # Assign auto_id manually on first save
        if not self.auto_id:
            max_id = self.__class__.objects.aggregate(max_auto_id=Max('auto_id'))['max_auto_id'] or 0
            self.auto_id = max_id + 1

        if not self.pk and user and user.is_authenticated:
            self.creator = user
        elif self.pk and user and user.is_authenticated:
            self.updater = user

        super().save(*args, **kwargs)
