from flask import Flask, render_template, request
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/station_status')

def station_status():

    station_id = int(request.args.get('station_id'))

    conn_string = 'mysql://{user}:{password}@{host}/{db}?charset={encoding}'.format(
        host = 'localhost',
        user = 'siegmanA',
        db = 'citibike',
        password = 'password',
        encoding = 'utf8mb4')

    engine = create_engine(conn_string)
    con = engine.connect()
    query = '''SELECT is_renting,
                      num_bikes_available,
                      num_bikes_disabled,
                      num_docks_available,
                      num_docks_disabled
               FROM StationInfo
               WHERE station_id = %s'''
    status = con.execute(query, (station_id,))

    con.close()

    return render_template('station_status.html', station_id = station_id, statuses=status)

app.run(host='0.0.0.0', port=5000, debug=True)
