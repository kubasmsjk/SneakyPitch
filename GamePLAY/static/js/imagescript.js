  jQuery(document).ready(function() {
   /*
        Background slideshow
    */
	var val = document.getElementById("top-content").getAttribute('data-value');
	$('.top-content').backstretch(val);
	var val_two = document.getElementById("section-2").getAttribute('data-value');
	$('.section-2-container').backstretch(val_two );
});