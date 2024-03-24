from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

#  Contact Page
class Contact(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    contactno = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),])
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.fname + ' ' + self.lname

    class Meta:
        verbose_name = "Contact Page Responses"
        verbose_name_plural = "Contact Page Responses"



# Mumbai Counselling
class MumbaiCounselling(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ACADEMY = [
        ('wakade', 'Wakade\'s Classes'),
        ('saraswati', 'Saraswati Coaching Classes'),
        ('nota', 'None Of The Above'),
    ]

    studentName = models.CharField(max_length=40, null=True, blank=True)
    studentEmail = models.EmailField(max_length=40, null=True, blank=True)
    studentPhone = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    studentTelegram = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    studentGender = models.CharField(max_length=40, choices=GENDER_CHOICES, null=True, blank=True)
    studentpcmscore = models.PositiveIntegerField(null=True, blank=True)
    studentjeescore = models.PositiveIntegerField(null=True, blank=True)
    academy = models.CharField(max_length=40, choices=ACADEMY, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.studentName

    class Meta:
        verbose_name = "Mumbai Counselling"
        verbose_name_plural = "Mumbai Counselling"


# Maharashtra Counselling
class Aniket(models.Model):
    DISTRICT = [
        ('ahmednagar','Ahmednagar'),
        ('akola', 'Akola'),
        ('amravati', 'Amravati'),
        ('beed', 'Beed'),
        ('bhandara', 'Bhandara'),
        ('buldhana', 'buldhana'),
        ('chandrapur', 'Chandrapur'),
        ('aurangabad', 'Chhatrapati Sambhaji Nagar'),
        ('dharashiv', 'Dharashiv'),
        ('dhule', 'Dhule'),
        ('gadchiroli', 'Gadchiroli'),
        ('gondia', 'Gondia'),
        ('hingoli', 'Hingoli'),
        ('jalgaon', 'Jalgaon'),
        ('kolhpaur', 'Kolhpaur'),
        ('latur', 'Latur'),
        ('mumbai', 'Mumbai'),
        ('nagpur', 'Nagpur'),
        ('nanded', 'Nanded'),
        ('nandurbar', 'Nandurbar'),
        ('nashik', 'Nashik'),
        ('palghar', 'Palghar'),
        ('parbhani', 'Parbhani'),
        ('pune', 'Pune'),
        ('raigad', 'Raigad'),
        ('ratnagiri', 'Ratnagiri'),
        ('sangli', 'Sangli'),
        ('satara', 'Satara'),
        ('solapur', 'Solapur'),
        ('sindhudurg', 'Sindhudurg'),
        ('thane', 'Thane'),
        ('wardha', 'Wardha'),
        ('washim', 'Washim'),
        ('yavatmal', 'Yavatmal'),
        ('outside', 'Outside Maharshtra'),
    ]


    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    PREFERENCE = [
        ('engineering', 'Engineering'),
        ('pharmacy', 'Pharmacy'),
        ('both', 'Both'),
    ]
    
    name = models.CharField(max_length=40, null=True, blank=True)
    phone = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    telegram = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null=True, blank=True)
    pcmscore = models.PositiveIntegerField(null=True, blank=True)
    pcbscore = models.PositiveIntegerField(null=True, blank=True)
    centralscore = models.PositiveIntegerField(null=True, blank=True)
    preference = models.CharField(max_length=40, choices=PREFERENCE, null=True, blank=True)
    locations = models.CharField(max_length=40, choices=DISTRICT, null=True, blank=True)
    source = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aniket"
        verbose_name_plural = "Maharashtra: Aniket"



class Samkit(models.Model):
    DISTRICT = [
        ('ahmednagar','Ahmednagar'),
        ('akola', 'Akola'),
        ('amravati', 'Amravati'),
        ('beed', 'Beed'),
        ('bhandara', 'Bhandara'),
        ('buldhana', 'buldhana'),
        ('chandrapur', 'Chandrapur'),
        ('aurangabad', 'Chhatrapati Sambhaji Nagar'),
        ('dharashiv', 'Dharashiv'),
        ('dhule', 'Dhule'),
        ('gadchiroli', 'Gadchiroli'),
        ('gondia', 'Gondia'),
        ('hingoli', 'Hingoli'),
        ('jalgaon', 'Jalgaon'),
        ('kolhpaur', 'Kolhpaur'),
        ('latur', 'Latur'),
        ('mumbai', 'Mumbai'),
        ('nagpur', 'Nagpur'),
        ('nanded', 'Nanded'),
        ('nandurbar', 'Nandurbar'),
        ('nashik', 'Nashik'),
        ('palghar', 'Palghar'),
        ('parbhani', 'Parbhani'),
        ('pune', 'Pune'),
        ('raigad', 'Raigad'),
        ('ratnagiri', 'Ratnagiri'),
        ('sangli', 'Sangli'),
        ('satara', 'Satara'),
        ('solapur', 'Solapur'),
        ('sindhudurg', 'Sindhudurg'),
        ('thane', 'Thane'),
        ('wardha', 'Wardha'),
        ('washim', 'Washim'),
        ('yavatmal', 'Yavatmal'),
        ('outside', 'Outside Maharshtra'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    PREFERENCE = [
        ('engineering', 'Engineering'),
        ('pharmacy', 'Pharmacy'),
        ('both', 'Both'),
    ]
    
    name = models.CharField(max_length=40, null=True, blank=True)
    phone = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    telegram = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null=True, blank=True)
    pcmscore = models.PositiveIntegerField(null=True, blank=True)
    pcbscore = models.PositiveIntegerField(null=True, blank=True)
    centralscore = models.PositiveIntegerField(null=True, blank=True)
    preference = models.CharField(max_length=40, choices=PREFERENCE, null=True, blank=True)
    locations = models.CharField(max_length=40, choices=DISTRICT, null=True, blank=True)
    source = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Samkit"
        verbose_name_plural = "Maharashtra: Samkit"

# Swift Undergrads Referral
class Swift(models.Model):
    DISTRICT = [
        ('ahmednagar','Ahmednagar'),
        ('akola', 'Akola'),
        ('amravati', 'Amravati'),
        ('beed', 'Beed'),
        ('bhandara', 'Bhandara'),
        ('buldhana', 'buldhana'),
        ('chandrapur', 'Chandrapur'),
        ('aurangabad', 'Chhatrapati Sambhaji Nagar'),
        ('dharashiv', 'Dharashiv'),
        ('dhule', 'Dhule'),
        ('gadchiroli', 'Gadchiroli'),
        ('gondia', 'Gondia'),
        ('hingoli', 'Hingoli'),
        ('jalgaon', 'Jalgaon'),
        ('kolhpaur', 'Kolhpaur'),
        ('latur', 'Latur'),
        ('mumbai', 'Mumbai'),
        ('nagpur', 'Nagpur'),
        ('nanded', 'Nanded'),
        ('nandurbar', 'Nandurbar'),
        ('nashik', 'Nashik'),
        ('palghar', 'Palghar'),
        ('parbhani', 'Parbhani'),
        ('pune', 'Pune'),
        ('raigad', 'Raigad'),
        ('ratnagiri', 'Ratnagiri'),
        ('sangli', 'Sangli'),
        ('satara', 'Satara'),
        ('solapur', 'Solapur'),
        ('sindhudurg', 'Sindhudurg'),
        ('thane', 'Thane'),
        ('wardha', 'Wardha'),
        ('washim', 'Washim'),
        ('yavatmal', 'Yavatmal'),
        ('outside', 'Outside Maharshtra'),
    ]


    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    PREFERENCE = [
        ('engineering', 'Engineering'),
        ('pharmacy', 'Pharmacy'),
        ('both', 'Both'),
    ]
    
    name = models.CharField(max_length=40, null=True, blank=True)
    phone = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    telegram = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null=True, blank=True)
    pcmscore = models.PositiveIntegerField(null=True, blank=True)
    pcbscore = models.PositiveIntegerField(null=True, blank=True)
    centralscore = models.PositiveIntegerField(null=True, blank=True)
    preference = models.CharField(max_length=40, choices=PREFERENCE, null=True, blank=True)
    locations = models.CharField(max_length=40, choices=DISTRICT, null=True, blank=True)
    source = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Swift"
        verbose_name_plural = "Maharashtra: Swift Undergrads"

class Others(models.Model):
    DISTRICT = [
        ('ahmednagar','Ahmednagar'),
        ('akola', 'Akola'),
        ('amravati', 'Amravati'),
        ('beed', 'Beed'),
        ('bhandara', 'Bhandara'),
        ('buldhana', 'buldhana'),
        ('chandrapur', 'Chandrapur'),
        ('aurangabad', 'Chhatrapati Sambhaji Nagar'),
        ('dharashiv', 'Dharashiv'),
        ('dhule', 'Dhule'),
        ('gadchiroli', 'Gadchiroli'),
        ('gondia', 'Gondia'),
        ('hingoli', 'Hingoli'),
        ('jalgaon', 'Jalgaon'),
        ('kolhpaur', 'Kolhpaur'),
        ('latur', 'Latur'),
        ('mumbai', 'Mumbai'),
        ('nagpur', 'Nagpur'),
        ('nanded', 'Nanded'),
        ('nandurbar', 'Nandurbar'),
        ('nashik', 'Nashik'),
        ('palghar', 'Palghar'),
        ('parbhani', 'Parbhani'),
        ('pune', 'Pune'),
        ('raigad', 'Raigad'),
        ('ratnagiri', 'Ratnagiri'),
        ('sangli', 'Sangli'),
        ('satara', 'Satara'),
        ('solapur', 'Solapur'),
        ('sindhudurg', 'Sindhudurg'),
        ('thane', 'Thane'),
        ('wardha', 'Wardha'),
        ('washim', 'Washim'),
        ('yavatmal', 'Yavatmal'),
        ('outside', 'Outside Maharshtra'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    PREFERENCE = [
        ('engineering', 'Engineering'),
        ('pharmacy', 'Pharmacy'),
        ('both', 'Both'),
    ]
    
    name = models.CharField(max_length=40, null=True, blank=True)
    phone = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    telegram = models.IntegerField(validators=[MinValueValidator(6000000000, message='Invalid contact number'), MaxValueValidator(9999999999, message='Invalid contact number'),], null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES, null=True, blank=True)
    pcmscore = models.PositiveIntegerField(null=True, blank=True)
    pcbscore = models.PositiveIntegerField(null=True, blank=True)
    centralscore = models.PositiveIntegerField(null=True, blank=True)
    preference = models.CharField(max_length=40, choices=PREFERENCE, null=True, blank=True)
    locations = models.CharField(max_length=40, choices=DISTRICT, null=True, blank=True)
    source = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Others"
        verbose_name_plural = "Maharashtra: Others"



# Payment Transaction Records
class PaymentRecords(models.Model):
    upiname = models.CharField(max_length=40, null=True, blank=True)
    transactionid = models.CharField(max_length=40, null=True, blank=True)

    def __str__(mine):
        return mine.upiname

    class Meta:
        verbose_name = "Payment Records"
        verbose_name_plural = "Payment Records"

