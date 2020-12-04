from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from main.models import Ea
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        # user.is_admin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name = 'profile' , verbose_name='user', null=True)

    ea = models.ManyToManyField(Ea, blank=True, verbose_name='EA')


    GENDER_CATEGORY = (
        ('男', '男'),
        ('女', '女'),
        ('その他', 'その他')
    )
    gender = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        choices=GENDER_CATEGORY,
        default='none'
    )
    age = models.IntegerField(
        
        null=True,
        blank=True
    )
    username = models.CharField(max_length=30, null=True, blank=True)

    kana_username = models.CharField(max_length= 50,  null=True, blank=True)

    account = models.IntegerField( null=True, blank=True)
    
    login_count = models.IntegerField(verbose_name='login_count', default=0)
    def __str__(self):
        return str(( 'EA: ' + str(self.ea.all()), 'メールアドレス: '+ self.user.email, '口座番号: '+ str(self.account),  'ログイン回数: ' + str(self.login_count)))
#  '名前: '+ self.username+'('+self.kana_username +')', '性別: ' + self.gender, '歳: '+ str(self.age),