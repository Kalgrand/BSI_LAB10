import asyncio
import websockets
from aes import *
from utils import *


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    secret_key = fill_to_block("abcdabcdabcdabcd", 16)
    decrypted_text = aes_decode(name, secret_key)

    greeting = f"{decrypted_text}"

    await websocket.send(greeting)
    print(f"{greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()