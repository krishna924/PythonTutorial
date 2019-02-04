

class excep(object):


    map1 = {'make' : 'hyundai', 'model': 'sonata', 'year': '2006'}

    def access(map, key):
        try:
            a = map[key]
            print(a)
        except:
            print('Theis is an exception')

o1 = excep()
o1.access('map1', 'key')
o2 = excep('make1')


