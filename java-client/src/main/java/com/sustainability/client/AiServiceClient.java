package com.sustainability.client;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import org.springframework.web.client.RestTemplate;
import java.util.HashMap;
import java.util.Map;

/**
 * AiServiceClient handles communication with the Flask-based AI Analysis service.
 * Implements Day 4 requirements: RestTemplate, 10s timeout, null return on error.
 */
public class AiServiceClient {

    private final RestTemplate restTemplate;
    private final String baseUrl = "http://127.0.0.1:5001/api/analyze";

    public AiServiceClient() {
        // Set 10s (10,000ms) timeout as required
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setConnectTimeout(10000);
        factory.setReadTimeout(10000);
        this.restTemplate = new RestTemplate(factory);
    }

    /**
     * Calls the /api/analyze Flask endpoint.
     * @param query The sustainability query to analyze.
     * @return Map containing response data, or null on error.
     */
    public Map<String, Object> analyzeCompliance(String query) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            Map<String, String> requestBody = new HashMap<>();
            requestBody.put("query", query);

            HttpEntity<Map<String, String>> request = new HttpEntity<>(requestBody, headers);

            // RestTemplate POST call
            @SuppressWarnings("unchecked")
            Map<String, Object> response = restTemplate.postForObject(baseUrl, request, Map.class);
            return response;
        } catch (Exception e) {
            // Requirement: null return on error
            System.err.println("🚨 [AiServiceClient] Error calling AI Service: " + e.getMessage());
            return null;
        }
    }

    public static void main(String[] args) {
        AiServiceClient client = new AiServiceClient();
        System.out.println("🚀 Testing AiServiceClient (Day 4)...");
        
        String testQuery = "Analyze the carbon footprint impact of solar panel production.";
        Map<String, Object> response = client.analyzeCompliance(testQuery);
        
        if (response != null) {
            System.out.println("✅ Service Response Success!");
            System.out.println("Analysis Result: " + response.get("data"));
        } else {
            System.out.println("❌ Failed to get response from AI Service. Ensure Flask app is running on port 5001.");
        }
    }
}
