import models

# detect changes while migrating a class
class StudentSchema(models.Model):
    id = models.IntegerField(primary=True, default=1, autoincrement=True)
    course = models.CharField(max_length=255)
    is_active = models.BooleanField(default=1)

class PersonSchema(models.Model):
    id = models.IntegerField(primary=True, default=1, autoincrement=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(default=1, null=True, blank=True)

