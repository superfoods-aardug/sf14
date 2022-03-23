# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


# class Picking(models.Model):
#     _inherit = 'stock.quant'

#     @api.constrains('product_id', 'lot_id', 'location_id')
#     def check_product_lot(self):
#         for record in self:
#             if record.product_id and record.product_id.tracking and record.product_id.stock_quant_ids:
#                 for quant_id in record.product_id.stock_quant_ids:
#                     if quant_id.location_id == record.location_id and quant_id.lot_id != record.lot_id and quant_id.quantity > 0:
#                         raise ValidationError(_('Product already on this location with lot NO : %s',quant_id.lot_id.name))

#         return True

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        for record in self:
            if record.move_line_ids_without_package and record.picking_type_code == 'internal':
                for move in record.move_line_ids_without_package:
                    if move.product_id and move.product_id.tracking and move.product_id.stock_quant_ids:
                        for quant_id in move.product_id.stock_quant_ids:
                            if move.location_dest_id.name != 'Ongestickerd' and quant_id.location_id == move.location_dest_id and quant_id.lot_id != move.lot_id and quant_id.quantity > 0:
                                raise ValidationError(_('Product already on this location with lot NO : %s',quant_id.lot_id.name))
        return res
