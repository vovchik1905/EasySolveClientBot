from peewee import *
import uuid
from settings.private.db_config import DbConfig


db = PostgresqlDatabase(database=DbConfig.DATABAZE,
                        user=DbConfig.USER,
                        password=DbConfig.PASSWORD,
                        host=DbConfig.HOST,
                        port=DbConfig.PORT)



class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order = 'id'

class BaseModelWithUUID(BaseModel):
    uuid_id = UUIDField(primary_key=False, default=uuid.uuid4)

class BotState(BaseModelWithUUID):
    state_name = CharField()
    class Meta:
        db_table = 'BotState'


class Language(BaseModelWithUUID):
    name = CharField()
    class Meta:
        db_table = 'Languages'


class TimeZone(BaseModelWithUUID):
    name = CharField()
    time_difference = IntegerField()
    class Meta:
        db_table = 'TimeZone'


class Payment_info(BaseModelWithUUID):  # реквизиты клиента
    card_number = CharField(null=True)
    card_bank = CharField(null=True)
    card_phone = CharField(null=True)
    cardholler_name = CharField(null=True)
    class Meta:
        db_table = 'PaymentInfo'


class Currency(BaseModelWithUUID):  # вылюта
    name = CharField(null = True)
    exchange_rate = FloatField(null=True, constraints=[Check('exchange_rate >= 0')])  # курс к рублю
    class Meta:
        db_table = 'Currencys'


class ClientStatus(BaseModelWithUUID):
    name = CharField()#Наименование статуса клиента
    class Meta:
        db_table = 'ClientStatus'


class Telegram(BaseModelWithUUID):
    tg_id = IntegerField()
    tg_name = CharField(default=None, null=True)
    tg_sername = CharField(default=None, null=True)
    tg_username = CharField(default=None, null=True)
    class Meta:
        db_table = 'Telegram'


class Client(BaseModelWithUUID):
    bot_state = ForeignKeyField(BotState) # состояние клиента в боте
    telegram = ForeignKeyField(Telegram)  # инфо-телега(1)
    client_status = ForeignKeyField(ClientStatus)  # статус(1)
    language = ForeignKeyField(Language)  # язык(2)
    time_zone = ForeignKeyField(TimeZone)
    currency = ForeignKeyField(Currency)  # валюта(3)
    payment_info = ForeignKeyField(Payment_info)  # платёжка(4)
    rating = FloatField(default=5.0) #рейтинг
    balance = FloatField(default=0, constraints=[Check('balance >= 0')])  # баланс
    refund_balance = FloatField(default=0, constraints=[Check('refund_balance >= 0')])  # баланс затребованный
    class Meta:
        db_table = 'Client'


#-------------------------------------------------------------------------------------------------


class OrderFormat(BaseModelWithUUID):
    name = CharField()#Наименование формата заказа
    class Meta:
        db_table = 'OrderFormat'


class OrderState(BaseModelWithUUID):
    name = CharField()#Наименование состояния заказа
    class Meta:
        db_table = 'OrderState'


class OrderImportance(BaseModelWithUUID):
    name = CharField()#Наименование важности заказа
    class Meta:
        db_table = 'OrderImportance'


class OrderSubject(BaseModelWithUUID):#new create
    name = CharField()
    class Meta:
        db_table = 'OrderSubjects'


class OrderTopic(BaseModelWithUUID):
    name = CharField()
    class Meta:
        db_table = 'OrderTopics'


class Order(BaseModelWithUUID):
    client_id = ForeignKeyField(Client)
    status = ForeignKeyField(OrderState)  # статус заказа
    format = ForeignKeyField(OrderFormat)  # формат заказа
    subject = ForeignKeyField(OrderSubject)  # предметная область заказа
    topic = ForeignKeyField(OrderTopic)  # подраздел предметной области
    percent_complet = IntegerField(null=True, default=None, constraints=[Check('percent_complet >= 0')])  # минимальный процент на который необходимо выполнить заказ
    start_date = DateField(null=True, default=None)  #
    start_time = TimeField(null=True, default=None)  # начало заказа
    deadline_date = DateField(null=True, default=None)
    deadline_time = TimeField(null=True, default=None)  # дэдлайн заказа
    number_of_tasks = IntegerField(null=True, default=None)
    duration_time = TimeField(null=True, default=None)        #продолжительность заказа
    preferred_budget = IntegerField(null=True, constraints=[Check('preferred_budget >= 0')])  # предпочитаемый бюджет от заказчика
    comment = CharField(null=True, default=None)  # комментарий к заказу
    importance = ForeignKeyField(OrderImportance) #Важность заказа
    support = BooleanField(null=True, default=False)  # есть ли поддержка работы (детали необходимо указать в комменте)
    support_date = DateField(null=True, default=None)
    support_time = TimeField(null=True, default=None)
    support_comment = CharField(null=True, default=None)  # комментарий к поддержке заказа
    at_work = BooleanField(null=True, default=False)

    class Meta:
        db_table = 'Orders'


class File(BaseModel):
    order_id = ForeignKeyField(Order)
    file_tg_id = CharField()
    file_name = CharField(null=True)
    file_format = CharField(null=True)   #Формат файла
    file_datetime_get = DateTimeField(null=True, default=None)
    
    class Meta:
        db_table = 'Files'