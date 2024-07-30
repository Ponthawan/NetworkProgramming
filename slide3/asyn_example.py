import asyncio

async def fetch_dta():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data' : 1}
async def print_numbers():
    for t in range(10)