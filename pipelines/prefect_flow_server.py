import pandas as pd
import os
from prefect import Flow, task


from datetime import timedelta

from prefect import Flow, Parameter, artifacts, task
from prefect.run_configs.local import LocalRun
from prefect.storage.local import Local
from prefect.tasks.airbyte.airbyte import AirbyteConnectionTask
from prefect.tasks.dbt.dbt import DbtShellTask
from prefect.tasks.secrets.base import PrefectSecret
# from prefect.tasks.snowflake.snowflake import SnowflakeQuery

from tasks import (
    HelloWorld
)

airbyte_conn = AirbyteConnectionTask(
        max_retries=3, retry_delay=timedelta(seconds=10),
        
     
)

# run_dbt = DbtShellTask(
#     command="dbt run",
#     environment="dev",
#     profile_name="covid_19",
#     helper_script="cd dbt",
#     set_profiles_envar=False,
#     max_retries=3,
#     retry_delay=timedelta(seconds=10),
# )

with Flow("first-airbyte-task", storage=Local(), run_config=LocalRun()) as flow:
    hello_world = HelloWorld()
    airbyte_file_sync = airbyte_conn(
        airbyte_server_host='34.125.42.0',
        airbyte_server_port=8000,
        airbyte_api_version="v1",
        connection_id="0f18a15b-ba3b-49ef-a17a-eb870641f7ee"
    )



