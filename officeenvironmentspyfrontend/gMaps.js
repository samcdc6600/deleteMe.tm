
var map;
function initMap()
{
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
	center: {lat: -34.397, lng: 150.644},
	mapTypeId: 'satellite'
    });
    map.setTilt(70);

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
    setMarker(local1);
}

//var latLng = new google.maps.LatLng(lat: -34.397, lng: 150.644);

// var marker = new google.maps.Marker({
//     //    position: latLng,
//     position: {lat: -34.397, lng: 150.644},
//     title: "Office 1"
// });

// marker.setMap(map);
