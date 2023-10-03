from django.db import models

# Create your models here.

class Header(models.Model):

    logo = models.ImageField('Logo', upload_to='images')
    title = models.CharField('Title', max_length=40)
    path1 = models.CharField('Path 1', max_length=40)
    path2 = models.CharField('Path 2', max_length=40)
    path3 = models.CharField('Path 3', max_length=40)
    path4 = models.CharField('Path 4', max_length=40)
    path5 = models.CharField('Path 5', max_length=40)
    path6 = models.CharField('Path 6', max_length=40)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Home(models.Model):

    background1 = models.ImageField('Background 1', upload_to='images')
    background2 = models.ImageField('Background 2', upload_to='images')
    background3 = models.ImageField('Background 3', upload_to='images')
    subtitle = models.CharField('Subtitle', max_length=50)
    title = models.CharField('Title', max_length=40)
    text = models.CharField('Text', max_length=80)
    button1 = models.CharField('Button 1', max_length=30)
    button2 = models.CharField('Button 2', max_length=30)

    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class About(models.Model):

    video = models.FileField('Video', upload_to='videos')
    video_title1 = models.CharField('Video Title 1', max_length=30)
    video_title2 = models.CharField('Video Title 2', max_length=30)
    subtitle = models.CharField('Subtitle', max_length=40)
    title = models.CharField('Title', max_length=50)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    button = models.CharField('Button', max_length=30)
    
    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class Title(models.Model):

    member_subtitle = models.CharField('Member Subtitle', max_length=50)
    member_title = models.CharField('Member title', max_length=40)
    review_subtitle = models.CharField('Review Subtitle', max_length=50)
    review_title = models.CharField('Review title', max_length=40)
    contact_subtitle = models.CharField('Contact Subtitle', max_length=50)
    contact_title = models.CharField('Contact title', max_length=40)
    reservation_subtitle = models.CharField('Reservation Subtitle', max_length=50)
    reservation_title = models.CharField('Reservation title', max_length=40)

class Member(models.Model):

    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=40)
    position = models.CharField('Position', max_length=30)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return f'{self.name} ---------------------------- {self.position}'

class Menu(models.Model):

    background = models.ImageField('Background', upload_to='images')

    class Meta:

        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

class MenuCategory(models.Model):

    subtitle = models.CharField('SubTitle', max_length=50)
    title = models.CharField('Title', max_length=40)

    class Meta:

        verbose_name = 'Menu Category'
        verbose_name_plural = 'Menu Category'

    def __str__(self) -> str:
        return self.title

class MenuContent(models.Model):

    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    recommend = models.BooleanField('Recommend', blank=True)
    price = models.FloatField('Price')
    new_price = models.FloatField('New Price', blank=True, null=True)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return f'{self.name} ------------------------ {self.category.title}'
    
class Testimonial(models.Model):

    background = models.ImageField('Background', upload_to='images')
    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=30)
    info = models.CharField('Info', max_length=40)
    text = models.TextField('Text')
    rating = models.FloatField('Rating')

    def __str__(self) -> str:
        return self.name
    
class ContactInfo(models.Model):

    background = models.ImageField('Background', upload_to='images')
    google_map = models.TextField('Google Map')
    button = models.CharField('Button', max_length=30)

class Footer(models.Model):

    address = models.CharField('Address', max_length=80)
    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')
    phone = models.CharField('Phone Number', max_length=30)
    email = models.EmailField('Email')

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

class OpenHours(models.Model):

    day = models.CharField('Day', max_length=30)
    time = models.CharField('Time', max_length=20)

    class Meta:

        verbose_name = 'Open Hours'
        verbose_name_plural = 'Open Hours'

    def __str__(self) -> str:
        return f'{self.day} ----------------------- {self.time}'
    
class Contact(models.Model):

    user_name = models.CharField('Name', max_length=50)
    user_email = models.EmailField('Email')
    user_message = models.TextField('Message')

    def __str__(self) -> str:
        return self.user_name
    
class ReservationInfo(models.Model):

    background = models.ImageField('Background', upload_to='images')
    button = models.CharField('Button', max_length=30)
    img = models.ImageField('Image', upload_to='images')

class Reservation(models.Model):

    user_name = models.CharField('Name', max_length=60)
    user_phone = models.CharField('Phone Number', max_length=30)
    user_time = models.CharField('Time', max_length=10)
    user_date = models.DateField('Date')
    user_count = models.IntegerField('Count')
    user_message = models.TextField('Message', null=True, blank=True)

    def __str__(self) -> str:
        return self.user_name