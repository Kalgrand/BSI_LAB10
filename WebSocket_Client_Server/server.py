"""
Server based on python websockets. It waits for encrypted message from client,
decrypts it and sends decrypted message back to client.

Autor: Maciej Milewski
"""


import asyncio
import websockets
from aes import *
from utils import *


async def message_handler(websocket, path):
    """ Waits for encrypted by AES message, decrypts it, sends it back to client"""
    name = await websocket.recv()
    print(f"< {name}")

    secret_key = fill_to_block("abcdabcdabcdabcd", 16)
    decrypted_text = aes_decode(name, secret_key)

    greeting = f"{decrypted_text}"

    await websocket.send(greeting)
    print(f"{greeting}")

start_server = websockets.serve(message_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()