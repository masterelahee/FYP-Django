   �         Zhttp://www.gingermutts.co.uk/wp-content/themes/sela/js/skip-link-focus-fix.js?ver=20140813     %�@#�      %��[Lx              �      
     H T T P / 1 . 1   2 0 0      Date   Mon, 16 Nov 2020 06:38:09 GMT   Server   Apache   Last-Modified   Mon, 06 Jul 2020 15:38:35 GMT   Etag   "2dd-5a9c7aafceb09-gzip"   Cache-Control   max-age=2592000   Expires   Wed, 16 Dec 2020 06:38:09 GMT   Content-Length   929   Content-Type   %application/javascript; charset=utf-8                 // Injected by Arachni::Browser::Javascript
                _arachni_js_namespaceTaintTracer.update_tracers();
                _arachni_js_namespaceDOMMonitor.update_trackers();
( function() {
	var is_webkit = navigator.userAgent.toLowerCase().indexOf( 'webkit' ) > -1,
	    is_opera  = navigator.userAgent.toLowerCase().indexOf( 'opera' )  > -1,
	    is_ie     = navigator.userAgent.toLowerCase().indexOf( 'msie' )   > -1;

	if ( ( is_webkit || is_opera || is_ie ) && 'undefined' !== typeof( document.getElementById ) ) {
		var eventMethod = ( window.addEventListener ) ? 'addEventListener' : 'attachEvent';
		window[ eventMethod ]( 'hashchange', function() {
			var element = document.getElementById( location.hash.substring( 1 ) );

			if ( element ) {
				if ( ! /^(?:a|select|input|button|textarea)$/i.test( element.tagName ) )
					element.tabIndex = -1;

				element.focus();
			}
		}, false );
	}
})();
;
