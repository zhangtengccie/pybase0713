from kamene.all import *
from kamene.layers.inet import ICMP, IP
class Qping():
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.srcip=None
        self.length = 100
        self.ping_pkt =IP(dst=self.ipaddr) / ICMP()


    def src(self, srcip):
        self.srcip = srcip
        self.ping_pkt = IP(dst=self.ipaddr, src=self.srcip) / ICMP()

    def size(self, length):
        self.length = length
        self.ping_pkt = IP(dst=self.ipaddr, src=self.srcip,len=self.length) / ICMP()

    def one(self):
        ping_result = sr1(self.ping_pkt, timeout=2, verbose=False)
        # print(self.ping_pkt.show())
        if ping_result:
            print(f'{self.ipaddr} 可达！')
        else:
            print(f'{self.ipaddr} 不可达！')
    def ping_five(self):
        for i in range(5):
            ret = sr1(self.ping_pkt,  timeout=2, verbose=False)
            # print(self.ping_pkt.show())
            if ret:
                print('!',end='',flush=True)
            else:
                print('.',end='',flush=True)
        print()

    def __str__(self):
        if self.srcip is None:
            return '<%5s=>dest_ip: %5s,size: %s>' % (self.__class__.__name__,self.ipaddr,self.length)
        else:
            return '<%5s=>dest_ip: %5s,src_ip:%5s,size: %s>' % (self.__class__.__name__,self.ipaddr,self.srcip,self.length)

class Newping():
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.srcip=None
        self.length = 100
        self.ping_pkt =IP(dst=self.ipaddr) / ICMP()
    def size(self, length):
        self.length = length
        self.ping_pkt = IP(dst=self.ipaddr, src=self.srcip,len=self.length) / ICMP()
    def ping_five(self):
        for i in range(5):
            ret = sr1(self.ping_pkt,  timeout=2, verbose=False)
            # print(self.ping_pkt.show())
            if ret:
                print('!',end='',flush=True)
            else:
                print('+',end='',flush=True)
        print()
    def __str__(self):
        if self.srcip is None:
            return '<%5s=>dest_ip: %5s,size: %s>' % (self.__class__.__name__,self.ipaddr,self.length)
        else:
            return '<%5s=>dest_ip: %5s,src_ip:%5s,size: %s>' % (self.__class__.__name__,self.ipaddr,self.srcip,self.length)

if __name__ == '__main__':
    ping = Qping('1.1.1.200')
    total_len  =70
    def pring_new(word,s='-'):
        print('{0}{1}{2}'.format(s*int((70-len(word))/2),word,s*int((70-len(word))/2)))
    pring_new('print class')
    print(ping)
    pring_new('ping one for sure reachable')
    ping.one()
    pring_new('ping five')
    ping.ping_five()
    pring_new('set payload lenth')
    ping.size(200)
    print(ping)
    ping.ping_five()
    pring_new('set ping src ip address')
    src_ipaddr = '2.2.2.20'
    ping.src(src_ipaddr)
    print(ping)
    ping.ping_five()
    pring_new('new class NewPing','=')
    newping=Newping('1.1.1.200')
    newping.size(400)
    print(newping)
    newping.ping_five()