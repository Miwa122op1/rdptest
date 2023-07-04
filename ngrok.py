import ngrok
async def create_tunnel(port):
    session = await ngrok.NgrokSessionBuilder().authtoken_from_env().connect()
    tunnel = await session.http_endpoint().listen()
    print (f"Ingress established at {tunnel.url()}")
    tunnel.forward_tcp(f"localhost:{port}")
await create_tunnel(3389)
while True:
    print(tunnel.url())
