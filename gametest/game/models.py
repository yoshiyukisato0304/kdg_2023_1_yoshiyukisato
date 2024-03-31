from django.db import models
from .consts import MAX_RATE

RATE_CHOICES=[(x,str(x)) for x in range(1, MAX_RATE+1)]

CATEGORY=(('apple','Apple'),('samsung','Samsung'),('google','Google'),('sony','SONY'),('oppo','OPPO'),('xiaomi','Xiaomi'),('asus','ASUS'),('motorola','Motolora'),('redmagic','Redmagic'),('nothing','Nothing'))
GAMECATEGORY=(('FPS','FPS'),('音楽ゲーム','音楽ゲーム'),('オープンワールド','オープンワールド'),('パズルゲーム','パズルゲーム'))

class Phonedata(models.Model):
    category=models.CharField(
        max_length=100,
        choices=CATEGORY
    )
    name=models.CharField(max_length=100)
    displaysize=models.FloatField()
    soc=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Gamedata(models.Model):
    gamecategory=models.CharField(
        max_length=100,
        choices=GAMECATEGORY
    )
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    phonecategory=models.ForeignKey(Phonedata, on_delete=models.CASCADE)
    gamecategory=models.ForeignKey(Gamedata, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    rate=models.IntegerField(choices=RATE_CHOICES, default=3)
    text=models.TextField()
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

