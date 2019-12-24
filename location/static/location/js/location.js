var map;
var marker;
var div;
var latitude_element;
var longitude_element;

function create_marker(latitude, longitude) {
    if (!map) return;
    marker = new google.maps.Marker({
        map: map,
        animation: google.maps.Animation.DROP,
        position: { lat: latitude, lng: longitude }
    });
    marker.addListener('click', toggleBounce);
    map.setCenter({
        lat: latitude, lng: longitude
    });
    map.setZoom(6.0);
}

function show_map() {
    if (!map) return;

    if (marker) {
        marker.setMap(null);
        marker = null;
    }

    if (!latitude_element || !longitude_element) {
        create_marker(11.562108, 104.888535);
        return;
    }

    var latitude = parseFloat(latitude_element.value);
    if (!latitude) return;

    var longitude = parseFloat(longitude_element.value);
    if (!longitude) return;

    create_marker(latitude, longitude);
}

function init_map() {
    setTimeout(function () {
        var element = document.getElementById('location-map');
        if(!element) return;
        map = new google.maps.Map(element, {
            zoom: 13,
        });
        show_map();
    }, 2000);
}

function toggleBounce() {
    if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
    } else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
    }
}

$(document).ready(function () {
    div = $("div#location-map");
    if(!div) return;

    if(!div[0]) return;
    latitude_element = div[0].attributes.latitude;
    longitude_element = div[0].attributes.longitude;
});