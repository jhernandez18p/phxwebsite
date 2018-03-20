var map, styleArray,locations;
var marker, i;

styleArray = [
    {"elementType": "geometry","stylers": [{"color": "#F2F2F2"}]},
    {"elementType": "labels.icon","stylers": [{"visibility": "off"}]},
    {"elementType": "labels.text.fill","stylers": [{"color": "#616161"}]},
    {"elementType": "labels.text.stroke","stylers": [{"color": "#f5f5f5"}]},
    {"featureType": "administrative.land_parcel","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "administrative.land_parcel","elementType": "labels.text.fill","stylers": [{"color": "#bdbdbd"}]},
    {"featureType": "administrative.locality","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "administrative.neighborhood","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "administrative.province","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "landscape","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "landscape.man_made","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "landscape.natural","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "landscape.natural.landcover","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "landscape.natural.terrain","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "poi","elementType": "geometry","stylers": [{"color": "#eeeeee"}]},
    {"featureType": "poi","elementType": "labels.text.fill","stylers": [{"color": "#757575"}]},
    {"featureType": "poi.attraction","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "poi.business","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "poi.medical","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "poi.park","elementType": "geometry","stylers": [{"color": "#e5e5e5"}]},
    {"featureType": "poi.park","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "poi.park","elementType": "labels.text.fill","stylers": [{"color": "#9e9e9e"}]},
    {"featureType": "poi.place_of_worship","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "poi.school","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "poi.sports_complex","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "road","elementType": "geometry","stylers": [{"color": "#ffffff"}]},
    {"featureType": "road","elementType": "geometry.fill","stylers": [{"color": "#009688"}]},
    {"featureType": "road","elementType": "geometry.stroke","stylers": [{"color": "#009688"}]},
    {"featureType": "road.arterial","elementType": "labels.text.fill","stylers": [{"color": "#757575"}]},
    {"featureType": "road.highway","elementType": "geometry","stylers": [{"color": "#dadada"}]},
    {"featureType": "road.highway","elementType": "geometry.fill","stylers": [{"color": "#009688"}]},
    {"featureType": "road.highway","elementType": "labels.text.fill","stylers": [{"color": "#616161"}]},
    {"featureType": "road.local","elementType": "labels.text.fill","stylers": [{"color": "#9e9e9e"}]},
    {"featureType": "transit.line","elementType": "geometry","stylers": [{"color": "#e5e5e5"}]},
    {"featureType": "transit.station","elementType": "geometry","stylers": [{"color": "#eeeeee"}]},
    {"featureType": "water","elementType": "geometry","stylers": [{"color": "#c9c9c9"}]},
    {"featureType": "water","elementType": "geometry.fill","stylers": [{"color": "#596d6a"}]},
    {"featureType": "water","elementType": "labels.text","stylers": [{"visibility": "off"}]},
    {"featureType": "water","elementType": "labels.text.fill","stylers": [{"color": "#9e9e9e"}]}
]

var markers = [
    [
        'Phoenix World Trade Inc., Venezuela',
        10.494779,
        -66.8413177,
        'Venezuela'
    ],
    [
        'Phoenix World Trade Inc., Ecuador',
        -2.186826,
        -79.916759,
        'Ecuador'
    ],
    [
        'Phoenix World Trade Inc., Colombia',
        4.696900,
        -74.006311,
        'Colombia'
    ],
    [
        'Phoenix World Trade Inc., Surinam',
        4.696900,
        -74.006311,
        'Suriname'
    ],
    [
        'Phoenix World Trade Inc., Canada',
        4.696900,
        -74.006311,
        'Canada'
    ],
    [
        'Phoenix World Trade Inc., China',
        4.696900,
        -74.006311,
        'China'
    ],
    [
        'Phoenix World Trade Inc., Brasil',
        4.696900,
        -74.006311,
        'Brasil'
    ],
    [
        'Phoenix World Trade Inc., Peru',
        4.696900,
        -74.006311,
        'Peru'
    ],
    [
        'Phoenix World Trade Inc., Curacao',
        12.1356696,
        -68.9569759,
        'Curacao',
    ],
    [
        'Phoenix World Trade Inc., Panamá',
        8.981022,
        -79.509901,
        'Panamá'
    ],
    [
        'Phoenix World Trade Inc., USA',
        25.747603,
        -80.340254,
        'USA'
    ],
    [
        'Phoenix World Trade Inc., Puerto Rico',
        18.4219004,
        -66.1092751,
        'Puerto Rico'
    ],
    [
        'Phoenix World Trade Inc., República Dominicana',
        18.4828372,
        -69.9459407,
        'Republica Dominicana'
    ],
    [
        'Phoenix World Trade Inc., Chile',
        -28.275386,
        -70.925212,
        'Chile'
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
        center: {lat: 14.987239, lng: -84.528809}, 
        zoom: 8,
        disableDefaultUI: true,
        scrollwheel: false,
        styles: styleArray,
    });

    var image = {
        url: "/static/base/images/phx-pin0.png",
        size: new google.maps.Size(20, 20),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 0)
    };

    var geocoder = new google.maps.Geocoder();


    for( i = 0; i < markers.length; i++ ) {
        // console.log(i);
        var _title = markers[i][0];var latitude = markers[i][1];
        var logitude = markers[i][2];var country = markers[i][3];
        
        geocoder.geocode( 
            { 'address': country },
            function(results, status) {
                // console.log(status);
                // console.log(results);
                console.log(results[0].geometry.location);
                if (status == google.maps.GeocoderStatus.OK) {
                    
                    marker = new google.maps.Marker({
                        position: results[0].geometry.location,
                        map: map,
                        icon: image,
                        title: results[0].address_components[0].long_name
                    });
                    // console.log(country,latitude,logitude);
                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                        // console.log(marker.title,i);
                        return function() {
                            
                        }
                    })(marker, i));
                    bounds.extend(results[0].geometry.location);
                }else if (status == google.maps.GeocoderStatus.OVER_QUERY_LIMIT) { 
                    marker = new google.maps.Marker({
                        position: {lat:latitude,lng:logitude},
                        map: map,
                        icon: image,
                        title: country
                    });
                    // console.log(country,latitude,logitude);
                }else {
                    // console.log("Geocode was not successful for the following reason: " + status);
                }
                map.fitBounds(bounds);
            }
        );
    }
}