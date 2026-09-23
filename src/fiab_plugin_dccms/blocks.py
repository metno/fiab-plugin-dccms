# (C) Copyright 2026- MET Norway.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

"""Blocks for fiab_plugin_dccms.

The Anemoi model run and GRIB output blocks are reused as-is from
`fiab_plugin_ecmwf` (see `fiab_plugin_dccms.__init__`); this module only adds
blocks that are specific to this plugin.

`CosmoSource` is a dummy source block, standing in for a future COSMO data
source integration: it returns a stub qube and performs no real data fetch.
"""

import numpy as np
from cascade.low.func import Either
from earthkit.workflows.fluent import Action, Payload, from_source
from qubed import Qube

from fiab_core.fable import (
    ActionLookup,
    BlockConfigurationOption,
    BlockInstanceOutput,
    ConfigurationOptionId,
    ConfigurationOptionRestriction,
    QubedOutput,
)
from fiab_core.plugin import Error
from fiab_core.tools.blocks import BlockInstanceRich, Source


class CosmoSource(Source):
    title: str = "COSMO Source"
    description: str = (
        "Dummy placeholder source for COSMO model data. Returns a stub qube and does not fetch any real data."
    )
    inputs: list[str] = []
    configuration_options: dict[ConfigurationOptionId, BlockConfigurationOption] = {}

    def validate(
        self, block: BlockInstanceRich, inputs: dict[str, QubedOutput], restrictions: ConfigurationOptionRestriction
    ) -> BlockInstanceOutput:
        return QubedOutput(
            dataqube=Qube.from_datacube({"param": ["2t"], "step": ["0"]}),
            datatype="cosmo-dummy",
        )

    def compile(
        self,
        inputs: ActionLookup,
        block: BlockInstanceRich,
    ) -> Either[Action, Error]:  # ty:ignore[invalid-type-arguments] # semigroup
        action = from_source(
            np.array([Payload("fiab_plugin_dccms.runtime.source.dummy_cosmo_source", [])]),
            dims=["param"],
            coords={"param": ["2t"]},
        )
        return Either.ok(action)

    def intersect(self, other: QubedOutput) -> bool:
        return False
