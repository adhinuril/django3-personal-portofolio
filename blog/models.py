from django.db import models

class Blog(models.Model) :
    title = models.CharField(max_length=100)
    post_date = models.DateField(auto_now=True)
    content = models.CharField(max_length=500)

    def __str__(self) :
        return self.title 

