try:
    from hypercorn.middleware import AsyncioWSGIMiddleware, TrioWSGIMiddleware
    from . import app
    asyncio_app = AsyncioWSGIMiddleware(app)
except:
    pass
