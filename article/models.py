from django.db import models
from tag.models import Tag
from mistune import markdown
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    raw_content = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    background = models.CharField(null=True,max_length=500)
    description = models.CharField(max_length=200,null=True)
    vote = models.IntegerField(default=0)
    pub_date=models.DateTimeField(editable=False)
    
    @property
    def render_content(self):
        return markdown(self.raw_content)

    @property
    def pub_time_format(self):
        return self.pub_date.strftime('%B %d, %Y')
    def save(self,*args,**kwargs):
        if not self.pub_date:
            self.pub_date=timezone.now()
        super(Article,self).save(*args,**kwargs)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-pub_date',)
            
        


# Create your models here.
