
pip install psycopg2==2.6.2

git clone https://github.com/malexander92/w205.git /home/w205

cd /home/w205

sparse quickstart extweetcount

rm -rf /home/w205/extweetcount/*

cp -R /home/w205/w205/exercise_2/tweetwordcount/* /home/w205/extweetcount/

python create_postgres_db.py



