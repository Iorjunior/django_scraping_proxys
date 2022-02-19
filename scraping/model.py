from peewee import SqliteDatabase, Model, CharField, IntegerField, DecimalField


DB_PATH = './django_proxys/db.sqlite3'
db = SqliteDatabase(DB_PATH)


class proxys_proxy(Model):
    ip_address = CharField()
    port = CharField()
    protocol = CharField()
    anonymity = CharField()
    country = CharField()
    region = CharField()
    city = CharField()
    uptime = DecimalField()
    response = IntegerField()
    transfer = IntegerField()

    class Meta:
        database = db


def save_data(data_dict):

    for data in data_dict:
        proxys_proxy.create(**data)


if __name__ == '__main__':

    proxys_proxy.create(
        ip_address='138.8.1.10',
        port='8080',
        protocol='http',
        anonymity='None',
        country='Br',
        region='SP',
        city='Sao Paulo',
        uptime='90.5',
        response='89',
        transfer='56',
    )
