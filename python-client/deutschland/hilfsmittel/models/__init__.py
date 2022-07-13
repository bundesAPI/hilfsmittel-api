# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.hilfsmittel.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.hilfsmittel.model.baum_knoten import BaumKnoten
from deutschland.hilfsmittel.model.detail_produkt import DetailProdukt
from deutschland.hilfsmittel.model.detail_produkt_all_of import DetailProduktAllOf
from deutschland.hilfsmittel.model.detail_produkt_all_of_kontruktionsmerkmale import (
    DetailProduktAllOfKontruktionsmerkmale,
)
from deutschland.hilfsmittel.model.nachweisschema import Nachweisschema
from deutschland.hilfsmittel.model.nachweisschema_nachweis_abschnitt_anforderungen_inner import (
    NachweisschemaNachweisAbschnittAnforderungenInner,
)
from deutschland.hilfsmittel.model.nachweisschema_nachweis_abschnitt_anforderungen_inner_abschnitt_anforderungen_inner import (
    NachweisschemaNachweisAbschnittAnforderungenInnerAbschnittAnforderungenInner,
)
from deutschland.hilfsmittel.model.nachweisschema_nachweisschema_kategorie_zuweisungen_inner import (
    NachweisschemaNachweisschemaKategorieZuweisungenInner,
)
from deutschland.hilfsmittel.model.produkt import Produkt
from deutschland.hilfsmittel.model.produktart import Produktart
from deutschland.hilfsmittel.model.produktgruppe import Produktgruppe
from deutschland.hilfsmittel.model.untergruppe import Untergruppe
