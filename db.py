from tortoise.models import Model
from tortoise import fields


class Ip(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=300 ,unique=True)
    ip = fields.TextField(null=True)
