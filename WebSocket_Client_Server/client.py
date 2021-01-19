import asyncio
import websockets
from aes import *
from utils import *

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("Message to send: ")

        secret_key = fill_to_block("abcdabcdabcdabcd", 16)
        encrypted_text = aes_encode(name, secret_key)

        await websocket.send(encrypted_text)
        print(f"{name}")

        greeting = await websocket.recv()
        print(f"{greeting}")

asyncio.get_event_loop().run_until_complete(hello())