from django.db import models

class User(models.Model):
    login_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s %s' % (self.login_id, self.password)

class Tag(models.Model):
    title = models.CharField(max_length=1000)

class Content(models.Model):
    tag = models.ForeignKey(Tag)
    content = models.TextField()
    author = models.ForeignKey(User)
    createDate = models.DateTimeField()
    updateDate = models.DateTimeField()
    
class UserLog(models.Model):
    login_date = models.DateTimeField()
    status = models.IntegerField()
    login_ip = models.GenericIPAddressField()
    login_user = models.ForeignKey(User)
    
    
    

    
    
