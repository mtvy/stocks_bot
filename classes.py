# 
# Bot's clasess
#


class Account:
    """
    This class creates accounts with all user data.
    Need array acc that includes twelve params.
    """
    def __init__(self, *args) -> None:
        
        (self.id         ,
         self.username   ,
         self.first_name ,
         self.last_name  ,
         self.reg_date   ,
         self.wallet     ) = args
    
    def __str__(self) -> str:
        return f'Account data ->                    \n\
                     id         : {self.id}         \n\
                     username   : {self.username}   \n\
                     first_name : {self.first_name} \n\
                     last_name  : {self.last_name}  \n\
                     reg_date   : {self.reg_date}   \n\
                     wallet     : {self.wallet}     \n'

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


if __name__ == '__main__':
	
    account   = Account('8888', 'mtvy', 'None', 'None', '04.01.22 02:20:22', 'C0DE000000000000')
    
    print(account)
    
    db_access = DB_Access(None, None, None, None, None)
    
    print(db_access)
