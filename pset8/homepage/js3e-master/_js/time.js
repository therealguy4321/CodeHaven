$(document).ready(function() {
	function displayTime() {
		$('#time').text(getTime(true));
	}
	displayTime();
	setInterval(displayTime,1000);
}); // end ready