import requests
import xmltodict
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .namecheap_integration import get_domain_suggestions, check_domain_availability, markup_pricing, display_pricing, purchase_domain
from .heroku_integration import create_heroku_subdomain, acquire_cname

app = FastAPI()

namecheap_api_user = 'NamecheapApiUser'
namecheap_api_key = 'NamecheapApiKey'
namecheap_user_name = 'NamecheapUserName'
namecheap_client_ip = 'ClientIp'
heroku_api_key = 'HerokuApiKey'
heroku_app_name = 'HerokuAppName'

@app.get("/")
def read_root():
    return {"message": "Welcome to Namecheap and Heroku FastAPI integration!"}

@app.get("/suggest_domains/{business_name}")
def suggest_domains_endpoint(business_name: str):
    suggestions = get_domain_suggestions(business_name)
    return {"suggestions": suggestions}

@app.get("/check_domain_availability/{domain_name}")
def check_domain_availability_endpoint(domain_name: str):
    availability = check_domain_availability(domain_name)
    return {"availability": availability}

@app.post("/purchase_domain/{domain_name}")


@app.post("/create_subdomain/{username}")
def create_subdomain_endpoint(username: str):
    subdomain = create_heroku_subdomain(heroku_api_key, heroku_app_name, username)
    return {"subdomain": subdomain}

@app.post("/acquire_cname/{subdomain}")
def acquire_cname_endpoint(subdomain: str):
    cname = acquire_cname(heroku_api_key, heroku_app_name, subdomain)
    return {"cname": cname}

heroku_api_key = ''
heroku_app_name = ''
namecheap_api_user = ''
namecheap_api_key = ''
namecheap_user_name = ''
namecheap_client_ip = ''
purchased_domain = 'example.com'  # replace with the purchased domain
heroku_cname_target = ''


def create_namecheap_cname(subdomain):
    api_url = f'https://api.namecheap.com/xml.response?ApiUser={namecheap_api_user}&ApiKey={namecheap_api_key}&UserName={namecheap_user_name}&Command=namecheap.domains.dns.create&ClientIp={namecheap_client_ip}&SLD={subdomain}&TLD={purchased_domain}&RecordType=CNAME&HostName={subdomain}&Address={heroku_cname_target}&TTL=1800'

    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            # Convert XML to JSON
            response_json = xmltodict.parse(response.text)

            # Check if the CNAME creation was successful (modify this based on the actual JSON structure)
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

@app.post("/create_subdomain/{username}")
def create_subdomain_endpoint(username: str):
    user_subdomain = f"{username}-subdomain"  # Modify this as needed
    success = create_heroku_subdomain(heroku_api_key, heroku_app_name, user_subdomain)

    if success:
        # Create Namecheap CNAME and assign it to the purchased domain
        cname_creation_successful = create_namecheap_cname(user_subdomain)

        if cname_creation_successful:
            return JSONResponse(content={"message": f"Heroku subdomain '{user_subdomain}' and Namecheap CNAME created successfully!"})
        else:
            raise HTTPException(status_code=500, detail="Failed to create Namecheap CNAME")
    else:
        raise HTTPException(status_code=500, detail="Failed to create Heroku subdomain")

@app.post("/purchase_domain/{domain_name}")
def purchase_domain_endpoint(domain_name: str):
    api_user = 'NamecheapApiUser'
    api_key = 'NamecheapApiKey'
    user_name = 'NamecheapUserName'
    client_ip = 'ClientIp'

    purchase_result = purchase_domain(api_user, api_key, user_name, client_ip, domain_name)
    return {"purchase_result": purchase_result}








