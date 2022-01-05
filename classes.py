# 
# Bot's clasess
#


class Account:
    """
    This class creates accounts with all user data.
    Need array acc that includes twelve params.
    """
    def __init__(self, *args) -> None:
        
        (self.user_id    ,
         self.username   ,
         self.language   ,
         self.first_name ,
         self.last_name  ,
         self.reg_date   ,
         self.status     ,
         self.wallet_id  ) = args
    
    def __str__(self) -> str:
        return f'Account data ->                      \n\
                     user_id    : { self.user_id    } \n\
                     username   : { self.username   } \n\
                     language   : { self.language   } \n\
                     first_name : { self.first_name } \n\
                     last_name  : { self.last_name  } \n\
                     reg_date   : { self.reg_date   } \n\
                     status     : { self.status     } \n\
                     wallet_id  : { self.wallet_id  } \n'


class DB_Access:
    """
    This class collect data for database connection.
    """
    def __init__(self, *args) -> None:
        self.database, self.user, self.password, self.host, self.port = args
    
    def __str__(self):
        return f'Data for database connection ->   \n\
                     database  : {self.database}   \n\
                     user      : {self.user}       \n\
                     password  : {self.password}   \n\
                     host      : {self.host}       \n\
                     port      : {self.port}       \n'
                     


class Balance:
    
    def __init__(self, *args) -> int:
        
        (self.usd ,
         self.rub ,
         self.euro,
         self.usdt,
         self.btc ,
         self.eth ,
         self.sol ) = args
         
        return generate_balance_id()
        
    def generate_balance_id(self) -> int:
        self.balance_id = 0
        return self.balance_id


class Wallet:
    
    
    def __init__(self, account : Account, *args) -> int:
        
        
        self.user_id, self.status = account.user_id, account.status
        
        self.hash = None
        
        self.balance_id = Balance(*args)
         
        return generate_wallet_id()
    
    def generate_wallet_id(self) -> int:
        self.wallet_id = 0
        return self.wallet_id

if __name__ == '__main__':
	
    account   = Account('8888', 'mtvy', 'None', 'None', 'None', '04.01.22 02:20:22', 'None', 'C0DE000000000000')
    
    print(account)
    
    db_access = DB_Access(None, None, None, None, None)
    
    print(db_access)
