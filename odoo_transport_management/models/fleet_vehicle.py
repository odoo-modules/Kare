# -*- coding: utf-8 -*-

from odoo import models, fields

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    transporter_id = fields.Many2one(
        'res.partner',
        string='Transporter',
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
