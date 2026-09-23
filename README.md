# Forecast-in-a-Box plugin for DCCMS

A [Forecast-in-a-Box](https://github.com/ecmwf/forecast-in-a-box) (FIAB) plugin
maintained by MET Norway / DCCMS. It follows the same plugin structure and
conventions as [`fiab-plugin-ecmwf`](https://github.com/ecmwf/forecast-in-a-box/tree/main/backend/packages/fiab-plugin-ecmwf).

## Blocks

- **Anemoi Model Run** (`anemoiSource`) and **GRIB Output** (`gribSink`) are
  reused directly from `fiab-plugin-ecmwf` (`fiab_plugin_ecmwf.anemoi.blocks.AnemoiSource`
  and `fiab_plugin_ecmwf.blocks.GribSink`), rather than being redefined here.
  This plugin depends on `fiab-plugin-ecmwf` and registers those classes under
  the same factory ids, so blueprints look and behave exactly as they would in
  `fiab-plugin-ecmwf`.
- **COSMO Source** (`cosmoSource`) - a dummy source block, specific to this
  plugin, that returns a stub qube standing in for a future COSMO data source
  integration. It performs no real data fetch.

## Workflow configuration

The plugin ships one placeholder [BlueprintTemplate](https://github.com/ecmwf/forecast-in-a-box):
a forecast workflow that runs an Anemoi model (`anemoiSource`) and writes its
output to GRIB (`gribSink`), using the same high-level configuration/glyph
pattern (`outputRoot`, `initialConditions`, templated GRIB output path, etc.)
as `fiab-plugin-ecmwf`'s `aifs_forecast` template. Since it reuses ECMWF's
actual Anemoi/GRIB blocks, this template will produce real output once its
`checkpoint` configuration value is replaced with a real, registered checkpoint
artifact id.
