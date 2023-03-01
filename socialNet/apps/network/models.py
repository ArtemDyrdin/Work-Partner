from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class Friends(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    friend = models.IntegerField()

    def __str__(self):
        return self.friend

    def get_absolute_url(self):
        return '/friends'

    class Meta:
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'


class Friends(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    friend = models.IntegerField('friend_id', default=True)


class Profile(models.Model):

    SPECIALS = (
        (1, 'Программирование'),
        (2, 'Музыка'),
        (3, 'Блоги и видео'),
    )

    author = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.BooleanField('theme', default=False)
    age = models.IntegerField('age', default=0)
    city = models.CharField('city', max_length=50, default=' ')
    spec = models.PositiveSmallIntegerField(
        'spec', choices=SPECIALS, default=True)
    descript = models.TextField('descript', default=' ')
    avatar = models.ImageField(upload_to='static/profile_images',
                               default='static/profile_images/default_picture.png')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(author=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )

    type = models.CharField(
        _('Тип'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(User, verbose_name=_("Участник"))

    def get_absolute_url(self):
        return reverse('users:messages', args=((), {'chat_id': self.pk}))


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=_(
        "Чат"), on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=_(
        "Пользователь"), on_delete=models.CASCADE)
    message = models.TextField(_("Сообщение"))
    pub_date = models.DateTimeField(
        _('Дата сообщения'), default=timezone.now)
    is_readed = models.BooleanField(
        _('Прочитано'), default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
