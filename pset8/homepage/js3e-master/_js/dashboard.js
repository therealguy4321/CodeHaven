$(document).ready(function() {
  $('#dashboard').hover(
     function() {
		$(this).stop().animate(
		{
			left: '0',
			backgroundColor: 'red'
		},
		500,
		'easeInSine'
		); // end animate
	 }, 
	 function() {
		 $(this).stop().animate(
		{
			left: '-92px',
			backgroundColor: 'red'
		},
		1500,
		'easeOutBounce'
		); // end animate
	 }
  ); // end hover
}); // end ready