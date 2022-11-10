import pony.orm.core
from pony.orm.examples.estore import populate_database
from pony import orm
from datetime import datetime
from decimal import Decimal


db = orm.Database()
# db.bind(provider='sqlite', filename=':memory:')
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


if __name__ == '__main__':    # pragma: no cover

    with orm.db_session:
        try:
            populate_database()
        except pony.orm.core.TransactionIntegrityError as err:
            print(err)
        result = db.select(
            'SELECT "customer"."country", COUNT(DISTINCT "customer"."id") '
            'FROM "Customer" "customer" '
            'GROUP BY "customer"."country" '
            'ORDER BY 2 DESC LIMIT 1'
        )
        print(f'{result=}')
        result = orm.select(
            (customer.country, orm.count(customer))
            for customer in Customer).order_by(-2).first()
        print(f'{result=}')

