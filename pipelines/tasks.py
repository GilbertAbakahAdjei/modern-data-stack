from asyncio import tasks
import pandas as pd
import prefect
from prefect import task

@task
def StartUp():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")
    print("This is the first task without logging")