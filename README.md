# API Explorer

A beautiful Frappe app to **generate** and **visualize** whitelisted APIs with interactive Swagger UI documentation.

---

## Features

- Automatically generates OpenAPI (Swagger) JSON files for all installed Frappe apps.
- Responsive Swagger UI portal with sidebar app selection.
- Displays API endpoints, parameters, sample requests, and responses.

---

## How to Use

1. **Install the app** in your Frappe site.
2. **Run `bench migrate`** to apply changes and update your site.
3. **Run the OpenAPI generator**.
4. **Access the API Explorer UI** at `/docs` (or your configured route).
5. **Select an app** from the sidebar to view its API documentation.
6. **Try out endpoints** directly from the Swagger UI.

---

## Whitelisting Functions for API Explorer

To ensure your APIs are documented correctly:

- **Whitelist your function** using `@frappe.whitelist()` or in `hooks.py`.
- **Add a detailed Python docstring** to your function, including:
  - **Description** of what the endpoint does.
  - **Sample Response** format (JSON).

**Example:**

```python
@frappe.whitelist()
def create_customer(name, email):
    """
    Create a new customer.

    Response:
    {
        "status": "success",
        "customer_id": "CUS12345"
    }
    """
    # Your code here
```

**Guidelines:**
- Always describe the endpoint's purpose.
- Include clear sample response blocks.
- Keep examples concise and relevant.
- These doc comments are parsed and shown in the API Explorer UI.

---

## License

agpl-3.0