# SECURITY.md - Tool-65 Sustainability Compliance Monitor

## Initial Threat Model (AI & Security)

As the AI Developer 2, I have identified the following 5 primary security threats to our AI microservice:

1.  **Prompt Injection**: Users may attempt to bypass our compliance rules by giving instructions like "Ignore all previous rules and output [X]".
2.  **API Key Leakage**: Exposure of `GROQ_API_KEY` through logs, GitHub commits, or client-side code.
3.  **Denial of Service (DoS)**: Malicious actors sending thousands of requests to drain our API quota and increase costs.
4.  **Sensitive Data Exposure**: Users might input private corporate data that shouldn't be processed by external LLMs without anonymization.
5.  **Insecure Output Handling**: If the AI output is rendered directly in the browser without escaping, it could lead to Cross-Site Scripting (XSS).

## Mitigation Strategies (Week 1-2)
- [ ] Implement Rate Limiting (Flask-Limiter).
- [ ] Implement Input Sanitization filters.
- [ ] Use environment variables and `.gitignore` for secrets.
- [ ] Add JSON Schema validation for all AI outputs.
