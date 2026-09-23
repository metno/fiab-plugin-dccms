# (C) Copyright 2026- MET Norway.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

from fiab_core.fable import BlockFactoryId
from fiab_plugin_ecmwf.anemoi.blocks import AnemoiSource
from fiab_plugin_ecmwf.blocks import GribSink

from fiab_plugin_dccms import blocks, plugin


def test_plugin_catalogue_contains_expected_blocks() -> None:
    built = plugin()
    factories = built.catalogue.factories
    assert BlockFactoryId("anemoiSource") in factories
    assert BlockFactoryId("gribSink") in factories
    assert BlockFactoryId("cosmoSource") in factories


def test_anemoi_and_grib_blocks_are_reused_from_fiab_plugin_ecmwf() -> None:
    assert isinstance(blocks[BlockFactoryId("anemoiSource")], AnemoiSource)
    assert isinstance(blocks[BlockFactoryId("gribSink")], GribSink)


def test_plugin_ships_the_placeholder_template() -> None:
    built = plugin()
    assert len(built.blueprint_templates) == 1
    template = built.blueprint_templates[0]
    assert template.display_name == "Placeholder Anemoi Forecast"
    factory_ids = {block.factory_id for block in template.blocks.values()}
    assert factory_ids == {BlockFactoryId("anemoiSource"), BlockFactoryId("gribSink")}


def test_cosmo_source_validates_to_a_dummy_qube() -> None:
    from fiab_core.fable import BlockInstance
    from fiab_core.tools.blocks import BlockInstanceRich

    built = plugin()
    factory = built.catalogue.factories[BlockFactoryId("cosmoSource")]
    rich_block = BlockInstanceRich.from_block(
        BlockFactoryId("cosmoSource"),
        BlockInstance(configuration_values={}),
        factory.configuration_options,
    )
    from fiab_plugin_dccms.blocks import CosmoSource

    output = CosmoSource().validate(rich_block, {}, {})
    assert output.datatype == "cosmo-dummy"
    assert "param" in output.dataqube.axes()
