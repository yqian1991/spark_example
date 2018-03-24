import peewee as pw

myDB = pw.MySQLDatabase("datascience",
                        host="localhost",
                        port=3306,
                        user="yuq",
                        passwd="123456")


class Base(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB
