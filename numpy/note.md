#NumPy
已安装以下包
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nosepython
##预备知识  
在阅读本教程之前，你应该了解一些Python。如果你想复习一下，请查看Python教程。
如果你希望使用教程中的示例，还必须在计算机上安装一些软件。有关说明，请参见[https://scipy.org/install.html]。
##基础
NumPy的数组类，ndarray，(array.array只处理一维数组提供少量功能）

    ndarray.ndim:数组轴的个数（秩r),the number of axes of the array
    ndarray.shape:a tuple of inteegers indicating the size of the array in each dimension n行m列的矩阵，shape属性是(n,m),
    ndarray.size:the total number of elements of the array(this is equal to the product of the elements of shape)
    ndarray.dtype:an object describing the type of the elements in the array.One can creat or specify dtype's using standard Python types.Numpy provides types of its own,eg:numpy.int32,numpy.float64
    ndarray.itemsize:数组中每个元素的字节大小
    ndarray.data:包含实际数组元素的缓冲区，通常我们不需要使用这个属性，因为我们总是通过索引来使用数组中的元素。
###示例    
###创建数组
array函数从常规的python列表和元组创造函数，数组类型由原序列中的元素推导出来
    
    >>> import numpy as np
    >>> a = np.array([2,3,4])
    >>> a
    array([2, 3, 4])
    >>> a.dtype
    dtype('int64')
    >>> b = np.array([1.2, 3.5, 5.1])
    >>> b.dtype
    dtype('float64')
常见错误：多个数值参数调用array是错误的
    
    >>> a = np.array(1,2,3,4)    # WRONG
    >>> a = np.array([1,2,3,4])  # RIGHT
array将包含序列的序列转换为二维数组，序列包含、包含序列的序列转化为三位序列，等等
    
    >>> b = np.array([(1.5,2,3), (4,5,6)])
    >>> b
    array([[ 1.5,  2. ,  3. ],
           [ 4. ,  5. ,  6. ]])
数组类型也可以在创建时显示指定：
    
    >>> c = np.array( [ [1,2], [3,4] ], dtype=complex )
    >>> c
    array([[ 1.+0.j,  2.+0.j],
           [ 3.+0.j,  4.+0.j]])
通常，数组的元素最初都是未知的，但是它的大小是一致的。因此，NumPy提供几个函数来创建包含初始占位符的数组。这最小化了扩展数组的必要性以及高昂的运算代价
函数zeros会创建一个元素全为0的数组，函数ones创建一个元素全为1的数组，函数empty创建一个初始内容随机且依赖内存状态的数组。默认情况下创建的数组类型是float64
    
    >>> np.zeros( (3,4) )
    array([[ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.]])
    >>> np.ones( (2,3,4), dtype=np.int16 )                # dtype can also be specified
    array([[[ 1, 1, 1, 1],
            [ 1, 1, 1, 1],
            [ 1, 1, 1, 1]],
           [[ 1, 1, 1, 1],
            [ 1, 1, 1, 1],
            [ 1, 1, 1, 1]]], dtype=int16)
    >>> np.empty( (2,3) )                                 # uninitialized, output may vary
    array([[  3.73603959e-262,   6.02658058e-154,   6.55490914e-260],
           [  5.30498948e-313,   3.14673309e-307,   1.00000000e+000]])
           
为了创建一个数列，Numpy提供一个类似range的函数(arange)来返回数组而不是列表 
    
    >>> np.arange( 10, 30, 5 )
    array([10, 15, 20, 25])
    >>> np.arange( 0, 2, 0.3 )                 # it accepts float arguments
    array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])   
当arange使用浮点参数时，由于有先的浮点数精度，通常无法预测得到元素数。因此，通常更好的选择是使用linspace函数来接收我们想要的元素个数来代替arange指定步长

    >>> from numpy import pi
    >>> np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
    array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
    >>> x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
    >>> f = np.sin(x)
    
###打印数组
当你打印一个数组，NumPy以类似嵌套列表的形式展示它，但是呈现以下布局  
·最后的轴从左到右打印  
·倒数第二的轴自顶向下打印  
·其余的轴自顶向下打印，切片间通过空行隔开  
一维数组被打印成行，二维数组被打印成矩阵，三位数组被打印成矩阵列表  

    >>> a = np.arange(6)                         # 1d array
    >>> print(a)
    [0 1 2 3 4 5]
    >>>
    >>> b = np.arange(12).reshape(4,3)           # 2d array
    >>> print(b)
    [[ 0  1  2]
     [ 3  4  5]
     [ 6  7  8]
     [ 9 10 11]]
    >>>
    >>> c = np.arange(24).reshape(2,3,4)         # 3d array
    >>> print(c)
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
如果要打印的数组太大了，NumPy会自动跳过中间部分纸打印边角部分
```
>>> print(np.arange(10000))
[   0    1    2 ..., 9997 9998 9999]
>>>
>>> print(np.arange(10000).reshape(100,100))
[[   0    1    2 ...,   97   98   99]
 [ 100  101  102 ...,  197  198  199]
 [ 200  201  202 ...,  297  298  299]
 ...,
 [9700 9701 9702 ..., 9797 9798 9799]
 [9800 9801 9802 ..., 9897 9898 9899]
 [9900 9901 9902 ..., 9997 9998 9999]]
```
想要禁用NumPy的这种行为来打印整个数组，可以使用 set_printoption来更改打印选项

    >>> np.set_printoptions(threshold=sys.maxsize)       # sys module should be imported
    
###基本运算
数组的算术运算是作用在元素上的，并且结果保存在新创建的数组中

    >>> a = np.array( [20,30,40,50] )
    >>> b = np.arange( 4 )
    >>> b
    array([0, 1, 2, 3])
    >>> c = a-b
    >>> c
    array([20, 29, 38, 47])
    >>> b**2
    array([0, 1, 4, 9])
    >>> 10*np.sin(a)
    array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
    >>> a<35
    array([ True, True, False, False])
与很多矩阵语言不同，NumPy中的乘法运算符*是作用在元素上。矩阵乘法可以使用@运算符（python 3.5及以上版本）或dot函数或方法    
```
>>> A = np.array( [[1,1],
...             [0,1]] )
>>> B = np.array( [[2,0],
...             [3,4]] )
>>> A * B                       # elementwise product
array([[2, 0],
       [0, 4]])
>>> A @ B                       # matrix product
array([[5, 4],
       [3, 4]])
>>> A.dot(B)                    # another matrix product
array([[5, 4],
       [3, 4]])
```
一些运算符 类似*=或+=，则是在原数组直接更改而不是创建一个新数组
```
>>> a = np.ones((2,3), dtype=int)
>>> b = np.random.random((2,3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])



gy>>> b += a
>>> b
array([[ 3.417022  ,  3.72032449,  3.00011437],
       [ 3.30233257,  3.14675589,  3.09233859]])
>>> a += b                  # b 不会自动转译为整型
Traceback (most recent call last):
  ...
TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```
当不同类型的数组间进行运算时，结果数组的类型对应为更一般或更精确的类型（这一行为称为向上转型）
```
>>> a = np.ones(3, dtype=np.int32)
>>> b = np.linspace(0,pi,3)
>>> b.dtype.name
'float64'
>>> c = a+b
>>> c
array([ 1.        ,  2.57079633,  4.14159265])
>>> c.dtype.name
'float64'
>>> d = np.exp(c*1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
>>> d.dtype.name
'complex128'
```
 许多一元运算，例如计算数组所有元素之和，都是作为ndarray类的方法实现的
```
>>> a = np.random.random((2,3))
>>> a
array([[ 0.18626021,  0.34556073,  0.39676747],
       [ 0.53881673,  0.41919451,  0.6852195 ]])
>>> a.sum()
2.5718191614547998
>>> a.min()
0.1862602113776709
>>> a.max()
0.6852195003967595
``` 
默认情况下，这些运算应用到数组好像它是一个数字组成的列表，无论这个数组的形状如何。然而，指定axis参数可以在指定轴上进行运算
```
>>> b = np.arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)                            # sum of each column
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)                            # min of each row
array([0, 4, 8])
>>>
>>> b.cumsum(axis=1)                         # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
```
###通用函数
NumPy提供常见的数学函数如 sin,cos,和exp。在NumPy中这些被称作通用函数（ufunc），这些函数作用在数组元素上进行匀速，产生一个数组作为输出
```
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([ 1.        ,  2.71828183,  7.3890561 ])
>>> np.sqrt(B)
array([ 0.        ,  1.        ,  1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([ 2.,  0.,  6.])
```
###索引，切片和迭代
一维数组可以被索引、切片和迭代，就像列表和其他Python序列
```
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
>>> a
array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
>>> a[ : :-1]                                 # reversed a
array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
>>> for i in a:
...     print(i**(1/3.))
...
nan
1.0
nan
3.0
nan
5.0
6.0
7.0
8.0
9.0
```
多维数组每个轴有一个索引，这些索引由一个用逗号分隔的元组给出：
```
>>> def f(x,y):
...     return 10*x+y
...
>>> b = np.fromfunction(f,(5,4),dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2,3]
23
>>> b[0:5, 1]                       # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[ : ,1]                        # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, : ]                      # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```
当提供的索引少于轴数时，则认为缺失的索引是整个切片
```
>>> b[-1]                                  # the last row. Equivalent to b[-1,:]
array([40, 41, 42, 43])
```
b[i]括号中的表达式被当作i,后面跟着的 ：表示剩余的轴。NumPy也允许使用‘.’如b[i,...]
(...)代表产生一个完整索引元组所必须的分号。例如，x是一个秩为5的数组，那么：
x[1,2,...] 相当于 x[1,2,:,:,:],
x[...,3] 相当于 x[:,:,:,:,3] 
x[4,...,5,:] 相当于 x[4,:,:,5,:].  
```
>>> c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
...                 [ 10, 12, 13]],
...                [[100,101,102],
...                 [110,112,113]]])
>>> c.shape
(2, 2, 3)
>>> c[1,...]                                   # same as c[1,:,:] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[...,2]                                   # same as c[:,:,2]
array([[  2,  13],
       [102, 113]])
```
多维数组的迭代是对第一个轴而言的
```
>>> for row in b:
...     print(row)
...
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```
如果要对数组中的每个元素执行操作，可以使用flat属性，它是数组中所有元素的迭代器:
```
>>> for element in b.flat:
...     print(element)
...
0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
```
##形状操作
###改变数组形状
一个数组的形状由每个轴上的元素个数给出
```
>>> a = np.floor(10*np.random.random((3,4)))        #floor向下取整
>>> a
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
>>> a.shape
(3, 4)
```
数组的形状可以被多种命令修改。以下三个命令返回一个修改后的数组，不改变原数组
```
>>> a.ravel()  # 返回一维数组
array([ 2.,  8.,  0.,  6.,  4.,  5.,  1.,  1.,  8.,  9.,  3.,  6.])
>>> a.reshape(6,2)  # 返回修改后的数组
array([[ 2.,  8.],
       [ 0.,  6.],
       [ 4.,  5.],
       [ 1.,  1.],
       [ 8.,  9.],
       [ 3.,  6.]])
>>> a.T  # 返回转置后的数组
array([[ 2.,  4.,  8.],
       [ 8.,  5.,  9.],
       [ 0.,  1.,  3.],
       [ 6.,  1.,  6.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
```
ravel()返回数组的元素顺序通常是“C风格”的，意思是最右边的索引变化的最快，所以a[0,0]之后的元素是a[0,1]。如果数组被改编成其他形状，数组仍然是“C风格”的。NumPy通常创建一个以这种顺序存储数据的数组，因此ravel()不用总是复制他的参数。但如果是通过其他数组的切片或者不是平常的选项构成的数组，它可能需要被复制。ravel()he reshape()函数也可以使用可选参数构建处FORTRAN风格的数组，即最左边的变化最快
reshape()函数返回修改后的数组，ndarray.resize方法修改数组本身
```
>>> a
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
>>> a.resize((2,6))
>>> a
array([[ 2.,  8.,  0.,  6.,  4.,  5.],
       [ 1.,  1.,  8.,  9.,  3.,  6.]])
```
如果在改变形状的操作中，一个维度给作-1，其他维度会被自动计算
```
>>> a.reshape(3,-1)
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
```
###合并不同的数组
几个数组可以沿着不同的轴将数组合并在一起:vstack()hstack()
```
>>> a = np.floor(10*np.random.random((2,2)))
>>> a
array([[ 8.,  8.],
       [ 0.,  0.]])
>>> b = np.floor(10*np.random.random((2,2)))
>>> b
array([[ 1.,  8.],
       [ 0.,  4.]])
>>> np.vstack((a,b))
array([[ 8.,  8.],
       [ 0.,  0.],
       [ 1.,  8.],
       [ 0.,  4.]])
>>> np.hstack((a,b))
array([[ 8.,  8.,  1.,  8.],
       [ 0.,  0.,  0.,  4.]])
```
column_stack函数将一维数组合并为二维数组，它相当于hastack()对二维数组的
```
>>> from numpy import newaxis
>>> np.column_stack((a,b))     # with 2D arrays
array([[ 8.,  8.,  1.,  8.],
       [ 0.,  0.,  0.,  4.]])
>>> a = np.array([4.,2.])
>>> b = np.array([3.,8.])
>>> np.column_stack((a,b))     # returns a 2D array
array([[ 4., 3.],
       [ 2., 8.]])
>>> np.hstack((a,b))           # the result is different
array([ 4., 2., 3., 8.])
>>> a[:,newaxis]               # this allows to have a 2D columns vector
array([[ 4.],
       [ 2.]])
>>> np.column_stack((a[:,newaxis],b[:,newaxis]))
array([[ 4.,  3.],
       [ 2.,  8.]])
>>> np.hstack((a[:,newaxis],b[:,newaxis]))   # the result is the same
array([[ 4.,  3.],
       [ 2.,  8.]])
```
另一方面，ma.row_stack 对于任意的输入的数组都等同于vstack。一般地说，对于二维以上的数组，hstack沿着第二个轴、vstack沿着第一个轴合并。concatenate 允许一个可选参数给出数组合并要沿着的轴的号码
####note
在复杂的情况下，r_ 和c_于vstack和hstack的默认行为相似，但是允许提供可变参数，给出要连接的轴的数量
```
>>> np.r_[1:4,0,4]
array([1, 2, 3, 0, 4])
```
###将一个数组分割成几个更小的数组
使用hsplit函数，将数组沿着它的水平轴分割，通过指定返回相同形状数组的数量或者在指定的列后进行分割
```
>>> a = np.floor(10*np.random.random((2,12)))
>>> a
array([[ 9.,  5.,  6.,  3.,  6.,  8.,  0.,  7.,  9.,  7.,  2.,  7.],
       [ 1.,  4.,  9.,  2.,  2.,  1.,  0.,  6.,  2.,  2.,  4.,  0.]])
>>> np.hsplit(a,3)   # Split a into 3
[array([[ 9.,  5.,  6.,  3.],
       [ 1.,  4.,  9.,  2.]]), array([[ 6.,  8.,  0.,  7.],
       [ 2.,  1.,  0.,  6.]]), array([[ 9.,  7.,  2.,  7.],
       [ 2.,  2.,  4.,  0.]])]
>>> np.hsplit(a,(3,4))   # Split a after the third and the fourth column
[array([[ 9.,  5.,  6.],
       [ 1.,  4.,  9.]]), array([[ 3.],
       [ 2.]]), array([[ 6.,  8.,  0.,  7.,  9.,  7.,  2.,  7.],
       [ 2.,  1.,  0.,  6.,  2.,  2.,  4.,  0.]])]
```
vsplit将数组沿着纵向轴分割，array_split指定沿着哪个轴分割
##复制和视图
当运算和处理数组时，数组数据有时时被复制有时不是。这常常是初学者困惑的来源。有三种情况：
###完全不复制
简单的赋值，不赋值数组对象或数组的数据
```
>>> a = np.arange(12)
>>> b = a            # no new object is created
>>> b is a           # a and b are two names for the same ndarray object
True
>>> b.shape = 3,4    # changes the shape of a
>>> a.shape
(3, 4)
```
Python将可变对象最为引用，因此函数调用不用复制数组
```
>>> def f(x):
...     print(id(x))
...
>>> id(a)                           # id is a unique identifier of an object
148293216
>>> f(a)
148293216
```
###视图和浅复制
不同的数组对象能分享同一个数组，视图方法创建一个新的数组对象查看相同的数据
```
>>> c = a.view()
>>> c is a
False
>>> c.base is a                        # c is a view of the data owned by a
True
>>> c.flags.owndata
False
>>>
>>> c.shape = 2,6                      # c变形不会对a产生改变
>>> a.shape
(3, 4)
>>> c[0,4] = 1234                      # c数据改变会引起a的变化
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
```
数组的切片返回它的一个视图
```
>>> s = a[ : , 1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
>>> s[:] = 10           # s[:] is a view of s. Note the difference between s=10 and s[:]=10
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```
###深复制
###函数和方法视图
##更少的基础
###广播规则
##有趣的索引和索引技巧
###
###
###
###
##线性代数
###简单的数组运算
##技巧和提示
提供一些简短且有用的提示
###“自动”变型
改变数组的维度，你可以省略一个维度它将被自动推导出来
```
>>> a = np.arange(30)
>>> a.shape = 2,-1,3  # -1 means "whatever is needed"
>>> a.shape
(2, 5, 3)
>>> a
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14]],
       [[15, 16, 17],
        [18, 19, 20],
        [21, 22, 23],
        [24, 25, 26],
        [27, 28, 29]]])
```
###向量堆栈
如何利用相同大小的行向量列表构造一个二维数组呢？在MATLAB中非常简单：如果x和y式两个相同长度的向量，你只需要做m = [x;y]。在NumPy中这项工作式通过column_stack,dstack,hstack和vstack来实现的，取决你选择在哪个维度上组合。例如：
```
x = np.arange(0,10,2)                     # x=([0,2,4,6,8])
y = np.arange(5)                          # y=([0,1,2,3,4])
m = np.vstack([x,y])                      # m=([[0,2,4,6,8],
                                          #     [0,1,2,3,4]])
xy = np.hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])
```
在二维以上的维度，这些函数背后的逻辑可能很奇怪
###直方图
NumPy中histogram函数应用到数组上返回一对变量：数组的直方图和bin向量。注意：matplotlib也有一个创建直方图的函数（hist，于Matlab中一样）于NumPy中的不同。主要的不同是p;ab.hist紫铜的绘制直方图，而numpy.histogram只是产生数据
```
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
>>> mu, sigma = 2, 0.5
>>> v = np.random.normal(mu,sigma,10000)
>>> # Plot a normalized histogram with 50 bins
>>> plt.hist(v, bins=50, density=1)       # matplotlib version (plot)
>>> plt.show()
```
```
>>> # Compute the histogram with numpy and then plot it
>>> (n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
>>> plt.plot(.5*(bins[1:]+bins[:-1]), n)
>>> plt.show()
```

##拓展阅读

[https://scipy.org/install.html]: https://scipy.org/install.html