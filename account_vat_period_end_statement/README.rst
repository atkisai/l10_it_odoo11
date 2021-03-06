[![Build Status](https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/l10n-italy)
[![license lgpl](https://img.shields.io/badge/licence-LGPL--3-7379c3.svg)](https://www.gnu.org/licenses/lgpl.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/l10n-italy?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/l10n-italy/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/l10n-italy/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](https://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Period End VAT Statement
========================

This module helps to register the VAT statement of period end.


Installation
------------

Configuration
-------------

In order to generate VAT statement's periods,
open Accounting > Configuration > Accounting > Date range > Generate Date Ranges and select:

* Prefix: Prefix identiying the year of the periods to be generated
* Duration: 1 month
* Number of ranges to generate: 12
* Type: Create a type or use an existing one, no specific type's configuration is required
* Date start: first day of the period's year (for instance 01/01/2018)

In order to load the correct amount from tax, the tax has to be
associated to the account involved in the statement.
This configuration can be performed for each tax: open a tax in
Accounting > Configuration > Accounting > Taxes, then in the tab Advanced options
select the correct account (for instance the account debit VAT)
for the field 'Account used for VAT statement'.

If you need to calculate interest, you can add default information in your
company data (percentage and account), in the VAT statement tab.

Italian - Configurazione

Per generare i periodi della dichiarazione IVA,
aprire Contabilità > Configurazione > Contabilità > Intervalli date > Genera intervalli date.

* Prefisso: Prefisso identificativo dell'anno dei periodi da generare
* Durata: 1 mese
* Numero di intervalli da generare: 12
* Tipo: Creare un tipo o utilizzarne uno esistente, non è richiesta una configurazione perticolare per il tipo
* Data di inizio: primo giorno dell'anno dei periodi da generare (ad esempio 01/01/2018)

Per caricare l'importo corretto, una tassa deve essere associata al conto utilizzato nella liquidazione.
Questa configurazione può essere fatta per ogni tassa:
aprire la tassa da Contabilità > Configurazione > Contabilità > Imposte,
quindi nel tab 'Impostazioni avanzate' selezionare il conto corretto (ad esempio IVA debito)
per il campo 'Conto utilizzato per la liquidazione IVA'.

Per calcolare gli interessi, è possibile aggiungere le informazioni da utilizzare (conto e percentuale)
nei dati aziendali, nel tab Liquidazione IVA.

Usage
-----

=====

In order to create a 'VAT Statement', open Accounting > Adviser > VAT Statements.
Select a Journal that will contain the journal entries of the statement.
The field Tax authority VAT account contains the account where the statement balance will be registered.

The 'VAT statement' object allows to specify every amount and relative account
used by the statement.
By default, amounts of debit and credit taxes are automatically loaded
from taxes of the selected periods (see Configuration to correctly generate the periods).
Previous debit or credit is loaded from previous VAT statement, according
to its payments status.

In order to generate the journal entry, click on 'Create move' button, inside the 'Accounts' tab.
If you select a payment term, the due date(s) will be set.

The 'tax authority' tab contains information about payment(s),
here you can see statement's result ('authority VAT amount') and residual
amount to pay ('Balance').
The statement can be paid like every other debit, by journal item
reconciliation.

It is also possible to print the 'VAT statement' clicking on print > Print VAT period end statement.

Italian - Utilizzo

Per fare la liquidazione IVA, aprire Contabilità > Contabilità > Liquidazioni IVA.
Selezionare un sezionale che conterrà le registrazioni contabili della liquidazione.
Il campo Conto IVA Erario contiene il conto dove verrà effettuata la registrazione della liquidazione IVA.

L'oggetto 'Liquidazione IVA' permette di specificare ogni importo e il conto utilizzato dalla liquidazione.
Di norma, gli importi di debito e credito delle tasse vengono caricati automaticamente dai periodi selezionati
(vedere Configurazione per generare correttamente i periodi).
I debiti e crediti precedenti vengono caricati dalle liquidazioni IVA precedenti, in base allo stato del loro pagamento.

Per creare la registrazione contabile, cliccare sul bottone 'Crea movimento', dentro il tab 'Conti'.
Se i termini di pagamento sono impostati viene scritta anche la scadenza (o le scadenze).

Il tab 'Erario' contiene informazioni sui pagamenti,
qui si possono visualizzare i risultati della liquidazione ('Importo IVA erario')
e l'importo residuo da pagare ('Importo a saldo').
La liquidazione può essere pagata come qualunque altro debito, con la riconciliazione delle registrazioni contabili.

È inoltre possibile stampare la liquidazione IVA cliccando su Stampa > Stampa liquidazione IVA.

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Credits
-------

### Contributors

* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Elena Carlesso <ecarlesso@linkgroup.it>
* Marco Marchiori <marcomarkiori@gmail.com>
* Sergio Corato <sergiocorato@gmail.com>
* Andrea Gallina <a.gallina@apuliasoftware.it>
* Alex Comba <alex.comba@agilebg.com>
* Alessandro Camilli <camillialex@gmail.com>
* Simone Rubino <simone.rubino@agilebg.com>

Do not contact contributors directly about support or help with technical issues.

### Funders

### Maintainer

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
[Zeroincombenze® distribution of Odoo](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Users can download from [Zeroincombenze® distribution](https://github.com/zeroincombenze/OCB) and deploy on local server.

[//]: # (end copyright)





[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
