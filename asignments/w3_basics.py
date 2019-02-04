
import datetime
class basics(object):

    def getDate(self):
        date = datetime.datetime.now()
        print(str(date))

a = basics()
a.getDate()
basics.getDate()


# a = datetime.date.today()
# print(str(a))
# b = datetime.datetime.now()
# print(b)
# c = datetime.datetime.now().time()
# print(c)