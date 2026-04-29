package backend.service;

import backend.entity.Record;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class RecordService {

    private final AiServiceClient aiClient;

    private final Map<Long, Record> database = new ConcurrentHashMap<>();
    private Long idCounter = 1L;

    public RecordService(AiServiceClient aiClient) {
        this.aiClient = aiClient;
    }

    public Record create(Record record) {

        // simulate DB save
        record.setId(idCounter++);
        database.put(record.getId(), record);

        // async AI call
        generateAiAsync(record.getId(), record.getInputText());

        return record;
    }

    @Async
    public void generateAiAsync(Long id, String inputText) {

        System.out.println("AI running in background...");

        Map<String, Object> response = aiClient.getDescription(inputText);

        Record record = database.get(id);
        if (record == null) return;

        if (response != null) {
            record.setAiDescription(response);
        } else {
            record.setAiDescription(Map.of("error", "AI unavailable"));
        }

        database.put(id, record);
    }

    public Record getById(Long id) {
        return database.get(id);
    }
}