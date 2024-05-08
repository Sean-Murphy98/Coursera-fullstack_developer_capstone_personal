# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    test = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    dealerId = models.IntegerField(blank=False)
    type = models.CharField(max_length=10, default="SUV",
            choices={"Sedan": "Sedan", "SUV": "SUV", "Wagon": "Wagon"})
    year = models.IntegerField(default=2023,
            validators=[
                MaxValueValidator(2023),
                MinValueValidator(2015)
            ])
    engineSize = models.DecimalField(max_digits=4,
                                     decimal_places=1)

    def __str__(self):
        return "Make " + self.car_make.name + "model " + 
        self.name + "type " + self.type
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
