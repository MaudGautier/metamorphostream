import os

import pytest

from old.src.__fixtures__.constants import TEST_DIRECTORY


def cleanup_files():
    for filename in os.listdir(TEST_DIRECTORY):
        os.remove(f"{TEST_DIRECTORY}/{filename}")


@pytest.fixture(autouse=True)
def clean_files(request):
    yield

    # Cleanup code
    request.addfinalizer(cleanup_files)
