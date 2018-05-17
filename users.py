from peewee import *

db = SqliteDatabase("users.db")


class users(Model):

    userId = IntegerField()
    username = TextField()
    password = TextField()

    class Meta:
        database = db


# users.create_table()

# users.create(userId='001',username='mufasa',password='dennis' )
# delete = users.delete().where(users.id == 2)
# delete.execute()

def search(name, password):
    name = name.lower()
    search = users.select()
    for s in search:
        if s.username == name and s.password == password:
            return True


#result = search('mufasa', 'dennis')
#print(result)
