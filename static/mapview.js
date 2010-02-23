var map;
var geoXml; 
var toggleState = 1;

function initialize() {
	if (GBrowserIsCompatible()) {
		geoXml = new GGeoXml("http://app.photomapapp.com:8000/maps.kml");
		map = new GMap2(document.getElementById("map_canvas")); 
		map.setCenter(new GLatLng(45.7,-123.3), 8); 

		map.addControl(new GLargeMapControl());
		map.addOverlay(geoXml);
	}
}
function toggleMyKml() {
	if (toggleState == 1) {
		map.removeOverlay(geoXml);
		toggleState = 0;
	} else {
		map.addOverlay(geoXml);
		toggleState = 1;
	}
}

$(document).ready(function() {

	initialize()

});
