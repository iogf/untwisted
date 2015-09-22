from untwisted.expect import Expect, LOAD, CLOSE
from untwisted import core
from untwisted.usual import xmap, die

def handle(expect, data):
    print data

expect = Expect('python', '-i', '-u')
xmap(expect, LOAD, handle)
xmap(expect, CLOSE, lambda expect: die())
expect.send('print "hello world"\nquit()\n')
core.gear.mainloop()



