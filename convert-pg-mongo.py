import os
import re
import subprocess
import psycopg2
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

try:
  load_dotenv()

  connection = psycopg2.connect(os.getenv('URI'))
  cursor = connection.cursor()
  cursor.execute(f"SELECT * FROM comment WHERE status='review'")
  rows = cursor.fetchall()
  comments_to_review = len(rows)

  cursor.execute(f'SELECT SUM (views) FROM post')
  rows = cursor.fetchall()

  out = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output('/home/codabool/scripts/bash-scripts/getHeroku.sh', shell=True)))

  # print(f'comments: {comments_to_review}')
  # print(f'views: {int(rows[0][0])}')
  # print(f'hours: {out}')

  client = MongoClient(os.getenv('MONGODB_URI'))
  mon = client['codadash']['collections']
  mon.update_one(
    {'name': 'heroku'},
    {'$set':
      {
        'Comments': comments_to_review,
        'Views': int(rows[0][0]),
        'hours': out,
        'Last Ran': datetime.now(),
      }
    }
  )

  # Close
  cursor.close()
  connection.close()

except (Exception, psycopg2.Error) as error :
  print (error)