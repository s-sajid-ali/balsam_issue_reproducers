from balsam.api import Job
from pathlib import Path
import site_def 

print("Python script making jobs")
sleep_time = 16
jobs = [
    Job(
        site_name=site_def.SITE_NAME,
        app_id="ProcessData",
        workdir=Path(f"sleep_test/{n}"),
        parameters={"sleep_time": sleep_time},
        num_nodes=1,
        threads_per_rank=1,
        threads_per_core=1,
        ranks_per_node=1,
        node_packing_count=32,
        gpus_per_rank=0,
    )  # no gpus on theta
    for n in range(64)
]

jobs = Job.objects.bulk_create(jobs)
