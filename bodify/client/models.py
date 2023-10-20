from django.db import models

# Create your models here.
class exercises(models.Model):
    part_id= models.AutoField
    part_name=models.CharField(max_length=50)

    exercise1= models.CharField(max_length=50, default='')
    desc1= models.CharField(max_length= 500)
    image1 = models.ImageField(upload_to="exercises/images", default='')

    exercise2=models.CharField(max_length=50, default='')
    image2 = models.ImageField(upload_to="exercises/images", default='')
    desc2= models.CharField(max_length= 500)

    exercise3= models.CharField(max_length=50, default='')
    image3 = models.ImageField(upload_to="exercises/images", default='')
    desc3= models.CharField(max_length= 500)

    # pub_date= models.DateField()

    def __str__(self):
        return self.part_name