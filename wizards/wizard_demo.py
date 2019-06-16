import json
from odoo import models, fields

class WizardDemo(models.TransientModel):
    _name = "wizard.demo"

    params = fields.Char("Params")

    def button_test(self):
        records = []
        params = {
            'id': 1,
        }
        #params = json.dumps(params)
        data = {
            'records':  records,
            'parameters': params,
        }
        return self.env.ref('demo.demo_report').report_action(self, data=data)
