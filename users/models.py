from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings


class CustomUserManager(UserManager):
    def create_user(self, name, email=None, password=None, **extra_fields):
        if not name:
            raise ValueError('Поле name должно быть указано')
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email=None, password=None, **extra_fields):
        if not name:
            raise ValueError('Поле name обязательно для суперпользователя')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(name=name, email=email, password=password, **extra_fields)


class CustomUser(AbstractUser):
    username = None  # отключаем стандартное поле username
    email = models.EmailField(blank=True, null=True)

    name = models.CharField(max_length=255, unique=True, blank=False, null=False)  # новое уникальное имя
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    links = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'name'  # используем name как уникальный идентификатор
    REQUIRED_FIELDS = []  # другие поля не обязательны

    objects = CustomUserManager()  # подключаем наш кастомный менеджер

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

