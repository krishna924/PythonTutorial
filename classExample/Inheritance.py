

class Cars(object):

    def __init__(self):
        print('You just invoked Car class')

    def drive(self):
        print('Car is started')
    def stop(self):
        print('Car is stopped')


class bmw(Cars):

    def __init__(self):
        Cars.__init__(self)
        print('You just invoked bmw class')

    def drive(self):
        super(bmw,self).drive()
        print('You are driving a BMW..')

    def autoHead(self):
        print('This is a special feature')

a = Cars()
a.drive()
a.stop()

b = bmw()
b.drive()
b.stop()
b.autoHead()
# b.drive(super)
