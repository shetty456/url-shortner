from tortoise.models import Model
from tortoise import fields
import datetime

class URL(Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=2048)
    short_code = fields.CharField(max_length=10, unique=True)
    created_at = fields.DatetimeField(default=datetime.datetime.utcnow)
    updated_at = fields.DatetimeField(auto_now=True)
    access_count = fields.IntField(default=0)

    class Meta:
        table = "urls"
