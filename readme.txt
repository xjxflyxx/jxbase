	
acquire_redis_lock(lock_name, redis_conn, expire_time=10, timeout=10)
功能说明：尝试获取 redis 中指定 lock_name 的锁， 以便对资源进行操作。主要用在分布式环境，因为各分布式电脑可能对 redis 的数据同时修改，所以修改前需要先获得锁，防止混乱。
Parameters
----------
        lock_name : TYPE：str
                说明：这是锁名称，实际上就是 redis 的一个 key
        expire_time : TYPE: int, optional
                说明：如果获到了锁，expire_time 是给锁加的超时时间，默认 10 秒，即本次加锁无论是否主动释放，锁都将在10秒后自动释放. The default is 10.
        timeout: type: int
                说明：这是本接口最多尝试的时间，单位秒，如果超过 timeout 还没获取到锁的话，则返回 False
 
Returns
-------
返回值：如果获取到锁，则返回给锁加的 uuid 值，否则返回 False
append_arr_to_df(df, arr)
功能说明：不直接修改传入的 df!!
        把数组形式的 arr （必须是一维）追加到 DataFrame 形式的 df 行末尾，并将 df 返回到主调函数，
        要求 arr 的元素个数及含意与 df 的列数及含义相同；注意：添加行后，将重建索引！
参数：df: pandas 格式； arr: 一维 list，要求元素个数及含义与 df 的列数及含义相同
返回值：在原 df 最后一行添加 arr 后生成新的 result_df
change_path_style(xpath=None, style='UNIX', end_slash=None)
功能说明：转换路径风格
参数：
        xpath: 为待转换的路径； 
        style： 为目标风格，接受值：'dos','windows','linux','unix', 以及他们的大写，含意与小写相同。默认 unix（linux）风格
        endwith: 表示转换路径后是否确保路径末尾必须有指定符号，默认 None，表示原汁原味，不在末尾添加任何符号，可接受以下符号
                None: 表示不添加任何符号，保持原样
                True: 表示确保路径末尾以'/'或'\'结尾
                False: 表示确保路径末尾没有'/'或'\'结尾
返回值：转换风格后的路径
concat(arr)
功能说明：本函数模仿 pandas.concat()，但可以接受 None 元素以及任何元素，但只有 df  元素才会被拼接，其他元素都将被忽略。
参数：
        arr: type: list
                说明：该参数必须是一个 list，其元素为 df （所有 df 的列名和顺序都必须相同）或 None或其他任何数据类型，但只有 df 会被采用，其他元素都会被忽略。                      
Returns
-------
返回值：拼接好后的 df. 若传入的 arr 中没有 df，则返回 None
convert_df_type(df, xtype=<class 'float'>, column_arr=None)
功能说明：不直接修改传入的 df!!
        对传入的 df ，根据传入的字段 column_arr （如果有的话，要是没有的话，则对 df 中所有字段转换），
        从 df 中找到对应的列，将其数据类型转换为 xtype 指定的类型；
        无法转换的数据值将用0填充，请调用者自己注意填 0 后返回去是否符合要求！  若不符合要求就不要调用本函数。
参数：
        df, 待转换字段类型的 df; 
        xtype, 目标数据类型；
        column_arr，需要转换哪些列
返回值：转换数据类型后的 df
decrypt(crypt_msg, key=None, xtype='ARC4', **kwargs)
功能说明：本接口用来对传入的数据 crypt_msg 调用 xtype 指向的解密类型用相应的密钥 key 进行解密
参数：
        crypt_msg: 字节流型，必填
                说明：该参数是待解密的字节流型串（原先已加密）
        key: str型或bytes型，可选，默认值 None, 
                说明：若参数 xtype='rsa'，则 key必须指定。大部分解密类型下，key 都必须指定
        xtype: str型，可选，默认值: 'ARC4'
                说明：该参数指出用哪种解密方式进行解密，解密方式取决于当初的加密方式，可取以下值（不区分大小写）：
                'rsa': 表示用 rsa 的私钥进行解密
                'chacha20': 表示用 chacha20 进行解密，需要传入当初用 chacha20 加密后返回的 key 和 nonce 分别给形参 key 和 nonce
                'aes': 表示用 aes 进行解密，需要传入当初用 aes 加密后返回的 key 和 nonce 分别给形参 key 和 nonce
                'arc4': 表示用 arc4 进行解密，需要传入当初用 arc4 加密后返回的 key 给形参 key
        kwargs: 用来传递某些解密方法需要用到却又未在本接口命名的形参，如传递 nonce 给形参 nonce 等
返回值：msg, str型，即解密后的数据
delete_api_list(filename)
功能说明：对一个 .py 文件，查找其中是否有 __all__ ，有的话将其定义的 list 删除，把删除后剩余的内容写到原文件。
 
Parameters
----------
        filename : TYPE：str
                只接受 .py 文件
Returns
-------
返回值：无。直接把删除 __all__ 定义后的 .py 文件，直接保存到原文件
df_to_list(df, head=False)
功能说明：将 df 转成二维数组
参数：
        df: pandas的 DataFrame数据
        head: type: bool, 表示要不要包含列头，可取以下值：
                True：保留列头
                False 不保留列头（默认）
返回值：二维数组
df_to_table(df, head=True, align='center', color_flag=False, fore_color1='black', fore_color2='black', bgcolor1='#F5F5DC', bgcolor2='#A7EEFB')
功能说明：将 df 转成 html 的 table 形式，并以字符串形式返回，主要是为了发电子邮件用
参数：
        df:待转换的 pandas DataFrame数据；
        head: type: bool, 表示要不要保留df 的列名，可取以下值：
                True ：表示保留列头（默认）
                False：表示不要保留
        align:对齐方式，可取值为： 'left','center','right'，默认 'center'；
        color_flag:要不要用前景色背景色装饰表格，取值True或False；
        在 color_flag = True 的前提下，后面这几个参数才有效，
        fore_color1: 前景色1（即定体颜色）；
        fore_color2:前景色2（字体颜色）；
        bgcolor1: 表格行背景色1；
        bgcolor2:表格行背景色2
返回值：字符串形式的 html table
df_to_tuple(df, head=False)
功能说明：将 df 转成二维元组（不包括列名），即整个是元组，里面每一行也是元组
参数：
        df: pandas的 DataFrame数据
        head: type: bool, 表示要不要包含列头，可取以下值：
                True：保留列头
                False 不保留列头（默认）
返回值：二维元组
df_to_webpage(df, head=True, align='center', color_flag=False, fore_color1='black', fore_color2='black', bgcolor1='#F5F5DC', bgcolor2='#A7EEFB')
功能说明：将 df 转成 html webpage 形式，并以字符串形式返回，主要是为了发电子邮件用
参数：
        df:待转换的 pandas DataFrame数据；
        head: type: bool, 表示要不要保留df 的列名，可取以下值：
                True ：表示保留列头（默认）
                False：表示不要保留
        align:对齐方式，可取值为： 'left','center','right'，默认 'center'；
        color_flag:要不要用前景色背景色装饰表格，取值True或False；
        在 color_flag = True 的前提下，后面这几个参数才有效，
        fore_color1: 前景色1（即定体颜色）；
        fore_color2:前景色2（字体颜色）；
        bgcolor1: 表格行背景色1；
        bgcolor2:表格行背景色2
返回值：字符串形式的 html webpage
encrypt(msg, key=None, key_len=32, xtype='ARC4', **kwargs)
功能说明：本接口用来对传入的数据 msg 调用 xtype的加密类型用密钥 key 进行加密
参数：
        msg: str型或字节流型，必填
                说明：该参数为待加密的字符串，（若是其他类型，可先转成字符串）
        key: str型或bytes型，可选，默认值 None, 
                说明：若参数 xtype='rsa'，则 key必须指定。
        key_len: int型，可选，默认值32
                说明：若参数 key 为 None，则 key_len 起作用，将由接口自动产一个长度为 key_len 的 key
        xtype: str型，可选，默认值: 'ARC4'
                说明：该参数指出用哪种加密方式进行加密，可取以下值（不区分大小写）：
                'rsa': 表示用 rsa 非对称加密（有限长加密）
                'chacha20': 表示用 chacha20 对称加密（流加密）
                'aes': 表示用 aes 对称加密（块加密）
                'arc4': 表示用 arc4 对称加密（流加密），这个加密方法比较简单，只要一个 key 即可加密和解密，所以设成了默认加密方法。
        kwargs: 预留扩展参数用
返回值：result_arr: 是一个 list, 第一个元素是加密后的信息，字节流类型（不转成 str 型返回是因为有些加密后的字节流在转成 str 过程中要出错，所以保留字节流型返回
                其他元素（若有的话）个数及含义取决于加密类型 xtype
                1. 若加密类型 xtype = 'rsa'，则返回值 result_arr中只有一个元素，即加密后的信息（字节流形式）
                2. 若加密类型 xtype = 'chacha20', 则返回值 result_arr 中有3个元素，第一个元素是加密后的信息（字节流形式），第二个元素是用来解密的 key, 第三个元素是解密要用到的参数 nonce
                3. 若加密类型 xtype = 'aes', 则返回值 result_arr 中有3个元素，第一个元素是加密后的信息（字节流形式），第二个元素是用来解密的 key, 第三个元素是解密要用到的参数 nonce
                4. 若加密类型 xtype = 'arc4', 则返回值 result_arr 中有2 个元素，第一个元素是加密后的信息（字节流形式），第2个元素是用来解密的 key
file_log(msg, filename=None)
功能说明：本接口的作用是把 msg 信息记录到 filename 文件中去（文件位置会由本接口自动指定，一般会指定到 report_dir）
 
Parameters
----------
msg : TYPE: str
        说明：这是待写到文件的信息
filename : TYPE：str, optional
        说明：这是文件名。 The default is None.
 
Returns
-------
返回值：写成功返回 True, 否则返回 False.
find(xpath, s, case_sensitive=False, out_file=None)
功能说明：本接口在指定的 xpath 目录（及子目录）下对所有文本文件中查找指定字符串 s，把所有包含 s 的文件显示出来；
                若指定了 out_file 的话，则将查找结果同时保存到 out_file 中。
 
Parameters
----------
        xpath: type: str, 待查找的目录
        s : TYPE：str, 待查找字符串
        case_sensitive: type:bool, 表示是否大小写敏感，可取值 True 或 False ，分别表示敏感或不敏感（默认 False)
        out_file : TYPE:str, optional
                如果有指定的话，则将查找结果输出到文件. 
 
Returns
-------
返回值：查找结果所在的文件形成的 list
ftp_close(ftp)
功能说明：关闭FTP 连接
参数：ftp: 已经连接的 ftp 对象
返回值：无
ftp_down(ftp, filename)
功能说明：该函数用来从 FTP 服务器下载文件，
参数：ftp: 指向 FTP 服务器的连接符；filename: 待下载的文件，可以是windows 格式包含全路径的文件
返回值：无
ftp_open(host=None, port=None, username=None, password=None)
功能说明：初始化 FTP 连接，返回指向 ftp 服务器的连接符。首先会尝试从传入的参数中读取信息，
        若没传入，则次选从用户的配置文件 user_config.ini 中读取FTP 服务器配置信息，若没有，则第3选择从 py 配置文件中读取，若还是没有，则返回 None
参数：host: FTP服务器；port: 服务器端口; username: 登录 ftp  的用户名; password: 登录 ftp 的密码
返回值：成功登录后的 ftp 操作对象（若登录失败则返回 None)
ftp_up(ftp, filename)
功能说明：该函数用来上传文件到FTP 服务器，
参数：ftp: 指向 FTP 服务器的连接符；filename: 待上传的文件，可以是windows 格式包含全路径的文件
返回值：无
get_api_list()
功能说明：本函数仅仅用于返回可用接口列表，不在列表中列出的函数或接口等请不要调用，他们一般在内部实现使用，未来可能会改名或调整！！
 
Returns
-------
返回值：可用接口, list形式
get_arr_add(arr1, arr2)
功能说明：计算两个数组（相同维度）对应元素（必须数值型）的加法
参数：arr1, arr2：参加求和的两个 list
返回值：arr1 和 arr2 对应元素的求和结果（list型）
get_arr_divide(arr1, arr2)
功能说明：计算两个数组（相同维度）对应元素（必须数值型）的除法(arr1 / arr2)
参数：arr1, arr2：参加求商的两个 list
返回值：arr1 和 arr2 对应元素的求商结果（list型）
get_arr_multiply(arr1, arr2)
功能说明：计算两个数组（相同维度）对应元素（必须数值型）的乘积
参数：arr1, arr2：参加求积的两个 list
返回值：arr1 和 arr2 对应元素的求积结果（list型）
get_arr_ratio(arr1, arr2)
功能说明：计算两个等长数值数组 arr2 各元素相对于 arr1 各对应元素的增长幅度，即 (arr2 - arr1 ) / arr1 这个意思，
        具体要用到 numpy ，python 的 list 无法直接这样计算，必须先转成 numpy 的 array 才行。
参数：arr1, arr2: 两个数值型 list
get_arr_sub(arr1, arr2)
功能说明：计算两个数组（相同维度）对应元素（必须数值型）的减法(arr1 - arr2)
参数：arr1, arr2：参加求差的两个 list
返回值：arr1 和 arr2 对应元素的求差结果（list型）
get_builtin_modules()
功能说明：查找所有已安装的随 python 内置的模块或包，以 list 形式将他们返回。
 
Returns
-------
返回值：所有已安装的随 python 内置的模块或包组成的 list
get_comment_start_symbol(line, comment_symbol_arr)
功能说明：从给定的程序源码行 line 的注释结束符（若有的话）之后的剩余内容中寻找一个有效的注释起始符，注释起始符和结束符配对情况要传给 comment_symbol_arr 
                # 按照 python 语法要求，一行代码中去掉注释结束符后剩余部分的内容，如果有的话，必须以注释起始符开始，否则在注释结束符后的同一行内写有效代码是语法错误。
                # 因此 本接口 对传入的 注释结束符之后的同一行剩余代码，都会检测是不是以注释符起始符开头，若不是，直接返回 None，否则才开始检测注释嵌套。
 
Parameters
----------
        line : TYPE：str，程序源码行（一行）
        comment_symbol_arr : TYPE，二维 list
                这是一个二维 list，每一个元素是一维 list,这一维 list 只包含两个元素，分别是起始注释符和结束注释符
Returns
-------
返回值，找到的有效起始符，若没找到，则返回 None
get_comment_symbols()
功能说明：定义一个字典，建立文件类型与其注释符对应关系
 
Returns
-------
返回值：是一个 dict,每个元素的 key 代表源码文件类型（如：.py），value 代表该源码文件的注释符(是一个二维 list，其中每个元素是一维 list，该一维 list 包含两个元素，表示开始注释符和结束注释符)
get_computer_name()
功能说明：该函数用于获取电脑名称
参数：无
返回值：电脑名称（字符串类型）
get_count_24(num_arr, result=24, operator_arr=None, times_arr=[0])
功能说明: 根据传入的操作数 num_arr (list形式) 和操作符 operator_arr(list 形式), 每个数用且只用一次, 返回计算结果和 result 一致的表达式
参数: num_arr: 操作数 list;  operator_arr: 操作符 list; result: 要求计算达到的结果
返回值: 解的步骤（list 类型），list 中的每个元素（字符串）代表其中一步解
get_current_function_name()
功能说明：当该函数被调用时，将返回上级函数（即主调函数）的函数名，所以一般用它放在函数内部来获取函数名 
参数：无
返回值：主调函数名（字符串形式）
get_current_time(xtime=None, time_format='%Y-%m-%d - %H:%M:%S')
功能说明：根据传入的时间戳，取出时间返回
参数：xtime: 是时间戳，如time.time() 返回的结果
返回值：返回该时间戳指向的时间部分，以HH：MM：SS字符串格式返回。
get_date(xtime=None)
功能说明：根据传入的时间戳，取出日期返回
参数：xtime: 是时间戳，如time.time() 返回的结果
返回值：返回该时间戳指向的日期部分，以YYYY-MM-DD字符串格式返回。
get_date_time(xtime=None, time_format='%Y-%m-%d - %H:%M:%S')
功能说明：根据传入的时间戳，取出日期时间返回
参数：xtime: 是时间戳，如time.time() 返回的结果
返回值：返回该时间戳指向的日期时间部分，以YYYY-MM-DD - HH:MM:SS 字符串格式返回。
get_day(xdate=None)
功能说明：对传入的日期取日份以数值型返回，
参数：xdate，表示传入日期，取值可以是YYYY-mm-dd格式，或用 python 构造的日期型，
返回值：整型日
get_days_step(n=1)
功能说明：根据传入的参数n，返回 n天
 
Parameters
----------
n : TYPE int, optional
        表示天数. The default is 1.
 
Returns
-------
返回值：python datetime.timedelta() 日期类型的天数
get_empty_df(df)
功能说明：不直接修改传入的 df!! 根据传入的df, 返回一个由该 df 的列头组成且保持顺序的空的 df
 
Parameters
----------
df : TYPE: pandas dataframe
 
Returns
-------
空的 df
get_file_info(filename)
功能说明：统计一个 程序源码文件的有效代码行数，注释行数，空白行数等
参数：
        filename, 表示一个程序源码文件（可能需全路径）
Returns
-------
返回值：df，该df包含有效代码行数，注释行数，空白行数等。
get_file_lines(filename, include_blank_line=False)
功能说明：统计一个 文件的行数
参数：
        filename, 表示一个文本文件（可能需全路径）
        include_blank_line: type: bool，表示是否统计空行，默认 False，表示不统计空行
Returns
-------
返回值：该文件的行数
get_hash(s, hash_mode='sha512')
功能说明：根据传入的哈希算法对传入的字符串 s 进行哈希计算，并将结果返回
参数：s: 待计算字符串，hash_mode: 哪种哈希算法
返回值：哈希计算后的结果（字符串类型）
get_hh(xtime=None)
功能说明：根据传入的时间 ，返回小时部分（整型）
参数：xtime，可以是格式为 hh:mm:ss 的时间字符串，也可以是时间戳
返回值：整型 hh
get_home_dir()
功能说明：本接口用于获取用户主目录路径。
        在 linux 上执行，获取到的是 home 所在路径；
        在 windows 上执行，获取到的是当前用户的用户目录，类似这样：C:\Users\Administrator
 
Returns
-------
返回值：用户目录所在路径
get_installed_modules()
功能说明：返回所有已安装的模块或包组成的 list（包括内置模块或包第3方安装的模块或包）
 
Returns
-------
返回值：返回所有已安装的模块或包组成的 list（包括内置模块或包第3方安装的模块或包）
get_kelly_percent(p, rl, rw)
功能说明：获取用凯利公式计算后的下注百分比（应用凯利公式的前提是数学期望必须大于0，否则用不用凯利公式的结局都是亏！！）
                凯利公式（Kelly Formula）: f = p/rl - q/rw，  (即下注百分比 = 赢的概率/净损失率 - 输的概率/净收益率)
                p:表示赢的概率（必须是达到 rw 的概率）
                q: 表示输的概率（p + q = 1)（必须是达到 rl 的概率）
                rl: 损失率，即输掉时应当支付的百分比，譬如今天炒股亏损 5%， 那这个 rl 就取 5%，而上述的 q，就是指 rl 发生的概率
                rw: 收益率，即赢到的百分比，譬如今天炒股盈利 7%，则 rw 就取 7%，而上述的 p，就是指 rw 发生的概率
                注意：按照凯利公式，p + q 必须为 1， rl 和 rw 也必须是对立事件，不是这个发生就是那个发生。
                        赌博不是输就是赢，其模型比较适合凯利公式；而炒股的股价是连续变化，未来股价变化有非常非常多的取值，每一个价格都有一个对应的概率，
                        所以，股票模型是个概率分布，不是非此即彼的对立事件，同时，rl 和 rw 也成了概率分布，如此一来，凯利公式无法直接用在股票模型上，
                        只有把股票的连续的价格变化通过抽象建模转换成二值对立事件，然后才可以套用凯利公式。
Parameters
----------
        p : TYPE: float
                表示赢的概率（必须是达到 rw 的概率）    
        rl : TYPE: float
                损失率，即输掉时应当支付的百分比，譬如今天炒股亏损 5%， 那这个 rl 就取 5%，而上述的 q，就是指 rl 发生的概率
        rw : TYPE: float
                收益率，即赢到的百分比，譬如今天炒股盈利 7%，则 rw 就取 7%，而上述的 p，就是指 rw 发生的概率
Returns
-------
返回值：是一个百分比，表示按照可以承受损失的总本金的这个百分比去下注，会使收益最大化。
        （注意：只有当返回值大于 0 才有意义，如果返回值小于或等于 0，则不赌就是赢！！！！）
get_lastfile(xpath)
功能说明：从 xpath 目录中找出修改时间为最新的一个文件，并返回给主调函数
参数：xpath: 表示一条目录路径
返回值：xpath 目录下修改时间最新的文件。
get_line_nums(filename, lines_arr=None)
功能说明：这个函数很重要，本包内的一些其他接口依赖他。
                扫描一个 程序源码文件，生成代码行行号 list, 注释行号 list, 空白行号 list，以及函数定义行号 list, 类定义行号 list（目前函数定义行及类定义行统计只针对 .py 源码）
                返回一个 dict, 有 5 个元素指向 5 个list,
                5 个元素分别是 'code'，表示代码行,'comment'，表示注释行，'blank'，表示空白行
                                以及 'func' 表示函数定义所在行，'xclass' 表示类定义所在行。
参数：
        filename, 表示一个程序源码文件（可能需全路径）
        lines_arr: 表示一个源码文件已用 linecache.getlines() 读取出来的结果传进来，如果这个值为 None，则采用 filename，否则先采用 lines_arr，避免重复到 filename 中读大量数据。
Returns
-------
返回值：    返回一个 dict, 有 5 个元素指向 5 个list,
                5 个元素分别是 'code'，表示代码行,'comment'，表示注释行，'blank'，表示空白行
                以及 'func' 表示函数定义所在行，'xclass' 表示类定义所在行。
get_mac_address()
功能说明：获取本机 MAC 地址
get_magic_square(n=3, arr=None)
功能说明：该函数用于产生一个幻方，使得每一行、每一列以及对角线，他们各自的和都相等。
参数：n: 方阵的边长，必须是大于等于 3 的正整数；
        arr（可选）: 是一个 list，表示需要对 arr 中的数求幻方，arr 的长度必须是一个奇数的平方数。
        arr 是可选的，如果输入 arr ，则不考虑 n
返回值：幻方（df格式）
get_mm(xtime=None)
功能说明：根据传入的时间 ，返回分钟部分（整型）
参数：xtime，可以是格式为 hh:mm:ss 的时间字符串，也可以是时间戳
返回值：整型 mm
get_month(xdate=None)
功能说明：对传入的日期取月份以数值型返回，
参数：xdate，表示传入日期，取值可以是YYYY-mm-dd格式，或用 python 构造的日期型，
返回值：整型月份
get_page_by_gevent(url_arr, xcount=None)
功能说明：调用该函数返回由url_arr 所指向的一堆url所对应的页面源码。
Parameters
----------
url_arr : list
        是 url list，每个元素是一个 url
xcount : int
        取值正整数或 None，表示url_arr 中完成几个即结束；默认值None ，表示需要完成所有 url 的请求
 
Returns
-------
是一个 list ，每个元素是 url_arr 中相应 url 的 page_source
get_page_by_requests(url, header=None)
说明：下载（获取）指定 URL 的页面源码。对于静态 html 或网站能直接提供数据的（包括api形式，string 形式，json形式等），
        请优先使用本接口去获取数据，次选上面的 get_page_by_urllib() 接口；
        若网站的数据没有直接给，而是用 js 方式提供的话，则请调用下面的 get_page_by_browser() 方式去获取，它是模拟浏览器的
参数：url：目标地址; headers: 请求头，若没有传入，则由本函数自己调用请求头。
返回值：url 指向的 page_source（本函数已经将取到的 page_source  decode() 成字符串形式（纯文本））
get_pid_arr(xname=None, accurate=False, include_name=True)
功能说明：根据参数 xname 查找相应的进程号，如果xname 为 None，则返回所有进程号
 
Parameters
----------
        xname : TYPE:str, optional，欲查找的进程名称，如果是 None，则返回所有进程id
        accurate: type:bool, default: False, 表示精确查找还是模糊查找，可取以下值：
                True: 表示精确查找，此时，只有进程名和输入的 xname 完全相等才返回进程id
                False: 表示模糊查找，此时，进程名只要包含 xname，则返回进程 id
        include_name: 表示返回的结果中是否需要包含进程名，可取以下值：
                True: 表示需要包含进程名（默认）
                False: 表示不需要包含进程名
Returns
-------
返回值：进程 id 组成的 list
get_pid_name_arr()
功能说明：获取所有进程
Returns
-------
返回值：list，其元素是 dict，每个 dict 包含两个 key，分别是 'name', 'pid'，他们指向进程名和进程id
get_prime_arr(n=100)
功能说明：返回 n 以内的所有素数
get_private_ip()
功能说明：获取本机内网ip地址，这是获取到真实的内网IP，应优先使用本函数。
参数：无
返回值：本机内网 IP。
get_project_info(project_dir, file_type_str='.py;.c;.cpp;.js;.go;.m;.pl;.lua;.rb;.rs;.scala;.java')
功能说明：根据项目所在路径，统计项目所有源码文件累计有效代码行数，注释行数，空白行数等，
Parameters
----------
        project_dir : TYPE:str
                说明：这是一条项目路径，必填。
        file_type: type:str
                说明：表示哪些文件类型需进行统计行数，它是一个字符串，把所有需统计的文件扩展名以点开头添加进这个字符，相互用分号隔开即可
        include_blank_line: type: bool，
                说明：表示是否统计空行，默认 False，表示不统计空行
Returns
-------
返回值：df，包含有效代码行数，注释行数，空白行数等列
get_project_lines(project_dir, file_type_str='.py;.c;.cpp;.js;.go;.m;.pl;.lua;.rb;.rs;.scala;.java', include_blank_line=False)
功能说明：根据项目所在路径，统计项目所有源码文件总行数
Parameters
----------
        project_dir : TYPE:str
                说明：这是一条项目路径，必填。
        file_type: type:str
                说明：表示哪些文件类型需进行统计行数，它是一个字符串，把所有需统计的文件扩展名以点开头添加进这个字符，相互用分号隔开即可
        include_blank_line: type: bool，
                说明：表示是否统计空行，默认 False，表示不统计空行
Returns
-------
返回值：总行数, int 型
get_public_ip()
功能说明：获取本机公网ip地址
参数：无
返回值：本机公网 ip
get_pyfile_imported_modules(pyfile)
功能说明：返回一个 .py 文件中所有被 import 到的模块及包组成的 list
 
Parameters
----------
        pyfile : TYPE: str  要求输入的一个 .py 文件（含全路径，否则只在当前目录找）
 
Returns
-------
返回值：返回一个 .py 文件中所有被 import 到的模块及包组成的 list
get_pyproject_imported_modules(project_dir, save_to_file=True, out_file='requirements.txt')
功能说明：返回一个 python 项目中的所有 import 到的模块和包构成的 list（不含版本号）,
        如果有指定 out_file 的话，则同时将输出保存到 out_file 所指的文件中，
        在输出文件中所有的包统一附加了版本号 >=0.0.1，使用者若引用输出文件的话，请考虑清楚统一版本号0.0.1 是否适合你，不要盲目引用！！
 
Parameters
----------
        project_dir : type:str 项目路径。如果为 None，则直接取当前目录路径
        save_to_file: type: bool. 表示是否保存到文件，
                取值 True or False，True 表示需要保存到文件， False 表示不需要保存。
                若该值为 True，则下面的 out_file 起作用，否则忽略 out_file
        out_file : TYPE:str, optional
                用于保存结果的文件，一般就是 'requirements.txt' 这个文件名，最好不要更改。
 
Returns
-------
返回值：项目中所有 import 的到模块或包构成的 list（不含版本号）
get_randint_arr(xbegin=1, xend=10)
功能说明：调用该函数返回一个在xbegin（含） 和 xend（含）之间的随机整数 list
参数：xbegin：起始整数；xend: 结束整数
返回值：随机整数构成的一维 list
get_randint_df(n=3)
功能说明：调用该函数返回一个 n x n 的 元素为不大于 n 的随机整数构成的 df
get_report_dir()
说明：该函数用来获取 report/路径，如果没有则创建之。并且以 '/' 结尾
返回值：report/ 目录在用户目录下完整路径
get_rsa_key(bit=1024)
功能说明：本接口用来产生一对rsa public key 和 rsa private key
参数：
        bit: int型，可选，默认值 1024
                说明：本参数表明密钥长度
        
返回值：list，共有3个元素，第1个元素是 public key,字节流类型, 第2个元素是 private key，字节流类型；
                第3个元素表示能加密的明文长度，int型。
get_site_modules(with_version=False)
功能说明：返回所有第3方安装的模块和包
 
Returns
-------
返回值：所有已安装的第 3方模块和包组成的 list
get_ss(xtime=None)
功能说明：根据传入的时间 ，返回秒数部分（整型）
参数：xtime，可以是格式为 hh:mm:ss 的时间字符串，也可以是时间戳
返回值：整型 ss
get_system_encoding()
功能说明：获取操作系统的编码字符集
get_time(xtime=None, time_format='%H:%M:%S')
功能说明：根据传入的时间戳，取出时间返回
参数：xtime: 是时间戳，如time.time() 返回的结果
返回值：返回该时间戳指向的时间部分，以 HH:MM:SS 字符串格式返回。
get_today()
功能说明：获取今天日期（python格式）
参数：无
返回值：今天日期（python 格式)
get_tomorrow()
功能说明：获取明天日期（python格式）
参数：无
返回值：明天日期（python格式）
get_uuid()
功能说明：该函数用于获取一个 uuid()，其作用是产生一个唯一数，一般用在某种场 合做 ID，并且以时间开头，方便需要时判断
参数：无
返回值：生成的十进制 uuid
get_verify_code(code_image)
功能说明：处理验证码，传入的参数 code_image 为待处理的验证码图片（不是图片文件，而是图片数据）
参数：code_image: 待处理的验证码图片（不是图片文件，而是图片数据）
返回值：文本验证码
get_year(xdate=None)
功能说明：对传入的日期取年份以数值型返回，
参数：xdate，表示传入日期，取值可以是YYYY-mm-dd格式，或用 python 构造的日期型，
返回值：年份（数值型）
get_yesterday()
功能说明：获取昨天日期（python格式）
参数：无
返回值：昨天日期（python 格式）
hms_to_minutes(xtime)
功能说明：将传入的 xtime 转为分钟数返回
参数：xtime，取值可以为 hh:mm:ss 或时间戳
返回值：分钟数
hms_to_seconds(xtime)
功能说明：将传入的 xtime 转为秒数返回
参数：xtime，取值可以为 hh:mm:ss 或时间戳
返回值：秒数
hms_to_timestamp(xtime, xdate=None)
功能说明：将输入的日期时间转成时间戳戳（timestamp），
参数：xdate 可以是字符串形式，也可以是python date 格式，如果没有输入，则取今天
        xtime 是时间，需要 hh:mm:ss 形式
返回值： 转换后的时间戳
int_to_list(intnum)
功能说明：对输入的一个整型数 intnum 以 list形式返回，list 中的每个元素都是整型，他们是原整型数的各个数位
is_linux()
功能说明：判断操作系统是否 linux，是的话返回 True, 否则返回 False
is_number(n)
功能说明：测试输入的参数是否为数值型（或数值型字符串），如是则返回 True，否则返回 False
参数：n: 待检测的数据
返回值：如是数字则返回 True，否则返回 False
is_valid_date(xdate)
功能说明：判断是否日期
参数：xdate: 表示传入的日期
返回值：True: 表示传入的的确是日期；False: 表示传入的不是日期
is_weekday(xdate=None)
功能说明：该函数用于判断传入的日期（若没传入，则判断今天）是否为周一到周五
参数：xdate: 日期，取值可以是'-' 分割的字符串日期，也可以是 python 格式的日期
返回值：如果是周一到周五，则返回True，否则返回 False
is_weekend(xdate=None)
功能说明：该函数用于判断传入的日期（若没传入，则判断今天）是否为双休日
参数：xdate: 日期，取值可以是'-' 分割的字符串日期，也可以是 python 格式的日期
返回值：若是双休日，则返回True，否则返回 False
is_windows()
功能说明：判断操作系统是否 windows，是的话返回 True, 否则返回 False
list_to_tuple(arr, quote_flag=False)
功能说明：该函数用于将 list 转成 tuple，包括只有一个元素的情形 (注意：本函数将 list 转成 tuple 主要是给数据库 sql 用的，用在其他地方不一定合适)
参数：arr, 待转换的数组，quote_flag 表示是否给转换后的每个元组元素加上单引号，如果是 True 的话就加，加上去主要为了给数据库查询语句 select 用
返回值：xtuple, 字符串形式的元组
make_api(dir_or_file, force=False, stop_func='z')
功能说明：本接口对指定的 python 项目或源码文件，生成 API 列表（不是说明文档），
        即相当于给 py 库文件的开头加上 __all__ , 并搜索所有接口定义（函数定义），将有定义的接口名放到 __all__ 这个 list 中，
 
Parameters
----------
        dir_or_file: 表示可以接受文件名或目录名
        force: type:bool, 表示是否重新生成 api list，无论是否已有 api list，可取以下值：
                True: 表示要重新生成 api list，即若有旧的 api list，则先删除它，然后生成新的 api list
                False: 表示如果已经有 api list，则直接返回。 （默认）
        stop_func : TYPE, optional
                是函数名，表示如果遇到了 stop_func，就停止搜索. 缺省函数名为 'z'.
 
Returns
-------
返回值：无
make_header()
说明：构造一个 http 请求头返回
merge_list(arr, drop_duplicates=False)
功能说明：合并 arr 中的元素（也是list）后返回
 
Parameters
----------
        arr: type:list，这是一个二维 list，其元素也是 list
        drop_duplicates: type:bool
                说明：该参数表示是合并 list 后是否去重，默认 False，表示不去重，即纯粹的合并，不做去重。
Returns
-------
返回值：合并后的 list
num_to_words(num)
功能说明：转换数字为大写（财务）货币格式( format_word.__len__() - 3 + 2位小数 )
参数：num: 待转换的数字，支持 float, int, long, string 格式
返回值：财务上的大写金额
recognize_verify_code(image_path)
功能说明：识别验证码，其中具体调用下面的 recognize_code_by_tesseract() 来识别
参数：image_path: 图片路径
返回值：文本形式的验证码
release_redis_lock(lock_name, lock_id, redis_conn)
功能说明：本接口用于释放 redis 锁
Parameters
----------
lock_name : TYPE: str
        说明：这是 redis 锁（本质是 key 名）
lock_id : TYPE: str
        说明：这是 redis 锁的值，本质是 key 所指向的 value
 
Returns
-------
返回值：释放成功返回 True，否则返回 False
remove_df(df, to_be_remove_df)
功能说明：不直接修改传入的 df!! 对传入的 df 去除 to_be_remove_df 中的数据后返回
 
Parameters
----------
        df : TYPE: pandas dataframe
                说明：股票信息数据（腾讯实时tick数据为宜，也可接受网易K线数据）
        to_be_remove_df: type: pandas dataframe
                说明：也是df格式的股票数据，这是从 df 中待删除的数据
 
Returns
-------
返回值：df 去除 to_be_remove_df 中的数据后返回（df格式）
retry_command(command, para='', wait_time=None, retry_count=10, auto_wait=True)
功能说明：对传入的命令command，尝试执行 retry_count 次, 只要执行到成功，立马返回
参数：
        command: 传入的命令（对象）；
        para: 字符串形式的参数链，必须完整；
        wait_time: 表示两次尝试之间的等待时间；
        retry_count: 尝试执行次数; 
        auto_wait: 表示在每次尝试失败后是否愿意等待一段时间尝试下一次，True 表示愿意，False 表示不等待。
        如果 wait_time 不为 None ，则直接用 wait_time 而不考虑 auto_wait， 否则考虑 auto_wait, 如果这时 auto_wait为 True，则由系统自己决定等待时间，如果为 False，则采用 0 等待
返回值：返回一个 list，包含两个元素[command, result], 第一个元素是传进来的 command 对象本身，第2个元素是执行结果。（因为有些执行是直接改变自身的，所以需要把自身改变后的 command 返回给主调函数）
run_process(func, name='process1', daemon=False, start=True, block=False, **kwargs)
功能说明：本接口用于运行进程
 
Parameters
----------
        func : 函数名或方法名
                说明：这是待运行的进程（即函数名或方法名）
        name: 表示要启动的进程名称，这里随机取一个预设值，这个名称最好由外部传入以表达正确含义
        daemon: 表示子进程是否依赖主进程，如果是，则设置 daemon 为 True，表示子进程必须随主进程退出而退出，避免子进程被启动后而主进程已退出导致子进程成为僵尸进程。
        start: type: bool, 表示是否在本接口内启动进程，默认 True，表示要启动；若为 False，则将进程返回给主调函数处理
        block: type:bool, 表示是否以阻塞方式运行 func，默认 False，表示非阻塞。              
        **kwargs : TYPE: dict
                说明：这是上述进程 func（函数或方法）要用到的参数，字典形式传入
 
Returns
-------
None.
run_thread(func, start=True, block=False, **kwargs)
功能说明：本接口用于运行线程
 
Parameters
----------
        func : 函数名或方法名
                说明：这是待运行的线程（即函数名或方法名）
        start: type: bool, 表示是否在本接口内启动线程，默认 True，表示要启动；若为 False，则将线程返回给主调函数处理
        block: type:bool, 表示是否以阻塞方式运行 func，默认 False，表示非阻塞。
        **kwargs : TYPE: dict
                说明：这是上述线程 func（函数或方法）要用到的参数，字典形式传入
 
Returns
-------
None.
seconds_to_hms(seconds)
功能说明：将秒数转为 hms 形式
参数：seconds，秒数
返回值：hms, 表示 HH:MM:SS 格式的时间
security_check(ip)
功能说明：本函数获取本机 公网 ip ，和传入的 ip 比较，以判断程序是否运行在传入的 ip 电脑上，
        若不是，则返回 False 给上层代码，以决定是否退出，这样可防止程序被非法运行在指定 IP 以外的电脑上。
参数：ip: 本程序能正确运行的电脑的 ip
返回值：True or False,
send_mail(msg_dict, receiver_arr, smtp_server, smtp_port, sender_email, sender_password, mode='inline')
功能说明：自定义发邮件函数，
参数：
        msg_dict: 为邮件标题和内容构成的字典，只需包含content 和 subject 两项即可，有其他项数据也是可以的; 
                如果要发送图片，则要在 msg_dict 中定义 image_arr，即要定义 msg_dict['image_arr'], 而 image_arr 中的元素都是一条条指向图片的路径。
        receiver_arr: 邮件接收者email 构成的数组,如果是单个接收者也可以是字符串形式的 email地址 ；
        smtp_server: smtp 服务器IP或域名；
        smtp_port: smtp 服务器端口；
        sender_email: 邮件发送者的email 地址；
        sender_passwprd: 发送者的密码；
        mode: 取值为 inline 或 attachment，表示对图片是内嵌方式发还是附件形式发；
        注意，参数 receiver_arr 为数组形式，每个元素是字符串，内容是email 地址，如果有多个收件人，则在数组中以逗号分割; sender: 发件人的邮箱地址，字符串格式。
返回值：无
sort_df_column(df, column_arr, inplace=False)
功能说明：对传入的 df ，将其各列按照 column_arr 中的列顺序排列后形成新的 df 返回。
        1. 若 df 中的列名与 column_arr 没有交集，则返回原 df;
        2. 若 df 中的列名与 column_arr 只有部分交集，则只对 df 中的交集字段按 column_arr 排序，然后放在新 df 的前面，
                df中有而column_arr 中没有的字段统统按原来顺序排在新生成的 df 后面；
        3. 若 df 中的列名是 column_arr 子集，则将 df 中的所有列完全按照 column_arr 中的顺序排列。
参数：
        df:待（按列）排序的 df; 
        column_arr: 被参照排序的字段 list
        inplace: 表示是否直接修改原 df，默认 False，表示先 copy 一个 df，然后对 copy 的 df 进行修改，inplace 可取以下值：
                True: 表示直接修改传入的 df
                False: 表示生成一个新的 df 进行修改，保持原 df 不变。
返回值：列排序后的 df
strdate_to_pydate(xdate)
功能说明：将字符串形的日期，转化成python datetime.date() 表示的日期
参数：xdate: 待转换的字符串形式的日期
返回值：py 形式的日期
time_spend(t1)
功能说明：该函数计算t1 到 t2 之间的时间差，并输出信息，一般在程序末尾调用，输出程序执行花了多少时间
参数：t1： 表示起始时间，需时间戳形式，即秒数
返回值：无
timestamp_to_hms(xtime)
功能说明：将时间戳转成 HH:MM:SS格式，丢掉日期部分
参数：xtime: 时间戳格式
返回值：HH:MM:SS格式的时间
to_path(xpath=None, style='UNIX', end_slash=True)
功能说明：转换路径风格
参数：
        xpath: 为待转换的路径； 
        style： 为目标风格，接受值：'dos','windows','linux','unix', 以及他们的大写，含意与小写相同。默认 unix（linux）风格
        endwith: 表示转换路径后是否确保路径末尾必须有指定符号，默认 True，表示路径末尾必须有斜杠或反斜杠
                None: 表示不添加任何符号，保持原样
                True: 表示确保路径末尾以'/'或'\'结尾
                False: 表示确保路径末尾没有'/'或'\'结尾
返回值：转换风格后的路径
to_pydate(xdate)
功能说明：将字符串形的日期，转化成python datetime.date() 表示的日期
参数：
        xdate: 待转换的日期，可以是字符串型，py datetime.date() 型，或 df 中含有 date 的列
返回值：py 形式的日期。如果传入的是 df ，则将 df 中 date列 转换成 py datetime.date() 然后返回 df，若没有 date 列，则将原 df 返回
        无论 df 中有没 'date' 列，返回的 df 的 index 和传入时保持一致。
xround(f, bit=2)
功能说明：由于 python3 的  round() 函数返回的结果与我们中国人的常规认识不同，所以自定义一个 xround() 函数 来代替系统提供的 round()
        注意：本函数是通过加一个较小的数（0.0000001） 来达到符合中国习惯的四舍五入目的的，精度为小数点后6位。
        请注意本法是否符合用户的四舍五入要求，若不符合，请不要调用！
参数：f: 要进行四舍五入的目标数值, 也可以是dataframe 的数值列；bit: 表示保留几位小数
        注意：若是df传给f, 则 df 最好是独立的，否则就是对其它df 的引用，若传其他 df 的引用进来，则会产生slice 警告
 
返回值：四舍五入后的数值
