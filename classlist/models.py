from django.db import models

# Create your models here.

class MyBaseModel(models.Model):
    class Meta:
        abstract=True

    a_field = models.CharField(max_length=2)

    def some_method(self):
        print("some method called @ %s" % str(self))

    def __str__(self):
        print("Output")
        return self.__class__.__name__

class A(MyBaseModel):
    name = models.CharField(max_length=255)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print("Constructor")

class B(MyBaseModel):
    name = models.CharField(max_length=255)

class C(MyBaseModel):
    name = models.CharField(max_length=255)

class D(MyBaseModel):
    name = models.CharField(max_length=255)

