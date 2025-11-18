import traceback
def check(n):
    try:
        if n<0:
            raise ValueError('x canot be zero')
    except Exception as e:
        print("Error",e)
        print("line_num",e.__traceback__.tb_lineno)
    else:
        print("n<0")
check(-1)