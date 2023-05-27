# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT



class MrpProductionPlanningLine(models.Model):
    _inherit = 'mrp.production.planning.line'

    prepress_proof_id = fields.Many2one(string='Prepress proof',related='mrp_production_request_id.prepress_proof_id')

