import aiohttp.web


async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    from utils.notify_users import on_day_notify
    #await on_day_notify(dp)


async def handler():
    return aiohttp.web.HTTPFound("http://127.0.0.1:443/")



if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp
    #handler()
    executor.start_polling(dp, on_startup=on_startup)
