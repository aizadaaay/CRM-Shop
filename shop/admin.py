from django.contrib import admin
from .models import Покупатель, Сотрудник, Поставщик, Продукт, Платеж, Заказ, Продажа, Расход

@admin.register(Покупатель)
class ПокупательAdmin(admin.ModelAdmin):
    list_display = ('ФИО', 'Телефон', 'Почта', 'Бонусы', 'Статус', 'Дата_регистрации')
    search_fields = ('ФИО', 'Почта')
    list_filter = ('Пол', 'Статус')

@admin.register(Сотрудник)
class СотрудникAdmin(admin.ModelAdmin):
    list_display = ('ФИО', 'Должность', 'Зарплата', 'День_найма', 'Телефон')
    search_fields = ('ФИО', 'Должность')
    list_filter = ('Должность',)

@admin.register(Поставщик)
class ПоставщикAdmin(admin.ModelAdmin):
    list_display = ('ФИО', 'Телефон', 'Почта', 'Город', 'Страна')
    search_fields = ('ФИО',)

@admin.register(Продукт)
class ПродуктAdmin(admin.ModelAdmin):
    list_display = ('Название', 'Категория', 'Цена', 'Количество_на_складе', 'Производитель')
    list_filter = ('Категория',)
    search_fields = ('Название', 'Производитель')

@admin.register(Платеж)
class ПлатежAdmin(admin.ModelAdmin):
    list_display = ('Когда_сделали_платеж', 'Сумма_платежа', 'Способ_платежа', 'Кто_оплачивает', 'Статус_платежа')
    list_filter = ('Статус_платежа', 'Способ_платежа')
    search_fields = ('Номер_счет_фактурный',)

@admin.register(Заказ)
class ЗаказAdmin(admin.ModelAdmin):
    list_display = ('Айди_покупателя', 'Дата_заказа', 'Сумма_заказа', 'Статус_заказа')
    list_filter = ('Статус_заказа',)
    search_fields = ('Адрес_заказа',)

@admin.register(Продажа)
class ПродажаAdmin(admin.ModelAdmin):
    list_display = ('Айди_заказа', 'Название_продукта', 'Количество', 'Цена_за_продажу', 'Общая_сумма', 'Дата')
    list_filter = ('Способ_оплаты',)
    search_fields = ('Название_продукта',)

@admin.register(Расход)
class РасходAdmin(admin.ModelAdmin):
    list_display = ('Категория_расхода', 'Цена_расхода', 'Когда_был_расход', 'Способ_расхода')
    list_filter = ('Категория_расхода',)
