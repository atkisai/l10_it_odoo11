# -*- coding: utf-8 -*-
#
# Copyright 2015    - AgileBG SAGL <http://www.agilebg.com>
# Copyright 2015    - innoviu Srl <http://www.innoviu.com>
# Copyright 2018    - Lorenzo Battistini
# Copyright 2018    - Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# Copyright 2018-19 - Odoo Italia Associazione <https://www.odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
{
    'name': 'Italian Localization - Fattura elettronica - Ricezione',
    'version': '10.0.1.3.0',
    'category': 'Localization/Italy',
    'summary': 'Ricezione fatture elettroniche',
    'author': 'Agile Business Group, Innoviu, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/l10n-italy/tree/10.0/'
               'l10n_it_fatturapa_in',
    'license': 'LGPL-3',
    "depends": [
        'l10n_it_einvoice_base',
        'l10n_it_fiscal_ipa',
        'l10n_it_causali_pagamento',
        'l10n_it_withholding_tax_causali',
    ],
    "data": [
        'views/account_view.xml',
        'views/partner_view.xml',
        'wizard/wizard_import_fatturapa_view.xml',
        'security/ir.model.access.csv',
        'wizard/link_to_existing_invoice.xml',
        # 'views/company_view.xml',
    ],
    "installable": True
}
