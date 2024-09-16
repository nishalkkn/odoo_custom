odoo.define('machine_management.snippet', function(require) {
    'use strict';
    var PublicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var qweb = core.qweb;
    var Dynamic = PublicWidget.Widget.extend({
        selector: '.dynamic_snippet_blog',
        willStart: async function() {
            var self = this;
            await rpc.query({
                route: '/latest_elearning_courses',
            }).then((data) => {
                this.data = data;
            });
        },
        start: function() {
            var chunks = _.chunk(this.data, 4)
            chunks[0].is_active = true
            this.$el.find('#courosel').html(
                qweb.render('machine_management.elearning_snippet_carousel', {
                    chunks
                })
            )
        },
    });
    PublicWidget.registry.dynamic_snippet_blog = Dynamic;
    return Dynamic;
});