from old.src.record import Record


def test_can_append_to_empty_log_segment(empty_log_segment):
    # GIVEN
    log_segment = empty_log_segment
    record = Record(offset=0, key=b'key', value=b'value')

    # WHEN
    log_segment.append(record=record)

    # THEN
    assert log_segment.log.file.tell() == record.size

