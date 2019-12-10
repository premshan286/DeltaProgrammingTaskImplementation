var originChoices =[]; 
var destinationChoices = [];


fetch('http://localhost:8000/origin-api/')
  .then(response => response.json())
                .then(origins => {
		origins.forEach(function(origin) {
			originChoices.push(origin);
			console.log('Adding ' + origin);
		});
});  

fetch('http://localhost:8000/destination-api/')
  .then(response => response.json())
                .then (destinations => {
		destinations.forEach(function(destination) {
			destinationChoices.push(destination);
		});
}); 


  

  
     function filterOriginUsingIndex(value) { 
        document.getElementById('origin_list').innerHTML = ''; 
         //setting datalist empty at the start of function 
         //if we skip this step, same name will be repeated 
	var n= originChoices.length;
     	for (var i = 0; i<n; i++) { 
          if(((originChoices[i].toLowerCase()).indexOf(value.toLowerCase()))>-1) 
          { 
             //comparing if input string is existing in origins[i] string   
             var node = document.createElement("option"); 
             var val = document.createTextNode(originChoices[i]); 
             node.appendChild(val);   
             document.getElementById("origin_list").appendChild(node); 
           } 
         } 
     } 

     function filterOriginUsingRegex(value) { 
        document.getElementById('origin_list').innerHTML = ''; 
	var n= originChoices.length;
	var PATTERN = value.toLowerCase();
	var filtered = originChoices.filter(function (str) { return str.indexOf(PATTERN) === -1; });
     	for (var i = 0; i<filtered.length; i++) { 
	     var node = document.createElement("option"); 
             var val = document.createTextNode(originChoices[i]); 
              node.appendChild(val);   
               document.getElementById("origin_list").appendChild(node);             
         } 
     } 
   
    function filterDestinationUsingRegex(destValue) { 
        document.getElementById('destination_list').innerHTML = ''; 
	var n= destinationChoices.length;
	var PATTERN = destValue.toLowerCase();
	var filtered_destination = destinationChoices.filter(function (str) { return str.indexOf(PATTERN) === -1; });
        for (var i = 0; i<filtered_destination.length; i++) { 
	     var node = document.createElement("option"); 
             var val = document.createTextNode(filtered_destination[i]); 
             node.appendChild(val); 
             document.getElementById("destination_list").appendChild(node); 
         } 
     } 

     function filterDestinationUsingIndex(value) { 
        document.getElementById('origin_list').innerHTML = ''; 
	var n= destinationChoices.length;
        for (var i = 0; i<n; i++) { 
           if(((destinationChoices[i].toLowerCase()).indexOf(value.toLowerCase()))>-1) 
           { 
             //comparing if input string is existing in origins[i] string 
               var node = document.createElement("option"); 
               var val = document.createTextNode(destinationChoices[i]); 
               node.appendChild(val); 
               document.getElementById("destination_list").appendChild(node); 
           } 
         } 
     } 

