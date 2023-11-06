from model import db

db.bind(provider='sqlite', filename=':memory:')
db.generate_mapping(create_tables=True)
