
## Database library
import psycopg2

## Supporting libraries
import traceback, sys


## Debug functions
import debug

## Different structures
import classes, paths, variables
from typing import Any, Dict, Tuple, Literal

ARGS_COUNT = 5

#===========================================================+
# database = 'postgres' , password = 'postgres'             |
# user     = 'postgres' , host     = '127.0.0.1'            |
# port     = '5432'                                         |
#===========================================================+
def connect(*args) -> (Tuple[Any, Any] or Tuple[Literal[False], Literal[False]]):
    if len(args) == ARGS_COUNT:
        db, pswrd, usr, hst, prt = args
        try:
            connection = psycopg2.connect(database = db, password = pswrd, user = usr, host = hst, port = prt)        
            return connection, connection.cursor()
        except:
            debug.saveLogs(f'ERROR! WRONG CONNECTION TO THE DATABASE\n\n{traceback.format_exc()}', paths.LOG_FILE)
    return False, False

#===========================================================+
#CREATE TABLE accounts_tb (                                 |
#                          Id         SERIAL PRIMARY KEY ,  |                 
#                          user_id    INTEGER            ,  |
#                          username   VARCHAR(255)       ,  |                           
#                          first_name VARCHAR(255)       ,  |                                                     
#                          last_name  VARCHAR(255)       ,  |                                                         
#                          reg_date   VARCHAR(255)       ,  |                                                          
#                          wallet     BIGINT                |
#                         );                                |
#===========================================================+
def get_accounts_data(*args, accounts : dict = {}) -> Dict[int, classes.Account]:
    connection, cursor = args
    if connection and cursor:
        try:
            cursor.execute("SELECT user_id, username, first_name, last_name, reg_date, wallet FROM accounts_tb")
            db_accounts = cursor.fetchall()
            for acc in db_accounts: accounts[acc[0]] = classes.Account(*acc)
            connection.commit()
        except:
            debug.saveLogs(f'ERROR! WRONG database DATA TAKING!\n\n{traceback.format_exc()}', paths.LOG_FILE)
    return accounts


if __name__ == '__main__':

    print('You need to enter more args to connect to database!\n'
           if connect(*sys.argv[1:]) == False else 'CONNECTED!\n')

    accounts = get_accounts_data(*connect(*sys.argv[1:]))

    print(*accounts.values())
