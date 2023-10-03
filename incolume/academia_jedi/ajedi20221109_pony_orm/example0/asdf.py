from pony import orm

db = orm.Database()


class Person(db.Entity):
    name = orm.Required(str)
    age = orm.Required(int)
    cars = orm.Set('Car')


class Car(db.Entity):
    make = orm.Required(str)
    model = orm.Required(str)
    owner = orm.Required(Person)


db.bind(provider='sqlite', filename=':memory:')
# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@orm.db_session
def persistir():
    p1 = Person(name='John', age=20)
    p2 = Person(name='Mary', age=22)
    p3 = Person(name='Bob', age=30)
    c1 = Car(make='Toyota', model='Prius', owner=p2)
    c2 = Car(make='Ford', model='Explorer', owner=p3)
    # orm.commit()


@orm.db_session
def print_person_name(person_id):
    p = Person[person_id]
    print(p.name, p.cars)
    # database session cache will be cleared automatically
    # database connection will be returned to the pool


@orm.db_session
def add_car(person_id, make, model):
    Car(make=make, model=model, owner=Person[person_id])
    # commit() will be done automatically
    # database session cache will be cleared automatically
    # database connection will be returned to the pool


def add_record(**kwargs):
    with orm.db_session:
        p = Person(name=kwargs.get('name', 'Kate'), age=kwargs.get('age', 33))
        Car(
            make=kwargs.get('make', 'Audi'),
            model=kwargs.get('model', 'R8'),
            owner=p,
        )
        # commit() will be done automatically
        # database session cache will be cleared automatically
        # database connection will be returned to the pool


if __name__ == '__main__':  # pragma: no cover
    orm.show(Person)
    persistir()
    print_person_name(3)
    add_car(3, 'hyundai', 'HB20s')
    add_record()
    print_person_name(4)

    with orm.db_session:
        print(
            orm.select(p for p in Person if p.age > 20),
            orm.select(p for p in Person if p.age > 20)[:],
            orm.select(p for p in Person).order_by(Person.name)[:2],
            sep='\n',
        )
        orm.select(p for p in Person).order_by(Person.name)[:2].show()
        Car.select().show()
        persons = orm.select(p for p in Person if 'o' in p.name)
        # SELECT "p"."id", "p"."name", "p"."age"
        # FROM "Person" "p"
        # WHERE "p"."name" LIKE '%o%'
        for person in persons:
            print(
                person.name,
                person.age,
                [f'{x.make}/{x.model}' for x in person.cars],
            )

        print(orm.select(p.name for p in Person if p.age != 30)[:])

        # SELECT DISTINCT "p"."name"
        # FROM "Person" "p"
        # WHERE "p"."age" <> 30

        print(orm.select((p, orm.count(p.cars)) for p in Person)[:])

        # SELECT "p"."id", COUNT(DISTINCT "car-1"."id")
        # FROM "Person" "p"
        #  LEFT JOIN "Car" "car-1"
        #    ON "p"."id" = "car-1"."owner"
        # GROUP BY "p"."id"

        print(max(orm.select(p.age for p in Person)))
        # SELECT MAX("p"."age")
        # FROM "Person" "p"

        p1 = Person[1]
        print(p1.name)

        mary = Person.get(name='Mary')

        # SELECT "id", "name", "age"
        # FROM "Person"
        # WHERE "name" = ?
        print(mary.name, mary.age, [f'{c.make}/{c.model}' for c in mary.cars])
        # orm.show(mary)
        mary.age += 1
        print(mary.age)
        Person.select().show()

        idade = 25
        for person in Person.select_by_sql(
            'SELECT * FROM Person p WHERE p.age < $idade'
        ):
            print(person.name, person.age)
