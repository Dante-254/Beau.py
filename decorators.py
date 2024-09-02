def logtime(func):
    def wrapper():
        print('Its either you time manage,')
        val = func()
        print ('Or time will manage you.')
        return val
    return wrapper


@logtime
def hello():
    print('You hear me bwana Dante,')

hello()




# def manoti(n):
#     n +=1

# print(manoti)