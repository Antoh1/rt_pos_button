odoo.define("rt_pos_butt.rt_pos_btn", function (require){
'use strict'
    var screens = require("point_of_sale.screens");

    var RtPosBn = screens.ActionButtonWidget.extend({
        template: "RtPosBn",
        button_click: function() {
            alert('My first Pos Button...');
        },
    });
    screens.define_action_button({
        name: "tr_pos_bn",
        widget: RtPosBn,
        condition: function() {
            return this.pos;
        },
    });
});