# PyTrends API

This is a lightweight Flask-based REST API wrapper around [pytrends](https://github.com/GeneralMills/pytrends) – an unofficial Google Trends API.

> Hosted on Render · Used by internal AI agents for trend analysis.

---

## 🚀 Available Endpoints

All endpoints accept query parameters and return JSON responses.

### `/interest_over_time`
Returns historical interest over time for a given keyword.

- **Query:** `keyword=ai`
- **Example:** `/interest_over_time?keyword=ai`

---

### `/interest_by_region`
Returns interest by geographic region.

- **Query:** `keyword=automation`
- **Example:** `/interest_by_region?keyword=automation`

---

### `/related_topics`
Returns related topics for a keyword.

- **Query:** `keyword=erp`
- **Example:** `/related_topics?keyword=erp`

---

### `/related_queries`
Returns related search queries for a keyword.

- **Query:** `keyword=ecommerce`
- **Example:** `/related_queries?keyword=ecommerce`

---

### `/suggestions`
Returns suggested keywords based on Google autocomplete.

- **Query:** `keyword=ai`
- **Example:** `/suggestions?keyword=ai`

---

### `/trending_searches`
Returns current trending searches.

- **Optional query:** `geo=united_states` (default)
- **Example:** `/trending_searches?geo=czech_republic`

---

### `/top_charts`
Returns top search topics for a given year.

- **Optional queries:** `year=2024`, `cid=all`
- **Example:** `/top_charts?year=2023&cid=all`

---

### `/categories`
Returns all supported categories.

- **Example:** `/categories`

---

## 🛠 Tech Stack

- Python + Flask
- pytrends (Google Trends client)
- Deployed on [Render](https://render.com/)
- Triggered by n8n workflows (ping + data retrieval)

---

## 📁 Files

- `main.py` – core Flask app with all endpoints
- `requirements.txt` – Python dependencies

---

## 📜 License

MIT – free for use in personal and internal projects.
