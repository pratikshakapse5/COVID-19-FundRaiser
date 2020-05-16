from django.db import models
from django.contrib.auth.models import User
import datetime
from uuid import UUID

Categories = (
    ('home','Home'),
    ('school', 'School'),
    ('work','Work'),
    ('self-improvement','Self-improvement'),
    ('other','Other'),
)

class OrganizationName(models.Model):
	orgName = models.CharField(max_length=128)
	
	def __str__(self):
		return self.orgName



class Donate(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	orgName = models.ForeignKey(OrganizationName,on_delete=models.CASCADE,null=True)
	amount=models.PositiveIntegerField(default=0)
	date = models.DateField(default=datetime.date.today)
	wish= models.CharField(max_length=100)
	#eyw_transactionref=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

class UserProfileCore(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	tasks_view_hide_flag=models.BooleanField(default=False)

def __str__(self):
	return self.user.username

    