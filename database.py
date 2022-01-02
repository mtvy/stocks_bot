
## Database library
import psycopg2

## Supporting libraries
import traceback, sys


## Debug functions
import debug

## Different structures
import classes, paths

#===============================================+
# database = 'postgres' , password = 'postgres' |
# user     = 'postgres' , host     = '127.0.0.1'|
# port     = '5432'                             |
#===============================================+
def connect(db, pswrd, usr, hst, prt):
    try:
        connection = psycopg2.connect(database = db, password = pswrd, user = usr, host = hst, port = prt)        
        return connection, connection.cursor()
    except:
        debug.saveLogs(f'ERROR! WRONG CONNECTION TO THE DATABASE\n\n{traceback.format_exc()}', paths.LOG_FILE)

    return False, False


def get_accounts_data():
    connection, cursor = connect()
    if connection == 0 and cursor == 0:
        return {}
    else:
        try:
            account_settings = {}
            cursor.execute("SELECT telegram_id, login, name, oper_ids, conversation, discount, tags, ref, personal_data, language, feedback_st, timer_conv FROM account_tb")
            accounts = cursor.fetchall()
            for acc in accounts:
                account = classes.Account(acc = acc)
                account_settings[account.telegram_id] = account
            connection.commit()
            #print('Successful account_tb data taken!')
            return account_settings
        except Exception as e:
            print('Error taking data from account_tb!', e)
            return {}


if __name__ == '__main__':
    print(sys.argv)
    #connect()