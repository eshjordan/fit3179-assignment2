let vega_lite_definition_1 = "js/nyc_rideshare.vg.json"
let vega_lite_definition_2 = "js/nyc_rideshare-2.vg.json"

// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
vegaEmbed('#visualisation-1', vega_lite_definition_1).then(result => {}).catch(console.error);

vegaEmbed('#visualisation-2', vega_lite_definition_2).then(result => {}).catch(console.error);

// https://github.com/fivethirtyeight/uber-tlc-foil-response
// https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Neighborhood-Tabulatio/swpk-hqdp
// https://data.cityofnewyork.us/City-Government/NTA-map/d3qk-pfyz
