from django.shortcuts import render
from rest_framework import viewsets
from .models import Server 
from .serializer import ServerSerializer
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.exceptions import  ValidationError , AuthenticationFailed
from django.db.models import Count

class ServerListViewSet(viewsets.ViewSet) : 
     
    query_set = Server.objects.all() 
    
    def list (self, request) : 
        category = request.query_params.get('category')
        quantity = request.query_params.get('qty')
        by_user = request.query_params.get("by_user") == "true"
        by_server_id = request.query_params.get("server_id") 
        with_num_members = request.query_params.get("with_num_members") == "true"
        
        if category : 
            self.query_set = self.query_set.filter(category=category)
    
        if quantity : 
            self.query_set = self.query_set[ : int(quantity)] 
        
        if by_user :
            user_id = request.user.id
            self.query_set = self.query_set.filter(memeber=user_id)
        
        if with_num_members:
            self.query_set = self.query_set.annotate(num_members=Count('memeber'))
        
        if by_server_id:
            try:
                self.query_set = self.query_set.filter(id=by_server_id)
                if not self.query_set.exists():
                    raise ValidationError(detail="Server with id wrong")
            except :
                    ValidationError(detail="detail error")
                        
                
        
        
        serializer = ServerSerializer(self.query_set, many=True)
        return Response(serializer.data)