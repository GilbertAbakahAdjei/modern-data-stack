import pandas as pd
import os



from datetime import timedelta

from prefect import Flow, Parameter, artifacts, task
from prefect.run_configs.local import LocalRun
from prefect.storage.local import Local
from prefect.tasks.airbyte.airbyte import AirbyteConnectionTask
from prefect.tasks.dbt.dbt import DbtShellTask
from prefect.tasks.secrets.base import PrefectSecret


from tasks import (
    StartUp
)

airbyte_conn = AirbyteConnectionTask(
        max_retries=3, retry_delay=timedelta(seconds=10),
        
     
)

run_dbt = DbtShellTask(
    command="dbt run",
    environment="dev",
    stream_output=True,
    profile_name="modern_data_stack",
    dbt_kwargs={
                'type': 'bigquery',
                'profiles_dir': 'profiles',
                'keyfile': '/code/pipelines/profiles/dbt_user_creds.json',
                
                'threads': 4,
                'project': 'modern-data-stack-343214',
                'dataset': 'dbt_gilbert_prefect',
                'timeout_seconds': 300,
                'location': 'US',
                'method': 'service-account',
                'priority': 'interactive'
            },
    overwrite_profiles=True,
    helper_script="cd ../dbt",
    set_profiles_envar=True,
    max_retries=3,
    retry_delay=timedelta(seconds=10),
    # log_stderr=True
)



with Flow("first-airbyte-task") as flow:
    start_up = StartUp()
    # airbyte_file_sync = airbyte_conn(
    #     airbyte_server_host='34.125.42.0',
    #     airbyte_server_port=8000,
    #     airbyte_api_version="v1",
    #     connection_id="0f18a15b-ba3b-49ef-a17a-eb870641f7ee"
    # )

    # dbt_run = run_dbt(
    #     upstream_tasks=[airbyte_file_sync]
    # )

    dbt_run = run_dbt(
    )


flow.run()

