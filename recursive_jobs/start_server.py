from balsam.api import Job, Site, BatchJob
from pathlib import Path
import site_def

spawn_job = Job(
    site_name=site_def.SITE_NAME,
    app_id="SpawnServer",
    workdir=Path("server"),
    num_nodes=1,
    threads_per_rank=1,
    threads_per_core=1,
    ranks_per_node=32,
    node_packing_count=1,
    gpus_per_rank=0,
)

spawn_job = spawn_job.save()


# Get the id for your site
site = Site.objects.get(site_def.SITE_NAME)

# Create a BatchJob to run server job
BatchJob.objects.create(
    num_nodes=2,
    wall_time_min=10,
    queue="debug-cache-quad",
    project="datascience",
    site_id=site.id,
    job_mode="mpi",
)
