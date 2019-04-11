from django.contrib import admin

# Register your models here.
from .models import Uzytkownicy
from .models import Autorzy
from .models import ksiazki
from .models import Zamowienia
from .models import Reklamacje

admin.site.register(Uzytkownicy)
admin.site.register(Autorzy)
admin.site.register(ksiazki)
admin.site.register(Zamowienia)
admin.site.register(Reklamacje)
