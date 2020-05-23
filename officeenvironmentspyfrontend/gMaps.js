
var map;
function initMap()
{
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
	center: {lat: -34.290, lng: 150.501},
	mapTypeId: 'satellite'
    });
//    map.setTilt(45);

    setMarkers();
}


// Add marker markerLocation to map
function setMarker(markerLocation) {
    marker = new google.maps.Marker({
	    position: markerLocation,
	    map: map
	});
}


// Add markers to map
function setMarkers() {
    local1 = new google.maps.LatLng(-34.391, 150.501);
    local2 = new google.maps.LatLng(-34.289, 150.5005);
    setMarker(local1);
    setMarker(local2);
}
