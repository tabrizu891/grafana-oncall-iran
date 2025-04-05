# Push task metrics to push gateway.
import socket

from prometheus_client import CollectorRegistry, Counter, push_to_gateway


def push_task_metric(task_name: str, task_target: str, status: str):
    registry = CollectorRegistry()
    task_counter = Counter(
        "celery_task_executions_total",
        "Total number of Celery task executions",
        ["task_name", "task_target", "status"],
        registry=registry
    )
    task_counter.labels(task_name=task_name, task_target=task_target, status=status).inc()

    push_to_gateway(
        "pushgateway:9091",
        job="oncall_celery_tasks",
        registry=registry,
        grouping_key={"instance": socket.gethostname()}
    )