# hilfsmittel.DefaultApi

All URIs are relative to *https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nachweisschema_id_get**](DefaultApi.md#nachweisschema_id_get) | **GET** /Nachweisschema/{id} | Details zu einem Nachweisschema abfragen
[**produkt_get**](DefaultApi.md#produkt_get) | **GET** /Produkt | Kompaktliste aller Produkte
[**produkt_id_get**](DefaultApi.md#produkt_id_get) | **GET** /Produkt/{id} | Details zu einem Produkt abfragen
[**produktart_id_get**](DefaultApi.md#produktart_id_get) | **GET** /Produktart/{id} | Details zu einer Produktart abfragen
[**produktgruppe_id_get**](DefaultApi.md#produktgruppe_id_get) | **GET** /Produktgruppe/{id} | Details zu einer Produktgruppe abfragen
[**untergruppe_id_get**](DefaultApi.md#untergruppe_id_get) | **GET** /Untergruppe/{id} | Details zu einer Untergruppe abfragen
[**verzeichnis_tree_level_get**](DefaultApi.md#verzeichnis_tree_level_get) | **GET** /VerzeichnisTree/{level} | Lädt alle Knoten im Produktbaum bis zum gegebenen Level.


# **nachweisschema_id_get**
> Nachweisschema nachweisschema_id_get(id)

Details zu einem Nachweisschema abfragen

### Example


```python
import time
from deutschland import hilfsmittel
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.nachweisschema import Nachweisschema
from pprint import pprint
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)


# Enter a context with an instance of the API client
with hilfsmittel.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einem Nachweisschema abfragen
        api_response = api_instance.nachweisschema_id_get(id)
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->nachweisschema_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Nachweisschema**](Nachweisschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailinformationen zu einem Nachweisschema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **produkt_get**
> [Produkt] produkt_get()

Kompaktliste aller Produkte

Achtung, Rückgabe ist relativ groß (über 30MB).

### Example


```python
import time
from deutschland import hilfsmittel
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.produkt import Produkt
from pprint import pprint
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)


# Enter a context with an instance of the API client
with hilfsmittel.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Kompaktliste aller Produkte
        api_response = api_instance.produkt_get()
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->produkt_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Produkt]**](Produkt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kompaktliste aller Produkte |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **produkt_id_get**
> DetailProdukt produkt_id_get(id)

Details zu einem Produkt abfragen

### Example


```python
import time
from deutschland import hilfsmittel
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.detail_produkt import DetailProdukt
from pprint import pprint
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)


# Enter a context with an instance of the API client
with hilfsmittel.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einem Produkt abfragen
        api_response = api_instance.produkt_id_get(id)
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->produkt_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DetailProdukt**](DetailProdukt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailinformationen zu einem Produkt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **produktart_id_get**
> Produktart produktart_id_get(id)

Details zu einer Produktart abfragen

### Example


```python
import time
from deutschland import hilfsmittel
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.produktart import Produktart
from pprint import pprint
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)


# Enter a context with an instance of the API client
with hilfsmittel.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einer Produktart abfragen
        api_response = api_instance.produktart_id_get(id)
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->produktart_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Produktart**](Produktart.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailinformationen zu einer Produktart |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **produktgruppe_id_get**
> Produktgruppe produktgruppe_id_get(id)

Details zu einer Produktgruppe abfragen

### Example


```python
import time
from deutschland import hilfsmittel
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.produktgruppe import Produktgruppe
from pprint import pprint
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)


# Enter a context with an instance of the API client
with hilfsmittel.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einer Produktgruppe abfragen
        api_response = api_instance.produktgruppe_id_get(id)
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->produktgruppe_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Produktgruppe**](Produktgruppe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailinformationen zu einer Produktgruppe |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **untergruppe_id_get**
> Untergruppe untergruppe_id_get(id)

Details zu einer Untergruppe abfragen

### Example


```python
import time
from deutschland import hilfsmittel
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.untergruppe import Untergruppe
from pprint import pprint
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)


# Enter a context with an instance of the API client
with hilfsmittel.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einer Untergruppe abfragen
        api_response = api_instance.untergruppe_id_get(id)
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->untergruppe_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Untergruppe**](Untergruppe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailinformationen zu einer Untergruppe |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verzeichnis_tree_level_get**
> BaumKnoten verzeichnis_tree_level_get(level)

Lädt alle Knoten im Produktbaum bis zum gegebenen Level.

### Example


```python
import time
from deutschland import hilfsmittel
from deutschland.hilfsmittel.api import default_api
from deutschland.hilfsmittel.model.baum_knoten import BaumKnoten
from pprint import pprint
# Defining the host is optional and defaults to https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis
# See configuration.py for a list of all supported configuration parameters.
configuration = hilfsmittel.Configuration(
    host = "https://hilfsmittel-api.gkv-spitzenverband.de/api/verzeichnis"
)


# Enter a context with an instance of the API client
with hilfsmittel.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    level = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Lädt alle Knoten im Produktbaum bis zum gegebenen Level.
        api_response = api_instance.verzeichnis_tree_level_get(level)
        pprint(api_response)
    except hilfsmittel.ApiException as e:
        print("Exception when calling DefaultApi->verzeichnis_tree_level_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **int**|  |

### Return type

[**BaumKnoten**](BaumKnoten.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Liste an Knoten aus dem Produktbaum |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

