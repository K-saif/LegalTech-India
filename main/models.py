from django.db import models
from django.utils.text import slugify

class ServiceManager(models.Manager):
    search_fields = ['title', 'description', 'price', 'duration', 'slug']

    def create_service(self, title, description, price, duration, image):
        service = self.create(title=title, description=description, price=price, duration=duration, image=image)
        service.slug = slugify(service.title)
        service.save()
        return service

class Documents(models.Model):
    doc_name = models.CharField(max_length=200)

    def __str__(self):
        return self.doc_name    
    
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, default='7972797444' )
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email
    
class Business_Registration(models.Model):
    main_service = models.CharField(max_length=50,default="Business Registration" )
    main_service_link = models.CharField(max_length=50, default="/business/")
    name = models.CharField(max_length=200)
    description1 = models.TextField()
    sec_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    third_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    quote = models.CharField(max_length=200)
    doc_title = models.CharField(max_length=200 ,default='Required Documents')
    documents = models.ManyToManyField(Documents)
    con_title = models.CharField(max_length=200, default='Conclusion')
    conclusion = models.TextField(default='default')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    question1 = models.CharField(max_length=255 , default='question1')
    answer1 = models.TextField( default='answer1')
    question2 = models.CharField(max_length=255, default='question2')
    answer2 = models.TextField(default='answer2')
    question3 = models.CharField(max_length=255, default='question3')
    answer3 = models.TextField(default='answer3')
    question4 = models.CharField(max_length=255, default='question4')
    answer4 = models.TextField(default='answer4')
    question5 = models.CharField(max_length=255, default='question5')
    answer5 = models.TextField(default='answer5')


    objects = ServiceManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Business_Registration, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
     
class Registration_Licencing(models.Model):
    main_service = models.CharField(max_length=50,default="Registration and Licencing" )
    main_service_link = models.CharField(max_length=50, default="/licencing/")
    name = models.CharField(max_length=200)
    description1 = models.TextField()
    sec_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    third_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    quote = models.CharField(max_length=200)
    doc_title = models.CharField(max_length=200 ,default='Required Documents')
    documents = models.ManyToManyField(Documents)
    con_title = models.CharField(max_length=200, default='Conclusion')
    conclusion = models.TextField(default='default')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    question1 = models.CharField(max_length=255 , default='question1')
    answer1 = models.TextField( default='answer1')
    question2 = models.CharField(max_length=255, default='question2')
    answer2 = models.TextField(default='answer2')
    question3 = models.CharField(max_length=255, default='question3')
    answer3 = models.TextField(default='answer3')
    question4 = models.CharField(max_length=255, default='question4')
    answer4 = models.TextField(default='answer4')
    question5 = models.CharField(max_length=255, default='question5')
    answer5 = models.TextField(default='answer5')

    objects = ServiceManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Registration_Licencing, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Gst_IncomeTax(models.Model):
    main_service = models.CharField(max_length=50,default="GST and Tax" )
    main_service_link = models.CharField(max_length=50, default="/taxation/")
    name = models.CharField(max_length=200)
    description1 = models.TextField()
    sec_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    third_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    quote = models.CharField(max_length=200)
    doc_title = models.CharField(max_length=200 ,default='Required Documents')
    documents = models.ManyToManyField(Documents)
    con_title = models.CharField(max_length=200, default='Conclusion')
    conclusion = models.TextField(default='default')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    question1 = models.CharField(max_length=255 , default='question1')
    answer1 = models.TextField( default='answer1')
    question2 = models.CharField(max_length=255, default='question2')
    answer2 = models.TextField(default='answer2')
    question3 = models.CharField(max_length=255, default='question3')
    answer3 = models.TextField(default='answer3')
    question4 = models.CharField(max_length=255, default='question4')
    answer4 = models.TextField(default='answer4')
    question5 = models.CharField(max_length=255, default='question5')
    answer5 = models.TextField(default='answer5')

    objects = ServiceManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Gst_IncomeTax, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Intellectual_Property(models.Model):
    main_service = models.CharField(max_length=50,default="Intellectual Property" )
    main_service_link = models.CharField(max_length=50, default="/ipr/")
    name = models.CharField(max_length=200)
    description1 = models.TextField()
    sec_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    third_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    quote = models.CharField(max_length=200)
    doc_title = models.CharField(max_length=200 ,default='Required Documents')
    documents = models.ManyToManyField(Documents)
    con_title = models.CharField(max_length=200, default='Conclusion')
    conclusion = models.TextField(default='default')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    question1 = models.CharField(max_length=255 , default='question1')
    answer1 = models.TextField( default='answer1')
    question2 = models.CharField(max_length=255, default='question2')
    answer2 = models.TextField(default='answer2')
    question3 = models.CharField(max_length=255, default='question3')
    answer3 = models.TextField(default='answer3')
    question4 = models.CharField(max_length=255, default='question4')
    answer4 = models.TextField(default='answer4')
    question5 = models.CharField(max_length=255, default='question5')
    answer5 = models.TextField(default='answer5')

    objects = ServiceManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Intellectual_Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Information_Technology(models.Model):
    main_service = models.CharField(max_length=50,default="Information Technology" )
    main_service_link = models.CharField(max_length=50, default="/it/")
    name = models.CharField(max_length=200)
    description1 = models.TextField()
    sec_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    third_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    quote = models.CharField(max_length=200)
    doc_title = models.CharField(max_length=200 ,default='Required Documents')
    documents = models.ManyToManyField(Documents)
    con_title = models.CharField(max_length=200, default='Conclusion')
    conclusion = models.TextField(default='default')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    question1 = models.CharField(max_length=255 , default='question1')
    answer1 = models.TextField( default='answer1')
    question2 = models.CharField(max_length=255, default='question2')
    answer2 = models.TextField(default='answer2')
    question3 = models.CharField(max_length=255, default='question3')
    answer3 = models.TextField(default='answer3')
    question4 = models.CharField(max_length=255, default='question4')
    answer4 = models.TextField(default='answer4')
    question5 = models.CharField(max_length=255, default='question5')
    answer5 = models.TextField(default='answer5')

    objects = ServiceManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Information_Technology, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Other_Service(models.Model):
    main_service = models.CharField(max_length=50,default="Other Service" )
    main_service_link = models.CharField(max_length=50, default="/other/")
    name = models.CharField(max_length=200)
    description1 = models.TextField()
    sec_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    third_name = models.CharField(max_length=200 ,default='Service Details',blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    quote = models.CharField(max_length=200)
    doc_title = models.CharField(max_length=200 ,default='Required Documents')
    documents = models.ManyToManyField(Documents)
    con_title = models.CharField(max_length=200, default='Conclusion')
    conclusion = models.TextField(default='default')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    question1 = models.CharField(max_length=255 , default='question1')
    answer1 = models.TextField( default='answer1')
    question2 = models.CharField(max_length=255, default='question2')
    answer2 = models.TextField(default='answer2')
    question3 = models.CharField(max_length=255, default='question3')
    answer3 = models.TextField(default='answer3')
    question4 = models.CharField(max_length=255, default='question4')
    answer4 = models.TextField(default='answer4')
    question5 = models.CharField(max_length=255, default='question5')
    answer5 = models.TextField(default='answer5')

    objects = ServiceManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Other_Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
