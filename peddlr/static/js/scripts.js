// Get the current location
$(document).ready(function() {
    navigator.geolocation.getCurrentPosition(setPosition);
});

function setPosition(position) {
    // Set our lat and lon fields with jquery
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    $('#id_latitude').val(latitude);
    $('#id_longitude').val(longitude);
    $('#id_location_0').val(latitude);
    $('#id_location_1').val(longitude);
}



