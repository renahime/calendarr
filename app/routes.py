from flask import Blueprint, render_template
import os
import sqlite3
from datetime import datetime

bp = Blueprint("main", __name__, "/")
DB_FILE = os.environ.get("DB_FILE")

@bp.route('/')
def main():
    with sqlite3.connect(DB_FILE) as conn:
        curs=conn.cursor()
        curs.execute("SELECT id, name ,start_datetime,end_datetime FROM appointments ORDER BY start_datetime")
        rows=curs.fetchall()

    for row in rows:
        # start_time= datetime.strptime(row[2],'%Y-%m-%d %H:%M:%S')
        start_time=str(row[2])[7:]
        row[2]=start_time.strftime(start_time,'%H:%M:%S')
        # end_time=datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S' )
        # row[3]=end_time[7:].strftime(row[3],'%H:%M:%S')
   

    return render_template("main.html", rows=rows)
