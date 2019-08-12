
import logging#不会抛出错误，且可以输出到文件

logging.basicConfig(level=logging.INFO)
#Info以下级别不报错

s = '0'

n = int(s)

logging.info('n = %d' % n)

print(10 / n)