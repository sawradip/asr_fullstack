import socketio
import asyncio

sio_client = socketio.AsyncClient()

@sio_client.event
async def connect():
    print('Client connected.')

@sio_client.event
async def disconnect():
    print('Client disconnect.')

async def main():
    await sio_client.connect(url='http://localhost:8000', wait_timeout = 10,socketio_path='socket.io') # )
    print('Client doing its processing.')
    await sio_client.disconnect()

asyncio.run(main())