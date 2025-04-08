# 🧩 Anecdotes Plugin: DummyJSON Evidence Collector

A small and extensible plugin built for Anecdotes' backend engineering assignment.  
The plugin authenticates with [DummyJSON](https://dummyjson.com) and collects evidence from its public REST API.

---

## 🧪 Evidence Collected

| Evidence ID | Description                                       |
|-------------|---------------------------------------------------|
| `E1`        | Authenticated user info (via `/auth/me`)         |
| `E2`        | First 60 posts (via `/posts?limit=60`)           |
| `E3`        | First 60 posts + each post’s comments            |

---

## ⚙️ How to Run

### 📦 Requirements

- Python 3.8+
- `requests` library

```bash
pip install -r requirements.txt
