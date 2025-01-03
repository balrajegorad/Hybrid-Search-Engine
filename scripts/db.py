import pymysql
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def get_mysql_conn():
    return pymysql.connect(
        host=config['mysql']['host'],
        port=int(config['mysql']['port']),
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database_name']
    )
