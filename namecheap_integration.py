import requests
import xmltodict

def get_domain_suggestions(api_user, api_key, user_name, client_ip, business_name):
    api_url = f'https://api.namecheap.com/xml.response?ApiUser={api_user}&ApiKey={api_key}&UserName={user_name}&Command=namecheap.domains.tld.getList&ClientIp={client_ip}&SearchTerm={business_name}'

    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            # Converts XML to JSON
            response_json = xmltodict.parse(response.text)

            # Extract domain suggestions
            suggestions = response_json.get('ApiResponse', {}).get('CommandResponse', {}).get('Tlds', {}).get('Tld', [])

            return suggestions
        except Exception as e:
            # Handle conversion errors
            print(f"Failed to convert XML to JSON: {e}")
            return None
    else:
        # Handle API request failure
        print(f"API request failed with status code {response.status_code}")
        return None

def check_domain_availability(api_user, api_key, user_name, client_ip, suggested_domains):
    availability_results = {}

    for domain in suggested_domains:
        api_url = f'https://api.namecheap.com/xml.response?ApiUser={api_user}&ApiKey={api_key}&UserName={user_name}&Command=namecheap.domains.check&ClientIp={client_ip}&DomainName={domain}'

        response = requests.get(api_url)

        if response.status_code == 200:
            try:
                # Converting XML to JSON
                response_json = xmltodict.parse(response.text)

                # Extracting availability status
                available = response_json.get('AvailabilityKey', {}).get('@Available', '').lower() == 'true'
                availability_results[domain] = available
            except Exception as e:
                # Handling conversion errors
                print(f"Failed to convert XML to JSON: {e}")
                availability_results[domain] = None
        else:
            print(f"API request failed with status code {response.status_code}")
            availability_results[domain] = None

    return availability_results

def markup_pricing(suggested_domains, base_price, markup_percentage):
    marked_up_prices = {}

    for domain in suggested_domains:
        # Calculate marked up price
        marked_up_price = base_price * (1 + markup_percentage / 100)
        marked_up_prices[domain] = marked_up_price

    return marked_up_prices

def display_pricing(prices):
    print("Domain pricing:")
    for domain, price in prices.items():
        print(f"{domain}: ${price:.2f}")

def display_domain_suggestions(suggestions):
    if suggestions:
        print("Domain suggestions: ")
        for suggestion in suggestions:
            print(suggestion)
    else:
        print("No suggestions available.")

def purchase_domain(api_user, api_key, user_name, client_ip, domain_name):
    api_url = f'https://api.namecheap.com/xml.response?ApiUser={api_user}&ApiKey={api_key}&UserName={user_name}&Command=namecheap.domains.create&ClientIp={client_ip}&DomainName={domain_name}&Years=1'

    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            # Convert XML to JSON
            response_json = xmltodict.parse(response.text)

            # Checking if the domain creation was successful
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

if __name__ == "__main__":
    # Add the Prompt values.
    api_user = ''
    api_key = ''
    user_name = ''
    client_ip = ''
    business_name = ''

    # Get domain suggestions
    suggestions = get_domain_suggestions(api_user, api_key, user_name, client_ip, business_name)

    # Check domain availability
    availability_results = check_domain_availability(api_user, api_key, user_name, client_ip, suggestions)

    # Markup pricing
    base_price = 5.98  
    markup_percentage = 10  
    marked_up_prices = markup_pricing(suggestions, base_price, markup_percentage)

    display_domain_suggestions(suggestions)

    # Display pricing to the user
    display_pricing(marked_up_prices)
