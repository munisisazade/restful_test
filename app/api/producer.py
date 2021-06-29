import json
import requests
import random
from flask import Blueprint, request, jsonify, Response

micro_api = Blueprint('micro_api', __name__)


@micro_api.route('/api/v1/rest/body', methods=['POST'])
def rest_body_example():
    data = request.data
    name = data["name"]
    surname = data["surname"]
    req = requests.get("https://cat-fact.herokuapp.com/facts/random")
    response = req.json()
    return {
        "data": response["text"]
    }


@micro_api.route('/api/v1/babat/service/<id>', methods=['POST'])
def rest_babat_service(id):
    body = str(request.data)
    query_parameter = str(request.args)
    path_parameter = id
    headers = str(request.headers)
    resp = Response(response=json.dumps({
        "body": body,
        "path_parameter": path_parameter,
        "headers": headers,
        "query_parameter": query_parameter
    }), mimetype='application/json')
    resp.headers['Header1'] = request.headers.get('Header1')
    resp.headers['Header2'] = request.headers.get('Header2')
    return resp


@micro_api.route('/api/v1/getCertificatesByPin', methods=['GET'])
def get_certificates_by_pin():
    code = request.args.get('code')
    if code == 'GX9ZZvd':
        return {
            "Status": 200,
            "Description": "OK",
            "Exception": None,
            "Timestamp": "2021-04-29 07:27:05",
            "Data": {
                "DataVals": [
                    {
                        "name": "SDASDA",
                        "surname": "DFGDFG",
                        "patronymic": "ASDAGSDF",
                    }
                ]
            }
        }
    elif len(code) != 7:
        return {
            "Status": 400,
            "Description": "BadRequest",
            "Exception": {
                "Code": 4000,
                "Message": "Code have 7 symbols"
            },
            "Timestamp": "2021-04-29 07:28:28",
            "Data": {
                "DataVals": None
            }
        }
    else:
        return {
            "Status": 400,
            "Description": "BadRequest",
            "Exception": {
                "Code": 5000,
                "Message": "Data not found"
            },
            "Timestamp": "2021-04-29 07:29:06",
            "Data": {
                "DataVals": None
            }
        }


@micro_api.route('/api/v1/getActiveContractsDetailByPin', methods=['POST'])
def rest_labor_contracts():
    body = request.data
    headers = request.headers
    pin = body.get("SEARCH_PIN", False)
    key = headers.get('Key')
    if key:
        if key != '758gf9hjdx9024ftg':
            return {
                "status": {
                    "code": 301,
                    "description": "Autentifikasiya xətası.",
                    "exception": None,
                    "transaction": None,
                    "timeStamp": "2021-03-15T16:46:15.8135075+04:00",
                    "requestDuration": 0
                },
                "data": None
            }

    if pin:
        if pin == "F9738SA":
            return {
                "status": {
                    "code": 200,
                    "description": "Uğurlu.",
                    "exception": None,
                    "transaction": "BD92AD6D3D8EA567E05302131DACAEB0",
                    "timeStamp": "2021-03-15T16:44:29.9587069+04:00",
                    "requestDuration": 1278.9898
                },
                'data': [{
                    'name': 'SUCCESS'
                }]
            }
        else:
            return {
                "status": {
                    "code": 201,
                    "description": "Uğurlu (nəticə tapılmadı).",
                    "exception": None,
                    "transaction": "BD92AD6D3D8FA567E05302131DACAEB0",
                    "timeStamp": "2021-03-15T16:45:28.8735055+04:00",
                    "requestDuration": 140.6385
                },
                "data": []
            }
    else:
        return {
            "status": {
                "code": 400,
                "description": "Kontent xətası.",
                "exception": None,
                "transaction": "BD92AD6D3D86A567E05302131DACAEB0",
                "timeStamp": "2021-03-15T16:26:32.1502693+04:00",
                "requestDuration": 0
            },
            'data': []
        }


@micro_api.route('/api/v1/header/example', methods=['GET'])
def rest_header_checker():
    return {
        "header": str(request.headers)
    }


@micro_api.route('/api/v1/body/example', methods=['POST'])
def rest_body_checker():
    return {
        "request_data": str(request.data)
    }


@micro_api.route('/api/v1/array/response', methods=['GET'])
def array_response_example():
    if request.headers.get('Authorization', None) == 'Basic YWdyYXJfc2lnb3J0YTphZ3Jhcl9zaWdvcnRhXyQuITIwMjA=':
        return [
            {
                "nickName": "Qırnızı",
                "registryNo": "759691",
                "birthDate": "2014-06-27T04:00:00.000+00:00",
                "animalGender": "DİŞİ",
                "animalHistory": [
                    {
                        "id": 143931,
                        "date": "2020-06-28T01:39:17.877+00:00",
                        "animalStatus": {
                            "id": 8,
                            "name": "SMM-ə müraciət edildi"
                        }
                    },
                    {
                        "id": 249011,
                        "date": "2020-10-28T20:22:01.540+00:00",
                        "animalStatus": {
                            "id": 8,
                            "name": "SMM-ə müraciət edildi"
                        }
                    }
                ],
                "animalOriginType": {
                    "id": 2,
                    "name": "Təbii mayalanma"
                },
                "animalSort": {
                    "id": 7,
                    "name": "Təyin edilməyib"
                },
                "animalType": {
                    "id": 1,
                    "name": "İnək"
                },
                "animalCategory": {
                    "id": 1,
                    "name": "İribuynuzlu"
                },
                "id": 143120
            },
            {
                "nickName": "Buzov_144245",
                "registryNo": "70183",
                "birthDate": "2020-06-16T04:00:00.000+00:00",
                "animalGender": "ERKƏK",
                "animalHistory": [
                    {
                        "id": 145204,
                        "date": "2020-06-29T19:37:08.097+00:00",
                        "animalStatus": {
                            "id": 7,
                            "name": "Baytara müraciət edildi"
                        }
                    }
                ],
                "animalOriginType": {
                    "id": 2,
                    "name": "Təbii mayalanma"
                },
                "animalSort": {
                    "id": 7,
                    "name": "Təyin edilməyib"
                },
                "animalType": {
                    "id": 1,
                    "name": "İnək"
                },
                "animalCategory": {
                    "id": 1,
                    "name": "İribuynuzlu"
                },
                "id": 144245
            }
        ]
    else:
        return {
                   "error": "Token verification failed"
               }, 403


@micro_api.route('/api/v1/example/get', methods=['GET'])
def default_get():
    return jsonify({
        "data": [{
            "type": "articles",
            "id": "1",
            "attributes": {
                "title": "Json api for testing",
                "body": "The shortest article. Ever.",
                "created": "2015-05-22T14:56:29.000Z",
                "updated": "2015-05-22T14:56:28.000Z"
            },
            "relationships": {
                "author": {
                    "data": {"id": "42", "type": "people"}
                }
            }
        }]
    })


@micro_api.route('/api/v1/info/test/rest/<pin>', methods=['GET'])
def info_api_get(pin):
    if not "Authorization" in request.headers:
        return jsonify({
            "error": "Authorization required"
        }), 403
    if not pin or pin == "":
        jsonify({
            "error": "Pin not found !!!"
        }), 404
    if request.headers["Authorization"] == "Token testing12345":
        return jsonify({
            "data": {
                "pin": pin
            }
        })
    return jsonify({
        "error": "Authorization required"
    }), 403


@micro_api.route('/api/v1/example2/<id>', methods=['GET'])
def example_two_get(id):
    if not id or id == "":
        return jsonify({
            "error": "Id not found !!!"
        }), 404

    return jsonify({
        "data": [{
            "type": "example 2 api",
            "id": f"{id}",
            "custom": {
                "title": "Json api for testing",
                "body": "The shortest article. Ever.",
                "userId": 1,
            }
        }]
    })


@micro_api.route('/api/v1/swagger/example1', methods=['GET'])
def besit_example1():
    return jsonify([
        {
            "key": "value",
            "object": {
                "v": "b"
            },
            "array": [
                {
                    "name": "value"
                }
            ]
        }
    ])


@micro_api.route('/api/v1/swagger/example2', methods=['GET'])
def besit_example2():
    return jsonify({
        'a': [{'a1': 'x'}],
        'b': {
            'b1': [{'b11': 'value'}]
        }
    })


@micro_api.route('/api/v1/example3/<id>', methods=['GET'])
def example_three(id):
    if not "Authorization" in request.headers:
        return jsonify({
            "error": "Authorization required"
        }), 403

    if not id or id == "":
        return jsonify({
            "error": "Id not found !!!"
        }), 404

    if request.headers["Authorization"] == "Token testing12345":
        return jsonify({
            "problems": [{
                "Diabetes": [{
                    "medications": [{
                        "medicationsClasses": [{
                            "className": [{
                                "associatedDrug": [{
                                    "name": "asprin",
                                    "dose": "",
                                    "strength": "500 mg"
                                }],
                                "associatedDrug#2": [{
                                    "name": "somethingElse",
                                    "dose": "",
                                    "strength": "500 mg"
                                }]
                            }],
                            "className2": [{
                                "associatedDrug": [{
                                    "name": "asprin",
                                    "dose": "",
                                    "strength": "500 mg"
                                }],
                                "associatedDrug#2": [{
                                    "name": "somethingElse",
                                    "dose": "",
                                    "strength": "500 mg"
                                }]
                            }]
                        }]
                    }],
                    "labs": [{
                        "missing_field": "missing_value"
                    }]
                }],
                "Asthma": [{}]
            }]})
    else:
        return jsonify({
            "problems": [{
                "Diabetes": [{
                    "medications": [{
                        "Error": [{"msg": "Token is invalid"}]
                    }]
                }],
                "labs": [{
                    "missing_field": "missing_value"
                }]
            }],
            "Asthma": [{}]
        }), 401


@micro_api.route('/api/v1/example4', methods=['POST'])
def example_four():
    return jsonify({
        "medications": [{
            "aceInhibitors": [{
                "name": "lisinopril",
                "strength": "10 mg Tab",
                "dose": "1 tab",
                "route": "PO",
                "sig": "daily",
                "pillCount": "#90",
                "refills": "Refill 3"
            }],
            "antianginal": [{
                "name": "nitroglycerin",
                "strength": "0.4 mg Sublingual Tab",
                "dose": "1 tab",
                "route": "SL",
                "sig": "q15min PRN",
                "pillCount": "#30",
                "refills": "Refill 1"
            }],
            "anticoagulants": [{
                "name": "warfarin sodium",
                "strength": "3 mg Tab",
                "dose": "1 tab",
                "route": "PO",
                "sig": "daily",
                "pillCount": "#90",
                "refills": "Refill 3"
            }],
            "betaBlocker": [{
                "name": "metoprolol tartrate",
                "strength": "25 mg Tab",
                "dose": "1 tab",
                "route": "PO",
                "sig": "daily",
                "pillCount": "#90",
                "refills": "Refill 3"
            }],
            "diuretic": [{
                "name": "furosemide",
                "strength": "40 mg Tab",
                "dose": "1 tab",
                "route": "PO",
                "sig": "daily",
                "pillCount": "#90",
                "refills": "Refill 3"
            }],
            "mineral": [{
                "name": "potassium chloride ER",
                "strength": "10 mEq Tab",
                "dose": "1 tab",
                "route": "PO",
                "sig": "daily",
                "pillCount": "#90",
                "refills": "Refill 3"
            }]
        }
        ],
        "labs": [{
            "name": "Arterial Blood Gas",
            "time": "Today",
            "location": "Main Hospital Lab"
        },
            {
                "name": "BMP",
                "time": "Today",
                "location": "Primary Care Clinic"
            },
            {
                "name": "BNP",
                "time": "3 Weeks",
                "location": "Primary Care Clinic"
            },
            {
                "name": "BUN",
                "time": "1 Year",
                "location": "Primary Care Clinic"
            },
            {
                "name": "Cardiac Enzymes",
                "time": "Today",
                "location": "Primary Care Clinic"
            },
            {
                "name": "CBC",
                "time": "1 Year",
                "location": "Primary Care Clinic"
            },
            {
                "name": "Creatinine",
                "time": "1 Year",
                "location": "Main Hospital Lab"
            },
            {
                "name": "Electrolyte Panel",
                "time": "1 Year",
                "location": "Primary Care Clinic"
            },
            {
                "name": "Glucose",
                "time": "1 Year",
                "location": "Main Hospital Lab"
            },
            {
                "name": "PT/INR",
                "time": "3 Weeks",
                "location": "Primary Care Clinic"
            },
            {
                "name": "PTT",
                "time": "3 Weeks",
                "location": "Coumadin Clinic"
            },
            {
                "name": "TSH",
                "time": "1 Year",
                "location": "Primary Care Clinic"
            }
        ],
        "imaging": [{
            "name": "Chest X-Ray",
            "time": "Today",
            "location": "Main Hospital Radiology"
        },
            {
                "name": "Chest X-Ray",
                "time": "Today",
                "location": "Main Hospital Radiology"
            },
            {
                "name": "Chest X-Ray",
                "time": "Today",
                "location": "Main Hospital Radiology"
            }
        ]
    })


@micro_api.route('/api/v1/example5/header', methods=['POST'])
def example_five():
    pass

@micro_api.route('/api/v1/fake/json', methods=['GET'])
def fake_json_response():
    data = "{\"title\":\"Internal Server Error\",\"detail\":\"\\n### Error updating database.  Cause: java.sql.SQLIntegrityConstraintViolationException: ORA-00001: unique constraint (SYSTEM.JOY_INFO_LOG_REQUEST_ID_IDX) violated\\n\\n### The error may exist in az/com/cybernet/integ/domain/mapper/permit/JoyInfoMapper.java (best guess)\\n### The error may involve az.com.cybernet.integ.domain.mapper.permit.JoyInfoMapper.insertJoyInfoLog-Inline\\n### The error occurred while setting parameters\\n### SQL: INSERT INTO WS.JOY_INFO_LOG (OID, INSERT_TIME, REQUEST_ID, INFO_COUNT) VALUES(?, TO_CHAR(SYSDATE, 'yyyymmddhh24miss'), ?, ?)\\n### Cause: java.sql.SQLIntegrityConstraintViolationException: ORA-00001: unique constraint (SYSTEM.JOY_INFO_LOG_REQUEST_ID_IDX) violated\\n\\n; ORA-00001: unique constraint (SYSTEM.JOY_INFO_LOG_REQUEST_ID_IDX) violated\\n; nested exception is java.sql.SQLIntegrityConstraintViolationException: ORA-00001: unique constraint (SYSTEM.JOY_INFO_LOG_REQUEST_ID_IDX) violated\\n\",\"status\":500,\"invalidParams\":[],\"traceId\":\"a002ce598951\"}"
    return Response(response=data, mimetype="text/plain"), 400


@micro_api.route('/api/v1/soap/example.asmx', methods=['GET', 'POST'])
def example_soap_service():
    if request.method == "GET":
        return Response(response="""<?xml version="1.0" encoding="utf-8"?>
<wsdl:definitions xmlns:s="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:tns="http://tempuri.org/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" targetNamespace="http://tempuri.org/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
  <wsdl:types>
    <s:schema elementFormDefault="qualified" targetNamespace="http://tempuri.org/">
      <s:element name="GetAppinfoByPIN">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="RequestKey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="PIN" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetAppinfoByPINResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="GetAppinfoByPINResult" type="tns:Response" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="Response">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="1" name="Status" type="tns:Status" />
          <s:element minOccurs="0" maxOccurs="1" name="Applications" type="tns:ArrayOfItem" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="Status">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Code" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="Description" type="s:string" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="ArrayOfItem">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="unbounded" name="Item" nillable="true" type="tns:Item" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="Item">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="1" name="PIN" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="Fullname" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="DecisionNumber" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="DecisionDate" nillable="true" type="s:dateTime" />
          <s:element minOccurs="0" maxOccurs="1" name="ICertificateNumber" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="TCertificateNumber" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="ECertificateNumber" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="CountryCode" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="CountryName" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="UniversitetCode" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="UniversitetName" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="EducationLevel" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="EducationLevelName" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="SpecialtyCode" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="SpecialtyName" type="s:string" />
        </s:sequence>
      </s:complexType>
      <s:element name="GetAppinfoByFullname">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="RequestKey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="Surname" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="Name" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="Patronymic" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="BirthDate" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetAppinfoByFullnameResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="GetAppinfoByFullnameResult" type="tns:Response" />
          </s:sequence>
        </s:complexType>
      </s:element>
    </s:schema>
  </wsdl:types>
  <wsdl:message name="GetAppinfoByPINSoapIn">
    <wsdl:part name="parameters" element="tns:GetAppinfoByPIN" />
  </wsdl:message>
  <wsdl:message name="GetAppinfoByPINSoapOut">
    <wsdl:part name="parameters" element="tns:GetAppinfoByPINResponse" />
  </wsdl:message>
  <wsdl:message name="GetAppinfoByFullnameSoapIn">
    <wsdl:part name="parameters" element="tns:GetAppinfoByFullname" />
  </wsdl:message>
  <wsdl:message name="GetAppinfoByFullnameSoapOut">
    <wsdl:part name="parameters" element="tns:GetAppinfoByFullnameResponse" />
  </wsdl:message>
  <wsdl:portType name="IntegrationsSoap">
    <wsdl:operation name="GetAppinfoByPIN">
      <wsdl:input message="tns:GetAppinfoByPINSoapIn" />
      <wsdl:output message="tns:GetAppinfoByPINSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetAppinfoByFullname">
      <wsdl:input message="tns:GetAppinfoByFullnameSoapIn" />
      <wsdl:output message="tns:GetAppinfoByFullnameSoapOut" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="IntegrationsSoap" type="tns:IntegrationsSoap">
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />
    <wsdl:operation name="GetAppinfoByPIN">
      <soap:operation soapAction="http://tempuri.org/GetAppinfoByPIN" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetAppinfoByFullname">
      <soap:operation soapAction="http://tempuri.org/GetAppinfoByFullname" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:binding name="IntegrationsSoap12" type="tns:IntegrationsSoap">
    <soap12:binding transport="http://schemas.xmlsoap.org/soap/http" />
    <wsdl:operation name="GetAppinfoByPIN">
      <soap12:operation soapAction="http://tempuri.org/GetAppinfoByPIN" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetAppinfoByFullname">
      <soap12:operation soapAction="http://tempuri.org/GetAppinfoByFullname" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="Integrations">
    <wsdl:port name="IntegrationsSoap" binding="tns:IntegrationsSoap">
      <soap:address location="https://rest.mpy.az/api/v1/soap/example.asmx" />
    </wsdl:port>
    <wsdl:port name="IntegrationsSoap12" binding="tns:IntegrationsSoap12">
      <soap12:address location="https://rest.mpy.az/api/v1/soap/example.asmx" />
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>""", mimetype="text/xml")
    else:
        if random.randint(0, 1):
            return Response(response="""<?xml version="1.0" encoding="UTF-8"?>
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
                <soapenv:Header/>
                <soapenv:Body>
                   <GetAppinfoByPINResult>
                      <Status>
                         <Code>402</Code>
                         <Description>fdgdfgfdgdfgdf</Description>
                      </Status>
                   </GetAppinfoByPINResult>
                   </soapenv:Body>
                </soapenv:Envelope>""", mimetype="text/xml")
        else:
            return Response(response="""<?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Header/>
    <soapenv:Body>
       <GetAppinfoByPINResult>
          <Applications>
             <Item>
                <element>
                   <CountryCode>99</CountryCode>
                   <CountryName>dfhdsf df hgdfhfh</CountryName>
                   <DecisionDate>2020-11-06T00:00:00.000Z</DecisionDate>
                   <DecisionNumber>23-23-364</DecisionNumber>
                   <EducationLevel>10</EducationLevel>
                   <EducationLevelName>Bakalavriat</EducationLevelName>
                   <Fullname>dfg sdgfdfsgfgdsfg</Fullname>
                   <ICertificateNumber>sdfsdf</ICertificateNumber>
                   <PIN>asfdsdfsdf</PIN>
                   <SpecialtyCode>sdfsdf</SpecialtyCode>
                   <SpecialtyName>Menecment</SpecialtyName>
                   <TCertificateNumber>sdfsdf</TCertificateNumber>
                   <UniversitetCode>sdfsdf</UniversitetCode>
                   <UniversitetName>Ardahan sdfsdf</UniversitetName>
                </element>
             </Item>
          </Applications>
          <Status>
             <Code>200</Code>
             <Description>Uğurlu.</Description>
          </Status>
       </GetAppinfoByPINResult>
       </soapenv:Body>
    </soapenv:Envelope>""", mimetype="text/xml")


