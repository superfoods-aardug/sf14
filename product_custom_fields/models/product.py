# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_aa_sf_is_biologisch = fields.Boolean(string="Is Biologisch", default=False)
    x_aa_sf_Skal_code = fields.Text(string="SKAL Code")
    x_aa_sf_land_desc = fields.Text(string="Land Van Herkomst")
