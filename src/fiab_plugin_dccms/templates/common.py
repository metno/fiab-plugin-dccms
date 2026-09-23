# (C) Copyright 2026- MET Norway.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

"""Values shared by this plugin's blueprint templates.

Mirrors the pattern used by `fiab_plugin_ecmwf.templates.common`.
"""

from fiab_core.fable import BlueprintTemplateExampleInput
from fiab_core.types import StringType

# `[shortName]` is the sink's own metadata templating, not a glyph.
GRIB_OUTPUT_PATH = "${outputRoot}/${runId}__${attemptCount}/[shortName].grib"

# Yesterday's 00Z: today's run is not published until mid-morning.
YESTERDAY_MIDNIGHT = "${submitDatetime |sub_days(1) |floor_day}"

OUTPUT_ROOT = BlueprintTemplateExampleInput(
    example_value="/tmp/outputRoot",
    display_name="Output Root Location",
    display_description="Each attempt writes to its own folder below this path",
    type_hint=StringType(),
)
