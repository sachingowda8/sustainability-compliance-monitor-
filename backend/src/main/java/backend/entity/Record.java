package backend.entity;

import lombok.*;

import java.util.Map;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Record {

    private Long id;
    private String inputText;

    // ✅ must be Map (not String)
    private Map<String, Object> aiDescription;
}