
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
ID_ITEM    = 0


def connect(*args) -> (Tuple[Any, Any] or Tuple[Literal[False], Literal[False]]):
    """
    This function allows the bot to connect to the database.
    
    param:
        +------------------------------------------------+
        | database = 'postgres' , password = 'postgres'  |      
        | user     = 'postgres' , host     = '127.0.0.1' |
        | port     = '5432'                              |
        +------------------------------------------------+
    """ 
    if len(args) == ARGS_COUNT:
        db, pswrd, usr, hst, prt = args
        try:
            connection = psycopg2.connect(
                                          database = db   , 
                                          password = pswrd, 
                                          user     = usr  , 
                                          host     = hst  , 
                                          port     = prt
                                         )        
            return connection, connection.cursor()
        except:
            debug.saveLogs(f'ERROR! WRONG CONNECTION TO THE DATABASE\n\n{traceback.format_exc()}', paths.LOG_FILE)
    return False, False

def get_message(text, connection, cursor) -> (Tuple[Any] or Literal[False]):
    """
    This function send text to database and returns answer.
    """
    try:
        cursor.execute(text)
        data = cursor.fetchall()
        connection.commit()
        return data
    except:
        debug.saveLogs(f'ERROR! WRONG database DATA TAKING!\n\n{traceback.format_exc()}', paths.LOG_FILE)
    return False

def get_accounts_data(*args, accounts : dict = {}) -> Dict[int, classes.Account]:
    """
    This function get accounts data from database table 'accounts_tb'
    
    return: 
        dict with id as a key and Account as value
    
    create:
        +------------------------------------------------------------+
        | CREATE TABLE accounts_tb (                                 |
        |                           Id         SERIAL PRIMARY KEY ,  |                 
        |                           user_id    INTEGER            ,  |
        |                           username   VARCHAR(255)       ,  |
        |                           language   VARCHAR(255)       ,  |
        |                           first_name VARCHAR(255)       ,  |                                                     
        |                           last_name  VARCHAR(255)       ,  |                                                         
        |                           reg_date   VARCHAR(255)       ,  |
        |                           status     VARCHAR(255)       ,  |                  
        |                           wallet_id  BIGINT                |
        |                          );                                |
        +------------------------------------------------------------+
    """
    connection, cursor = args
    if connection and cursor:
        try:
            db_accounts = get_message(variables.db_accounts_get, connection, cursor)

            for acc in db_accounts: accounts[acc[ID_ITEM]] = classes.Account(*acc)
        except:
            debug.saveLogs(f'ERROR! WRONG database DATA TAKING!\n\n{traceback.format_exc()}', paths.LOG_FILE)
    return accounts


if __name__ == '__main__':
	
    args = sys.argv[1:]
    
    print('You need to enter more args to connect to database!\n'
          if connect(*args) == (False, False) else 'CONNECTED!\n')

    accounts = get_accounts_data(*connect(*args))

    print(*accounts.values())


#INSERT INTO accounts_tb (user_id, username, language, first_name, last_name, reg_date, status, wallet_id) VALUES (8888, 'mtvy', 'None', 'None', 'None', '04.01.22 02:20:22', 'None', 88888888888);
