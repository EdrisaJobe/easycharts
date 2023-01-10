from django.db import models

# Create your models here.
class UserInput(models.Model):
    
    category = models.CharField(max_length=100, blank=False, verbose_name="")
    num_of_items = models.IntegerField(verbose_name="")
    
    def __str__(self):
        
        return f'{self.category} - {self.num_of_items}'