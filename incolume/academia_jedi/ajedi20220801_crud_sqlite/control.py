from faker import Faker

# ruff: noqa: B007, D100
from incolume.academia_jedi.ajedi20220801_crud_sqlite.model import Pessoa

faker = Faker('pt_BR')


if __name__ == '__main__':
    d = []
    for i in range(10):
        fname = faker.first_name()
        lname = faker.last_name()
        d.append(
            Pessoa(
                f'{fname} {lname}',
                faker.date_time_this_century(),
                [f'{fname.casefold()}_{lname.casefold()}@example.org'],
            ),
        )
    print(d)
