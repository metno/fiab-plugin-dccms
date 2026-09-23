# (C) Copyright 2026- MET Norway.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

import dataclasses

from fiab_core.fable import BlockFactoryId
from fiab_core.plugin import Plugin
from fiab_core.tools.blocks import QubedBlockBuilder
from fiab_core.tools.plugins import QubedPluginBuilder
from fiab_plugin_ecmwf.anemoi.blocks import AnemoiSource
from fiab_plugin_ecmwf.blocks import GribSink

from fiab_plugin_dccms.blocks import CosmoSource
from fiab_plugin_dccms.templates.anemoi_forecast import template as _anemoi_forecast_template

blocks: dict[BlockFactoryId, QubedBlockBuilder] = {
    BlockFactoryId("anemoiSource"): AnemoiSource(),
    BlockFactoryId("gribSink"): GribSink(),
    BlockFactoryId("cosmoSource"): CosmoSource(),
}

_base_plugin = QubedPluginBuilder(block_builders=blocks, base_environment=["fiab-plugin-dccms"]).as_plugin()


def plugin() -> Plugin:
    # Declaration order is presentation order.
    return dataclasses.replace(
        _base_plugin(),
        blueprint_templates=(_anemoi_forecast_template,),
    )
