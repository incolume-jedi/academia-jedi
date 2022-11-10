from model import db, orm

db.bind(provider='sqlite', filename=':memory:')
db.generate_mapping(create_tables=True)
