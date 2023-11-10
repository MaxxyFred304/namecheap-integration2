import requests
import xmltodict

def create_namecheap_cname(api_user, api_key, user_name, client_ip, domain, subdomain, target):
    api_url = f'https://api.sandbox.namecheap.com/xml.response?ApiUser={api_user}&ApiKey={api_key}&UserName={user_name}&Command=namecheap.domains.dns.create&ClientIp={client_ip}&SLD={subdomain}&TLD={domain}&RecordType=CNAME&HostName={subdomain}&Address={target}&TTL=1800'

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

def create_and_assign_cname(api_user, api_key, user_name, client_ip, purchased_domain, heroku_subdomain, heroku_cname_target):
    # Your existing code for Namecheap API
    namecheap_api_url = f'https://api.sandbox.namecheap.com/xml.response?ApiUser={api_user}&ApiKey={api_key}&UserName={user_name}&Command=namecheap.domains.dns.create&ClientIp={client_ip}&SLD={heroku_subdomain}&TLD={purchased_domain}&RecordType=CNAME&HostName={heroku_subdomain}&Address={heroku_cname_target}&TTL=1800'

    namecheap_response = requests.get(namecheap_api_url)

    if namecheap_response.status_code == 200:
        try:
            # Convert XML to JSON
            response_json = xmltodict.parse(namecheap_response.text)

            # Check if the CNAME creation was successful (modify this based on the actual JSON structure)
            success = response_json.get('YourSuccessKey', {}).get('@Value', '').lower() == 'true'

            return success
        except Exception as e:
            # Handle conversion errors
            print(f"Failed to convert XML to JSON: {e}")
            return False
    else:
        # Handle API request failure
        print(f"Namecheap API request failed with status code {namecheap_response.status_code}")
        return False


if __name__ == "__main__":
    # Replace with actual values
    namecheap_api_user = 'NamecheapApiUser'
    namecheap_api_key = 'NamecheapApiKey'
    namecheap_user_name = 'NamecheapUserName'
    namecheap_client_ip = 'ClientIp'
    purchased_domain = 'example.com'  # replace with the purchased domain
    heroku_subdomain = 'usersubdomain'
    heroku_cname_target = 'heroku-app-name.herokuapp.com'  # replace with the actual Heroku app name

    # Create Namecheap CNAME and assign it to the purchased domain
    cname_creation_successful = create_namecheap_cname(namecheap_api_user, namecheap_api_key, namecheap_user_name, namecheap_client_ip, purchased_domain, heroku_subdomain, heroku_cname_target)

    if cname_creation_successful:
        print(f"Namecheap CNAME for '{heroku_subdomain}' created and assigned to '{purchased_domain}' successfully!")
    else:
        print(f"Failed to create Namecheap CNAME or assign it to '{purchased_domain}'.")
