
var map;
function initMap()
{
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
	center: {lat: -34.397, lng: 150.644},
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
    local1 = new google.maps.LatLng(-34.397, 150.644);
    local2 = new google.maps.LatLng(-34.290, 150.500);
    setMarker(local1);
    setMarker(local2);
}
