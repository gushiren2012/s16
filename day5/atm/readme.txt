run 函数，main 调用run，运行程序
user_data字典，
trans_logger 交易日志
 
auth acc_login调取acc_auth2
acc_auth2 调取db_handle，file_execute的内存地址，
data输入sql语句，
db_handler连接数据库，
conn_params获取数据库的配置，
conn_params如果引擎是file_storage
return 调用文件处理的接口，传到file_db_handle
file_db_handle解析了db文件的路径，返回函数file_execute的内存地址
file_execute
可以传sql语句，
db_path 路径拼起来，解析SQL语句，
account就是账号名，一个账号一个文件，
如果是select语句，按等号分割，
判断字段名是否account，判断是不是一个文件，是文件打开读取，并返回数据，返给data
判断密码，
exp_time过期时间，account_sample.如果过期了就不允许登录了，否则返回数据
settings 定义database，engine存储引擎，name数据库名，path，数据库路径

main.py
acc_data传回来的账户信息
如果账户认证成功，就交互

取款
withdraw
account_data 重新加载accoun最新数据，打印信用值和余额，如果不回退，就一直循环
如果输入长度大于0，并且输入的是数字
薪的余额为 记录交易日志，
make_transaction main.py 
type交易类型，
interest 手续费，当前金额乘
old_balance旧的余额
判断加减，如果加钱plus，
如果取款，原始余额-取款金额-手续费
如果余额小于0，就提示余额不足
dump_conunt 最新数据存到账户文件里
log_obj.info 记录日志

作者:Alex Li
版本:示例版本 v0.1
程序介绍:
    实现ATM常用功能
    功能全部用python的基础知识实现,用到了time\os\sys\json\open\logging\函数\模块知识, 主要帮给大家一个简单的模块化编程的示例

    注意:只实现了"还款"和"取现功能"

程序结构:
day5-atm/
├── README
├── atm #ATM主程目录
│   ├── __init__.py
│   ├── bin #ATM 执行文件 目录
│   │   ├── __init__.py
│   │   ├── atm.py  #ATM 执行程序
│   │   └── manage.py #ATM 管理端,未实现
│   ├── conf #配置文件
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core #主要程序逻辑都 在这个目录 里
│   │   ├── __init__.py
│   │   ├── accounts.py  #用于从文件里加载和存储账户数据
│   │   ├── auth.py      #用户认证模块
│   │   ├── db_handler.py   #数据库连接引擎
│   │   ├── logger.py       #日志记录模块
│   │   ├── main.py         #主逻辑交互程序
│   │   └── transaction.py  #记账\还钱\取钱等所有的与账户金额相关的操作都 在这
│   ├── db  #用户数据存储的地方
│   │   ├── __init__.py
│   │   ├── account_sample.py #生成一个初始的账户数据 ,把这个数据 存成一个 以这个账户id为文件名的文件,放在accounts目录 就行了,程序自己去会这里找
│   │   └── accounts #存各个用户的账户数据 ,一个用户一个文件
│   │       └── 1234.json #一个用户账户示例文件
│   └── log #日志目录
│       ├── __init__.py
│       ├── access.log #用户访问和操作的相关日志
│       └── transactions.log    #所有的交易日志
└── shopping_mall #电子商城程序,需单独实现
    └── __init__.py
