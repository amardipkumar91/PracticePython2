# --------Mysql -------
After Pulling images;

start container : - docker run --rm -d -v mysql:/var/lib/mysql -v mysql_config:/etc/mysql -p 3306:3306 --name mysqldb -e MYSQL_ROOT_PASSWORD=1234 mysql

Run Docker compose : docker-compose -f docker-compose.dev.yml up --build
Run Mysql Shell : - docker exec -it <container name> bash or
docker exec -ti vicky mysql -u root -p

# ---- connect Mysql -----

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="vicky",
    password="1234",
    database="test"
  )

cursor = mydb.cursor()
cursor.execute("SELECT * FROM Persons")
cursor.fetchall()