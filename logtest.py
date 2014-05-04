import logging
#logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',level=logging.DEBUG)
#logging.warning('is when this event was logged.')
import time
def lastLines(f,lines = 1,block_size=1024):
    f.seek(0, 2)
    block = ''
    start = 0
    #get seek position
    curpos = f.tell()
    while(curpos > 0): #while not BOF
        #seek ahead block_size+the length of last read block
        curpos -= (block_size + len(block));
        if curpos < 0: curpos = 0
        f.seek(curpos)
        #read to end
        block = f.read()
        nl_count = block.count('\n')
        #if read enough(more)
        if nl_count > lines: break
        #get the exact start position
    for n in range(nl_count-lines):
        start = block.find('\n', start)+1
    return block[start:]
f = open('weipan.log','r')
ss = lastLines(f,1)
dit = eval(ss[ss.find('INFO',0)+5:])
print dit['access_token']
print int(time.time())
ts = "/xx/yy/zz/nwiho"
t=[]
for it in ts.split('/'):
    t.extend(it.split('\\'))
print t