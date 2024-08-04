from old.src.record import Record
from old.src.records_file import RecordsFile


class LogSegment:
    def __init__(self, log: RecordsFile, base_offset: int, ):
        self.log = log  # The log file containing log entries
        self.base_offset = base_offset  # The base offset of the log segment

    def append(self, record: Record):
        """Appends a record at the end of the log file.
        """
        self.log.write(data=record.serialize())
