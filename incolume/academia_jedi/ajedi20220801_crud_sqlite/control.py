from faker import Faker
from model import Pessoa

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
            )
        )
    print(d)
