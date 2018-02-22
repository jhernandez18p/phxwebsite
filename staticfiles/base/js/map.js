var map, styleArray,locations;
var marker, i;

styleArray = [
    {"elementType": "geometry","stylers": [{"color": "#F2F2F2"}]},{"elementType": "labels.icon","stylers": [{"visibility": "off"}]},{"elementType": "labels.text.fill","stylers": [{"color": "#616161"}]},{"elementType": "labels.text.stroke","stylers": [{"color": "#f5f5f5"}]},{"featureType": "administrative.land_parcel","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "administrative.land_parcel","elementType": "labels.text.fill","stylers": [{"color": "#bdbdbd"}]},{"featureType": "administrative.locality","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "administrative.neighborhood","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "administrative.province","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "landscape","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "landscape.man_made","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "landscape.natural","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "landscape.natural.landcover","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "landscape.natural.terrain","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi","elementType": "geometry","stylers": [{"color": "#eeeeee"}]},{"featureType": "poi","elementType": "labels.text.fill","stylers": [{"color": "#757575"}]},{"featureType": "poi.attraction","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi.business","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi.medical","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi.park","elementType": "geometry","stylers": [{"color": "#e5e5e5"}]},{"featureType": "poi.park","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi.park","elementType": "labels.text.fill","stylers": [{"color": "#9e9e9e"}]},{"featureType": "poi.place_of_worship","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi.school","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "poi.sports_complex","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "road","elementType": "geometry","stylers": [{"color": "#ffffff"}]},{"featureType": "road","elementType": "geometry.fill","stylers": [{"color": "#009688"}]},{"featureType": "road","elementType": "geometry.stroke","stylers": [{"color": "#009688"}]},{"featureType": "road.arterial","elementType": "labels.text.fill","stylers": [{"color": "#757575"}]},{"featureType": "road.highway","elementType": "geometry","stylers": [{"color": "#dadada"}]},{"featureType": "road.highway","elementType": "geometry.fill","stylers": [{"color": "#009688"}]},{"featureType": "road.highway","elementType": "labels.text.fill","stylers": [{"color": "#616161"}]},{"featureType": "road.local","elementType": "labels.text.fill","stylers": [{"color": "#9e9e9e"}]},{"featureType": "transit.line","elementType": "geometry","stylers": [{"color": "#e5e5e5"}]},{"featureType": "transit.station","elementType": "geometry","stylers": [{"color": "#eeeeee"}]},{"featureType": "water","elementType": "geometry","stylers": [{"color": "#c9c9c9"}]},{"featureType": "water","elementType": "geometry.fill","stylers": [{"color": "#009688"}]},{"featureType": "water","elementType": "labels.text","stylers": [{"visibility": "off"}]},{"featureType": "water","elementType": "labels.text.fill","stylers": [{"color": "#9e9e9e"}]}
]

var markers = [
    [
        'Phoenix World Trade Inc., Panamá',
        8.981022, -79.509901,
    ],
    [
        'Phoenix World Trade Inc., USA',
        25.747603, -80.340254,
    ],
    [
        'Phoenix World Trade Inc., Curacao',
        12.1356696,-68.9569759,
    ],
    [
        'Phoenix World Trade Inc., Puerto Rico',
        18.4219004,-66.1092751,
    ],
    [
        'Phoenix World Trade Inc., República Dominicana',
        18.4828372,-69.9459407,
    ],
    [
        'Phoenix World Trade Inc., Chile',
        -28.275386, -70.925212,
    ],
    [
        'Phoenix World Trade Inc., Venezuela',
        10.494779,-66.8413177,
    ],
    [
        'Phoenix World Trade Inc., Ecuador',
        -2.186826, -79.916759,
    ],
    [
        'Phoenix World Trade Inc., Colombia',
        4.696900, -74.006311,
    ],
];

var infoWindowContent = [
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc, Panamá</h3>`+
            `<p>P.H. Oceanía Business Plaza Torre 2000</p>`+
            `<p>Punta Pacifica, Ciudad de Panamá.</p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc, USA</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc, Curcao</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc, Puerto Rico</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc, República Dominicana</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc., Chile</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc., Venezuela</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc., Ecuador</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
    [
        `<div class="info_content uk-card">`+
            `<h3>Phoenix World Trade Inc., Colombia</h3>`+
            `<p></p>`+
            `<p></p>`+
        `</div>`
    ],
];  

function initMap() {
    var bounds = new google.maps.LatLngBounds();
    var infoWindow = new google.maps.InfoWindow(), marker, i;
    map = new google.maps.Map(document.getElementById('map'), {
        mapTypeId: 'satellite',
        center: {lat: 14.987239, lng: -84.528809}, 
        //center: {lat: -6.9645954, lng: -76.3220646},
        //center: {lat: 8.6571004, lng: -60.1603678}, 
        //zoomControl: true,
        //scaleControl: true,
        //draggable: false,
        zoom: 8,
        disableDefaultUI: true,
        scrollwheel: false,
        //styles: styleArray,
    });

    var image = {
        url: "/static/base/images/phx-pin0.png",
        // This marker is 20 pixels wide by 32 pixels high.
        size: new google.maps.Size(20, 20),
        // The origin for this image is (0, 0).
        origin: new google.maps.Point(0, 0),
        // The anchor for this image is the base of the flagpole at (0, 32).
        anchor: new google.maps.Point(5, 20)
    };

    for( i = 0; i < markers.length; i++ ) {
        var position = new google.maps.LatLng(markers[i][1], markers[i][2]);
        bounds.extend(position);
        marker = new google.maps.Marker({
            position: position,
            map: map,
            icon: image,
            title: markers[i][0]
        });
        
        // Allow each marker to have an info window    
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infoWindow.setContent(infoWindowContent[i][0]);
                infoWindow.open(map, marker);
            }
        })(marker, i));

        // Automatically center the map fitting all markers on the screen
        map.fitBounds(bounds);
    }
}