from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='exnaton_test',
        user='airbyte_user',
        password='exnaton'
    )
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    table = request.args.get('table')

    query = f'SELECT * FROM {table} WHERE 1=1'
    params = []

    if start_date:
        query += ' AND timestamp_ >= %s'
        params.append(start_date)
    if end_date:
        query += ' AND timestamp_ <= %s'
        params.append(end_date)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, tuple(params))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
