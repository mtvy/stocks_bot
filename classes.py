# 
# Bot's clasess
#


class Account:
    """
    This class creates accounts with all user data.
    Need array acc that includes twelve params.
    """
    def __init__(self, *args):
        
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
    def __init__(self, *args):
        
        self.database, self.user, self.password, self.host, self.port = args
    
    def __str__(self):
        return f'Data for database connection ->   \n\
                     database  : {self.database}   \n\
                     user      : {self.user}       \n\
                     password  : {self.password}   \n\
                     host      : {self.host}       \n\
                     port      : {self.port}       \n'
                     


class Balance:
    """
    This object include balance of the account.
    """ 
    def __init__(self, *args):
        
        (self.usd , self.rub , self.euro,
         self.usdt, self.btc , self.eth ,
         self.sol                       ) = args
         
        self.balance_id   = self.generate_balance_id()
        self.balance_hash = None # generate_hash()
        
    
    def generate_balance_id(self) -> int:
    	
        self.balance_id = 0
        
        return self.balance_id


class Wallet(Balance):
    """
    This object include info about wallet and balance.
    """
    def __init__(self, user_info : (int, str), *args):
        
        super().__init__(*args)
        self.user_id, self.status = user_info
        
        self.wallet_id   = self.generate_wallet_id()
        self.wallet_hash = None # generate_hash()
        
    
    def generate_wallet_id(self) -> int:
        
        self.wallet_id = 0
        
        return self.wallet_id
    
    def __str__(self) -> str:
        
        return f'Wallet info ->                           \n\
                 user_id    : { self.user_id    }         \n\
                 status     : { self.status     }         \n\
                 wallet_id  : { self.wallet_id  }         \n\
                 balance_id : { self.balance_id }         \n\
                                                          \n\
                 Balance info ->                          \n\
                                   usd  : { self.usd  }   \n\
                                   rub  : { self.rub  }   \n\
                                   euro : { self.euro }   \n\
                                   usdt : { self.usdt }   \n\
                                   btc  : { self.btc  }   \n\
                                   eth  : { self.eth  }   \n\
                                   sol  : { self.sol  } \n\n\
                 wallet_hash  = { self.wallet_hash  }     \n\
                 balance_hash = { self.balance_hash }     \n'





if __name__ == '__main__':
	
    account = Account('8888', 'mtvy', 'None', 'None', 'None', '04.01.22 02:20:22', 'None', 'C0DE000000000000')
    
    print(account)
    
    db_access = DB_Access(None, None, None, None, None)
    
    print(db_access)
    
    value  = (0, 0, 0, 0, 0, 0, 0)
    
    wallet = Wallet((account.user_id, account.status), *value)
    
    print(wallet)
