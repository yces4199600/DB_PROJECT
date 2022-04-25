import os,pymysql
from flask import Flask

app = Flask(__name__)

db_settings = {
    "host": os.environ.get('CLEARDB_DATABASE_HOST'),
    "user": os.environ.get('CLEARDB_DATABASE_USER'),
    "password": os.environ.get('CLEARDB_DATABASE_PASSWORD'),
    "db": os.environ.get('CLEARDB_DATABASE_DB'),
    "charset": "utf8"
}
db = pymysql.connect(**db_settings)

cursor = db.cursor()

command = "SELECT * FROM student"
cursor.execute(command)
result = cursor.fetchmany(5)
print(type(result))
print(result[0])

print(result[0][0])
@app.route('/')
def hello_world():  # put application's code here
    return result[0][0]


if __name__ == '__main__':
    app.run()
db.close()