from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_verified = models.BooleanField(_('verified'), default=False)
    
    # 2FA fields
    two_factor_enabled = models.BooleanField(_('2FA enabled'), default=False)
    two_factor_code = models.CharField(_('2FA code'), max_length=6, blank=True)
    two_factor_code_timestamp = models.DateTimeField(null=True, blank=True)
    
    # Password reset fields
    reset_password_token = models.CharField(_('reset password token'), max_length=100, blank=True)
    reset_password_timestamp = models.DateTimeField(null=True, blank=True)
    
    # Email verification fields
    email_verification_token = models.CharField(_('email verification token'), max_length=100, blank=True)
    email_verification_timestamp = models.DateTimeField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def __str__(self):
        return self.email 