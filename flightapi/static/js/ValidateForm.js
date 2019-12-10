function validateForm() {
	console.log('starting validation..');
        var originVal = document.forms["searchForm"]["origin"].value;
        var destinationVal = document.forms["searchForm"]["destination"].value;

        if ((originVal.length == "" ) && (destinationVal == "")) {
            alert("Please select origin and/or destination to continue");
	    return false;
	}
    }