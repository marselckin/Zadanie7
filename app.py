
import database.tab as tab
import sqlite3
import pandas as pd

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tab')
def get_tab():
 tconn=sqlite3.connect('example.db')
 tcursor = tconn.cursor()
 df = pd.read_sql('SELECT name, present, cost, status FROM TPresent', tconn)
 tconn.close()
 return  render_template('tab.html', tables=[df.to_html()], titles=[''])

if __name__ == '__main__':
  app.run(host='0.0.0.0')
