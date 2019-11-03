from marshmallow import post_load

from ma import ma
from model.task import Task


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'done')
        
    @post_load
    def make_user(self, data, **kwargs):
        return Task(**data)
