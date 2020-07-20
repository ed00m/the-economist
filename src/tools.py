"""
the-economist - Project X_periment.

Python3.x
"""

import logging
import google.cloud.logging


class Tools():
    """
    Now, Tools is only a class definition.

    In the future, it could will be a package.
    """

    def __init__(self, app=None):
        """
        Declare Object.

        Initialize provider client.
        """
        if not app:
            app = __name__
        self.app = app
        # I'm still migrating a solution that I made, calm down and wait.
        self.log_provider = "GoogleNot"
        # [START setup_logging]
        if self.log_provider.lower() == "google".lower():
            self.logging_client = google.cloud.logging.Client()
            self.logger = self.logging_client.logger(self.app)
            # Attaches a Google Stackdriver logging handler to the root logger
        else:
            logging.basicConfig()
            self.logger = logging.getLogger(self.app)
        # [END setup_logging]

    def debujer(self, log={}, severity=None):
        """
        Configure log object.

        if Google Cloud provider or Python module.
        """
        self.log = log
        # self.log["instance"] = self.hash_id
        self.log_severity = severity

        if (
            "severity" in self.log and self.log["severity"]
            and self.log_severity is None
        ):
            self.log_severity = self.log["severity"]
        elif (
            "severity" not in self.log
            and self.log_severity is None
        ):
            self.log_severity = "DEBUG"
            self.log["severity"] = self.log_severity

        if self.log_provider.lower() == "google".lower():
            if isinstance(self.log, dict):
                return self.logger.log_struct(
                    self.log,
                    severity=self.log_severity
                )
            else:
                return self.logger.text(
                    self.log,
                    severity=self.log_severity
                )
        else:
            return self.logger.debug(self.log)
