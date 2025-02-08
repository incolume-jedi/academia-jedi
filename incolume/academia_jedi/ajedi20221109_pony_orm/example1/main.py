from datetime import datetime

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from decimal import Decimal

import pony.orm.core
from pony import orm
from pony.orm.examples.estore import populate_database

db = orm.Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Customer(db.Entity):
    email = orm.Required(str, unique=False)
    password = orm.Required(str)
    name = orm.Required(str)
    country = orm.Required(str)
    address = orm.Required(str)
    cart_items = orm.Set('CartItem')
    orders = orm.Set('Order')


class Product(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str)
    categories = orm.Set('Category')
    description = orm.Optional(str)
    picture = orm.Optional(orm.buffer)
    price = orm.Required(Decimal)
    quantity = orm.Required(int)
    cart_items = orm.Set('CartItem')
    order_items = orm.Set('OrderItem')


class CartItem(db.Entity):
    quantity = orm.Required(int)
    customer = orm.Required(Customer)
    product = orm.Required(Product)


class OrderItem(db.Entity):
    quantity = orm.Required(int)
    price = orm.Required(Decimal)
    order = orm.Required('Order')
    product = orm.Required(Product)
    orm.PrimaryKey(order, product)


class Order(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    state = orm.Required(str)
    date_created = orm.Required(datetime)
    date_shipped = orm.Optional(datetime)
    date_delivered = orm.Optional(datetime)
    total_price = orm.Required(Decimal)
    customer = orm.Required(Customer)
    items = orm.Set(OrderItem)


class Category(db.Entity):
    name = orm.Required(str)
    products = orm.Set(Product)


db.generate_mapping(create_tables=True)


if __name__ == '__main__':  # pragma: no cover
    with orm.db_session:
        try:
            populate_database()
        except pony.orm.core.TransactionIntegrityError as err:
            print(err)
        result = db.select(
            'SELECT "customer"."country", COUNT(DISTINCT "customer"."id") '
            'FROM "Customer" "customer" '
            'GROUP BY "customer"."country" '
            'ORDER BY 2 DESC LIMIT 1',
        )
        print(f'{result=}')
        result = (
            orm.select(
                (customer.country, orm.count(customer))
                for customer in Customer
            )
            .order_by(-2)
            .first()
        )
        print(f'{result=}')
