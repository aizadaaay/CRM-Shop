
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Покупатель
    path('покупатели/', views.ПокупательListView.as_view(), name='покупатель_список'),
    path('покупатели/добавить/', views.ПокупательCreateView.as_view(), name='покупатель_создать'),
    path('покупатели/<int:pk>/', views.ПокупательDetailView.as_view(), name='покупатель_детали'),
    path('покупатели/<int:pk>/изменить/', views.ПокупательUpdateView.as_view(), name='покупатель_изменить'),
    path('покупатели/<int:pk>/удалить/', views.ПокупательDeleteView.as_view(), name='покупатель_удалить'),
    path('обновить_бонусы/<int:покупатель_id>/', views.update_bonus, name='обновить_бонусы'),

    # Сотрудник
    path('сотрудники/', views.СотрудникListView.as_view(), name='сотрудник_список'),
    path('сотрудники/добавить/', views.СотрудникCreateView.as_view(), name='сотрудник_создать'),
    path('сотрудники/<int:pk>/', views.СотрудникDetailView.as_view(), name='сотрудник_детали'),
    path('сотрудники/<int:pk>/изменить/', views.СотрудникUpdateView.as_view(), name='сотрудник_изменить'),
    path('сотрудники/<int:pk>/удалить/', views.СотрудникDeleteView.as_view(), name='сотрудник_удалить'),

    # Поставщик
    path('поставщики/', views.ПоставщикListView.as_view(), name='поставщик_список'),
    path('поставщики/добавить/', views.ПоставщикCreateView.as_view(), name='поставщик_создать'),
    path('поставщики/<int:pk>/', views.ПоставщикDetailView.as_view(), name='поставщик_детали'),
    path('поставщики/<int:pk>/изменить/', views.ПоставщикUpdateView.as_view(), name='поставщик_изменить'),
    path('поставщики/<int:pk>/удалить/', views.ПоставщикDeleteView.as_view(), name='поставщик_удалить'),

    # И так далее для всех остальных моделей:
    path('продукты/', views.ПродуктListView.as_view(), name='продукт_список'),
    path('продукты/добавить/', views.ПродуктCreateView.as_view(), name='продукт_создать'),
    path('продукты/<int:pk>/', views.ПродуктDetailView.as_view(), name='продукт_детали'),
    path('продукты/<int:pk>/изменить/', views.ПродуктUpdateView.as_view(), name='продукт_изменить'),
    path('продукты/<int:pk>/удалить/', views.ПродуктDeleteView.as_view(), name='продукт_удалить'),

    path('платежи/', views.ПлатежListView.as_view(), name='платеж_список'),
    path('платежи/добавить/', views.ПлатежCreateView.as_view(), name='платеж_создать'),
    path('платежи/<int:pk>/', views.ПлатежDetailView.as_view(), name='платеж_детали'),
    path('платежи/<int:pk>/изменить/', views.ПлатежUpdateView.as_view(), name='платеж_изменить'),
    path('платежи/<int:pk>/удалить/', views.ПлатежDeleteView.as_view(), name='платеж_удалить'),

    path('заказы/', views.ЗаказListView.as_view(), name='заказ_список'),
    path('заказы/добавить/', views.ЗаказCreateView.as_view(), name='заказ_создать'),
    path('заказы/<int:pk>/', views.ЗаказDetailView.as_view(), name='заказ_детали'),
    path('заказы/<int:pk>/изменить/', views.ЗаказUpdateView.as_view(), name='заказ_изменить'),
    path('заказы/<int:pk>/удалить/', views.ЗаказDeleteView.as_view(), name='заказ_удалить'),

    path('продажи/', views.ПродажаListView.as_view(), name='продажа_список'),
    path('продажи/добавить/', views.ПродажаCreateView.as_view(), name='продажа_создать'),
    path('продажи/<int:pk>/', views.ПродажаDetailView.as_view(), name='продажа_детали'),
    path('продажи/<int:pk>/изменить/', views.ПродажаUpdateView.as_view(), name='продажа_изменить'),
    path('продажи/<int:pk>/удалить/', views.ПродажаDeleteView.as_view(), name='продажа_удалить'),

    path('расходы/', views.РасходListView.as_view(), name='расход_список'),
    path('расходы/добавить/', views.РасходCreateView.as_view(), name='расход_создать'),
    path('расходы/<int:pk>/', views.РасходDetailView.as_view(), name='расход_детали'),
    path('расходы/<int:pk>/изменить/', views.РасходUpdateView.as_view(), name='расход_изменить'),
    path('расходы/<int:pk>/удалить/', views.РасходDeleteView.as_view(), name='расход_удалить'),

    path('', views.home, name='index'),  # главная страница
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
