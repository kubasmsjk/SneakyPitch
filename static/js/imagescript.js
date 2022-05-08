  jQuery(document).ready(function() {
   /*
        Background slideshow
    */
	var val = document.getElementById("top-content").getAttribute('data-value');
	$('.top-content').backstretch(val);
});