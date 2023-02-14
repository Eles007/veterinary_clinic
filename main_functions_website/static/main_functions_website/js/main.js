$(document).ready(function (){
	$( ".menu a" ).click(function() {
		$(".menu a").removeClass("block-menu-button-active")
		$( this ).toggleClass("block-menu-button-active")
	});

	$(".logo a").click(function (){
		$(".menu a").removeClass("block-menu-button-active")
	});
})