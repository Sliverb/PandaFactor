from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime

# Enum of possible user type mask values
class UserTypeMasks:
    Business = 1
    School   = 2
    Student  = 4
    MaxValue = (Business | School | Student)

    
class InternNestUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, date_of_birth, email, user_type_mask, password):
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')
        if not email:
            raise ValueError('Users must have an email address')
        if (user_type_mask <= 0 or user_type_mask > UserTypeMasks.MaxValue):
            raise ValueError('Users must have a valid user type. ' + user_type_mask + ' is not supported')

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            email = InternNestUserManager.normalize_email(email),
            user_type_mask = user_type_mask,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            first_name = "JARON",
            last_name = "Andre",
            date_of_birth = datetime.now(),
            email = email,
            user_type_mask = 4,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class InternNestUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, db_index=True, max_length=254)
    date_of_birth = models.DateField()
    last_login_at = models.DateField(default=datetime.now())
    user_type_mask = models.IntegerField()
    
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    
    objects = InternNestUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
        
    def __unicode__(self):
        return self.email
     
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True # Simplest possible answer: Yes, always

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True # Simplest possible answer: Yes, always
     
    @property
    def is_staff(self):
        return self.is_admin
        
    def is_business(self):
        return self.user_type_mask & UserTypeMasks.Business
        
    def is_student(self):
        return self.user_type_mask & UserTypeMasks.Student
    
    def is_school(self):
        return self.user_type_mask & UserTypeMasks.School

