   �         Qhttp://www.gingermutts.co.uk/wp-content/themes/sela/js/navigation.js?ver=20140813     %�@#��      %��[Lx              �      
     H T T P / 1 . 1   2 0 0      Date   Mon, 16 Nov 2020 06:38:09 GMT   Server   Apache   Last-Modified   Mon, 06 Jul 2020 15:38:35 GMT   Etag   "8f5-5a9c7aafcdb69-gzip"   Cache-Control   max-age=2592000   Expires   Wed, 16 Dec 2020 06:38:09 GMT   Content-Length   2489   Content-Type   %application/javascript; charset=utf-8                 // Injected by Arachni::Browser::Javascript
                _arachni_js_namespaceTaintTracer.update_tracers();
                _arachni_js_namespaceDOMMonitor.update_trackers();
/**
 * navigation.js
 *
 * Handles toggling the navigation menu for small screens.
 */
( function() {
	var container, button, menu;

	container = document.getElementById( 'site-navigation' );
	if ( ! container )
		return;

	button = container.getElementsByTagName( 'button' )[0];
	if ( 'undefined' === typeof button )
		return;

	menu = container.getElementsByTagName( 'ul' )[0];

	// Hide menu toggle button if menu is empty and return early.
	if ( 'undefined' === typeof menu ) {
		button.style.display = 'none';
		return;
	}

	if ( -1 === menu.className.indexOf( 'nav-menu' ) )
		menu.className += ' nav-menu';

	button.onclick = function() {
		if ( -1 !== container.className.indexOf( 'toggled' ) )
			container.className = container.className.replace( ' toggled', '' );
		else
			container.className += ' toggled';
	};

    // Fix child menus for touch devices.
    function fixMenuTouchTaps( container ) {
            var touchStartFn,
                parentLink = container.querySelectorAll( '.menu-item-has-children > a, .page_item_has_children > a' );

            if ( 'ontouchstart' in window ) {
                    touchStartFn = function( e ) {
                            var menuItem = this.parentNode;

                            if ( ! menuItem.classList.contains( 'focus' ) ) {
                                    e.preventDefault();
                                    for( var i = 0; i < menuItem.parentNode.children.length; ++i ) {
                                            if ( menuItem === menuItem.parentNode.children[i] ) {
                                                        continue;
                                            }
                                            menuItem.parentNode.children[i].classList.remove( 'focus' );
                                    }
                                    menuItem.classList.add( 'focus' );
                            } else {
                                    menuItem.classList.remove( 'focus' );
                            }
                    };

                    for ( var i = 0; i < parentLink.length; ++i ) {
                            parentLink[i].addEventListener( 'touchstart', touchStartFn, false )
                    }
            }
    }

    fixMenuTouchTaps( container );
} )();
;
