from typing import Callable, Union, Coroutine
from datetime import datetime

CallbackFn = Callable[[str], Coroutine[None, None, None]]


async def acknowledge_job(payload: str, fn: CallbackFn) -> None:
    print(f"{datetime.now()}:{payload}")

    await fn("ack response")

