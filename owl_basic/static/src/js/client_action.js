/**@odoo-module*/
import { registry } from '@web/core/registry';
import { Component } from "@odoo/owl";
import { InputBox } from "./input_box"

class AdvancedDashboard extends Component {

}
AdvancedDashboard.template = 'owl_basic.advanced_dashboard'
AdvancedDashboard.components = {
InputBox
}
registry.category('actions').add('advanced_dashboard', AdvancedDashboard)