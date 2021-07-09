# -*- coding: utf-8 -*-

import time
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class LaundryManagement(models.Model):
    _inherit = 'laundry.order'
    _description = "Laundry Order"

    conv = fields.Selection([
        ('475z', '475z'),
        ('476z', '476z'),
        ('477z', '477z'),
        ('478z', '478z')
    ], string='Réfrence sur le convoyeur', store=True)
