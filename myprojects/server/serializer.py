from rest_framework.serializers import SerializerMethodField, ModelSerializer
from .models import Server, Category, Channel 

class ChannelSerializer(ModelSerializer) : 
    class Meta : 
        model = Channel
        fields = '__all__'


class ServerSerializer (ModelSerializer) :
    num_members = SerializerMethodField()
    channel_server = ChannelSerializer(many=True)
    class Meta : 
        model = Server
        exclude = ('memeber',)
    
    def get_num_members(self, obj) :
        if hasattr(obj,'num_members') : 
            return obj.num_members
        else : 
            return None    