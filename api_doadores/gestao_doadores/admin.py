from django.contrib import admin
from .models import Doador, CriterioDoacao, LocalDoacao, DemonstracaoInteresse


admin.site.register(Doador)
admin.site.register(CriterioDoacao)
admin.site.register(LocalDoacao)
admin.site.register(DemonstracaoInteresse)