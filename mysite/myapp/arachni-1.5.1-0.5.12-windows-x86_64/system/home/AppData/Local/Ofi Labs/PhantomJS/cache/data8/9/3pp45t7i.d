   �         yhttp://www.gingermutts.co.uk/wp-content/plugins/easy-testimonials/include/assets/js/easy-testimonials-reveal.js?ver=5.5.3     %�@#�(      %�� 9O�              �      
     H T T P / 1 . 1   2 0 0      Date   Mon, 16 Nov 2020 06:38:09 GMT   Server   Apache   Last-Modified   Wed, 30 Sep 2020 01:02:36 GMT   Etag   "63c-5b07d749354f5-gzip"   Cache-Control   max-age=2592000   Expires   Wed, 16 Dec 2020 06:38:09 GMT   Content-Length   1792   Content-Type   %application/javascript; charset=utf-8                 // Injected by Arachni::Browser::Javascript
                _arachni_js_namespaceTaintTracer.update_tracers();
                _arachni_js_namespaceDOMMonitor.update_trackers();
jQuery(function ($) {
	
	var reveal_text = function (ev) {
		var trg_link = $(ev.currentTarget);
		var testimonial = trg_link.parents('.easy_testimonial:first');
		var testimonial_body = trg_link.parents('.testimonial_body:first');
		var reveal_content = testimonial.find('.reveal_full_content:first');
		var reveal_content_html = testimonial.find('.reveal_full_content:first').html();
		
		// abort if already revealed, i.e., double-click
		if ( testimonial_body.data('revealed') ) {
			return;
		}
		
		// save excerpt
		testimonial_body.data( 'save_excerpt', testimonial_body.html() );
		show_less_link = jQuery('<a href="#" class=".show_less_link">' + easy_testimonials_reveal.show_less_text + '</a>');
		show_less_link.on('click', show_less);
		
		// switch in full content and show it
		testimonial_body.html(reveal_content_html);
		testimonial_body.append( show_less_link );
		testimonial_body.data('revealed', true);
		
		ev.preventDefault();
		return false;
	};

	var show_less = function (ev) {
		var trg_link = $(ev.currentTarget);
		var testimonial = trg_link.parents('.easy_testimonial:first');
		var testimonial_body = trg_link.parents('.testimonial_body:first');
		var reveal_content_html = testimonial_body.data('save_excerpt');
		
		// switch excerpt back in and reset state
		testimonial_body.html(reveal_content_html);
		testimonial_body.data('revealed', false);
		
		ev.preventDefault();
		return false;
	};

	jQuery('.easy_testimonial').on('click', '.testimonial_body .reveal_link a, .testimonial_body .more-link', reveal_text);
});;
