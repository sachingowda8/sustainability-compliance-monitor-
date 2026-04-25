# SECURITY.md - Tool-65 Sustainability Compliance Monitor

## Initial Threat Model (AI & Security)

As the AI Developer 2, I have identified the following primary security threats:

1.  **Prompt Injection**: Users may attempt to bypass compliance rules by injecting instructions.
2.  **API Key Leakage**: Exposure of `GROQ_API_KEY`.
3.  **Denial of Service (DoS)**: High volume requests draining API quota.
4.  **Sensitive Data Exposure**: User input containing PII or corporate secrets.
5.  **Insecure Output Handling**: AI output leading to XSS if rendered unescaped.

## Mitigation Strategies (Implemented)
- [x] Implement Rate Limiting (Flask-Limiter).
- [x] Implement Input Sanitization (HTML stripping).
- [x] Implement Prompt Injection Detection (Regex patterns).
- [x] Use environment variables for secrets.
- [x] Added check for empty/whitespace-only input (Day 5).

## Week 1 Security Test Results (Day 5)

I have performed security testing on the `/api/analyze` endpoint.

### 1. Empty Input Test
- **Status**: PASSED
- **Details**: 
    - Empty query string returns `400 Bad Request`.
    - Whitespace-only query returns `400 Bad Request` (Fixed in Day 5).
    - Missing query key returns `400 Bad Request`.

### 2. SQL Injection Test
- **Status**: PASSED
- **Details**: 
    - Payloads like `' OR '1'='1` are treated as literal text.
    - System is robust as no database is currently connected to this endpoint.

### 3. Prompt Injection Test
- **Status**: PASSED (Enhanced)
- **Details**: 
    - Tested common injection phrases.
    - **Result**: The application successfully detects patterns like "Ignore previous instructions" and returns a `400 Bad Request` with a security warning.
    - **Sanitization**: HTML tags are automatically stripped.

### 4. Rate Limiting Verification
- **Status**: PASSED
- **Details**: 
    - Confirmed that 429 status is returned when exceeding limits.
