

def exceptionhandeling():

    try:
        a = 10
        b = 20
        c = 0

        d = (a+b)/c
        print(d)
    except ZeroDivisionError:
        print("We are in the exception block - Zero Division")
        raise Exception ("This is an exception")
    except:
        print("We are in the exception block")
    else:
        print("Bec there are no excpetions")
    finally:
        print('FInally, always gets executed')
exceptionhandeling()