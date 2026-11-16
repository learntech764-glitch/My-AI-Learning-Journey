
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from datetime import datetime
from app.models import PromptLog
from app.logger import save_log

def test_promptlog():

    log = PromptLog(
        timestamp=datetime.now(),
        prompt="AI",
        response="Artificial Intelligence",
        latency=1.5
    )
    save_log(log)
    assert log.prompt == "AI"
    assert log.latency == 1.5