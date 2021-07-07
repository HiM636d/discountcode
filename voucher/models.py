from django.db import models
from django.db.models.fields.related import ForeignKey



#model Groups that will hold the name of the groups connected to codes
class Groups(models.Model):
    groupName=models.CharField(max_length=50,null=True,blank=True)

#model Code That will hold all the generated codes and relate them in a many to one relationship to Groups
class Code(models.Model):
    code=models.CharField(max_length=15)
    Group=models.ForeignKey("Groups",on_delete=models.CASCADE,related_name='Code')
    

   

