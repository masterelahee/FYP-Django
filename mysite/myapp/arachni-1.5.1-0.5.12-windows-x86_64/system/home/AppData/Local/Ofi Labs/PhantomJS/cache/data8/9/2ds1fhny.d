   �         Chttps://assets.awwwards.com/dist/js/nominee.1f4ed568007f8e2e6bf7.js     %�|0��      %��J          
     H T T P / 1 . 1   2 0 0           �      Server   nginx   Date   Mon, 16 Nov 2020 06:52:13 GMT   Content-Type   %application/javascript; charset=utf-8   Last-Modified   Fri, 13 Nov 2020 17:27:48 GMT   Etag   W/"5faec214-53f8"   Expires   Sun, 14 Feb 2021 06:52:13 GMT   Cache-Control   max-age=7776000   Access-Control-Allow-Origin   *   Access-Control-Allow-Methods   GET   Access-Control-Allow-Headers   fDNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type   Content-Length   21692                 // Injected by Arachni::Browser::Javascript
                _arachni_js_namespaceTaintTracer.update_tracers();
                _arachni_js_namespaceDOMMonitor.update_trackers();
!function(t){function e(e){for(var i,o,l=e[0],r=e[1],c=e[2],d=0,h=[];d<l.length;d++)o=l[d],Object.prototype.hasOwnProperty.call(s,o)&&s[o]&&h.push(s[o][0]),s[o]=0;for(i in r)Object.prototype.hasOwnProperty.call(r,i)&&(t[i]=r[i]);for(u&&u(e);h.length;)h.shift()();return a.push.apply(a,c||[]),n()}function n(){for(var t,e=0;e<a.length;e++){for(var n=a[e],i=!0,l=1;l<n.length;l++){var r=n[l];0!==s[r]&&(i=!1)}i&&(a.splice(e--,1),t=o(o.s=n[0]))}return t}var i={},s={34:0},a=[];function o(e){if(i[e])return i[e].exports;var n=i[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.e=function(t){var e=[],n=s[t];if(0!==n)if(n)e.push(n[2]);else{var i=new Promise((function(e,i){n=s[t]=[e,i]}));e.push(n[2]=i);var a,l=document.createElement("script");l.charset="utf-8",l.timeout=120,o.nc&&l.setAttribute("nonce",o.nc),l.src=function(t){return o.p+""+({1:"vendors~create-collection~edit-collection",8:"contact",13:"create-collection",15:"edit-collection",16:"forgot-password",41:"register",42:"search",66:"vendors~zxcvbn"}[t]||t)+"."+{1:"57d9dab74408e1566998",8:"e8968375496518ff45eb",13:"f8f42cdf74bf7f9048a1",15:"91c4570a10a6f668c6b5",16:"ae0b0620e247dffac267",41:"ea665e4566a620073b4d",42:"62ea7da193b9ece9a236",66:"0ff374b97753475bbf91"}[t]+".js"}(t);var r=new Error;a=function(e){l.onerror=l.onload=null,clearTimeout(c);var n=s[t];if(0!==n){if(n){var i=e&&("load"===e.type?"missing":e.type),a=e&&e.target&&e.target.src;r.message="Loading chunk "+t+" failed.\n("+i+": "+a+")",r.name="ChunkLoadError",r.type=i,r.request=a,n[1](r)}s[t]=void 0}};var c=setTimeout((function(){a({type:"timeout",target:l})}),12e4);l.onerror=l.onload=a,document.head.appendChild(l)}return Promise.all(e)},o.m=t,o.c=i,o.d=function(t,e,n){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},o.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var i in t)o.d(n,i,function(e){return t[e]}.bind(null,i));return n},o.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="https://assets.awwwards.com/dist/js/",o.oe=function(t){throw console.error(t),t};var l=window.webpackJsonp=window.webpackJsonp||[],r=l.push.bind(l);l.push=e,l=l.slice();for(var c=0;c<l.length;c++)e(l[c]);var u=r;a.push([299,0]),n()}({118:function(t,e,n){"use strict";n.d(e,"a",(function(){return s}));var i=function(){return(i=Object.assign||function(t){for(var e,n=1,i=arguments.length;n<i;n++)for(var s in e=arguments[n])Object.prototype.hasOwnProperty.call(e,s)&&(t[s]=e[s]);return t}).apply(this,arguments)},s=function(){function t(t,e,n){var s=this;this.target=t,this.endVal=e,this.options=n,this.version="2.0.4",this.defaults={startVal:0,decimalPlaces:0,duration:2,useEasing:!0,useGrouping:!0,smartEasingThreshold:999,smartEasingAmount:333,separator:",",decimal:".",prefix:"",suffix:""},this.finalEndVal=null,this.useEasing=!0,this.countDown=!1,this.error="",this.startVal=0,this.paused=!0,this.count=function(t){s.startTime||(s.startTime=t);var e=t-s.startTime;s.remaining=s.duration-e,s.useEasing?s.countDown?s.frameVal=s.startVal-s.easingFn(e,0,s.startVal-s.endVal,s.duration):s.frameVal=s.easingFn(e,s.startVal,s.endVal-s.startVal,s.duration):s.countDown?s.frameVal=s.startVal-(s.startVal-s.endVal)*(e/s.duration):s.frameVal=s.startVal+(s.endVal-s.startVal)*(e/s.duration),s.countDown?s.frameVal=s.frameVal<s.endVal?s.endVal:s.frameVal:s.frameVal=s.frameVal>s.endVal?s.endVal:s.frameVal,s.frameVal=Math.round(s.frameVal*s.decimalMult)/s.decimalMult,s.printValue(s.frameVal),e<s.duration?s.rAF=requestAnimationFrame(s.count):null!==s.finalEndVal?s.update(s.finalEndVal):s.callback&&s.callback()},this.formatNumber=function(t){var e,n,i,a,o,l=t<0?"-":"";if(e=Math.abs(t).toFixed(s.options.decimalPlaces),i=(n=(e+="").split("."))[0],a=n.length>1?s.options.decimal+n[1]:"",s.options.useGrouping){o="";for(var r=0,c=i.length;r<c;++r)0!==r&&r%3==0&&(o=s.options.separator+o),o=i[c-r-1]+o;i=o}return s.options.numerals&&s.options.numerals.length&&(i=i.replace(/[0-9]/g,(function(t){return s.options.numerals[+t]})),a=a.replace(/[0-9]/g,(function(t){return s.options.numerals[+t]}))),l+s.options.prefix+i+a+s.options.suffix},this.easeOutExpo=function(t,e,n,i){return n*(1-Math.pow(2,-10*t/i))*1024/1023+e},this.options=i({},this.defaults,n),this.formattingFn=this.options.formattingFn?this.options.formattingFn:this.formatNumber,this.easingFn=this.options.easingFn?this.options.easingFn:this.easeOutExpo,this.startVal=this.validateValue(this.options.startVal),this.frameVal=this.startVal,this.endVal=this.validateValue(e),this.options.decimalPlaces=Math.max(this.options.decimalPlaces),this.decimalMult=Math.pow(10,this.options.decimalPlaces),this.resetDuration(),this.options.separator=String(this.options.separator),this.useEasing=this.options.useEasing,""===this.options.separator&&(this.options.useGrouping=!1),this.el="string"==typeof t?document.getElementById(t):t,this.el?this.printValue(this.startVal):this.error="[CountUp] target is null or undefined"}return t.prototype.determineDirectionAndSmartEasing=function(){var t=this.finalEndVal?this.finalEndVal:this.endVal;this.countDown=this.startVal>t;var e=t-this.startVal;if(Math.abs(e)>this.options.smartEasingThreshold){this.finalEndVal=t;var n=this.countDown?1:-1;this.endVal=t+n*this.options.smartEasingAmount,this.duration=this.duration/2}else this.endVal=t,this.finalEndVal=null;this.finalEndVal?this.useEasing=!1:this.useEasing=this.options.useEasing},t.prototype.start=function(t){this.error||(this.callback=t,this.duration>0?(this.determineDirectionAndSmartEasing(),this.paused=!1,this.rAF=requestAnimationFrame(this.count)):this.printValue(this.endVal))},t.prototype.pauseResume=function(){this.paused?(this.startTime=null,this.duration=this.remaining,this.startVal=this.frameVal,this.determineDirectionAndSmartEasing(),this.rAF=requestAnimationFrame(this.count)):cancelAnimationFrame(this.rAF),this.paused=!this.paused},t.prototype.reset=function(){cancelAnimationFrame(this.rAF),this.paused=!0,this.resetDuration(),this.startVal=this.validateValue(this.options.startVal),this.frameVal=this.startVal,this.printValue(this.startVal)},t.prototype.update=function(t){cancelAnimationFrame(this.rAF),this.startTime=null,this.endVal=this.validateValue(t),this.endVal!==this.frameVal&&(this.startVal=this.frameVal,this.finalEndVal||this.resetDuration(),this.determineDirectionAndSmartEasing(),this.rAF=requestAnimationFrame(this.count))},t.prototype.printValue=function(t){var e=this.formattingFn(t);"INPUT"===this.el.tagName?this.el.value=e:"text"===this.el.tagName||"tspan"===this.el.tagName?this.el.textContent=e:this.el.innerHTML=e},t.prototype.ensureNumber=function(t){return"number"==typeof t&&!isNaN(t)},t.prototype.validateValue=function(t){var e=Number(t);return this.ensureNumber(e)?e:(this.error="[CountUp] invalid start or end value: "+t,null)},t.prototype.resetDuration=function(){this.startTime=null,this.duration=1e3*Number(this.options.duration),this.remaining=this.duration},t}()},120:function(t,e,n){"use strict";var i=n(6),s=n.n(i),a=n(13),o=s.a.View.extend({el:".js-sidebar-nominee",events:{"click .js-lightbox-submit-status":"_showInfo"},initialize:function(){document.querySelector(".js-sidebar-nominee")&&document.body.classList.add("site-status")},_showInfo:function(t){var e=new a.a({remove_after_close:!0}),n=t.currentTarget.dataset.type,i=this.el.querySelector(".js-submit-status-"+n).cloneNode(!0);i.classList.remove("hidden"),e.show(i)}});e.a=o},135:function(t,e,n){"use strict";(function(t){var i=n(6),s=n.n(i),a=n(16),o=n(20),l=n(144),r=n(146),c=n(13),u=n(31),d=n(118),h=s.a.View.extend({el:".box-vote-site",isVoting:!1,votes:[],events:{"click .js-votenow":"startVoting","click .js-sendvote":"sendVote","click .js-editvote":"editVote"},initialize:function(){this.checkIfItsJustVoted(),this.el&&(this.votes=this._getStepConfiguration(),this.render())},_getStepConfiguration:function(){return[]},checkIfItsJustVoted:function(){var t=document.querySelector(".box-vote-info");if(t){var e=this;setTimeout((function(){e.showScorePoints(t)}),1e3)}},editVote:function(){this.el.querySelector(".slide-result").classList.remove("active"),this.step=0,this.votes[0].view.show()},startVoting:function(t){o.a.isLoggedIn()?(this.step=0,t.currentTarget.style.display="none",this.$(".slides").fadeIn(),document.querySelector(".box-screenshot").classList.add("style2"),document.querySelector(".box-vote-site").classList.add("voting"),this.votes[0].view.show()):(new u.a).open()},render:function(){var t=1,e=this,n=this.votes.length;a.default.each(this.votes,(function(i){var s=new l.a({model:new r.a({key:i.key,title:i.title,step:t,total_steps:n})});s.on("voted",e._nextStep,e),i.view=s,e.el.querySelector(".slides").appendChild(s.render().el),t++}))},_nextStep:function(t){t===this.votes.length?this._showTotal():this.votes[t].view.show()},_showTotal:function(){this.el.querySelector(".slide-result").classList.add("active"),document.querySelector(".box-screenshot").classList.add("style3");var t=this.el.querySelector(".js-result-grades");t&&(t.innerHTML="",a.default.each(this.votes,(function(e){var n=document.createElement("li");n.innerText=e.view.model.getTitle().toUpperCase();var i=document.createElement("strong");i.innerText=" "+e.view.model.getGrade(),n.appendChild(i),t.appendChild(n)})));var e=new d.a("total-note",this._calculateAverage(),{useEasing:!0,useGrouping:!0,separator:",",decimal:".",decimalPlaces:2,prefix:"",suffix:"",duration:2.5});setTimeout((function(){e.start()}),500)},_calculateAverage:function(){var t=0;return a.default.each(this.votes,(function(e){t+=e.view.model.getGrade()*e.percent})),t.toFixed(2)},sendVote:function(t){t.preventDefault(),this._doSendVote()},_doSendVote:function(){if(!this.isVoting){this._showLoading(),this.isVoting=!0,a.default.each(this.votes,(function(t){document.querySelector("input.vote-"+t.view.model.getKey()).value=t.view.model.getGrade()}));var e=this,n=this.$(".js-vote-form");t.ajax({type:"POST",url:n.attr("action"),data:n.serialize(),success:function(e){t(".js-sendvote").fadeOut(),setTimeout((function(){e.hasOwnProperty("url")?location.href=e.url:location.reload()}),500)},error:function(t){var n=JSON.parse(t.responseText).error;e._resetVoting(),new c.a({remove_after_close:!0}).openConfirmation(n,"OK")},complete:function(){e.isVoting=!1}})}},_resetVoting:function(){this.el.querySelector(".slide-result").classList.remove("active"),this.step=0,this.votes[0].view.show(),this._hideLoading()},_showLoading:function(){var t=document.createElement("div");t.classList.add("box-loading","style2","open");var e=document.createElement("div");e.classList.add("spinner"),t.appendChild(e);var n=document.querySelector(".box-screenshot");n.appendChild(t),[].forEach.call(document.querySelectorAll(".slide"),(function(t){t.classList.remove("active")})),n.classList.remove("style2")},_hideLoading:function(){document.querySelector(".box-screenshot .box-loading").remove(),document.querySelector(".box-screenshot").classList.add("style2")},showScorePoints:function(e){e.classList.remove("off");var n=1,i=setInterval((function(){if(6==n)clearInterval(i),setTimeout((function(){e.classList.add("off")}),2200);else{var t=++n-1,s=document.querySelector(".js-scorepoints");s&&(s.innerText="+"+t)}}),300);t(".js-bar").animate({width:"100%"},1800)}});e.a=h}).call(this,n(12))},143:function(t,e,n){"use strict";(function(t){var i=n(6),s=n.n(i),a=n(9),o=n(16),l=n(48),r=n(68),c=n(118),u=n(47),d=n(76),h=n(113),p=n(120),m=s.a.View.extend({el:"body",page:2,events:{"click #load_more_votes":"loadMoreVotes"},initialize:function(t){var e=this.el.querySelector(".js-credits-container");e&&new u.a({el:e}),this.options=t,this.el.querySelector(".js-single-element")&&(this.options.submissionModel=JSON.parse(this.el.querySelector(".js-single-element").dataset.model)),Object(l.b)(),new r.a;var n=this.$("#total-note-voted");if(1===n.length){var i=new c.a("total-note-voted",n.data("note"),{useEasing:!0,useGrouping:!0,separator:",",decimal:".",decimalPlaces:2,prefix:"",suffix:"",duration:2.5});setTimeout((function(){i.start()}),500)}var s=document.getElementById("voting");if(s){var a=d.a.getOffset(s).top,m=document.querySelector(".box-footer-bts");m&&window.addEventListener("scroll",o.default.throttle((function(){(window.pageYOffset||document.documentElement.scrollTop||document.body.scrollTop||0)>a-d.a.getHeight()?m.classList.add("fade-out"):m.classList.remove("fade-out")}),100))}this.options.submissionModel&&h.a.add(this.options.submissionModel.slug,"submission"),new p.a},loadMoreVotes:function(e){var n=t(e.currentTarget),i=this;t.ajax({url:a.a.generate("tv_site_get_user_votes",{slug:this.options.submissionModel.slug}),data:{page:i.page},success:function(e){t("#user_votes").append(e.items),Object(l.b)(),parseInt(e.items_left)<=0&&n.hide(),i.page++}})}});e.a=m}).call(this,n(12))},144:function(t,e,n){"use strict";var i=n(6),s=n.n(i),a=n(145),o=n.n(a),l=s.a.View.extend({className:"slide",events:{"click li":"vote"},template:o.a,render:function(){var t={step:this.model.getStep(),title:this.model.getTitle(),key:this.model.getKey()};return this.el.classList.add("slide-"+this.model.getKey()),this.$el.html(this.template({vote_process:t})),this},vote:function(t){var e=parseInt(t.currentTarget.innerText);this._closeView(),this.model.setGrade(e),this.trigger("voted",this.model.get("step"))},show:function(){this.el.classList.add("active")},_closeView:function(){this.el.classList.remove("active")}});e.a=l},145:function(t,e,n){var i=n(25);t.exports=(i.default||i).template({compiler:[8,">= 4.3.0"],main:function(t,e,n,i,s){var a,o=t.lambda,l=t.escapeExpression,r=t.lookupProperty||function(t,e){if(Object.prototype.hasOwnProperty.call(t,e))return t[e]};return'\n<ul class="vote-site vote-'+l(o(null!=(a=null!=e?r(e,"vote_process"):e)?r(a,"key"):a,e))+'">\n    <li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li><li>7</li><li>8</li><li>9</li><li>10</li>\n</ul>\n<div class="step">\n    <span>'+l(o(null!=(a=null!=e?r(e,"vote_process"):e)?r(a,"title"):a,e))+"</span>\n    <span>"+l(o(null!=(a=null!=e?r(e,"vote_process"):e)?r(a,"step"):a,e))+"</span>\n</div>\n"},useData:!0})},146:function(t,e,n){"use strict";var i=n(6),s=n.n(i).a.Model.extend({defaults:{total_steps:0,grade:0,step:0,key:"",title:""},setGrade:function(t){this.set("grade",t)},getGrade:function(){return this.get("grade")},getStep:function(){return this.get("step")+"/"+this.get("total_steps")},getKey:function(){return this.get("key")},getTitle:function(){return this.get("title")}});e.a=s},176:function(t,e,n){"use strict";n.r(e);var i=n(21);e.default=function(t,e){return i.a.assetTv(t,e)}},238:function(t,e,n){var i=n(25);function s(t){return t&&(t.__esModule?t.default:t)}t.exports=(i.default||i).template({1:function(t,e,i,a,o,l){var r=t.lambda,c=t.escapeExpression;return'        <li>\n            <div class="input-check">\n                <input type="checkbox" id="think_'+c(r(l[0][1],e))+'" value="'+c(r(l[0][1],e))+'">\n                <label for="think_'+c(r(l[0][1],e))+'">'+c(s(n(11)).call(null!=e?e:t.nullContext||{},l[0][0],{name:"helpers/trans",hash:{},data:o,blockParams:l,loc:{start:{line:24,column:43},end:{line:24,column:69}}}))+"</label>\n            </div>\n        </li>\n"},3:function(t,e,i,a,o,l){var r=t.lambda,c=t.escapeExpression;return'            <li>\n                <div class="input-check">\n                    <input type="checkbox" id="like_'+c(r(l[0][1],e))+'" value="'+c(r(l[0][1],e))+'">\n                    <label for="like_'+c(r(l[0][1],e))+'">'+c(s(n(11)).call(null!=e?e:t.nullContext||{},l[0][0],{name:"helpers/trans",hash:{},data:o,blockParams:l,loc:{start:{line:35,column:46},end:{line:35,column:72}}}))+"</label>\n                </div>\n            </li>\n"},5:function(t,e,i,a,o,l){var r=t.lambda,c=t.escapeExpression;return'            <li>\n                <div class="input-check">\n                    <input type="checkbox" id="details_'+c(r(l[0][1],e))+'" value="'+c(r(l[0][1],e))+'">\n                    <label for="details_'+c(r(l[0][1],e))+'">'+c(s(n(11)).call(null!=e?e:t.nullContext||{},l[0][0],{name:"helpers/trans",hash:{},data:o,blockParams:l,loc:{start:{line:46,column:49},end:{line:46,column:75}}}))+"</label>\n                </div>\n            </li>\n"},compiler:[8,">= 4.3.0"],main:function(t,e,i,a,o,l){var r,c=null!=e?e:t.nullContext||{},u=t.escapeExpression,d=t.lookupProperty||function(t,e){if(Object.prototype.hasOwnProperty.call(t,e))return t[e]};return'<div class="header">\n    <div class="box-photo">\n        <img src="'+u(s(n(176)).call(c,null!=e?d(e,"image"):e,{name:"helpers/asset_tv",hash:{},data:o,blockParams:l,loc:{start:{line:3,column:18},end:{line:3,column:48}}}))+'" width="300" alt="">\n    </div>\n    <div class="box-note">\n        <div class="total-note">'+u(t.lambda(null!=e?d(e,"score"):e,e))+'</div>\n        <a href="#" class="box-bt">\n            <div class="bt-ico">\n                <div class="ico">\n                    '+(null!=(r=s(n(78)).call(c,"reload",14,14,{name:"helpers/icon",hash:{},data:o,blockParams:l,loc:{start:{line:10,column:20},end:{line:10,column:57}}}))?r:"")+'\n                </div>\n            </div>\n            <span class="js-edit-vote-opinion text-uppercase">'+u(s(n(11)).call(c,"app.edit_your_vote",{name:"helpers/trans",hash:{},data:o,blockParams:l,loc:{start:{line:13,column:62},end:{line:13,column:104}}}))+'</span>\n        </a>\n    </div>\n</div>\n<div class="content">\n    <h4>'+u(s(n(11)).call(c,"vote_opinion.what_do_you_think",{name:"helpers/trans",hash:{},data:o,blockParams:l,loc:{start:{line:18,column:8},end:{line:18,column:62}}}))+'</h4>\n    <ul class="js-think">\n'+(null!=(r=d(i,"each").call(c,null!=(r=null!=e?d(e,"opinions"):e)?d(r,"think"):r,{name:"each",hash:{},fn:t.program(1,o,2,l),inverse:t.noop,data:o,blockParams:l,loc:{start:{line:20,column:8},end:{line:27,column:17}}}))?r:"")+"    </ul>\n    <h4>"+u(s(n(11)).call(c,"vote_opinion.what_do_you_like",{name:"helpers/trans",hash:{},data:o,blockParams:l,loc:{start:{line:29,column:8},end:{line:29,column:61}}}))+'</h4>\n    <ul class="js-like">\n'+(null!=(r=d(i,"each").call(c,null!=(r=null!=e?d(e,"opinions"):e)?d(r,"like"):r,{name:"each",hash:{},fn:t.program(3,o,2,l),inverse:t.noop,data:o,blockParams:l,loc:{start:{line:31,column:8},end:{line:38,column:17}}}))?r:"")+'    </ul>\n    <hr>\n    <ul class="js-details">\n'+(null!=(r=d(i,"each").call(c,null!=(r=null!=e?d(e,"opinions"):e)?d(r,"details"):r,{name:"each",hash:{},fn:t.program(5,o,2,l),inverse:t.noop,data:o,blockParams:l,loc:{start:{line:42,column:8},end:{line:49,column:17}}}))?r:"")+'    </ul>\n    <div class="js-submit button width-full text-uppercase">'+u(s(n(11)).call(c,"app.send_vote",{name:"helpers/trans",hash:{},data:o,blockParams:l,loc:{start:{line:51,column:60},end:{line:51,column:97}}}))+"</div>\n</div>\n"},useData:!0,useBlockParams:!0})},299:function(t,e,n){n(17),t.exports=n(429)},429:function(t,e,n){"use strict";n.r(e);var i=n(10),s=n(143),a=n(135),o=n(6),l=n.n(o),r=n(238),c=n.n(r),u=n(13),d=l.a.View.extend({lightbox:null,className:"box-content-confirm-vote",events:{"click .js-submit":"_submit","click .js-edit-vote-opinion":"_editVote"},opinions:[],image:"",score:0,initialize:function(t){this.opinions=t.opinions,this.image=t.image,this.score=t.score,this.close_callback=t.close_callback},open:function(){this.lightBox=new u.a({remove_after_close:!0,close_callback:this.close_callback}),this.el.innerHTML=c()({opinions:this.opinions,score:this.score,image:this.image}),this.lightBox.show(this.el)},_editVote:function(){this.lightBox.close()},_submit:function(){var t={think:[],like:[],details:[]},e=this;[].forEach.call(["think","like","details"],(function(n){[].forEach.call(e.el.querySelectorAll(".js-"+n+" input:checked"),(function(e){t[n].push(e.value)}))})),this.lightBox.closeWithoutCallback(),this.trigger("opinion_sent",t)}}),h=n(15),p=a.a.extend({_getStepConfiguration:function(){return[{key:"design",title:h.a.trans("legend_circle.design"),color:"#FF9A3D",percent:.4},{key:"usability",title:h.a.trans("legend_circle.usability"),color:"#FFCF81",percent:.3},{key:"creativity",title:h.a.trans("legend_circle.creativity"),color:"#01AF9D",percent:.2},{key:"content",title:h.a.trans("legend_circle.content"),color:"#12A5C8",percent:.1}]},_showTotal:function(){a.a.prototype._showTotal.call(this);var t=this._calculateAverage();if(!(t<7)){var e=JSON.parse(document.body.querySelector(".box-vote-site").dataset.opinions);if(Object.keys(e).length>0){var n=this,i=new d({opinions:e,image:JSON.parse(document.body.querySelector(".js-single-element").dataset.model).images.thumbnail,score:t,close_callback:function(){n.editVote()}});i.open(),i.on("opinion_sent",this._saveOpinionAndSubmit,this)}}},_saveOpinionAndSubmit:function(t){[].forEach.call(["think","like","details"],(function(e){[].forEach.call(t[e],(function(t){var e=document.body.querySelector('.js-opinion input[value="'+t+'"]');e&&(e.checked=!0)}))})),this._doSendVote()}});document.addEventListener("DOMContentLoaded",(function(){new i.a,new s.a({voting:new p})}))}});;
