import os
import requests
import json
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential

# Load environment variables
load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
PURVIEW_ENDPOINT = os.getenv("PURVIEW_ENDPOINT", "https://api.purview-service.microsoft.com")

if not all([TENANT_ID, CLIENT_ID, CLIENT_SECRET]):
    raise ValueError("Missing required environment variables")

def get_access_token():
    credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    token = credential.get_token("https://purview.azure.net/.default")
    return token.token

def list_data_products(skip=0, top=100):
    token = get_access_token()
    url = f"{PURVIEW_ENDPOINT}/datagovernance/catalog/dataProducts"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    params = {
        "api-version": "2025-09-15-preview",
        "skip": skip,
        "top": top
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.text)
        response.raise_for_status()

def get_all_products():
    all_products = []
    skip = 0
    top = 100

    while True:
        data = list_data_products(skip, top)

        if "value" not in data:
            break

        products = data["value"]
        all_products.extend(products)

        print(f"Fetched {len(products)} records (Total: {len(all_products)})")

        if not data.get("nextLink"):
            break

        skip += top

    return all_products

def display_products(products):
    print(f"\nTotal Products: {len(products)}\n")
    for p in products:
        print(f"Name: {p.get('name')}")
        print(f"Status: {p.get('status')}")
        print(f"Domain: {p.get('domain')}")
        print(f"Type: {p.get('type')}")
        print("-" * 40)

def save_to_json(products, filename="data_products_output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)
    print(f"Saved output to {filename}")

if __name__ == "__main__":
    try:
        print("Fetching data products from Microsoft Purview...")
        products = get_all_products()
        display_products(products)
        save_to_json(products)
    except Exception as e:
        print(f"Error: {e}")
