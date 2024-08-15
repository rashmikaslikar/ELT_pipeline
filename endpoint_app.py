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
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    muid = request.args.get('muid')

    query = f'SELECT * FROM {muid} WHERE 1=1'
    params = []

    if start_date:
        query += ' AND timestamp_ >= %s'
        params.append(start_date)
    if end_date:
        query += ' AND timestamp_ <= %s'
        params.append(end_date)

    query += ' LIMIT %s OFFSET %s'
    params.extend([limit, offset])

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, tuple(params))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
