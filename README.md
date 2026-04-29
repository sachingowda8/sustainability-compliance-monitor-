# Sustainability Compliance Monitor

A tool-based AI solution to monitor and ensure sustainability compliance.

## Project Progress

### 📅 Day 1
* Set up project folders and basic structure.
* Configured API keys and environment variables (.env).
* Initialized Git for version control.
* Verified the initial connection to the Groq AI API.

### 📅 Day 2
* Developed a robust and reusable GroqClient.
* Added error handling and automatic retries for better reliability.
* Integrated logging to track service performance.
* Created test scripts to verify AI responses and client stability.

### 📅 Day 3
* Built a Flask API with a POST endpoint (`/api/analyze`) for AI analysis.
* Implemented `flask-limiter` for rate limiting (30 requests/minute).
* Added security features to strip HTML and block prompt injection.
* Configured specialized system prompts for sustainability compliance expertise.
### 📅 Day 4
* Developed AiServiceClient.java using Spring RestTemplate.
* Configured a 10-second timeout for robust service communication.
* Implemented fail-safe error handling (returns null on failure).
* Created a Maven project structure for the Java client.
* Added AiServiceClientStandard.java for instant running without Maven dependencies.
* Provided run_standard_client.bat for easy execution.

### 📅 Day 5
* Conducted security testing and verification of AI response integrity.
* Documented API security measures and rate limiting configurations.
* Refined input sanitization to include prompt injection detection.

### 📅 Day 6
* Implemented **Prompt Tuning** for enhanced ESG compliance analysis.
* Externalized system prompts to `ai-service/prompts/` for better maintainability.
* Refined the "Sustainability Expert" persona with structured analysis (Pillars, Regulations, Risks).
* Created `tune_prompts.py` to automate accuracy scoring across 10 real-world inputs.
* Validated results, achieving high-accuracy structured responses.

### 📅 Day 7
* Conducted simulated OWASP ZAP security scan.
* Generated mock `owasp_zap_report.md` with Critical and Medium findings.
* Fixed Critical finding: Added HTTP Security Headers (`X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`, `Content-Security-Policy`).
* Fixed Critical finding: Disabled hardcoded `debug=True` in production for Flask.
* Planned Medium fixes (CORS configuration, detailed error hiding, version obfuscation) for upcoming days.
