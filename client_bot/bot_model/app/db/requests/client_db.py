from __future__ import annotations
from ast import Tuple
from datetime import datetime
from bot_model.app.db.db_model.db_model import *
from settings.general.general_settings import GeneralSettings
from settings.general.order_subject import ORDER_SUBJECT
from settings.general.order_topic import ORDER_TOPIC


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ClientDataBase(metaclass=Singleton):
    def __init__(self, db: PostgresqlDatabase, tables: list) -> None:
        self.db: PostgresqlDatabase = db
        self.tables: list = tables
    

    @property
    def create_tables(self):
        with self.db:
            self.db.create_tables(self.tables)
    
    def _setting_up_language_table(self, languages: dict):
        data_source = []
        for language in languages:
            if languages[language] is True:
                data_source.append(language)

        with self.db:
            for language_name in data_source:
                create_language = Language(name=language_name)
                create_language.save()
    
    def _setting_up_time_zone_table(self, time_zones: dict):
        data_source = []
        for time_zone in time_zones:
            data_source.append((time_zone, time_zones[time_zone]))
        with self.db:
            for time_zone_values in data_source:
                create_time_zone = TimeZone(name=time_zone_values[0],
                                            time_difference=time_zone_values[1])
                create_time_zone.save()
    
    def _setting_up_currency_table(self, currencys: dict):
        # дописать курс валют
        data_source = []
        for currency in currencys:
            if currencys[currency] is True:
                data_source.append((currency))
        with self.db:
            for currency_name in data_source:
                create_currency = Currency(name=currency_name)
                create_currency.save()
    
    def _setting_up_client_status_table(self, client_status_settings: list):
        data_source = []
        for client_status in client_status_settings:
            data_source.append((client_status))
        with self.db:
            for client_status_name in data_source:
                create_client_status = ClientStatus(name=client_status_name)
                create_client_status.save()
    
    def _setting_up_order_format_table(self, order_format_settings: list):
        data_source = []
        for order_format in order_format_settings:
            data_source.append((order_format))
        with self.db:
            for order_format_name in data_source:
                create_order_format = OrderFormat(name=order_format_name)
                create_order_format.save()
    
    def _setting_up_order_state_table(self, order_state_settings: list):
        data_source = []
        for order_state in order_state_settings:
            data_source.append(order_state)
        with self.db:
            for order_state_name in data_source:
                create_order_state = OrderState(name=order_state_name)
                create_order_state.save()
    
    def _setting_up_order_importance_table(self, order_importance_settings: list):
        data_source = []
        for order_importance in order_importance_settings:
            data_source.append((order_importance))
        with self.db:
            for order_importance_name in data_source:
                create_order_importance = OrderImportance(
                    name=order_importance_name)
                create_order_importance.save()
    
    def _setting_up_order_subject_table(self, order_subject_settings: list):
        data_source = []
        for order_subject in order_subject_settings:
            data_source.append(order_subject)
        with self.db:
            for order_subject_name in data_source:
                create_order_subject = OrderSubject(name=order_subject_name)
                create_order_subject.save()

    def _setting_up_order_topic_table(self, order_topic_settings: list):
        data_source = []
        for order_topic in order_topic_settings:
            data_source.append(order_topic)
        with self.db:
            for order_topic_name in data_source:
                create_order_topic = OrderTopic(name=order_topic_name)
                create_order_topic.save()
    
    @property
    def setting_up_all_tables(self) -> bool:
        self._setting_up_language_table(GeneralSettings.LANGUAGES)
        self._setting_up_time_zone_table(GeneralSettings.TIME_ZONES)
        self._setting_up_currency_table(GeneralSettings.CURRENCY)
        self._setting_up_client_status_table(GeneralSettings.CLIENT_STATUS_SETTINGS)
        self._setting_up_order_format_table(GeneralSettings.ORDER_FORMAT_SETTINGS)
        self._setting_up_order_state_table([state for state in GeneralSettings.ORDER_STATE])
        self._setting_up_order_importance_table(GeneralSettings.ORDER_IMPORTANCE_SETTINGS)
        self._setting_up_order_subject_table(ORDER_SUBJECT)
        self._setting_up_order_topic_table([topic for topic in ORDER_TOPIC])
    

    



db_storage = ClientDataBase(db, [Language, TimeZone,
                                Payment_info, Currency,
                                ClientStatus, Telegram,
                                Client, OrderFormat, OrderState,
                                OrderImportance, OrderSubject,
                                OrderTopic, Order, File])