import sys
import io

from multiprocessing import Process,Queue
from Strategies.core.sstream import sstream

class scriptExec():
    def __init__(self):
        self.stdout_ori = sys.stdout
        self.stdin_ori = sys.stdin
        self.stderr_ori = sys.stderr
        self.sString=sstream()
        sys.stdout=self.sString
        sys.stderr=self.sString
        pass
    def exec(self,script):
        exec(script)
        return self.sString.read()
def hande_script(queue,script):
    scriptEx = scriptExec()
    scriptEx.exec(script)
    # scriptEx.sString.display(scriptEx.stdout_ori)
    res=scriptEx.sString.read()
    queue.put(res)

def exec_script(script):
    ss=sstream()
    q=Queue()
    p=Process(target=hande_script,args=(q,script,)).start()
    res=q.get()
    return res

def main():
    script = "print([2, 2, 3])\nprint('123')\nprint([3, 2, 3])"
    # scriptEx=scriptExec()
    ss=sstream()
    q=Queue()
    print("before test!")
    p = Process(target=hande_script, args=(q,script,))
    p.start()
    res=q.get()
    print("---执行----")
    print(res)
    print("---完成----")
    print("after test!")
    #
    #
    # stdout_ori=sys.stdout
    # ex=scriptExec()
    # # print('test')
    # res=ex.exec(script)
    #
    # # print('123')
    # # ss=sString()
    # print('data in sStream>>:',res,file=stdout_ori)
    # ss=sString()
    # a = [1, 2, 3]
    # # print(ss.buff)
    # # ss.write(a)
    # # ss.display()
    # print(ss.readline())
    # ss.display()
if __name__=='__main__':
    main()

    # print(a.__str__())


