from random import choice
from django.db import models

SHORT_CODE_CHARS =  'abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ0123456789'


class ShortUrl(models.Model):
    long_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=6, unique=True)

    def generate_short_code(self) -> None:
        while True:
            short_code = ''.join([choice(SHORT_CODE_CHARS) for _ in range(6)])
            if not ShortUrl.objects.filter(short_code=short_code).exists():
                break
        
        self.short_code = short_code
    
    def long_url_exist(self, long_url: str) -> bool:
        return ShortUrl.objects.filter(long_url=long_url).exists()

    def save(self, *args, **kwargs) -> None:
        if self.long_url and not self.short_code:
            self.generate_short_code()
        return super().save(*args, **kwargs)