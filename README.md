# Microsoft Purview Unified Catalog

## Data Products API — Setup & Developer Guide

**API Version:** 2025-09-15-preview
**Language:** Python
**Authentication:** OAuth 2.0 (Client Credentials Flow)

---

# 1. Overview

This project demonstrates how to programmatically retrieve **Data Products** from Microsoft Purview using its Unified Catalog API.

Instead of manually navigating the UI, this script allows you to:

* Fetch all data products automatically
* Build dashboards and reports
* Monitor metadata quality
* Integrate with external systems

---

## 🔧 What This Project Does

* Authenticates with Azure Active Directory
* Calls the Purview REST API
* Handles pagination automatically
* Displays readable output
* Saves full data to JSON file

---

## 🌐 API Details

| Item            | Value                                     |
| --------------- | ----------------------------------------- |
| Base Endpoint   | https://api.purview-service.microsoft.com |
| Resource Path   | `/datagovernance/catalog/dataProducts`    |
| Auth Type       | OAuth 2.0 Client Credentials              |
| Response Format | JSON                                      |

---

# 2. Azure Prerequisites (VERY IMPORTANT)

Before running the project, you must configure Azure properly.

---

## 2.1 Tenant ID

**What it is:**
Your Azure Active Directory identifier.

**How to get it:**

1. Go to Azure Portal
2. Open **Azure Active Directory**
3. Click **Overview**
4. Copy **Tenant ID**

---

## 2.2 Client ID (App Registration)

**What it is:**
Represents your application in Azure.

**Steps:**

1. Go to **App Registrations**
2. Click **New Registration**
3. Name it: `purview-api-client`
4. Click **Register**
5. Copy **Application (client) ID**

---

## 2.3 Client Secret

**What it is:**
Password for your application.

**Steps:**

1. Open your App Registration
2. Go to **Certificates & Secrets**
3. Click **New Client Secret**
4. Copy the value immediately

⚠️ You cannot retrieve it again.

---

## 2.4 Assign Purview Permissions

Your app must be authorized to read Purview data.

**Steps:**

1. Go to your Purview Account
2. Open **Access Control (IAM)**
3. Click **Add Role Assignment**
4. Assign:

* **Purview Data Reader** (read-only)
* OR **Data Curator** (read/write)

---

# 3. Project Setup

---

## 3.1 Project Structure

```id="v4y0zw"
purview-data-products/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
├── .gitignore
└── data_products_output.json (generated)
```

---

## 3.2 Install Dependencies

```bash id="dbqgdb"
pip install -r requirements.txt
```

---

### Required Libraries

| Library        | Purpose                    |
| -------------- | -------------------------- |
| requests       | HTTP API calls             |
| python-dotenv  | Load environment variables |
| azure-identity | Azure authentication       |

---

# 4. Environment Configuration

Create a `.env` file:

```env id="r7rsya"
TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
CLIENT_SECRET=your-secret
PURVIEW_ENDPOINT=https://api.purview-service.microsoft.com
```

---

## 🔐 Security Best Practices

* NEVER commit `.env` to Git
* Add `.env` to `.gitignore`
* Use **Azure Key Vault** in production

---

# 5. Running the Project

---

## ▶️ Run Command

```bash id="jjg0w0"
python app.py
```

---

## ⚙️ What Happens Internally

1. Loads `.env` variables
2. Authenticates with Azure AD
3. Receives Bearer Token (~1 hour validity)
4. Calls Purview API
5. Fetches all pages of data
6. Prints summary
7. Saves JSON output

---

# 6. Code Breakdown

---

## 🔐 `get_access_token()`

* Authenticates with Azure
* Returns access token

---

## 📡 `list_data_products()`

* Calls API
* Returns one page (max 100 items)

---

## 🔁 `get_all_products()`

* Handles pagination
* Combines all pages

---

## 📊 `display_products()`

* Prints readable output

---

## 💾 `save_to_json()` *(recommended add)*

* Saves full API response
* Useful for dashboards

---

# 7. Data Returned from API

Each Data Product contains:

```json id="v5w8j2"
{
  "name": "Customer Analytics",
  "id": "uuid",
  "status": "Published",
  "type": "Analytics",
  "domain": "Marketing",
  "endorsed": true,
  "description": "Tracks behavior",
  "businessUse": "Marketing insights",
  "updateFrequency": "Daily",
  "additionalProperties": {
    "assetCount": 25
  }
}
```

---

## 📊 Field Breakdown

| Field           | Meaning           |
| --------------- | ----------------- |
| name            | Product name      |
| status          | Draft / Published |
| type            | Category          |
| domain          | Owner             |
| endorsed        | Quality status    |
| updateFrequency | Refresh rate      |
| assetCount      | Number of assets  |

---

# 8. Pagination Explained

The API limits results to **100 per request**.

| Request  | Records |
| -------- | ------- |
| skip=0   | 1–100   |
| skip=100 | 101–200 |

The script:

* Detects `nextLink`
* Continues until all data is retrieved

---

# 9. Output

---

## Console Output

```id="le1k7k"
Name: Customer Data
Status: Published
Domain: Finance
Type: Master Data
----------------------------------------
```

---

## JSON Output

File generated:

```id="a3y9dt"
data_products_output.json
```

---

## Where You Can Use It

* Power BI
* Excel (Power Query)
* Dashboards
* Internal tools

---

# 10. Troubleshooting

| Error            | Fix                         |
| ---------------- | --------------------------- |
| 401 Unauthorized | Check credentials           |
| 403 Forbidden    | Assign correct role         |
| No data          | Ensure catalog has products |
| Module error     | Run pip install             |

---



# 11. Summary

This project turns Microsoft Purview into a **programmable data platform**.

Instead of manual checks, you can now:

* Automate governance
* Track data quality
* Build real-time dashboards
* Integrate with enterprise tools

---
