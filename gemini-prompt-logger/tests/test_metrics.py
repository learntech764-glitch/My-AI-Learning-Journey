
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
from app.metrics import (
    average_latency
)


def test_metrics():

    result = average_latency()

    assert result >= 0