# (C) Copyright 2026- MET Norway.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

"""Runtime payloads used by fiab_plugin_dccms's own blocks.

The Anemoi model run and GRIB output blocks are reused from
`fiab_plugin_ecmwf` and use that package's own runtime payloads; this module
only covers this plugin's own blocks (currently just `CosmoSource`), whose
payload is an intentionally trivial stand-in that does not fetch or process
any real data.
"""
