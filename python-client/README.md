# hilfsmittel
Der GKV-Spitzenverbund führt ein Register über alle Hilfsmittel, die der Leistungspflicht der Kassen unterliegen. Struktur: Produktgruppe -> Anwendungsort -> Untergruppe -> Produktart -> Produkt

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

```sh
pip install deutschland[hilfsmittel]
```

### poetry install

```sh
poetry add deutschland -E hilfsmittel
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Usage

Import the package:
```python
from deutschland import hilfsmittel
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
from deutschland import hilfsmittel
from pprint import pprint
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.baum_knoten import BaumKnoten
from deutschland.hilfsmittel.model.detail_produkt import DetailProdukt
from deutschland.hilfsmittel.model.nachweisschema import Nachweisschema
from deutschland.hilfsmittel.model.produkt import Produkt
from deutschland.hilfsmittel.model.produktart import Produktart
from deutschland.hilfsmittel.model.produktgruppe import Produktgruppe
from deutschland.hilfsmittel.model.untergruppe import Untergruppe
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)



# Enter a context with an instance of the API client
with hilfsmittel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    try:
        # Details zu einem Nachweisschema abfragen
        api_response = api_instance.nachweisschema_id_get(id)
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->nachweisschema_id_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**nachweisschema_id_get**](docs/DefaultApi.md#nachweisschema_id_get) | **GET** /Nachweisschema/{id} | Details zu einem Nachweisschema abfragen
*DefaultApi* | [**produkt_get**](docs/DefaultApi.md#produkt_get) | **GET** /Produkt | Kompaktliste aller Produkte
*DefaultApi* | [**produkt_id_get**](docs/DefaultApi.md#produkt_id_get) | **GET** /Produkt/{id} | Details zu einem Produkt abfragen
*DefaultApi* | [**produktart_id_get**](docs/DefaultApi.md#produktart_id_get) | **GET** /Produktart/{id} | Details zu einer Produktart abfragen
*DefaultApi* | [**produktgruppe_id_get**](docs/DefaultApi.md#produktgruppe_id_get) | **GET** /Produktgruppe/{id} | Details zu einer Produktgruppe abfragen
*DefaultApi* | [**untergruppe_id_get**](docs/DefaultApi.md#untergruppe_id_get) | **GET** /Untergruppe/{id} | Details zu einer Untergruppe abfragen
*DefaultApi* | [**verzeichnis_tree_level_get**](docs/DefaultApi.md#verzeichnis_tree_level_get) | **GET** /VerzeichnisTree/{level} | Lädt alle Knoten im Produktbaum bis zum gegebenen Level.


## Documentation For Models

 - [BaumKnoten](docs/BaumKnoten.md)
 - [DetailProdukt](docs/DetailProdukt.md)
 - [DetailProduktAllOf](docs/DetailProduktAllOf.md)
 - [DetailProduktAllOfKontruktionsmerkmale](docs/DetailProduktAllOfKontruktionsmerkmale.md)
 - [Nachweisschema](docs/Nachweisschema.md)
 - [NachweisschemaNachweisAbschnittAnforderungenInner](docs/NachweisschemaNachweisAbschnittAnforderungenInner.md)
 - [NachweisschemaNachweisAbschnittAnforderungenInnerAbschnittAnforderungenInner](docs/NachweisschemaNachweisAbschnittAnforderungenInnerAbschnittAnforderungenInner.md)
 - [NachweisschemaNachweisschemaKategorieZuweisungenInner](docs/NachweisschemaNachweisschemaKategorieZuweisungenInner.md)
 - [Produkt](docs/Produkt.md)
 - [Produktart](docs/Produktart.md)
 - [Produktgruppe](docs/Produktgruppe.md)
 - [Untergruppe](docs/Untergruppe.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

kontakt@bund.dev


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in hilfsmittel.apis and hilfsmittel.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from deutschland.hilfsmittel.api.default_api import DefaultApi`
- `from deutschland.hilfsmittel.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
from deutschland import hilfsmittel
from deutschland.hilfsmittel.apis import *
from deutschland.hilfsmittel.models import *
```

