from datetime import datetime
from asyncio import sleep


async def acknowledge_job(payload: str) -> str:
    print(f"{datetime.now()}: {payload}")

    # replace with real business logic
    await sleep(10)

    return "ack response"
