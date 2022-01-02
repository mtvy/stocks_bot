### Main libraries
import telebot

## Debug libraries
import traceback


### Project files

## Bot's Token
import config

## Database functions and classes
import database, classes

## Supporting functions
import utility

## Debug functions
import debug


# Init Bot
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message) -> None:
    
    accounts = database.get_accounts_data()

    
    
    for account in account.keys():
        if account[account].telegram_id == new_account[0]:
            if account[account].language == "Русский":
                if account[account].personal_data == "YES":
                    bot.send_message(message.chat.id,"🔱Вы уже зарегистрированы в системе!")
                    keyboardRefMaker(message = message, lang = 0)
                elif account[account].personal_data == "NO":
                    inlineMessages(markup_text = openfileforRead(None, path.first_lang), message = message, 
                                   markup_arr = [["Согласен"   , "Согласен"   ], 
                                                 ["Отказываюсь", "Отказываюсь"]], action = False
                                  )
            elif account[account].language == "Ozbek":
                if account[account].personal_data == "YES":
                    bot.send_message(message.chat.id,"🔱Siz allaqachon ro'yxatdan o'tgansiz!")
                    keyboardRefMaker(message = message, lang = 1)
                elif account[account].personal_data == "NO":
                    inlineMessages(markup_text = openfileforRead(None, path.second_lang), message = message,
                                   markup_arr = [["ROZIMAN"      , "Agree"   ], 
                                                 ["Qo'shilmayman", "Disagree"]], action = False
                                  )
            else:
                inlineMessages(markup_text = "🔱Choose language", message = message, 
                               markup_arr = [["Русский", "Русский"], ["Ozbek", "Ozbek"]], action = False)
            break
    else:
        new_account += [str(message.chat.username), str(message.chat.first_name), [], "close", "0", [], "0", "NO", None, 'close', 0]
        account = classes.Account(new_account)
        database.insert_account_data(account)
        account[account.telegram_id] = account
        inlineMessages(markup_text = "🔱Choose language", message = message, 
                       markup_arr = [["Русский", "Русский"], ["Ozbek", "Ozbek"]], action = False)





@bot.message_handler(content_types=['text', 'photo'])
def lol(message):
    
    account = database.get_accounts_data()
    
    if message.chat.type == 'private':
        if message.text in variables.message_text_dict.keys():
            if   variables.message_text_dict[message.text][0] == 'office': 
                selectOffice(message, str(message.chat.id), variables.STEP_FIRST)
            elif variables.message_text_dict[message.text][0] == 'text_show': 
                pushingLabelFromFile(message, variables.message_text_dict[message.text][1], variables.message_text_dict[message.text][2])
            elif variables.message_text_dict[message.text][0] == 'oper_show': 
                operInit(message, variables.message_text_dict[message.text][1], variables.message_text_dict[message.text][2], str(message.chat.id))





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    account = database.get_accounts_data()
    try:
        if call.data in variables.call_data_dict.keys():
            if variables.call_data_dict[call.data][0] == 'set_lang':
                database.change_account_data(account = account[str(call.message.chat.id)], parametr = 'language', data = call.data)
                account = database.get_accounts_data()
                inlineMessages(markup_text = openfileforRead(None, variables.call_data_dict[call.data][1]), call = call, 
                               markup_arr = variables.call_data_dict[call.data][2])
            
            elif variables.call_data_dict[call.data][0] == 'disagree_data':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, variables.call_data_dict[call.data][1])
            
            


    except Exception as error:
        debug.saveLogs(f"Error in the 'call' part!\n\n[\n{traceback.format_exc()}\n]", path.log_file)
        for id in variables.label_change_ids_arr:
            bot.send_message(int(id), f"Error in the 'call' part!\n\n{traceback.format_exc()}")

if __name__ == '__main__':
    try: 
        bot.polling(none_stop=True)
    except Exception as _:
        debug.saveLogs(f"Program error!\n\n{traceback.format_exc()}", path.log_file)