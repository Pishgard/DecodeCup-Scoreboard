from django.db import models


class League(models.Model):
    name = models.CharField('نام لیگ', max_length=500)

    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'لیگ'
        verbose_name_plural = 'لیگ ها'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField('نام تیم', max_length=500)
    team_id = models.IntegerField('ایدی', unique=True, null=True, blank=True)
    university = models.CharField('دانشگاه', max_length=250, null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='لیگ', related_name="league_team")

    code_level1 = models.BooleanField('کد مرحله ۱', default=False)
    code_level2 = models.BooleanField('کد مرحله ۲', default=False)

    score_level1 = models.IntegerField('نمره مرحله اول', default=0)
    score_level2 = models.IntegerField('نمره مرحله دوم', default=0)
    time = models.IntegerField('زمان کل', default=0)

    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'تیم'
        verbose_name_plural = 'تیم ها'

    def __str__(self):
        return str(self.team_id)

    def total_score(self):
        return self.score_level1 + self.score_level2


class Submit(models.Model):
    Level_CHOICES = (
        ('1', '1'),
        ('2', '2'),
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='تیم', related_name="team_submit")
    level = models.CharField('مرحله', choices=Level_CHOICES, default='1', max_length=128)
    team_broken = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='کد شکسته شده', related_name="team_broken_submit")
    time = models.IntegerField('زمان پاسخ درست')
    # submit_count = models.IntegerField('تعداد ارسال', default=0)
    status = models.BooleanField('وضعیت درستی', default=False)

    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'ارسال'
        verbose_name_plural = 'ارسال ها'

    def __str__(self):
        return str(self.team)