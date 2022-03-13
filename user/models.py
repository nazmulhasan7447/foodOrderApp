from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, phone_no, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_no=phone_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_no, password=None):
        user = self.create_user(
            email,
            username=username,
            phone_no=phone_no,
            password=password,
        )

        user.is_admin = True
        user.is_a_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    options = (
        ('1', 'Verified'),
        ('0', 'Not Verified'),
    )

    fname = models.CharField(max_length=255, default='')
    lname = models.CharField(max_length=255, default='')
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(verbose_name='username', max_length=50, unique=True)
    phone_no = models.CharField(max_length=255, default='', unique=True)
    nid_no = models.CharField(max_length=255, default='', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_a_staff = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=options, blank=True, null=True, default=0)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_no']

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# verification code model
class VerificationCode(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    user_email = models.CharField(max_length=255, default='', blank=True, null=True)
    code = models.CharField(max_length=6, default='')
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return str(self.user_email) + '|| Code: ' + self.code
