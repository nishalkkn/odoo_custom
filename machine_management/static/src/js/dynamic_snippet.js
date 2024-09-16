/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";

publicWidget.registry.DynamicSnippet = publicWidget.Widget.extend({
   selector: '.dynamic_snippet',

   events: {
       	'click .carousel-control-prev': '_onClickPrev',
   	},

   	_onClickPrev: function(ev){
   	    var data = jsonrpc('/machine/list', {})
//        console.log('data',data);
    	},

   start: function () {
       var self = this;
       var data = jsonrpc('/machine/list', {}).then((data) => {
           self.$target.empty().append(data)
//           console.log('ffff',data)
//           console.log('this',this)

       });
   }
});

export default publicWidget.registry.DynamicSnippet;
