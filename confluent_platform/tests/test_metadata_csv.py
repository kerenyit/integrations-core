# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from .common import HERE


def get_metadata_csv():
    with open(os.path.join(HERE, '..', 'metadata.csv'), 'r') as f:
        metadata_csv = f.read()
    return metadata_csv


def test_metadata_csv():
    pass
    # actual_metadata_csv = get_metadata_csv()
    # expected_metadata_csv = build_metadata_csv(actual_metadata_csv)
    #
    # # printed for convenience so you can copy/paste the content to metadata.csv
    # print("=== ACTUAL metadata.csv")
    # print(actual_metadata_csv)
    # print("=== EXPECTED metadata.csv")
    # print(expected_metadata_csv)
    # print("=== END")

    # assert expected_metadata_csv == actual_metadata_csv
