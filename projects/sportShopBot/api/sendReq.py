import aiohttp


async def makeApiCall(url, method, data=None, file=False):

    async with aiohttp.ClientSession() as session:

        if method == 'get':
            async with session.get(url) as resp:
                response = await resp.json()
        elif method == 'post':
            if file is False:
                async with session.post(url, json=data) as resp:
                    response = await resp.json()
            else:
                if data is not None:
                    async with session.post(url, data=data) as resp:
                        response = await resp.json()
                else:
                    async with session.post(url) as resp:
                        response = await resp.json()
        elif method == 'put':
            async with session.put(url, json=data) as resp:
                response = await resp.json()
        elif method == 'delete':
            async with session.delete(url) as resp:
                response = await resp.json()

    return response
