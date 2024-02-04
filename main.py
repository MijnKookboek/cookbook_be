from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def main(request: web.Request):
    return web.Response(text='hello world')


app = web.Application()
app.add_routes(routes)
web.run_app(app)