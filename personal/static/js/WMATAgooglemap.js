function initMap() {
    //initiate the google map, with the center of middle array bus
                    map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 14,                   
                    center: { lat: markers[parseInt(markers.length / 2)].Lat, lng: markers[parseInt(markers.length / 2)].Lon }
                });

                addmarker(markers);//call the addmarker function to addmarkers to the map

                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function (position) {//get the lat and lon of the current position
                        var pos = {
                            lat: position.coords.latitude,
                            lng: position.coords.longitude
                        };
                        var marker = new google.maps.Marker({
                            position: pos,
                            map: map,
                            title: "your location",
                        });
                        map.setCenter(pos);
                    }, function () {
                        handleLocationError();
                    });
                } else {
                    // Browser doesn't support Geolocation, error handle
                    alert("Please allow your location");
                }
            }
            function handleLocationError() {
                alert("Please allow your location");
            }
            

            function addmarker(markers) {
                googlemarkers = [];

                var infowindow = new google.maps.InfoWindow({ // initiate the information window
                    content: ' '
                });

                function iconset(markers) { // judge the directiion of the bus
                    if (markers.DirectionText == "NORTH" || markers.DirectionText == "EAST") {
                        return '../../../static/images/bus1.png';
                    }
                    else {
                        return '../../../static/images/bus2.png';
                    }
                }

                for (var i = 0; i < markers.length; i++) { // get all position data and add to an array, create markers
                    var marker = new google.maps.Marker({
                        position: { lat: markers[i].Lat, lng: markers[i].Lon },
                        map: map,
                        icon: iconset(markers[i]),
                        destination: markers[i].TripHeadsign,
                        direction: markers[i].DirectionText,
                        ID: markers[i].VehicleID,
                        routenumber: markers[i].RouteID
                    });
                    googlemarkers.push(marker);
                    message(marker, marker.destination, marker.direction, infowindow, marker.ID, marker.routenumber);
                }

                function message(marker, destination, direction, infowindow, vehicleid, routenumber) { //listen to click and show the bus infomation
                    marker.addListener('click', function () {
                        infowindow.open(marker.get('map'), marker);
                        infowindow.setContent('Route ' + routenumber + ' , ' + 'To ' + destination + ',' + ' ' + direction);
                        document.getElementById("route").innerHTML = routenumber;
                        document.getElementById("destination").innerHTML = destination;
                        document.getElementById("vehicle").innerHTML = vehicleid;
                        document.getElementById("direction").innerHTML = direction;
                    });
                }

                setMapOnAll(map);
                setTimeout("refresh(routenumber)", 15000); // refresh every 15s, redo the function

            }

            function setMapOnAll(map) {
                for (var i = 0; i < googlemarkers.length; i++) {
                    googlemarkers[i].setMap(map);
                }
            }

            // Removes the markers from the map first, and refresh the array.
            function refresh(routenumber) {
                setMapOnAll(null);
                getjson(routenumber);
                addmarker(markers);
            }

            // Listen to the search and reload the map markers
            $(document).ready(function () {
                $("#search").click(function () {
                    data = $("#searchform").serialize();
//                    console.log(data);
                    arr = data.split("=");
                    var newsearch = arr[1];
//                    console.log(newsearch == "");
                    setMapOnAll(null);
                    routenumber = newsearch;
                    getjson(routenumber);
                    addmarker(markers);
                });
            });
