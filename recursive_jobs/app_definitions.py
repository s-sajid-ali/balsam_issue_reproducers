from balsam.api import ApplicationDefinition
import site_def

class ProcessData(ApplicationDefinition):
    site = site_def.SITE_NAME
    command_template = "/projects/HEP_on_HPC/sajid/icarus_hepnos/recursive_job_balsam/hello_sleeper.sh {{sleep_time}}"


ProcessData.sync()


class SpawnServer(ApplicationDefinition):
    site = site_def.SITE_NAME
    command_template = (
        "/projects/HEP_on_HPC/sajid/icarus_hepnos/recursive_job_balsam/spawn_server.sh"
    )

    def shell_preamble(self):
        return """export https_proxy=http://theta-proxy.tmi.alcf.anl.gov:3128
        __conda_setup="$('/lus/swift/home/sajid/packages/mambaforge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
        if [ $? -eq 0 ]; then
            eval "$__conda_setup"
        else
            if [ -f "/lus/swift/home/sajid/packages/mambaforge/etc/profile.d/conda.sh" ]; then
                . "/lus/swift/home/sajid/packages/mambaforge/etc/profile.d/conda.sh"
            else
            export PATH="/lus/swift/home/sajid/packages/mambaforge/bin:$PATH"
            fi
        fi
        unset __conda_setup
        if [ -f "/lus/swift/home/sajid/packages/mambaforge/etc/profile.d/mamba.sh" ]; then
            . "/lus/swift/home/sajid/packages/mambaforge/etc/profile.d/mamba.sh"
        fi
        mamba activate py3"""


SpawnServer.sync()
