   �         @https://assets.awwwards.com/dist/js/home.ffec5c203aa949c02b48.js     %�|/�$      %��J               �      
     H T T P / 1 . 1   2 0 0      Server   nginx   Date   Mon, 16 Nov 2020 06:51:12 GMT   Content-Type   %application/javascript; charset=utf-8   Last-Modified   Fri, 13 Nov 2020 17:27:48 GMT   Etag   W/"5faec214-359c"   Expires   Sun, 14 Feb 2021 06:51:12 GMT   Cache-Control   max-age=7776000   Access-Control-Allow-Origin   *   Access-Control-Allow-Methods   GET   Access-Control-Allow-Headers   fDNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type   Content-Length   13920                 // Injected by Arachni::Browser::Javascript
                _arachni_js_namespaceTaintTracer.update_tracers();
                _arachni_js_namespaceDOMMonitor.update_trackers();
!function(e){function t(t){for(var s,r,a=t[0],i=t[1],u=t[2],d=0,p=[];d<a.length;d++)r=a[d],Object.prototype.hasOwnProperty.call(o,r)&&o[r]&&p.push(o[r][0]),o[r]=0;for(s in i)Object.prototype.hasOwnProperty.call(i,s)&&(e[s]=i[s]);for(c&&c(t);p.length;)p.shift()();return l.push.apply(l,u||[]),n()}function n(){for(var e,t=0;t<l.length;t++){for(var n=l[t],s=!0,a=1;a<n.length;a++){var i=n[a];0!==o[i]&&(s=!1)}s&&(l.splice(t--,1),e=r(r.s=n[0]))}return e}var s={},o={18:0},l=[];function r(t){if(s[t])return s[t].exports;var n=s[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,r),n.l=!0,n.exports}r.e=function(e){var t=[],n=o[e];if(0!==n)if(n)t.push(n[2]);else{var s=new Promise((function(t,s){n=o[e]=[t,s]}));t.push(n[2]=s);var l,a=document.createElement("script");a.charset="utf-8",a.timeout=120,r.nc&&a.setAttribute("nonce",r.nc),a.src=function(e){return r.p+""+({1:"vendors~create-collection~edit-collection",8:"contact",13:"create-collection",15:"edit-collection",16:"forgot-password",30:"message",41:"register",42:"search",66:"vendors~zxcvbn"}[e]||e)+"."+{1:"57d9dab74408e1566998",8:"e8968375496518ff45eb",13:"f8f42cdf74bf7f9048a1",15:"91c4570a10a6f668c6b5",16:"ae0b0620e247dffac267",30:"1d6242bef97ae20bfde3",41:"ea665e4566a620073b4d",42:"62ea7da193b9ece9a236",66:"0ff374b97753475bbf91"}[e]+".js"}(e);var i=new Error;l=function(t){a.onerror=a.onload=null,clearTimeout(u);var n=o[e];if(0!==n){if(n){var s=t&&("load"===t.type?"missing":t.type),l=t&&t.target&&t.target.src;i.message="Loading chunk "+e+" failed.\n("+s+": "+l+")",i.name="ChunkLoadError",i.type=s,i.request=l,n[1](i)}o[e]=void 0}};var u=setTimeout((function(){l({type:"timeout",target:a})}),12e4);a.onerror=a.onload=l,document.head.appendChild(a)}return Promise.all(t)},r.m=e,r.c=s,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var s in e)r.d(n,s,function(t){return e[t]}.bind(null,s));return n},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="https://assets.awwwards.com/dist/js/",r.oe=function(e){throw console.error(e),e};var a=window.webpackJsonp=window.webpackJsonp||[],i=a.push.bind(a);a.push=t,a=a.slice();for(var u=0;u<a.length;u++)t(a[u]);var c=i;l.push([297,0]),n()}({234:function(e,t,n){"use strict";(function(e){var s=n(6),o=n.n(s),l=n(13),r=n(235),a=n.n(r),i=n(9),u=o.a.View.extend({events:{"click .js-user-votes":"_showUserVotes","click .js-jury-votes":"_showJudgeVotes"},className:"box-content-likes",votes:[],slug:null,numberOfUserVotes:0,areUsersLoaded:!1,initialize:function(e){this.slug=e.slug,this.votes=e.votes,this.numberOfUserVotes=e.numberOfUserVotes},open:function(){this.lightBox=new l.a({remove_after_close:!0}),this.el.innerHTML=a()({votes:this.votes,numberOfUserVotes:this.numberOfUserVotes}),this.lightBox.show(this.el)},_showJudgeVotes:function(e){var t=e.currentTarget;this.el.querySelector(".js-user-votes").parentNode.classList.remove("active"),t.parentNode.classList.add("active"),this.el.querySelector("#jury-votes").style.display="block",this.el.querySelector("#user-votes").style.display="none"},_showUserVotes:function(t){var n=t.currentTarget;if(this.el.querySelector(".js-jury-votes").parentNode.classList.remove("active"),n.parentNode.classList.add("active"),this.areUsersLoaded)this.el.querySelector("#jury-votes").style.display="none",this.el.querySelector("#user-votes").style.display="block";else{var s=this;e.ajax({url:i.a.generate("tv_site_get_user_votes_score",{slug:s.slug}),success:function(e){s.el.querySelector("#user-votes").innerHTML=e.list,s.areUsersLoaded=!0,s.el.querySelector("#jury-votes").style.display="none",s.el.querySelector("#user-votes").style.display="block"}})}}});t.a=u}).call(this,n(12))},235:function(e,t,n){var s=n(25);function o(e){return e&&(e.__esModule?e.default:e)}e.exports=(s.default||s).template({1:function(e,t,s,l,r,a){var i,u=null!=t?t:e.nullContext||{},c=e.lookupProperty||function(e,t){if(Object.prototype.hasOwnProperty.call(e,t))return e[t]};return"        <li>\n"+(null!=(i=o(n(28)).call(u,null!=(i=null!=(i=null!=(i=a[0][0])?c(i,"judge"):i)?c(i,"user"):i)?c(i,"username"):i,"awwwards_users",{name:"helpers/compare",hash:{},fn:e.program(2,r,0,a),inverse:e.noop,data:r,blockParams:a,loc:{start:{line:22,column:12},end:{line:34,column:35}}}))?i:"")+(null!=(i=o(n(28)).call(u,null!=(i=null!=(i=null!=(i=a[0][0])?c(i,"judge"):i)?c(i,"user"):i)?c(i,"username"):i,"!=","awwwards_users",{name:"helpers/compare",hash:{},fn:e.program(4,r,0,a),inverse:e.noop,data:r,blockParams:a,loc:{start:{line:35,column:12},end:{line:50,column:35}}}))?i:"")+"        </li>\n"},2:function(e,t,n,s,o,l){var r,a=e.lookupProperty||function(e,t){if(Object.prototype.hasOwnProperty.call(e,t))return e[t]};return'                <figure>\n                    <a href="/"><img src="https://assets.awwwards.com/assets/images/total-users.jpg" width="50" height="50" alt="Awwwards Users - Pro and Chief"></a>\n                </figure>\n                <div class="data">\n                    <div class="row">\n                        <strong><a href="/">Awwwards Users - Pro and Chief</a></strong>\n                    </div>\n                </div>\n                <div class="box-right">\n                    <div class="note">'+e.escapeExpression(e.lambda(null!=(r=l[1][0])?a(r,"average"):r,t))+"</div>\n                </div>\n"},4:function(e,t,s,l,r,a){var i,u=null!=t?t:e.nullContext||{},c=e.escapeExpression,d=e.lambda,p=e.lookupProperty||function(e,t){if(Object.prototype.hasOwnProperty.call(e,t))return e[t]};return'                <figure>\n                    <a href="'+c(o(n(49)).call(u,"tv_user_homepage",{name:"helpers/path",hash:{username:null!=(i=null!=(i=null!=(i=a[1][0])?p(i,"judge"):i)?p(i,"user"):i)?p(i,"username"):i},data:r,blockParams:a,loc:{start:{line:37,column:29},end:{line:37,column:102}}}))+'"><img src="'+c(o(n(116)).call(u,null!=(i=null!=(i=null!=(i=a[1][0])?p(i,"judge"):i)?p(i,"images"):i)?p(i,"photo"):i,"thumb_user_70",{name:"helpers/asset_thumb",hash:{},data:r,blockParams:a,loc:{start:{line:37,column:114},end:{line:37,column:181}}}))+'" width="50" height="50" alt="'+c(d(null!=(i=null!=(i=null!=(i=a[1][0])?p(i,"judge"):i)?p(i,"user"):i)?p(i,"displayName"):i,t))+'"></a>\n                </figure>\n                <div class="data">\n                    <div class="row">\n                        <strong><a href="'+c(o(n(49)).call(u,"tv_user_homepage",{name:"helpers/path",hash:{username:null!=(i=null!=(i=null!=(i=a[1][0])?p(i,"judge"):i)?p(i,"user"):i)?p(i,"username"):i},data:r,blockParams:a,loc:{start:{line:41,column:41},end:{line:41,column:114}}}))+'">'+c(d(null!=(i=null!=(i=null!=(i=a[1][0])?p(i,"judge"):i)?p(i,"user"):i)?p(i,"displayName"):i,t))+'</a></strong>\n                    </div>\n                    <div class="row">\n                        '+c(d(null!=(i=null!=(i=null!=(i=a[1][0])?p(i,"judge"):i)?p(i,"country"):i)?p(i,"name"):i,t))+'\n                    </div>\n                </div>\n                <div class="box-right">\n                    <div class="note">'+c(d(null!=(i=a[1][0])?p(i,"average"):i,t))+"</div>\n                </div>\n"},compiler:[8,">= 4.3.0"],main:function(e,t,s,l,r,a){var i,u=null!=t?t:e.nullContext||{},c=e.escapeExpression,d=e.lambda,p=e.lookupProperty||function(e,t){if(Object.prototype.hasOwnProperty.call(e,t))return e[t]};return'<div class="box-inside">\n    <div class="info style2">\n        <div class="box-left">\n            '+c(o(n(163)).call(u,"app.votes",0,{name:"helpers/transchoice",hash:{},data:r,blockParams:a,loc:{start:{line:4,column:12},end:{line:4,column:53}}}))+'\n            <ul class="menu-tabs">\n                <li class="active">\n                    <div class="menu-item js-jury-votes">\n                        '+c(d(null!=(i=null!=t?p(t,"votes"):t)?p(i,"length"):i,t))+" "+c(o(n(163)).call(u,"app.judges",null!=(i=null!=t?p(t,"votes"):t)?p(i,"length"):i,{name:"helpers/transchoice",hash:{},data:r,blockParams:a,loc:{start:{line:8,column:43},end:{line:8,column:96}}}))+'\n                    </div>\n                </li>\n                <li>\n                    <div class="menu-item js-user-votes">\n                        '+c(d(null!=t?p(t,"numberOfUserVotes"):t,t))+" "+c(o(n(163)).call(u,"app.users",null!=t?p(t,"numberOfUserVotes"):t,{name:"helpers/transchoice",hash:{},data:r,blockParams:a,loc:{start:{line:13,column:48},end:{line:13,column:105}}}))+'\n                    </div>\n                </li>\n            </ul>\n        </div>\n    </div>\n    <ul id="jury-votes" class="list-user-likes">\n'+(null!=(i=p(s,"each").call(u,null!=t?p(t,"votes"):t,{name:"each",hash:{},fn:e.program(1,r,1,a),inverse:e.noop,data:r,blockParams:a,loc:{start:{line:20,column:4},end:{line:52,column:13}}}))?i:"")+'    </ul>\n    <ul id="user-votes" class="list-user-likes hidden">\n    </ul>\n</div>\n'},useData:!0,useBlockParams:!0})},236:function(e,t,n){var s=n(25);e.exports=(s.default||s).template({compiler:[8,">= 4.3.0"],main:function(e,t,n,s,o){var l,r=null!=t?t:e.nullContext||{},a=e.hooks.helperMissing,i=e.escapeExpression,u=e.lookupProperty||function(e,t){if(Object.prototype.hasOwnProperty.call(e,t))return e[t]};return'<div class="circle-note-progress style-developer" data-note="'+i("function"==typeof(l=null!=(l=u(n,"score")||(null!=t?u(t,"score"):t))?l:a)?l.call(r,{name:"score",hash:{},data:o,loc:{start:{line:1,column:61},end:{line:1,column:72}}}):l)+'" id="user-note">\n    <div class="circle">\n        <svg width="80" height="80">\n            <circle r="38" cy="40" cx="40" />\n            <circle r="38" cy="40" cx="40" stroke-linejoin="round" stroke-linecap="round" class="circle-progress" />\n        </svg>\n        <div class="percent">\n            <span class="int">0</span><span class="dec">.00</span>\n        </div>\n    </div>\n</div>\n<div class="row-user">\n    <strong>'+i("function"==typeof(l=null!=(l=u(n,"displayName")||(null!=t?u(t,"displayName"):t))?l:a)?l.call(r,{name:"displayName",hash:{},data:o,loc:{start:{line:13,column:12},end:{line:13,column:29}}}):l)+'</strong>\n</div>\n<div class="row-user">\n    <span class="text-gray">'+i("function"==typeof(l=null!=(l=u(n,"countryName")||(null!=t?u(t,"countryName"):t))?l:a)?l.call(r,{name:"countryName",hash:{},data:o,loc:{start:{line:16,column:28},end:{line:16,column:45}}}):l)+"</span>\n</div>"},useData:!0})},297:function(e,t,n){n(17),e.exports=n(431)},431:function(e,t,n){"use strict";n.r(t);var s=n(6),o=n.n(s),l=n(10),r=n(133),a=n(234),i=n(48),u=n(47),c=n(169),d=n(236),p=n.n(d),h=c.a.extend({tagName:"div",aborted:!1,className:"tooltip-user",initialize:function(e){this.options=e},abort:function(){this.aborted=!0;var e=this;this.el.classList.remove("open"),setTimeout((function(){e.remove()}),300)},render:function(){this._loading();var e=this;return setTimeout((function(){e.el.classList.add("open")}),100),this._render(),this},_loading:function(){this.el.innerHTML='<div class="box-loading style3"><div class="spinner"></div></div>',this.options.classBottom&&this.el.classList.add(this.options.classBottom),this.options.target.appendChild(this.el)},_render:function(){if(!this.aborted){this.el.innerHTML=p()({score:this.options.info.score,countryName:this.options.info.country.name,displayName:this.options.info.displayName}),this.options.target.appendChild(this.el),Object(i.a)(this.el)}}}),m=n(76),f=o.a.View.extend({el:"body",events:{"click .js-country-selector":"_showCountries",click:"_hideCountryList","click .js-more-users":"_showFollowers","click .js-show-jury-votes":"_showJuryVotes","mouseenter .js-judge-note":"_openTooltip","mouseleave .js-judge-note":"_closeTooltip"},page:2,inspirationView:null,route:"",homeUrl:window.location.href,tooltipJudge:null,initialize:function(){new u.a({el:".js-agency-content"}),document.querySelector(".login")&&document.body.classList.add("ht-visible"),Object(i.a)(document.querySelector(".js-notes"));var e=document.querySelector("#js-message");e&&n.e(30).then(n.bind(null,470)).then((function(t){t.default.showMessage(e.dataset.message)}))},_openTooltip:function(e){var t=m.a.getHeight()/2>e.clientY?"tooltip-bottom":"",n=e.currentTarget;[].forEach.call(this.el.querySelectorAll(".tooltip-user"),(function(e){e.classList.contains("open")?e.classList.remove("open"):e.parentNode.removeChild(e)}));var s=JSON.parse(n.dataset.info);this.tooltipJudge=new h({info:s,target:n,classBottom:t}).render()},_closeTooltip:function(){this.tooltipJudge&&this.tooltipJudge.abort()},_showJuryVotes:function(e){var t=JSON.parse(e.currentTarget.dataset.votes),n=e.currentTarget.dataset.numberUserVotes,s=JSON.parse(this.el.querySelector(".js-single-element").dataset.model).slug;new a.a({slug:s,votes:t,numberOfUserVotes:n}).open()},_showFollowers:function(e){var t=e.currentTarget.dataset.username;new r.a({routeToFetch:"tv_user_followers_list",routeParameters:{username:t},total:e.currentTarget.dataset.total}).show()},_showCountries:function(e){e.stopPropagation(),e.currentTarget.classList.toggle("open")},_hideCountryList:function(){[].forEach.call(this.el.querySelectorAll(".js-country-selector"),(function(e){e.classList.remove("open")}))}}),v=function(){new l.a,new f};"loading"==document.readyState?document.addEventListener("DOMContentLoaded",v):v()}});;
