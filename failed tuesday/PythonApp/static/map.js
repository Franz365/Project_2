function createMap(breweries) {

  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "light-v10",
    accessToken: API_KEY
  });

  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = {
    "Light Map": lightmap
  };

  // Create an overlayMaps object to hold the breweries layer
  var overlayMaps = {
    "Breweries": breweries
  };

  // Create the map object with options
  var myMap = L.map("map-id", {
    center: [37.0902, -95.7129],
    zoom: 4,
    layers: [lightmap, breweries]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}

function createMarkers(response) {
  // Create a new marker cluster group
  var markers = L.markerClusterGroup();

  // Loop through data
  for (var i = 0; i < response.length; i++) {

    // Set the brewery property to a variable
    var brewery = response[i];

    // Check for brewery
    if (brewery) {

      // Add a new marker to the cluster group and bind a pop-up
      markers.addLayer(L.marker([brewery.Coordinates[0], brewery.Coordinates[1]])
        .bindPopup("<h3>" + brewery.Name + "<h3><h3>Address: " + brewery.Address + "</h3>"));
    }

  }

  // Add our marker cluster layer to the map
  myMap.addLayer(markers);

}



// // // Perform an API call to the /api route to get brewery information. Call createMarkers when complete
d3.json("/api", function (data) {
  // Log the data
  console.log(data);
  // Run the createMarkers function
  createMarkers(data);
});