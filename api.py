from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

req_url = 'https://api.mbpj.gov.my/eservices/aduan/get?'


@app.route('/api', methods=['GET'])
@app.route('/<token>/api', methods=['GET'])
def api(token=None):
    if request.method == 'GET':
        # Get rid parameter (REQUIRED)
        rid = request.values.get('rid')
        mbpj_token = str(token)

        headers = {
            'mbpj-clientid': 'Aduan23Dev',
            'mbpj-token': mbpj_token
        }
        # Optional parameters
        year = request.values.get('year')
        month = request.values.get('month')

        if not rid:
            # Return error if user not specify any Rid parameter
            return jsonify({'error': 'Please specify Rid parameter (REQUIRED)'})

        if not token:
            # Return error if user not specify mbpj_token
            return jsonify({'error': 'Please specify Token in Url (REQUIRED)'})

        params = {'rid': rid}

        if year:
            params['year'] = year
        if month:
            params['month'] = month

        response = requests.get(
            url=req_url,
            headers=headers,
            params=params
        )

        get_response = response.json()

        if 'data' in get_response and len(get_response['data']) > 0:
            # Check if response only has one row (only count)
            if len(get_response['data']) == 1 and len(get_response['data'][0]) == 1:
                # Get only count data
                get_count = {'COUNT': get_response['data'][0]['COUNT']}
                return jsonify(get_count)
            else:
                # Remove title
                get_response.pop('title', None)
                return jsonify(get_response)
        else:
            # Return default error if mbpj-token is invalid or no data found
            return jsonify(get_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60015, debug=True)


