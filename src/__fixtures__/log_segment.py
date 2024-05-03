import pytest

from src.__fixtures__.constants import TEST_DIRECTORY
from src.log_segment import LogSegment
from src.records_file import RecordsFile


@pytest.fixture
def empty_log_segment():
    log_file = RecordsFile.create(path=f"{TEST_DIRECTORY}/empty_log_file.txt")
    return LogSegment(base_offset=0, log=log_file)
