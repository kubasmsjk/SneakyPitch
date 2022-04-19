from django.contrib import admin
from .models import Player
from .models import Druzyna
from .models import Mecz
# Register your models here.

admin.site.register(Player)
admin.site.register(Druzyna)
admin.site.register(Mecz)
