from django.db import models

class account(models.Model):
	account_id=models.IntegerField(default=1)
	account_name=models.CharField(max_length=100)
	debts = models.IntegerField()
	credit=models.IntegerField()

