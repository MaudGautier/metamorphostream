from old.src.record import Record


def test_deserialize_record():
    # GIVEN
    record = Record(key=b'key', value=b'value', offset=0)
    encoded_record = record.serialize()

    # WHEN
    deserialized_record = Record.deserialize(data=encoded_record)

    # THEN
    assert record == deserialized_record
