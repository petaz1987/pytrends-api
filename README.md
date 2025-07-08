# PyTrends API for Petr Staroba

A lightweight Flask-based API wrapper over [pytrends](https://github.com/GeneralMills/pytrends), hosted on Render. Built to power AI agents with real-time topic insights.

---

## 🛠️ Available Endpoints

All endpoints support optional query parameters:

- `lang` – default: `en-US`
- `geo` – default: `''` (empty = worldwide)
- `tz` – default: `360` (CET)

---

### `/suggestions?keyword=ai`

Returns search term suggestions related to the keyword.

---

### `/related_queries?keyword=ai`

Returns related queries for a given keyword (top and rising).

---

### `/interest_over_time?keyword=ai`

Returns time-series data of keyword interest.

---

### `/interest_by_region?keyword=ai&resolution=COUNTRY`

Returns interest by region.

---

### `/trending_searches?geo=united_states`

Returns trending searches for a region (e.g. `united_states`, `czech_republic`, `united_kingdom`).

---

### `/top_charts?year=2024&geo=CZ`

Returns top Google searches for a given year.

---

## 🧪 Example Call

```bash
curl "https://your-domain.onrender.com/interest_over_time?keyword=chatgpt&geo=CZ&lang=cs-CZ"
```

---

## 📦 Tech Stack

- Python 3.11+
- Flask
- pytrends
- Hosted on [Render.com](https://render.com)

---

## 📄 License

MIT
