from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Платеж, Заказ, Покупатель

# Сигнал: начисление бонусов покупателю при создании платежа
@receiver(post_save, sender=Платеж)
def update_customer_bonus(sender, instance, created, **kwargs):
    if not created:
        return  # избегаем начисления бонусов при редактировании

    покупатель = instance.Кто_оплачивает  # ForeignKey на Покупатель
    покупатель.Бонусы += int(instance.Сумма_платежа // 100)  # 1 бонус за каждые 100
    покупатель.save()
     # <- должен появиться при запуске сервера


from django.db.models.signals import post_save
from django.dispatch import receiver

# Сигнал: если сумма заказа > 10 000, ставим статус как VIP, иначе обычный заказ
@receiver(post_save, sender=Заказ)
def update_order_status(sender, instance, created, **kwargs):
    if not created:  # Это обновление, не создание нового заказа
        return

    # Проверяем сумму заказа и устанавливаем тип статуса
    if instance.Сумма_заказа > 10000:
        instance.Тип_статуса = 'VIP'
    else:
        instance.Тип_статуса = 'Обычный'

    # Сохраняем изменения в типе статуса
    instance.save()







def обработать_расход(расход):
    if расход.Цена_расхода > 50000:
        расход.Тип_расхода = 'Большой'
    else:
        расход.Тип_расхода = 'Обычный'
    расход.save(update_fields=["Тип_расхода"])


