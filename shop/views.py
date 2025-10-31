
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Покупатель, Сотрудник, Поставщик, Продукт, Платеж, Заказ, Продажа, Расход
from django.urls import reverse_lazy
from .forms import ПокупательForm, СотрудникForm, ПоставщикForm, РасходForm, ПродажаForm, ЗаказForm, ПлатежForm, \
    ПродуктForm, CustomUserCreationForm


# Покупатель
class ПокупательListView(ListView):
    model = Покупатель
    template_name = 'покупатель/покупатель_list.html'
    context_object_name = 'покупатели'

# shop/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Покупатель

class ПокупательDetailView(DetailView):
    model = Покупатель
    template_name = 'покупатель/покупатель_detail.html'
    context_object_name = 'покупатель'

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)

        # Дополнительно добавляем количество заказов и баланс бонусов
        покупатель = self.get_object()
        context['количество_заказов'] = покупатель.get_order_count()
        context['баланс_бонусов'] = покупатель.get_balance()

        return context


from django.contrib.auth.mixins import LoginRequiredMixin

class ПокупательCreateView(LoginRequiredMixin, CreateView):
    model = Покупатель
    form_class = ПокупательForm
    template_name = 'покупатель/покупатель_form.html'
    success_url = reverse_lazy('покупатель_список')

    def form_valid(self, form):
        # Проверка: уже есть Покупатель с этим пользователем?
        if Покупатель.objects.filter(user=self.request.user).exists():
            form.add_error(None, 'Покупатель для этого пользователя уже существует.')
            return self.form_invalid(form)

        # Привязать текущего пользователя
        form.instance.user = self.request.user
        return super().form_valid(form)


class ПокупательUpdateView(UpdateView):
    model = Покупатель
    template_name = 'покупатель/покупатель_form.html'
    form_class = ПокупательForm
    success_url = reverse_lazy('покупатель_список')

class ПокупательDeleteView(DeleteView):
    model = Покупатель
    template_name = 'покупатель/покупатель_confirm_delete.html'
    success_url = reverse_lazy('покупатель_список')

# Сотрудник
class СотрудникListView(ListView):
    model = Сотрудник
    template_name = 'сотрудник/сотрудник_list.html'
    context_object_name = 'сотрудники'

class СотрудникDetailView(DetailView):
    model = Сотрудник
    template_name = 'сотрудник/сотрудник_detail.html'
    context_object_name = 'сотрудник'

class СотрудникCreateView(CreateView):
    model = Сотрудник
    template_name = 'сотрудник/сотрудник_form.html'
    form_class = СотрудникForm
    success_url = reverse_lazy('сотрудник_список')

class СотрудникUpdateView(UpdateView):
    model = Сотрудник
    template_name = 'сотрудник/сотрудник_form.html'
    form_class = СотрудникForm
    success_url = reverse_lazy('сотрудник_список')

class СотрудникDeleteView(DeleteView):
    model = Сотрудник
    template_name = 'сотрудник/сотрудник_confirm_delete.html'
    success_url = reverse_lazy('сотрудник_список')

# Поставщик
class ПоставщикListView(ListView):
    model = Поставщик
    template_name = 'Поставщик/поставщик_list.html'
    context_object_name = 'поставщики'

class ПоставщикDetailView(DetailView):
    model = Поставщик
    template_name = 'Поставщик/поставщик_detail.html'
    context_object_name = 'поставщик'

class ПоставщикCreateView(CreateView):
    model = Поставщик
    template_name = 'Поставщик/поставщик_form.html'
    form_class = ПоставщикForm
    success_url = reverse_lazy('поставщик_список')

class ПоставщикUpdateView(UpdateView):
    model = Поставщик
    template_name = 'Поставщик/поставщик_form.html'
    form_class = ПоставщикForm
    success_url = reverse_lazy('поставщик_список')

class ПоставщикDeleteView(DeleteView):
    model = Поставщик
    template_name = 'Поставщик/поставщик_confirm_delete.html'
    success_url = reverse_lazy('поставщик_список')

# Продукт
class ПродуктListView(ListView):
    model = Продукт
    template_name = 'Продукт/продукт_list.html'
    context_object_name = 'продукты'

class ПродуктDetailView(DetailView):
    model = Продукт
    template_name = 'Продукт/продукт_detail.html'
    context_object_name = 'продукт'

class ПродуктCreateView(CreateView):
    model = Продукт
    template_name = 'Продукт/продукт_form.html'
    form_class = ПродуктForm
    success_url = reverse_lazy('продукт_список')

class ПродуктUpdateView(UpdateView):
    model = Продукт
    template_name = 'Продукт/продукт_form.html'
    form_class = ПродуктForm
    success_url = reverse_lazy('продукт_список')

class ПродуктDeleteView(DeleteView):
    model = Продукт
    template_name = 'Продукт/продукт_confirm_delete.html'
    success_url = reverse_lazy('продукт_список')

# Платеж
class ПлатежListView(ListView):
    model = Платеж
    template_name = 'Платеж/платеж_list.html'
    context_object_name = 'платежи'

class ПлатежDetailView(DetailView):
    model = Платеж
    template_name = 'Платеж/платеж_detail.html'
    context_object_name = 'платеж'

class ПлатежCreateView(CreateView):
    model = Платеж
    template_name = 'Платеж/платеж_form.html'
    form_class = ПлатежForm
    success_url = reverse_lazy('платеж_список')

class ПлатежUpdateView(UpdateView):
    model = Платеж
    template_name = 'Платеж/платеж_form.html'
    form_class = ПлатежForm
    success_url = reverse_lazy('платеж_список')

class ПлатежDeleteView(DeleteView):
    model = Платеж
    template_name = 'Платеж/платеж_confirm_delete.html'
    success_url = reverse_lazy('платеж_список')

# Заказ
class ЗаказListView(ListView):
    model = Заказ
    template_name = 'Заказ/заказ_list.html'
    context_object_name = 'заказы'

class ЗаказDetailView(DetailView):
    model = Заказ
    template_name = 'Заказ/заказ_detail.html'
    context_object_name = 'заказ'

import logging

logger = logging.getLogger(__name__)

class ЗаказCreateView(CreateView):
    model = Заказ
    template_name = 'Заказ/заказ_form.html'
    form_class = ЗаказForm
    success_url = reverse_lazy('заказ_список')

    def form_valid(self, form):
        logger.info(f"Создается заказ: {form.instance}")
        response = super().form_valid(form)
        logger.info(f"Заказ успешно создан: {form.instance}")
        return response


from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Заказ
from .forms import ЗаказForm

class ЗаказUpdateView(UpdateView):
    model = Заказ
    template_name = 'Заказ/заказ_form.html'
    form_class = ЗаказForm
    success_url = reverse_lazy('заказ_список')

    def form_valid(self, form):
        # Сохраняем изменения заказа
        заказ = form.save(commit=False)
        заказ.Сумма_заказа = заказ.get_total()  # Обновляем сумму заказа
        заказ.save()  # Сохраняем заказ с новой суммой

        # Возвращаем результат
        return super().form_valid(form)

class ЗаказDeleteView(DeleteView):
    model = Заказ
    template_name = 'Заказ/заказ_confirm_delete.html'
    success_url = reverse_lazy('заказ_список')

# Продажа
class ПродажаListView(ListView):
    model = Продажа
    template_name = 'Продажа/продажа_list.html'
    context_object_name = 'продажи'

class ПродажаDetailView(DetailView):
    model = Продажа
    template_name = 'Продажа/продажа_detail.html'
    context_object_name = 'продажа'

class ПродажаCreateView(CreateView):
    model = Продажа
    template_name = 'Продажа/продажа_form.html'
    form_class = ПродажаForm
    success_url = reverse_lazy('продажа_список')

class ПродажаUpdateView(UpdateView):
    model = Продажа
    template_name = 'Продажа/продажа_form.html'
    form_class = ПродажаForm
    success_url = reverse_lazy('продажа_список')

class ПродажаDeleteView(DeleteView):
    model = Продажа
    template_name = 'Продажа/продажа_confirm_delete.html'
    success_url = reverse_lazy('продажа_список')

# Расход
class РасходListView(ListView):
    model = Расход
    template_name = 'Расход/расход_list.html'
    context_object_name = 'расходы'

class РасходDetailView(DetailView):
    model = Расход
    template_name = 'Расход/расход_detail.html'
    context_object_name = 'расход'
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Расход
from .forms import РасходForm # Егер функция басқа файлда болса

class РасходCreateView(CreateView):
    model = Расход
    template_name = 'Расход/расход_form.html'
    form_class = РасходForm
    success_url = reverse_lazy('расход_список')

    def form_valid(self, form):
        response = super().form_valid(form)
        обработать_расход(self.object)  # ✅ Тип_расхода орнатылады
        return response

class РасходUpdateView(UpdateView):
    model = Расход
    template_name = 'Расход/расход_form.html'
    form_class = РасходForm
    success_url = reverse_lazy('расход_список')

    def form_valid(self, form):
        response = super().form_valid(form)
        обработать_расход(self.object)  # ✅ Тип_расхода қайта тексеріледі
        return response



from .models import Расход
from .models import Расход

def обработать_расход(расход: Расход):
    # Тип_расхода орнату
    if расход.Цена_расхода > 50000:
        расход.Тип_расхода = 'Большой'
    else:
        расход.Тип_расхода = 'Обычный'

    # Сақтау
    расход.save(update_fields=['Тип_расхода'])


class РасходDeleteView(DeleteView):
    model = Расход
    template_name = 'Расход/расход_confirm_delete.html'
    success_url = reverse_lazy('расход_список')

# views.py
from django.http import JsonResponse
from .models import Покупатель

def update_bonus(request, покупатель_id):
    покупатель = Покупатель.objects.get(id=покупатель_id)
    return JsonResponse({'баланс': покупатель.Бонусы})


from django.contrib.auth.decorators import login_required
from .models import Покупатель  # Импортируем модель Покупатель


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm  # Импортируй кастомную форму


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ПокупательForm
from django.contrib.auth.models import User
from .models import Покупатель

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Покупатель

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Покупатель

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Покупатель

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import CustomUserCreationForm
from .models import Покупатель

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Создаем только пользователя
            user.refresh_from_db()

            try:
                # Здесь пытаемся создать покупателя, но не сохраняем его сразу
                покупатель = Покупатель(user=user)
                покупатель.save()  # Пытаемся сохранить покупателя

            except IntegrityError:
                # Если возникнет ошибка (например, дублирование), просто пропустим её
                pass

            # Перенаправляем пользователя на страницу входа (login)
            login(request, user)
            return redirect('login')  # Перенаправляем на страницу входа

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseForbidden

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')  # Перенаправление на главную страницу или другую
    else:
        return HttpResponseForbidden("Only POST method is allowed.")



from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


from .models import Расход

def обработать_расход(расход: Расход):
    if расход.Цена_расхода > 50000:
        расход.Тип_расхода = 'Большой'
        print(f"⚠️ Большой расход: {расход.Цена_расхода} тенге. Чек № {расход.Номер_чека}")
    else:
        расход.Тип_расхода = 'Обычный'
        print(f"✅ Обычный расход: {расход.Цена_расхода} тенге.")

    расход.save(update_fields=['Тип_расхода'])  # Сохраняем только поле Тип_расхода
