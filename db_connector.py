import pymysql
import datetime

schema_name = "freedb_sql.freedb.tech123123"


conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_DevOps_morhemo', passwd='dJxS8ZQ9y#ACaz2', db=schema_name)
conn.autocommit(True)


cursor = conn.cursor()


now = datetime.datetime.now()


cursor.execute("CREATE TABLE `"+schema_name+"`.`users`(`id` INT NOT NULL,`name` VARCHAR(45), `creation_time` VARCHAR(45));")


sql = "INSERT into `"+schema_name+"`.`users` (id, name, creation_time) VALUES (1, 'John', %s)"

cursor.execute(sql, (now,))


conn.commit()
conn.close()


