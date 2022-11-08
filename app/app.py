from flask import Flask
import mysql.connector
import json



app = Flask(__name__)


config = {
       'user': 'root',
       'password': 'root',
       'host': 'db',
       'port': '3306',
       'database': 'name_age'
}


def bd_data():
   with mysql.connector.connect(**config) as connection:
      with connection.cursor() as cursor:
         cursor.execute('SELECT * FROM name_age_table')
         results = {name: age for (name, age) in cursor}
   return results


@app.route('/', methods=['GET'])
def index():
   results = bd_data()
   return json.dumps(results, indent=4)


@app.route('/health', methods=['GET'])
def status(): 
   return json.dumps({"status": "OK"})

@app.errorhandler(404)
def page_not_found(e):
     return '404', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

