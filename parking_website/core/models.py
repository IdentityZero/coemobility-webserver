from django.db import models

# Create your models here.
class UsersDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    dept_abbr = models.CharField(unique=True, max_length=10)
    dept_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users_department'