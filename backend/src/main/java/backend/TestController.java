package backend;

import backend.entity.Record;
import backend.service.RecordService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class TestController {

    private final RecordService service;

    public TestController(RecordService service) {
        this.service = service;
    }

    @PostMapping("/create")
    public Record create(@RequestBody Record record) {
        return service.create(record);
    }

    @GetMapping("/{id}")
    public Record get(@PathVariable Long id) {
        return service.getById(id);
    }
}