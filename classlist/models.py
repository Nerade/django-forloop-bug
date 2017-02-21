from django.db import models
from django.core.exceptions import ImproperlyConfigured,FieldDoesNotExist

class Case(models.Model):
    name = models.CharField(max_length=255)

class FormDocument(models.Model):
    class Meta:
        abstract = True

    date_created = models.DateTimeField(auto_now_add=True,editable=False)
    editable = models.BooleanField(default=True,editable=False,blank=True)

    def __init__(self,*args,**kwargs):
        super(FormDocument,self).__init__(*args,**kwargs)

        case_field = True
        try:
            case_type = self._meta.get_field('case')
        except FieldDoesNotExist:
            case_field = False
        if not (case_field and issubclass(case_type,models.ForeignKey)):
            raise ImproperlyConfigured(
                    ("The model '%(cls)s' is missing a Case field. "
                    "Successors of FormDocument model must implement a relation to a case instance." % 
                    {'cls':self.__class__.__name__}
                    ))

    def get_absolute_url(self):
        return reverse('core:form-direct',kwargs={'form_name':self.__class__.__name__.lower(),'pk':self.id})

    def get_display_datetime(self):
        return self.date_created.strftime("%d.%m.%Y %H:%M:%S")
    
    def get_display_date(self):
        return self.date_created.strftime("%d.%m.%Y")
    
    @classmethod
    def get_doc_type(cls):
        print("Doc type")
        return cls._meta.verbose_name

    def get_icon(self):
        if hasattr(self,'icon'):
            return self.icon

    def __str__(self):
        print("STR Bla!")
        return "{}-Formular {}".format(self._meta.verbose_name,self.get_display_date())

class A(FormDocument):
    class Meta:
        verbose_name = "A-Form"
    name = models.CharField(max_length=255)
    case = models.OneToOneField(Case)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print("Constructor")

class B(FormDocument):
    class Meta:
        verbose_name = "B-Form"
    name = models.CharField(max_length=255)
    case = models.ForeignKey(Case)

class C(FormDocument):
    class Meta:
        verbose_name = "C-Form"
    name = models.CharField(max_length=255)
    case = models.ForeignKey(Case)

class D(FormDocument):
    class Meta:
        verbose_name = "D-Form"
    name = models.CharField(max_length=255)
    case = models.OneToOneField(Case)

