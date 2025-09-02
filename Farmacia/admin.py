from django.contrib import admin
from . import models


<<<<<<< HEAD


=======
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
class MedicamentoInline(admin.TabularInline):
    model = models.ClienteMedicamento
    extra = 0
    fields = ('medicamento', 'get_fornecedora')
    readonly_fields = ('get_fornecedora',)

<<<<<<< HEAD

=======
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
    def get_fornecedora(self, obj):
        return obj.medicamento.fornecedora.nome if obj.medicamento.fornecedora else "-"
    get_fornecedora.short_description = 'Fornecedora'


<<<<<<< HEAD


=======
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [MedicamentoInline]
    list_display = ('nome', 'email', 'telefone')


<<<<<<< HEAD


=======
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
@admin.register(models.Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'fornecedora')
    list_filter = ('fornecedora',)


<<<<<<< HEAD


=======
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
@admin.register(models.Fornecedora)  
class FornecedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')


<<<<<<< HEAD


admin.site.register(models.ClienteMedicamento)


=======
admin.site.register(models.ClienteMedicamento)
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
