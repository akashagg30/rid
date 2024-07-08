from django.db import models
from base.boards.constants import BOARD_SLUG_MAX_LENGTH
from base.users.models import Users, Organizations, ExternalUsers

# Create your models here.
class Boards(models.Model):
    board_id = models.BigAutoField(primary_key=True)
    board_name = models.CharField(max_length=30)
    slug = models.CharField(max_length=BOARD_SLUG_MAX_LENGTH, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE, db_index=True)
    configurable_fields = models.JSONField(default={})
    configurable_fields_options = models.JSONField(default={})

class BoardCards(models.Model):
    PRIORIRTY_VERY_HIGH = 1
    PRIORIRTY_HIGH = 2
    PRIORITY_MEDIUM = 3
    PRIORITY_LOW = 4
    PRIORIRTY_VERY_LOW = 5
    
    PRIORITY_OPTIONS = (
        (PRIORIRTY_VERY_HIGH, "very high priority"),
        (PRIORIRTY_HIGH, "high priority"),
        (PRIORITY_MEDIUM, "medium priority"),
        (PRIORITY_LOW, "low priority"),
        (PRIORIRTY_VERY_LOW, "very low priority"),
    )
    
    card_id = models.BigAutoField(primary_key=True)
    board = models.ForeignKey(Boards, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=40, unique=True, db_index=True)
    description = models.TextField()
    status = models.CharField(max_length=20)
    priority = models.IntegerField(options=PRIORITY_OPTIONS)
    additional_field = models.JSONField(default={})
    meta = models.JSONField(default={})
    assigned_to = models.ForeignKey(Users, on_delete=models.SET_NULL)
    assigned_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    reportee = models.ForeignKey(ExternalUsers, on_delete=models.SET_NULL, null=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class BoardCardsComments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    card = models.ForeignKey(BoardCards, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now=True)
