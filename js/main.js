let vega_lite_definition_1 = "js/nyc_rideshare.vg.json"
let vega_lite_definition_2 = "js/nyc_rideshare-2.vg.json"

// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
vegaEmbed('#visualisation-1', vega_lite_definition_1).then(result => { }).catch(console.error);

vegaEmbed('#visualisation-2', vega_lite_definition_2).then(result => {

    let internal_element = document.getElementsByName("selected_borough")[0];
    let external_element = document.getElementById("time_of_day_external_div");

    internal_element.parentElement.insertAdjacentElement('afterend', external_element);

    let pickup_time = document.getElementById("time_of_day_external_input");

    pickup_time.addEventListener('input', (e) => {
        let pickup_time_text = document.getElementById("time_of_day_external_text");
        let meridian = pickup_time.value < 12 ? " AM" : " PM";
        let _12Hour = pickup_time.value % 12;
        _12Hour = _12Hour == 0 ? 12 : _12Hour;

        pickup_time_text.innerHTML = _12Hour + meridian;
    });

    setInterval(() => {
        let currentValue = parseInt(pickup_time.value);
        pickup_time.value = (currentValue + 1) % 24;
        pickup_time.dispatchEvent(new Event('input'));
    }, 1000)

}).catch(console.error);


// https://github.com/fivethirtyeight/uber-tlc-foil-response
// https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Neighborhood-Tabulatio/swpk-hqdp
// https://data.cityofnewyork.us/City-Government/NTA-map/d3qk-pfyz
