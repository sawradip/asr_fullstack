import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[],
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='socket.io'
)

@sio_server.event
async def connect(sid, environ, auth):
    print(f"Connected to {sid}")

@sio_server.event
async def connect(sid):
    print(f"Disconnected from {sid}")