# (C) Copyright 2026- MET Norway.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

"""Placeholder blueprint template: an Anemoi model run producing a GRIB output.

Mirrors the high-level shape of `fiab_plugin_ecmwf.templates.aifs_forecast`
(same block kinds, configuration option ids, and glyph pattern), reusing
`fiab_plugin_ecmwf`'s own `AnemoiSource`/`GribSink` block implementations
(registered under the `anemoiSource`/`gribSink` factory ids in
`fiab_plugin_dccms.__init__`) rather than redefining them.
"""

from fiab_core.fable import (
    BlockFactoryId,
    BlockInstance,
    BlockInstanceId,
    BlueprintTemplate,
    BlueprintTemplateBlock,
    BlueprintTemplateExampleInput,
    ConfigurationOptionId,
)
from fiab_core.types import ClosedEnumType

from fiab_plugin_dccms.templates.common import GRIB_OUTPUT_PATH, OUTPUT_ROOT, YESTERDAY_MIDNIGHT

template = BlueprintTemplate(
    display_name="Placeholder Anemoi Forecast",
    display_description=(
        "A placeholder forecast workflow: an Anemoi model run producing the full field set as GRIB, "
        "reusing fiab-plugin-ecmwf's Anemoi and GRIB blocks. Intended as a starting point for "
        "DCCMS workflows; replace the checkpoint with a real one for this to produce actual output."
    ),
    tags=["Anemoi", "GRIB", "Placeholder"],
    blocks={
        BlockInstanceId("source"): BlueprintTemplateBlock(
            factory_id=BlockFactoryId("anemoiSource"),
            instance=BlockInstance(
                configuration_values={
                    ConfigurationOptionId("checkpoint"): "BRIS-Malawi-2025.10",
                    ConfigurationOptionId("input_source"): "${initialConditions}",
                    ConfigurationOptionId("lead_time"): "72",
                    ConfigurationOptionId("base_time"): YESTERDAY_MIDNIGHT,
                    ConfigurationOptionId("number"): "1",
                },
                input_ids={},
            ),
        ),
        BlockInstanceId("gribSink"): BlueprintTemplateBlock(
            factory_id=BlockFactoryId("gribSink"),
            instance=BlockInstance(
                configuration_values={
                    ConfigurationOptionId("path"): GRIB_OUTPUT_PATH,
                },
                input_ids={
                    "dataset": BlockInstanceId("source"),
                },
            ),
        ),
    },
    environment=None,
    local_glyphs={},
    example_glyphs={
        "outputRoot": OUTPUT_ROOT,
        "initialConditions": BlueprintTemplateExampleInput(
            example_value="opendata",
            display_name="Initial Conditions",
            display_description="Source of the initial conditions",
            type_hint=ClosedEnumType(["mars", "opendata", "polytope"]),
        ),
    },
)
