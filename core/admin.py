from django.contrib import admin

from .models import (
    Cargo, 
    Servico, 
    Funcionario,
    Feature
)
# print('CARGO._meta.fields: ',  Cargo._meta.fields)
# # print('CARGO: ',Cargo.__dict__)
# print('\n--------------: ', Cargo)
# # print('Type CARGO: ', type(Cargo.__dict__['__doc__']))
# # print('CARGO: ',Cargo.__dict__['__doc__'])
# print('CARGO keys: ',Cargo.__dict__.keys())
# print('\n--------------: ')
# print('CARGO._meta.fields: ',  Cargo._meta.fields)
# (<django.db.models.fields.AutoField: id>, 
# <django.db.models.fields.DateField: criado>, 
# <django.db.models.fields.DateField: modificado>, 
# <django.db.models.fields.BooleanField: ativo>, 
# <django.db.models.fields.CharField: cargo>)
# print('\n--------------: ')
# for f in Cargo._meta.fields:
#     print(f)
#     print(f.name)


# lista = [f.name for f in Cargo._meta.fields]
# print(lista)
# print('\n--------------: ')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cargo._meta.fields]
    # list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Servico._meta.fields]
    # list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Funcionario._meta.fields]
    # list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Feature)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Feature._meta.fields]
    # list_display = ('nome', 'cargo', 'ativo', 'modificado')