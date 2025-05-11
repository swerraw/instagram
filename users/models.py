from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings



class CustomUserManager(UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        Создаёт суперпользователя с email и паролем.
        Если email не передан, то используем пустое значение.
        """
        if not email:
            email = ''  # Можно оставить пустым, если не передан email
        email = self.normalize_email(email)

        if not extra_fields.get('name'):
            raise ValueError('The Name field must be set')  # Обязательное поле name

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None  # отключаем поле username
    email = models.EmailField(blank=True, null=True)

    name = models.CharField(max_length=255, unique=True,  blank=False, null=False)  # добавлено поле name
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    links = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []  # теперь name обязательно при создании пользователя

    objects = CustomUserManager()  # Используем свой менеджер

    def __str__(self):
        return self.email or self.name or "User"

class UserSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='settings'
    )
    is_private = models.BooleanField(default=False, help_text="Сделать профиль закрытым")
    allow_comments = models.BooleanField(default=True, help_text="Разрешить комментарии к постам")
    notify_likes = models.BooleanField(default=True, help_text="Уведомления о лайках")
    notify_comments = models.BooleanField(default=True, help_text="Уведомления о комментариях")
    notify_follows = models.BooleanField(default=True, help_text="Уведомления о подписках")

    def __str__(self):
        return f"Настройки пользователя: {self.user.name}"
