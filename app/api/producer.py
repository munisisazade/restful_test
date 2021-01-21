import requests
from flask import Blueprint, request, jsonify

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

@micro_api.route('/api/v1/header/example', methods=['GET'])
def rest_header_checker():
    return {
        "header": request.headers
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
