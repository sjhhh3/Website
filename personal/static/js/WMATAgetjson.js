 function getjson(routenumber) {
                markers = [];//create a global array

                var params = {
                    "api_key": "a05836e2c67a486d9dbcf0b206a266f4",
                    //Request parameters
                    "RouteID": routenumber, // function with parameters of route request
                };

                data = $.ajax({
                    url: "https://api.wmata.com/Bus.svc/json/jBusPositions?" + $.param(params),
                    type: "GET",
                    async: false
                })
                .done(function (data, textStatus, jqXHR) {  //when data received
                    if (data.BusPositions.length == 0) {
                        alert("Sorry there's no bus for this route or WMATA data is not available currently.");
                        location.replace("map.html"); //error handle
                    }
                    markers = data.BusPositions; // when data received, give it to the "marker" array
                })
                .fail(function () {
                    alert("WMATA Data Disconnected");
                });
            }

            getjson(routenumber); // call the function for the first time visit
