from django import forms
from .models import Покупатель, Сотрудник, Поставщик, Продукт, Платеж, Заказ, Продажа, Расход

from django import forms
from .models import Покупатель

from django import forms
from .models import Покупатель
from django.contrib.auth.models import User  # Добавлен импорт User

class ПокупательForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('client', 'Клиент'),
        ('admin', 'Администратор'),
    ]

    # Добавляем поле выбора типа пользователя
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, label="Тип пользователя")
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label="Выберите аккаунт")

    class Meta:
        model = Покупатель
        fields = [
            'ФИО',
            'Телефон',
            'Почта',
            'Адрес',
            'Дата_рождения',
            'Пол',
            'Бонусы',
            'Статус',
            'user_type',
            'user',  # добавляем поле выбора типа пользователя
        ]

        widgets = {
            'ФИО': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО покупателя'
            }),
            'Телефон': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: +7XXXXXXXXXX'
            }),
            'Почта': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@domain.com'
            }),
            'Адрес': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес покупателя'
            }),
            'Дата_рождения': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'Пол': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Бонусы': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество бонусных баллов'
            }),
            'Статус': forms.Select(attrs={
                'class': 'form-control'
            }),
            'user_type': forms.Select(attrs={
                'class': 'form-control'
            }),  # добавляем виджет для поля user_type
        }



class СотрудникForm(forms.ModelForm):
    class Meta:
        model = Сотрудник
        fields = '__all__'

        widgets = {
            'ФИО': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО сотрудника'
            }),
            'Должность': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность сотрудника'
            }),
            'Зарплата': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Зарплата сотрудника'
            }),
            'День_найма': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата найма сотрудника'
            }),
            'Телефон': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон сотрудника'
            }),
            'Почта': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта сотрудника'
            }),
            'Адрес': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Адрес сотрудника'
            }),
            'Дата_рождения': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата рождения сотрудника'
            }),
            'Отделение': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отделение сотрудника'
            }),
        }

from django import forms
from .models import Поставщик

class ПоставщикForm(forms.ModelForm):
    class Meta:
        model = Поставщик
        fields = [
            'ФИО',
            'С_кем_можно_связаться',
            'Должность',
            'Адрес',
            'Почтовой_индекс',
            'Город',
            'Страна',
            'Телефон',
            'Почта',
        ]

        widgets = {
            'ФИО': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО поставщика'}),
            'С_кем_можно_связаться': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите контактное лицо'}),
            'Должность': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите должность'}),
            'Адрес': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите адрес поставщика'}),
            'Почтовой_индекс': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите почтовый индекс'}),
            'Город': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите город'}),
            'Страна': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите страну'}),
            'Телефон': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'}),
            'Почта': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите электронную почту'}),
        }

class ПродуктForm(forms.ModelForm):
    class Meta:
        model = Продукт
        fields = '__all__'

        widgets = {
            'Название': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта'
            }),
            'Категория': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория товара (например, электроника)'
            }),
            'Цена': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена продукта'
            }),
            'Количество_на_складе': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество на складе'
            }),
            'Производитель': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Производитель продукта'
            }),
            'Срок_годности': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Срок годности продукта'
            }),
            'Поставщик': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите поставщика'
            }),
            'Вес': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес продукта (кг)'
            }),
            'Описание_товара': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Описание товара...'
            }),
        }


from django import forms
from .models import Платеж

class ПлатежForm(forms.ModelForm):
    class Meta:
        model = Платеж
        fields = [
            'Способ_платежа',
            'Сумма_платежа',
            'Кто_оплачивает',
            'Номер_счет_фактурный',
            'Описание_платежа',
            'Статус_платежа',
            'Кто_берет_оплату',
        ]

        widgets = {
            'Способ_платежа': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Карта, Наличные, Банковский перевод...'
            }),
            'Сумма_платежа': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: 1000.00'
            }),
            'Кто_оплачивает': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Номер_счет_фактурный': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уникальный номер счета'
            }),
            'Описание_платежа': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Дополнительная информация о платеже...'
            }),
            'Статус_платежа': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Кто_берет_оплату': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


from django import forms
from .models import Заказ

class ЗаказForm(forms.ModelForm):
    class Meta:
        model = Заказ
        fields = '__all__'
        widgets = {
            'Айди_покупателя': forms.Select(attrs={'class': 'form-control'}),
            'Сумма_заказа': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Мысалы: 15000.00'}),
            'Статус_заказа': forms.Select(attrs={'class': 'form-control'}),
            'Адрес_заказа': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Көше, үй, пәтер'}),
            'Город_заказа': forms.TextInput(attrs={'class': 'form-control'}),
            'Область_заказа': forms.TextInput(attrs={'class': 'form-control'}),
            'Страна_заказа': forms.TextInput(attrs={'class': 'form-control'}),
            'Способ_оплаты': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        instance.Сумма_заказа = instance.get_total()  # Обновить сумму заказа после сохранения
        instance.save()  # Пересохранить, чтобы обновить сумму
        return instance



class ПродажаForm(forms.ModelForm):
    class Meta:
        model = Продажа
        fields = '__all__'

        widgets = {
            'Айди_заказа': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите заказ'
            }),
            'Айди_продукта': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите продукт'
            }),
            'Название_продукта': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название продукта'
            }),
            'Количество': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
            'Цена_за_продажу': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена за продажу'
            }),
            'Дата': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата продажи',
                'type': 'datetime-local'
            }),
            'Айди_сотрудника': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите сотрудника'
            }),
            'Способ_оплаты': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Способ оплаты (Карта, Наличные и т.д.)'
            }),
        }
class РасходForm(forms.ModelForm):
    class Meta:
        model = Расход
        fields = [
            'Категория_расхода',
            'Цена_расхода',
            'Способ_расхода',
            'Кому_оплатил',
            'Номер_чека',
            'Описание_расхода',
            # 'Когда_написали_о_расходе' алып тасталды!
            # 'Когда_был_расход' және 'Тип_расхода' қоспаймыз
        ]

        widgets = {
            'Категория_расхода': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория расхода (например, офисные расходы)'
            }),
            'Цена_расхода': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сумму расхода'
            }),
            'Способ_расхода': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Как был произведен расход (наличные, перевод и т.д.)'
            }),
            'Кому_оплатил': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите сотрудника'
            }),
            'Номер_чека': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уникальный номер чека'
            }),
            'Описание_расхода': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Дополнительная информация о расходе...'
            }),
            # 'Когда_написали_о_расходе' өрісін алып тастадық
        }




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Покупатель

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('client', 'Клиент'),
        ('admin', 'Администратор'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, label="Тип аккаунта")

    class Meta:
        model = User  # Будет использовать модель User для создания аккаунта
        fields = ['username', 'password1', 'password2']  # Обычные поля для регистрации
