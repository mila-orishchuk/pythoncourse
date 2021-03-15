'''
Echo server with asyncio

Create a socket echo server which handles each connection using asyncio Tasks.
'''
import logging
import asyncio

class EchoServer:
    def __init__(self):
        self.clients = {}

    async def echo(self):
        while True:
            for client_name, client in self.clients.items():
                logging.debug(f"Sending echo to client {client_name}")
                logging.info(await client.send_request('echo-m', 'hello {client_name} from server'))
            await asyncio.sleep(3)

    async def start(self):
        loop = asyncio.get_running_loop()

        server = await loop.create_server(lambda: asyncio.Protocol(server=self, loop=loop), host= 'localhost', port=8888)
        logging.info(f'Serving on {server.sockets[0].getsockname()}')

        async with server:
            await asyncio.gather(server.serve_forever(), self.echo())


async def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)

    server = EchoServer()
    await server.start()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    logging.info("SIGINT received.")


