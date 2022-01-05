### Main libraries
import telebot, datetime, sys

## Debug libraries
import traceback


### Project files

## Bot's Token
import config

## Database functions and classes
import database, classes, paths

## Supporting functions
import utility

## Debug functions
import debug


# Init Bot
bot = telebot.TeleBot(config.TOKEN)
db_access : classes.DB_Access


@bot.message_handler(commands=['start'])
def welcome(message) -> None:
    
    accounts = database.get_accounts_data()

    if message.chat.id not in accounts.keys():
        accounts[message.chat.id] = classes.Account(message.chat.id              ,
                                                    message.chat.username        ,
                                                    None                         ,
                                                    message.chat.first_name      ,
                                                    message.chat.last_name       ,
                                                    str(datetime.datetime.now()) ,
                                                    8888                         )






@bot.message_handler(content_types=['text', 'photo'])
def lol(message):
    
    account = database.get_accounts_data()
    
    if message.chat.type == 'private':
        pass





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    accounts = database.get_accounts_data()
    try:
        pass
    except:
        debug.saveLogs(f'Error in [call]!\n\n{traceback.format_exc()}', paths.LOG_FILE)

if __name__ == '__main__':
    try: 
        db_access = classes.DB_Access(*sys.argv[1:])
        bot.polling(none_stop=True)
    except : debug.saveLogs (f'Program error!\n\n{traceback.format_exc()}', paths.LOG_FILE)
