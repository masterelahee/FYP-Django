   �         Khttp://www.gingermutts.co.uk/wp-content/themes/sela/js/sela.js?ver=20140813     %�@#��      %��[Lx              �      
     H T T P / 1 . 1   2 0 0      Date   Mon, 16 Nov 2020 06:38:09 GMT   Server   Apache   Last-Modified   Mon, 06 Jul 2020 15:38:35 GMT   Etag   "1bf-5a9c7aafceb09-gzip"   Cache-Control   max-age=2592000   Expires   Wed, 16 Dec 2020 06:38:09 GMT   Content-Length   643   Content-Type   %application/javascript; charset=utf-8                 // Injected by Arachni::Browser::Javascript
                _arachni_js_namespaceTaintTracer.update_tracers();
                _arachni_js_namespaceDOMMonitor.update_trackers();
( function( $ ) {

	// Focus styles for menus.
	$( '.main-navigation' ).find( 'a' ).on( 'focus.sela blur.sela', function() {
		$( this ).parents().toggleClass( 'focus' );
	} );

	// Additional class for posts with thumbnails
    function addHentryClass() {
        $( '.hentry + .has-post-thumbnail' ).prev().addClass( 'has-post-thumbnail-prev' );
    }

	$( document.body ).on( 'post-load',  addHentryClass );

	addHentryClass();

} )( jQuery );
;
