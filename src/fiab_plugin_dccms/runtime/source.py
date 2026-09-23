# (C) Copyright 2026- MET Norway.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

"""Placeholder data-source payloads.

`dummy_cosmo_source` does not fetch real data - it returns a small dummy
in-memory structure so that `CosmoSource` can be compiled and executed
end-to-end while a real COSMO integration is still pending.
"""

from typing import Any


def dummy_cosmo_source() -> dict[str, Any]:
    """Stand in for a COSMO data-source fetch.

    Returns a dummy in-memory record instead of a real COSMO field.
    """
    return {
        "source": "cosmo",
        "param": "2t",
        "step": 0,
        "values": [0.0],
    }
