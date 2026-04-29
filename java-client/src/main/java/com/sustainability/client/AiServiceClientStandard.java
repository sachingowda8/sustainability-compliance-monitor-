package com.sustainability.client;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

/**
 * Standard Java implementation of the AI Service Client.
 * This version uses only standard Java libraries (no dependencies).
 * Fulfills logic requirements: 10s timeout, null return on error.
 */
public class AiServiceClientStandard {

    private final String baseUrl = "http://127.0.0.1:5001/api/analyze";

    /**
     * Calls the /api/analyze Flask endpoint using standard HttpURLConnection.
     * @param query The sustainability query to analyze.
     * @return String containing response JSON, or null on error.
     */
    public String analyzeCompliance(String query) {
        HttpURLConnection connection = null;
        try {
            URL url = new URL(baseUrl);
            connection = (HttpURLConnection) url.openConnection();
            
            // Requirement: 10s timeout
            connection.setConnectTimeout(10000);
            connection.setReadTimeout(10000);
            
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setDoOutput(true);

            String jsonInputString = "{\"query\": \"" + query + "\"}";

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonInputString.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                try (BufferedReader br = new BufferedReader(
                        new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8))) {
                    StringBuilder response = new StringBuilder();
                    String responseLine;
                    while ((responseLine = br.readLine()) != null) {
                        response.append(responseLine.trim());
                    }
                    return response.toString();
                }
            } else {
                System.err.println("🚨 Server returned code: " + responseCode);
                return null;
            }
        } catch (Exception e) {
            // Requirement: null return on error
            System.err.println("🚨 Error calling AI Service: " + e.getMessage());
            return null;
        } finally {
            if (connection != null) {
                connection.disconnect();
            }
        }
    }

    public static void main(String[] args) {
        AiServiceClientStandard client = new AiServiceClientStandard();
        System.out.println("🚀 Testing Standard Java AI Client (No Dependencies)...");
        
        String testQuery = "What are the ESG risks of solar panel disposal?";
        String response = client.analyzeCompliance(testQuery);
        
        if (response != null) {
            System.out.println("✅ Success! Response: " + response);
        } else {
            System.out.println("❌ Failed to get response. Ensure Flask app is running on port 5001.");
        }
    }
}
