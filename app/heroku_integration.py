import requests
import xmltodict

def create_heroku_subdomain(api_key, app_name, subdomain):
    headers = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': f'Bearer {api_key}',
    }

    payload = {
        'hostname': subdomain,
        'kind': 'custom',
    }

    # Creates subdomain
    response = requests.post(f'https://api.heroku.com/apps/{app_name}/domains', headers=headers, json=payload)

    if response.status_code == 201:
        return True
    else:
        # Handling API request failure
        print(f"Failed to create Heroku subdomain. Status code: {response.status_code}")
        print(response.text)
        return False

def acquire_cname(api_key, app_name):
    headers = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': f'Bearer {api_key}',
    }

    # Get the CNAME record
    response = requests.get(f'https://api.heroku.com/apps/{app_name}/domains', headers=headers)

    if response.status_code == 200:
        cname_records = response.json()
        return cname_records
    else:
        print(f"Failed to get Heroku CNAME record. Status code: {response.status_code}")
        print(response.text)
        return None

def create_and_assign_cname(api_user, api_key, user_name, client_ip, purchased_domain, heroku_subdomain, heroku_cname_target):
    api_url = f'https://api.namecheap.com/xml.response?ApiUser={api_user}&ApiKey={api_key}&UserName={user_name}&Command=namecheap.domains.dns.create&ClientIp={client_ip}&SLD={heroku_subdomain}&TLD={purchased_domain}&RecordType=CNAME&HostName={heroku_subdomain}&Address={heroku_cname_target}&TTL=1800'

    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            # Convert XML to JSON
            response_json = xmltodict.parse(response.text)

            # Checking if the CNAME creation was successful
            success = response_json.get('YourSuccessKey', {}).get('@Value', '').lower() == 'true'

            return success
        except Exception as e:
            # Handle conversion errors
            print(f"Failed to convert XML to JSON: {e}")
            return False
    else:
        # Handle API request failure
        print(f"API request failed with status code {response.status_code}")
        return False

def assign_cname_to_heroku(api_key, app_name, subdomain):
    headers = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': f'Bearer {api_key}',
    }

    # Get the CNAME record
    response = requests.get(f'https://api.heroku.com/apps/{app_name}/domains', headers=headers)

    if response.status_code == 200:
        cname_records = response.json()
        # Your logic to assign CNAME to Heroku goes here
    else:
        print(f"Failed to get Heroku CNAME record. Status code: {response.status_code}")
        print(response.text)
        return None


