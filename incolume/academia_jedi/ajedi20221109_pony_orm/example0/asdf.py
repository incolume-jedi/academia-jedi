from pony import orm

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
db.generate_mapping(create_tables=True)


@orm.db_session
def persistir():
    Person(name='John', age=20)
    p2 = Person(name='Mary', age=22)
    p3 = Person(name='Bob', age=30)
    Car(make='Toyota', model='Prius', owner=p2)
    Car(make='Ford', model='Explorer', owner=p3)


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
        mary.age += 1
        print(mary.age)
        Person.select().show()

        idade = 25
        for person in Person.select_by_sql(
            'SELECT * FROM Person p WHERE p.age < $idade',
        ):
            print(person.name, person.age)
