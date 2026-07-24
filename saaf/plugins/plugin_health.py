from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PluginHealth:

    """
    Runtime health information
    for a plugin.
    """

    healthy: bool = True

    enabled: bool = True

    success_count: int = 0

    failure_count: int = 0

    last_error: str | None = None

    last_execution: datetime | None = None

    average_response_time: float = 0.0

    total_response_time: float = 0.0

    execution_count: int = 0


    def record_success(
        self,
        execution_time: float
    ):

        self.success_count += 1

        self.execution_count += 1

        self.last_execution = datetime.now()

        self.total_response_time += execution_time

        self.average_response_time = (

            self.total_response_time

            / self.execution_count

        )

        self.last_error = None

        self.healthy = True


    def record_failure(
        self,
        error: str
    ):

        self.failure_count += 1

        self.last_execution = datetime.now()

        self.last_error = error

        # Temporary rule
        if self.failure_count >= 3:

            self.healthy = False


    def reset(self):

        self.healthy = True

        self.failure_count = 0

        self.last_error = None