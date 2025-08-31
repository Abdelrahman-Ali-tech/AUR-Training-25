from time import time
from rich.console import Console
console = Console()
def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)


class BaseMsg:
    def __init__(self, data: str):
        self._data = data
    
    @property
    def style(self):
        return '' # BaseMsg-specific
        
    @property
    def data(self):
        return self._data
    
    def __str__(self):
        return self._data # BaseMsg-specific
    
    def __len__(self):
        return len(self.data)
    
    def __eq__(self, other):
         if  isinstance(other,BaseMsg):
             other =str(other.data)
         return other == self.data   
             
    
    def __add__(self, other):
        if isinstance(other,BaseMsg):
            new = self.__class__(str(self.data)+ str(other))
        else :
            new = self.__class__(str(self.data)+ other)
        return new    



class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = int(time())
    def __str__(self):
        return f"[{self._timestamp}]"+self._data   
    @property
    def style(self):
        return 'on yellow' 
class WarnMsg(LogMsg):
    def __init__(self, data):
        super().__init__(data)
    def __str__(self):
        return f"[!WARN] [{self._timestamp}] "+self._data   
    @property
    def style(self):
        return 'bold white on red' 

if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)