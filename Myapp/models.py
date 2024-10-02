from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from django.contrib.auth import get_user_model



# User = get_user_model()
# Create your models here.




from django.core.exceptions import ValidationError


    

# def validate_video_size(value):
#     limit = 15 * 1024 * 1024
#     if value.size > limit:
#         raise ValidationError('Video File is too large. Size should not Exceed 15MB.')



class Property(models.Model):
    STATUS_CHOICES =('For Rent','For Rent'),('For Sale','For Sale')
    P_STATUS_CHOICES =('Active','Active'),('Sold','Sold')
    MKOA = [('ARS','Arusha'), ('DSM','Dar es salaam'), ('DDM','Dodoma'), ('RVM','Ruvuma'), ('TBR','Tabora'), ('MBY','Mbeya'), ('MRG','Morogoro'), ('LND','Lindi'), ('KGM','Kigoma'),( 'KTV','Katavi'),('GIT','Geita'), ('MNR','Manyara'), ('KLR','Kilimanjaro'), ('MR','Mara'), ('MTR','Mtwara'), ('MZ','Mwanza'), ('NB','Njombe'), ('SNG','Songwe'), ('TNG','Tanga'), ('SNG','Shinyanga'), ('IRN','Iringa'), ('KGR','Kagera'), ('PMB','Pemba Kaskazini'), ('PK','Pemba Kusini'), ('PN','Pwani'),('RK','Rukwa'),('SGD','Singida'),('SMY','Simiyu'), ('ZKA','Zanzibar Kaskazini'), ('ZKU','Zanzibar Kusini'),('ZMG','Zanzibar Mjini Magharibi')]
    PROPERTY_TYPES = [('Apartment','Apartment'), ('House','House'),('Commercial','Commercial')]
    # name = models.CharField(max_length=10)

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    #bookmarks = models.ManyToManyField(User, related_name="bookmarked_properties", blank=True)
    status = models.CharField(max_length=30,choices=STATUS_CHOICES)
    p_status = models.CharField(max_length=30,choices=P_STATUS_CHOICES)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    country = models.CharField(max_length=25, default='Tanzania')
    region = models.CharField(max_length=30, choices=MKOA)
    district = models.CharField(max_length=30)
    ward = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    #rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    viewers = models.ManyToManyField(User, related_name='viewed_properties', blank=True)
    view_count = models.IntegerField(default=0)
    business_phone = models.CharField(max_length=13)
    business_email = models.EmailField(max_length=60)
    #kitchen = models.IntegerField()

    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_size = models.IntegerField()
    nearby = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    image1 = models.ImageField(upload_to='property_images/')
    image2 = models.ImageField(upload_to='property_images/')
    image3 = models.ImageField(upload_to='property_images/')
    property_owner = models.ImageField(upload_to='property_owner/')
    # video = models.FileField(upload_to='property_video/',validators=[validate_video_size], blank=True, null=True default=)
    video_link = models.URLField(max_length=300, blank=True, null=True)






    def add_view(self,user):
        if user not in self.viewers.all():
            self.viewers.add(user)
            self.view_count +=1
            self.save()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/property/{self.id}/"



class ChatMessage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver} at {self.timestamp}'



class Review(models.Model):
    # property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(default=0)

class Profile(models.Model):
    ROLE_CHOICE = [
        ('owner','Owner'),
        ('customer','Customer')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=20,choices=ROLE_CHOICE, default='customer')
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=250, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'





class PopularPlace(models.Model):
    name_of_place = models.CharField(max_length=50)
    number_of_property = models.IntegerField()
    image_of_place = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.name_of_place


class Offer(models.Model):
    Title = models.CharField(max_length=250)
    offer_image = models.ImageField(upload_to='property_images/')
    def __str__(self):
        return self.Title

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Transaction_image = models.ImageField(upload_to='transactions/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Myapp_payment'
    def __str__(self):
        return f" Payment by {self.user.username}"




class Featured(models.Model):
    f_property_name = models.OneToOneField(Property, related_name="featured_properties", on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_property_name.title

class PopularProperty(models.Model):
    p_property_name = models.OneToOneField(Property, related_name="popular_properties", on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_property_name.title

class Agent(models.Model):
    jina = models.CharField(max_length=50)
    Cheo = models.CharField(max_length=50)
    image_of_agent = models.ImageField(upload_to='property_images/')
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
    instagram_link = models.URLField(max_length=300, blank=True, null=True)
    linkedIn = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self. jina

class Partner(models.Model):
    jina = models.CharField(max_length=50)
    image_of_partners = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.jina





class Client(models.Model):
    name = models.CharField(max_length=50)  
    client_image = models.ImageField(upload_to='property_images/')
    location = models.CharField(max_length=50)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self. name





class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inquiries")
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inquiry from {self.full_name} for {self.property.title}'

