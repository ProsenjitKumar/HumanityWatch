
from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, BaseUserManager
)
from django.db.models.signals import post_save
from simple_history.models import HistoricalRecords



class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an Email address.")
        if not password:
            raise ValueError("Users must have a Password")
        if not full_name:
            raise ValueError("Users must have a Full Name")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=False # will be True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    #address = models.CharField(max_length=455)
    active = models.BooleanField(default=True) # Can Login
    staff = models.BooleanField(default=False) # staff user non Superuser
    admin = models.BooleanField(default=False) # Superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    # confirm = models.BooleanField(default=False)
    # confiremed_date = models.DateTimeField(default=False)

    # Profile
    first_address = models.CharField(max_length=255, blank=True)
    second_address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=12)
    update = models.DateTimeField(null=True, blank=True)
    last_donation_date = models.DateField(null=True, blank=True, unique=True)

    PROFESSION_CHOICES = (
        ('Student', 'Student'),
        ('Employer', 'Employer'),
        ('Unemployed', 'Unemployed'),
        ('Businessman', 'Businessman'),
    )
    profession = models.CharField(max_length=20, choices=PROFESSION_CHOICES)

    BLOOD_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    blood = models.CharField(max_length=20, choices=BLOOD_CHOICES)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)



    #changed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Personal Info
    age = models.IntegerField(default='')

    USERNAME_FIELD = 'email'  # Username
    # USERNAME_FILED and password are required by default
    REQUIRED_FIELDS = ['full_name'] # 'full_name'

    objects = UserManager()



    def __str__(self):
        return self.email

    def  get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



#register(User, inherit=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # extend extra data
    #lead = models.CharField(max_length=45)
    history = HistoricalRecords()
    #update_time = models.DateTimeField()
    #monthy_lead = models.ForeignKey(UserManager, on_delete=models.CASCADE)



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)



