package app;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.lucene.queryparser.classic.ParseException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import ir.QuestionSearcher;

@RestController
public class SearchController {
	
	QuestionSearcher qs;
	
	public SearchController() throws IOException {
		this.qs = new QuestionSearcher("indexer_service/src/main/resources/questions_index");
	}

	@PostMapping("/submit-question")
	public ResponseEntity<String> submitQuestion(@RequestBody Map<String, String> request) {
		String question = request.get("question");
		return ResponseEntity.ok("You submitted: " + question);
	}
	
	@GetMapping("/")
	public String hello() {
		return "Index Searcher Working!";
	}
	
	@GetMapping("/search")
	public ResponseEntity<List<Map<String, String>>> search(@RequestParam String q) 
			throws IOException, ParseException {
		
		String[][] retval = this.qs.find(q);
		List<Map<String, String>> res = new ArrayList<Map<String,String>>();

		for (int i = 0; i < retval.length; i++) {
			HashMap<String, String> h = new HashMap<String, String>();
			h.put("q", retval[i][0]);
			h.put("a", retval[i][1]);
			res.add(h);
		}

		HashMap<String,String> korisnicko = new HashMap<String, String>();
		korisnicko.put("q", q);
		korisnicko.put("a", "");
		res.add(korisnicko);

		return ResponseEntity.ok(res);
	}

}
