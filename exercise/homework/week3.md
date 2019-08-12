#####IO编程
    同步
    异步

######文件读写
    读文件
        open,f=open('位置’,'r') r表示读且读取UTF-8编码的文本文件
        read,f.read()   一次性读取全部内容，用一个str对象表
            read(size)  每次调用size个字节，适用于不明确大小的文件
            readline()  每次返回一行
            readlines() 读取全部并按行返回list，适用于配置文件
        close，f.close() 关闭
        文件读写都可能出现error，可以用 try……finally
            try：
                f=open('xxxx',r)
                 print(f.read())
            finally:
                if f:
                    f.close()
        引入with语句将上述方法简化：
            with open('path/to/file/','r')
                print(f.read())
                  
    file-like Object
        类似open()函数返回的有read()方法的对象，统称file-like Object
        除file外还可以时内存的字节流，网络流，自定义流，等
        不要求从特定类继承，只要写个read()方法
        StringIO就是内存中的，常用作内存缓冲
        
    二进制
        f=open（'path/to/file/','rb'）
       
    字符编码
        非UTF-8编码的文本文件，要传入encoding参数
            f=open（'path/to/file/','r',encoding='编码类型'）
            >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
         
    写文件
        类似读文件，open()在调用时，传入，w或wb，表示写文本文件，或写二进制文件
        读写之后都要记得的close(),为了保险，同样使用with，使用encoding转码
        w,wb写入都会覆盖之前文本形成新文件，入要追加open（）可传入其他字符
            https://docs.python.org/3/library/functions.html#open
            
                         
            

######StringIO & BytesIO
    from io import StringIO/BytesIO
    f.write('***',encoding('编码')
    f.getvalue()
######操作文件和目录
    import os
        os.name#nt代表windows
        os.uname#详细的系统信息，win不支持
        os的某些函数是和操作系统相关的
    环境变量
        os.environ
        os.environ.get('KEY')#获取某个环境变量的值
    操作文件和目录
        os.path.join('','')
                split()
                abspath('.')
        os.mkdir()
        os.rmdir()
        os.rename()重命名
        os.remove()删除
        os.path.split('/Users/michael/testdir/file.txt')拆分后得到最后级别的目录or文件名
        os.path.splittext('/path/to/file.txt')得到扩展名       
        [ x for x in os.listdir('.') if os.path.isdir(x)]列出所有目录
        列出目录中所有的.py文件
        [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
######序列化
    把变量从内存中变为可存储的过程称为序列化pickling（其他语言serialization,marshalling,flattening
    把变量内容从序列化的对象重新读到内存里叫反序列化unpickling
    import pickle
    见do pickling.py
    不同编程语言之间传递，就要将对象序列化为标准格式
    JSON能被所有语言读取，并且更快
    JSON            PYTHON
    {}              dict
    []              list
    "string"        str
    1234.56         int或float
    true/false      True/False
    null            None
    impot josn
    
    
    


#####进程和线程
######多进程
######多线程
######ThreadLocal
######进程 vs. 线程
######分布式进程
#####正则表达式
    用字符来描述字符，规则：好多
    re模块包含所有正则表达式的功能
        需要注意转义，建议开头用r，不用考虑转义啦
    切分字符串split（）
    分组（group） （）
    贪婪匹配（默认）
        re.match(r'^(\d+?)(0*)$', '102300').groups()
        ？表示非贪婪匹配
    编译
        f=re.compile(r'正则表达式')
        f.match('str').groups()#groups()tuple
                 
        
#####常用内建模块
######datetime
######collections
    nametuple
        定义一种数据类型，具有tuple的不变性，且可以根据属性来引用
    deque
        快熟实现插入和删除，适用队列和栈
        append(),pop(),appendleft(),Popleft()
    defaultdict
        Key不存在返回默认值，其他同dict一致
    OrderedDict
        会按key的插入顺序排序，不是Key本身
    ChainMap
        把一组dict串起来组成逻辑上的dict，本身也是dict
    Counter
######base64
    base64.b64encode(b'str')
    base64.b64decode(b'str')
    urlsafe 的base64，把+，/，变为-,_
    '='易造成歧义，编码后会把'='去掉，解码前要加上'='把长度变为4的倍数
    

######struct
    https://docs.python.org/3/library/struct.html#format-characters
######hashlib
    
######hmac
######itertools
    count（）要和for语句搭配无限迭代
    repeat（‘***’，n）第一个元素无限，如果有第二个参数则限定次数
    takewhile（）配合条件判断截取有限数列
    chain
    groupby
######contextlib
    @contextmanager （装饰器），接收受成其，简化上下文，（？？？，执行指定操作）
    @closing把任意对象变为上下文对象，并支持with语句
######urllib
    get
    post 
        parse.urlencode
    handler 复杂控制，ProxyHandler 看不懂啊
######XML
######HTMLParser
    先放放吧，看不懂，唉
    