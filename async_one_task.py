import asyncio
class Owner:
    def __init__(self):
        print("Owner is initialed")


class Auto:
    def __init__(self,owner:Owner=None):
        self.owner=owner
        

class Message(Auto):
    async def send_message(self,name):
        await asyncio.sleep(3)
        return f"hello, your name is {name}"
    async def say_hello(self,tt):
        await asyncio.sleep(1)
        return f"say hi for everyone {tt}"

if __name__ == '__main__':   
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    oo = Owner()  
    mm = Message(oo)
    # result = loop.run_until_complete(Message(oo).send_message("USA"))
    result = loop.run_until_complete(mm.send_message("USA"))
    print(result)