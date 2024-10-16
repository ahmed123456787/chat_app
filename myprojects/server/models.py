from django.db import models
from django.conf import settings


def get_category_path(instance, filename) : 
    return f"category/{instance.id}/category_icon/{filename}"




class Category(models.Model) :
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(null=True, blank=True,upload_to=get_category_path)
    
    def save(self,*args,**kwargs) :
        pass
    
    
    def __str__(self) : 
        return self.name

class Server(models.Model) :
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='server_owner')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True, null=True)   
    memeber = models.ManyToManyField(settings.AUTH_USER_MODEL)  
    
    def __str__(self) : 
        return self.name
    
class Channel(models.Model) : 
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='channel_owner')
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server,on_delete=models.CASCADE,related_name='channel_server')

    def save(self,*args, **kwargs):
        self.name = self.name.lower()
        super(Channel,self).save()
    
    def __str__(self) : 
        return self.name         