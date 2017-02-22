from django.db import models

# Create your models here.

class MyBaseModel(models.Model):
    class Meta:
        abstract=True

    a_field = models.CharField(max_length=2)

    @classmethod
    def some_method(cls):
        print("some method called")

    @classmethod
    def __str__(cls):
        print("Output")
        return cls.__name__

class A(MyBaseModel):
    name = models.CharField(max_length=255)
    def __init__(self,*args,**kwargs):
        import pdb;pdb.set_trace()
        super().__init__(*args,**kwargs)
        print("Constructor")

class B(MyBaseModel):
    name = models.CharField(max_length=255)

class C(MyBaseModel):
    name = models.CharField(max_length=255)

class D(MyBaseModel):
    name = models.CharField(max_length=255)

