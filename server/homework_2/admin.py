from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Корректный номер телефона")
def edit_phone(modeladmin, request, queryset):
    queryset.update(phone='Укажите корректный номер телефона')


@admin.action(description="Корректный адрес")
def edit_address(modeladmin, request, queryset):
    queryset.update(address='Укажите корректный адрес')


class ClientAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'phone', 'address', 'date']
    ordering = ['-date']
    list_filter = ['name', 'email', 'phone']
    search_fields = ['name']
    search_help_text = 'Поиск по имени Клиента'
    actions = [edit_phone, edit_address]

    readonly_fields = ['date']

    fieldsets = [
        ('Client',
         {
             'classes': ['wide'],
             'fields': ['name', 'date'],
         },
         ),
        ('Details',
         {
             'classes': ['collapse'],
             'description': 'Адрес клиента',
             'fields': ['address'],
         },
         ),
        ('Contacts',
         {
             'classes': ['collapse'],
             'description': 'Контактная информация',
             'fields': ['email', 'phone'],
         }
         ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'lot', 'date']
    ordering = ['-date']
    list_filter = ['name', 'description']
    search_fields = ['name']
    search_help_text = 'Поиск по названию Продукта'

    readonly_fields = ['price', 'date']

    fieldsets = [
        ('Product',
         {
             'classes': ['wide'],
             'fields': ['name', 'description', 'date'],
         },
         ),
        ('Details',
         {
             'classes': ['collapse'],
             'description': 'Цена и количество',
             'fields': ['price', 'lot'],
         },
         ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'total_order', 'date']
    ordering = ['-date']
    list_filter = ['customer', 'product']
    search_fields = ['customer__name', 'product__name']
    search_help_text = 'Поиск по Заказчику или продукту'

    readonly_fields = ['total_order', 'date']

    fieldsets = [
        ('Order',
         {
             'classes': ['wide'],
             'fields': ['customer', 'product', 'date'],
         },
         ),
        ('Details',
         {
             'classes': ['collapse'],
             'description': 'Сумма заказа',
             'fields': ['total_order'],
         },
         ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
