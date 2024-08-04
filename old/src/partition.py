# Look at https://github.com/apache/kafka/blob/trunk/storage/src/main/java/org/apache/kafka/storage/internals/log/LogSegment.java

# lgoSegment: # TODO at some point: allow batch of messages






class Fetcher:
    pass
    # read()

# class Partition:
#     # Can write messages to it + can contain multiple segments =>
#     def __init__(self):
#         pass
#
#     def

# Log = partition. Multple LogSegments, serves as entry point
# LogSegment = associated to an OffsetIndex
# Fetcher = pull records from the log to serve to consumers
