from django.db import models
from django.contrib.auth.models import User

class Покупатель(models.Model):
    ПОЛ_CHOICES = [('Мужской', 'Мужской'), ('Женский', 'Женский')]
    СТАТУСЫ = [
        ('Активный', 'Активный'),
        ('Неактивный', 'Неактивный'),
        ('Заблокирован', 'Заблокирован'),
    ]
    user_type = models.CharField(max_length=10, choices=[
        ('client', 'Покупатель'),
        ('admin', 'Администратор')
    ], default='client')

    ФИО = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=100, blank=True)  # Для имени
    Last_Name = models.CharField(max_length=100, blank=True)  # Для фамилии
    Телефон = models.CharField(max_length=20, unique=True)
    Почта = models.EmailField(max_length=100, unique=True)
    Адрес = models.TextField(blank=True, null=True)
    Дата_рождения = models.DateField(blank=True, null=True)
    Пол = models.CharField(max_length=10, choices=ПОЛ_CHOICES)
    Дата_регистрации = models.DateTimeField(auto_now_add=True)
    Бонусы = models.IntegerField(default=0)
    Статус = models.CharField(max_length=50, choices=СТАТУСЫ, default='Активный')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ФИО

    def get_order_count(self):
        return Заказ.objects.filter(Айди_покупателя=self).count()

    def get_balance(self):
        return self.Бонусы

    def save(self, *args, **kwargs):
        # Разделяем ФИО на имя и фамилию перед сохранением
        if self.ФИО:
            full_name = self.ФИО.split()
            if len(full_name) > 0:
                self.First_Name = full_name[0]  # Имя
            if len(full_name) > 1:
                self.Last_Name = full_name[1]  # Фамилия
        super().save(*args, **kwargs)


class Сотрудник(models.Model):
    ФИО = models.CharField(max_length=255)
    Должность = models.CharField(max_length=100)
    Зарплата = models.DecimalField(max_digits=10, decimal_places=2)
    День_найма = models.DateField()
    Телефон = models.CharField(max_length=20, unique=True)
    Почта = models.EmailField(max_length=100, unique=True)
    Адрес = models.TextField(blank=True, null=True)
    Дата_рождения = models.DateField(blank=True, null=True)
    Отделение = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ФИО

class Поставщик(models.Model):
    ФИО = models.CharField(max_length=255)
    С_кем_можно_связаться = models.CharField(max_length=255, blank=True, null=True)
    Должность = models.CharField(max_length=100, blank=True, null=True)
    Адрес = models.TextField(blank=True, null=True)
    Почтовой_индекс = models.CharField(max_length=20, blank=True, null=True)
    Город = models.CharField(max_length=100, blank=True, null=True)
    Страна = models.CharField(max_length=100, blank=True, null=True)
    Телефон = models.CharField(max_length=20, unique=True)
    Почта = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.ФИО

class Продукт(models.Model):
    Название = models.CharField(max_length=255)
    Категория = models.CharField(max_length=100, blank=True, null=True)
    Цена = models.DecimalField(max_digits=10, decimal_places=2)
    Количество_на_складе = models.IntegerField(default=0)
    Производитель = models.CharField(max_length=255, blank=True, null=True)
    Срок_годности = models.DateField(blank=True, null=True)
    Поставщик = models.ForeignKey(Поставщик, on_delete=models.SET_NULL, null=True, blank=True)
    Вес = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Описание_товара = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Название
    @property
    def Общая_сумма(self):
        if self.Количество_на_складе and self.Цена:
            return self.Количество_на_складе * self.Цена
        return 0


class Платеж(models.Model):
    СТАТУСЫ_ПЛАТЕЖА = [
        ('Ожидание', 'Ожидание'),
        ('Оплачен', 'Оплачен'),
        ('Не оплачен', 'Не оплачен'),
        ('Ошибка', 'Ошибка'),
    ]
    Когда_сделали_платеж = models.DateTimeField(auto_now_add=True)
    Способ_платежа = models.CharField(max_length=50)
    Сумма_платежа = models.DecimalField(max_digits=10, decimal_places=2)
    Кто_оплачивает = models.ForeignKey(Покупатель, on_delete=models.CASCADE)
    Номер_счет_фактурный = models.CharField(max_length=50, unique=True, blank=True, null=True)
    Описание_платежа = models.TextField(blank=True, null=True)
    Статус_платежа = models.CharField(max_length=50, choices=СТАТУСЫ_ПЛАТЕЖА, default='Ожидание')
    Когда_написали_о_платеже = models.DateTimeField(auto_now_add=True)
    Кто_берет_оплату = models.ForeignKey(Сотрудник, on_delete=models.SET_NULL, null=True, blank=True)


from django.db import models, transaction

class Заказ(models.Model):
    # Связь с покупателем
    Айди_покупателя = models.ForeignKey('Покупатель', on_delete=models.CASCADE, related_name='заказы')

    # Основные данные заказа
    Дата_заказа = models.DateTimeField(auto_now_add=True)
    Сумма_заказа = models.DecimalField(max_digits=10, decimal_places=2)
    ТИП_СТАТУСА = [
        ('Обычный', 'Обычный'),
        ('VIP', 'VIP'),
    ]
    Тип_статуса = models.CharField(max_length=50, choices=ТИП_СТАТУСА, default='Обычный')

    # Статус заказа с choices
    СТАТУСЫ = [
        ('В обработке', 'В обработке'),
        ('Отправлен', 'Отправлен'),
        ('Доставлен', 'Доставлен'),
        ('Отменен', 'Отменен'),
    ]
    Статус_заказа = models.CharField(max_length=50, choices=СТАТУСЫ, default='В обработке')

    # Адресные данные
    Адрес_заказа = models.TextField()
    Город_заказа = models.CharField(max_length=100, blank=True, null=True)
    Область_заказа = models.CharField(max_length=100, blank=True, null=True)
    Страна_заказа = models.CharField(max_length=100, blank=True, null=True)
    # Связь многие ко многим с продуктами
    продукты = models.ManyToManyField(Продукт, related_name='заказы')

    # Способ оплаты
    Способ_оплаты = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        # Более читаемое представление
        return f"Заказ №{self.id} для {self.Айди_покупателя.ФИО}, Статус: {self.Статус_заказа}"
    def get_total(self):
        продажи = Продажа.objects.filter(Айди_заказа=self)
        total = sum([продажа.Общая_сумма for продажа in продажи])
        return total

    from django.db import transaction

    def save(self, *args, **kwargs):
        with transaction.atomic():  # Открытие транзакции
            super().save(*args, **kwargs)
            # Дополнительные действия внутри транзакции, например:
            if self.Сумма_заказа > 10000:
                # Например, добавление бонусов покупателю при заказе на сумму более 10 000
                self.Айди_покупателя.Бонусы += 100
                self.Айди_покупателя.save()




class Продажа(models.Model):
    Айди_заказа = models.ForeignKey(Заказ, on_delete=models.CASCADE)
    Айди_продукта = models.ForeignKey(Продукт, on_delete=models.CASCADE)
    Название_продукта = models.CharField(max_length=255)
    Количество = models.IntegerField(default=1)
    Цена_за_продажу = models.DecimalField(max_digits=10, decimal_places=2)
    Дата = models.DateTimeField(auto_now_add=True)
    Айди_сотрудника = models.ForeignKey(Сотрудник, on_delete=models.SET_NULL, null=True, blank=True)
    Способ_оплаты = models.CharField(max_length=50, blank=True, null=True)

    @property
    def Общая_сумма(self):
        return self.Количество * self.Цена_за_продажу

    def save(self, *args, **kwargs):
        # Обновить общую сумму заказа при сохранении продажи
        super().save(*args, **kwargs)
        self.Айди_заказа.save()  # Обновить общую сумму для заказа

class Расход(models.Model):
    Категория_расхода = models.CharField(max_length=100, blank=True, null=True)
    Цена_расхода = models.DecimalField(max_digits=10, decimal_places=2)
    Когда_был_расход = models.DateTimeField(auto_now_add=True)
    Способ_расхода = models.CharField(max_length=50, blank=True, null=True)
    Кому_оплатил = models.ForeignKey(Сотрудник, on_delete=models.SET_NULL, null=True, blank=True)
    Номер_чека = models.CharField(max_length=50, unique=True, blank=True, null=True)
    Описание_расхода = models.TextField(blank=True, null=True)
    Когда_написали_о_расходе = models.DateTimeField(auto_now_add=True)
    Тип_расхода = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ('Большой', '⚠️ Большой расход'),
            ('Обычный', '✅ Обычный расход'),
        ]
    )

