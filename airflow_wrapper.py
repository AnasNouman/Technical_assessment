from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Define default arguments for the DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the function to run the Python script
def run_data_ingestion():
    script_path = 'ETL.py'
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed with return code {result.returncode}\n{result.stderr}")

# Define the DAG
dag = DAG(
    'data_ingestion_dag',
    default_args=default_args,
    description='A DAG to run data ingestion script',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Define the task
run_data_ingestion_task = PythonOperator(
    task_id='run_data_ingestion_task',
    python_callable=run_data_ingestion,
    dag=dag,
)

# Define task dependencies (if any)
# For example, if you have more tasks, you can set dependencies like this:
# run_data_ingestion_task >> next_task
