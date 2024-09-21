/**@odoo-module*/
import { InputBox } from "./input_box"
import { patch } from "@web/core/utils/patch";
import { useState, useEffect, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

patch(InputBox.prototype, {
    setup() {
        super.setup()
        this.user = useService("orm");
        this.action = useService("action");
        this.state = useState({
            value: 0,
        })
        this.demoFunctionPatch

        useEffect(
            (rec) => {
                console.log("rec", rec)
            },
            () => [this.state.value]
        )
        this.inputRef = useRef('input_ref')
    },
    demo(){
//    console.log('field',this.inputRef.el.value)
    console.log('field',this.inputRef.el.value)
    },
    demoFunctionPatch(e) {
        this.state.value += e
    },
    async useServiceFunc(record) {
        this.sale_order = await this.user.call("orm.model", "search_sale_order",[]);
        console.log('sale',this.sale_order)
        this.sale_order_search = await this.user.search("sale.order",[]);
        console.log('sale',this.sale_order_search)
    }
     openDocument({ id, model }) {
        this.env.services.action.doAction({
            type: "ir.actions.act_window",
            res_model: model,
            views: [[false, "form"]],
            res_id: id,
        });
    }

});
