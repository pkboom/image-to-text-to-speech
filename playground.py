from contextlib import contextmanager
from nicegui import ui
import asyncio


@contextmanager
def spinner() -> None:
    spinner = ui.spinner()

    try:
        yield
    finally:
        spinner.set_visibility(False)


async def slow_operation() -> None:
    with spinner():
        print("in slow operation")
        await asyncio.sleep(3)
        print("after sleep")


ui.button("Run spinner", on_click=slow_operation)

ui.run()
