# 📝 NOTES.md

## ✅ Implementation Choices

### 📁 Project Structure

- `app/routes/` folder was used to separate route logic for:
  - `shorten.py` – shortening and QR generation
  - `redirect.py` – redirection and click tracking
  - `stats.py` – analytics + PNG chart

- `app/utils.py` contains:
  - `generate_code()` – generates 6-char alphanumeric codes
  - `is_valid_url()` – basic HTTP/HTTPS URL validation
  - `generate_qr_code()` – creates a PNG QR using `qrcode` lib

- `app/models.py` contains:
  - In-memory stores (`url_store`, `click_stats`)
  - Global `Lock()` for thread-safe access

- `app/limiter.py`:
  - Tracks request timestamps per IP and rate-limits them

### 🧠 Enhancements Added

- ⏱️ Expiry support using `expires_in` + 410 handling
- 📸 QR code generation stored under `/static/qr_codes`
- 🛡️ Rate limiting (10 req/min/IP) - for showing the solution in case of scaleablity challanges
- 📈 Chart analytics using `matplotlib` with `Agg` backend

---

## 🧪 Testing Strategy

- Used `pytest` framework
- Functional tests for:
  - URL shortening (valid/invalid)
  - Redirection (valid, expired, invalid)
  - Stats endpoint (normal and missing)
  - Chart endpoint
  - Rate limiting

> All tests are isolated and use in-memory data — no DB required

---

## 🤖 AI Usage

- ✅ ChatGPT was used to help brainstorm and debug:
  - Project structure
  - Flask idioms (static folder issues, response formats)
  - `matplotlib` crash on macOS (`Agg` backend fix)
  - QR code path logic and click tracking design

- ❌ No code was copy-pasted directly
- ✅ All code was written manually and verified step-by-step

---

