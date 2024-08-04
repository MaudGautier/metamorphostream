import pytest

from old.src.__fixtures__.constants import TEST_DIRECTORY
from old.src.log_segment import LogSegment
from old.src.records_file import RecordsFile


@pytest.fixture
def empty_log_segment():
    log_file = RecordsFile.create(path=f"{TEST_DIRECTORY}/empty_log_file.txt")
    return LogSegment(base_offset=0, log=log_file)
