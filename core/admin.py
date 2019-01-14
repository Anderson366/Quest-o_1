from django.contrib import admin

from datetime import timedelta
from django.utils.timezone import now

# Register your models here.
#from django.template.defaulttags import now
admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Atividade Anderson'

from .models import DespesaAna

class DespesaAnaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'tipo_despesa', 'descricao', 'forma_pagamento', 'vencimento', 'quitado', 'prox_venc',)
    list_filter = ('vencimento', 'quitado')

    date_hierarchy = 'vencimento'
    #search_fields = 'data_criacao',
    #filter_horizontal = 'vencimento',

    def prox_venc(self, obj):
        return obj.vencimento >= now().date() - timedelta(days=2)
    prox_venc.short_description = 'Próximo Vencimento'
    prox_venc.boolean = True

admin.site.register(DespesaAna, DespesaAnaAdmin)
