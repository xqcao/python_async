import asyncio
class Owner:
    def __init__(self):
        print("Owner is initialed")


class Auto:
    def __init__(self,owner:Owner=None):
        self.owner=owner
        

class Message(Auto):
    async def send_message(self,name):
        await asyncio.sleep(0.5)
        return f"hello, are you from {name}"
    async def say_hello(self,tt):
        await asyncio.sleep(0.5)
        return f"say hi for everyone {tt}?"
    async def multi_tasks(self,aaa,bbb):
        input_coroutines =[self.say_hello(aaa),self.send_message(bbb)]
        res = await asyncio.gather(*input_coroutines, return_exceptions=True)
        return res
        
if __name__ == '__main__':   
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    oo = Owner()  
    mm = Message(oo)
    results= loop.run_until_complete(mm.multi_tasks("xiao","USA"))
    for r in results:
        print(r)
    