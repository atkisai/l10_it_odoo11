#
# Copyright 2014    Associazione Odoo Italia (<https://www.odoo-italia.org>)
# Copyright 2015    Alessio Gerace <alessio.gerace@agilebg.com>
# Copyright 2016    Andrea Gallina (Apulia Software)
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    rea_office = fields.Many2one(
        'res.country.state', string='Office Province')
    rea_code = fields.Char('REA Code', size=20)
    rea_capital = fields.Float('Capital')
    rea_member_type = fields.Selection(
        [('SU', 'Unique Member'),
         ('SM', 'Multiple Members')], 'Member Type')
    rea_liquidation_state = fields.Selection(
        [('LS', 'In liquidation'),
         ('LN', 'Active')], 'Liquidation State')

    _sql_constraints = [
        ('rea_code_uniq', 'unique (rea_code, company_id)',
         'The rea code code must be unique per company !'),
    ]
