from app.services.datebase_api import DatebaseAPI
import asyncio 


async def test():
    async with DatebaseAPI() as client:
        uuid = await client.get("id")
        print(uuid)
        
asyncio.run(test())