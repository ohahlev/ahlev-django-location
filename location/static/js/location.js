var map;
var marker;
var form;
var latitude_element;
var longitude_element;

function create_marker(latitude, longitude) {
    if(!map) return;
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

function on_location_change() {
    if(!map) return;

    if(marker) {
        marker.setMap(null);
        marker = null;
    }
    
    if(!latitude_element || !longitude_element) {
        create_marker(11.562108, 104.888535);
        return;
    } 

    var latitude = parseFloat(latitude_element.val());
    if(!latitude) return;

    var longitude = parseFloat(longitude_element.val());
    if(!longitude) return;

    create_marker(latitude, longitude);
}

function init_map() {
    map = new google.maps.Map(document.getElementById('ahlev-map'), {
        zoom: 13,
    });
    on_location_change();
}

function toggleBounce() {
    if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
    } else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
    }
}

$(document).ready(function () {
    form = $("form#location_form");
    latitude_element = form.find("input#id_latitude");
    longitude_element = form.find("input#id_longitude");

    if(!form || !latitude_element || !longitude_element) return;

    on_location_change();

    latitude_element.change(on_location_change);
    longitude_element.change(on_location_change);
});