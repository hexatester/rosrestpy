from ros._base import BaseProps

from .environment import Environment
from .job import Job
from .script import Script


class ScriptModule(BaseProps[Script]):
    _environment: BaseProps[Environment] = None
    _job: BaseProps[Job] = None

    @property
    def job(self):
        if not self._job:
            self._job = BaseProps(self.ros, "/system/script/job", Job)
            self._job._create = False
            self._job._write = False
        return self._job

    @property
    def environment(self):
        if not self._environment:
            self._environment = BaseProps(
                self.ros, "/system/script/environment", Environment
            )
        return self._environment

    def run(self, script: Script):
        return self.ros.post_as("/system/script/run", None, {".id": script.id})


__all__ = ["Environment", "Job", "Script", "ScriptModule"]
