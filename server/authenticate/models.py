from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations: True

    def create_user(self,login_id,name,password,**kwargs):
        if not name:
            raise ValueError('Users must have username')
        user=self.model(
            name=name,
            login_id =login_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,login_id=None,name=None,password=None,**extra_fields):
        superuser=self.create_user(
            login_id=login_id,
            name=name,
            password=password,
        )
        superuser.is_staff=True
        superuser.is_superuser=True
        superuser.is_active=True
        superuser.save(using=self._db)
        return superuser
class AuthUser(AbstractBaseUser,PermissionsMixin):
    id=models.AutoField(null=False,primary_key=True)
    login_id=models.CharField(max_length=30,unique=True,null=False,blank=False)
    name=models.CharField(max_length=15,unique=True,null=False,blank=False)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD='login_id'
    REQUIRED_FIELDS=['name']

    class Meta:
        db_table='authuser'
    