
# 📝 NOTES.md

## ✅ Implementation Choices

### 📁 Project Structure

* `app/routes/` folder was used to separate route logic for:

  * `shorten.py` – shortening and QR generation
  * `redirect.py` – redirection and click tracking
  * `stats.py` – analytics + PNG chart

* `app/utils.py` contains:

  * `generate_code()` – generates 6-char alphanumeric codes
  * `is_valid_url()` – basic HTTP/HTTPS URL validation
  * `generate_qr_code()` – creates a PNG QR using `qrcode` lib

* `app/models.py` contains:

  * In-memory stores (`url_store`, `click_stats`)
  * Global `Lock()` for thread-safe access

* `app/limiter.py`:

  * Tracks request timestamps per IP and rate-limits them
  * ✅ Added `reset_limiter()` to help clear rate-limiter state between tests

---

## 🧠 Enhancements Added

* ⏱️ Expiry support using `expires_in` + 410 Gone handling
* 📸 QR code generation stored under `/static/qr_codes`
* 🛡️ Rate limiting (10 req/min/IP) — to demonstrate handling of scalability challenges
* 🔁 Test-friendly limiter reset for clean test environment
* 📈 Chart analytics using `matplotlib` with `Agg` backend for server-side rendering

---

## 🧪 Testing Strategy

* Used `pytest` framework
* Functional test coverage includes:

  * URL shortening (valid/invalid URLs)
  * Redirection behavior (valid, expired, invalid codes)
  * Stats endpoint (correct output and missing codes)
  * PNG chart endpoint
  * Rate limiting enforcement

### ⚙️ Shared Setup

* `tests/conftest.py` uses `reset_limiter()` before each test to ensure isolation
* All tests run with in-memory data only — no external DB or I/O dependency

---

## 🤖 AI Usage

* ✅ ChatGPT was used to assist with:

  * Project architecture guidance
  * Flask debugging (e.g., static asset resolution, test config issues)
  * Design choices (QR storage, chart generation, redirect logic)
  * Test coverage brainstorming (e.g., rate limiter resets)

* ❌ No direct code copy-pasting

* ✅ All implementation and testing code was written manually and reviewed

* ✅ README content collaborated with Claude AI


