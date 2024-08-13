package ir;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;

public class QuestionSearcher {

	private static final int NUM_HITS = 10;
	
	private IndexReader indexReader;
	private IndexSearcher indexSearcher;
	private QueryParser queryParser;
	
	public QuestionSearcher(String indexDir) throws IOException {
		
		Path p = Paths.get(indexDir);
				
		this.indexReader = DirectoryReader.open(
				FSDirectory.open(
						p
					)
			);
		
		System.out.println(this.indexReader.getDocCount("question"));
		
		this.indexSearcher = new IndexSearcher(indexReader);
		
		Analyzer analyzer = new StandardAnalyzer();
			
		this.queryParser = new QueryParser("question", analyzer);
		
	}
	
	public String[][] find(String query) throws IOException, ParseException {
		
		Query q = this.queryParser.parse(query);
		
		TopDocs results = this.indexSearcher.search(q, NUM_HITS);
		ScoreDoc[] hits = results.scoreDocs;

		String[][] res = new String[hits.length][2];
		
		for (int i = 0; i < hits.length; i++) {
			Document doc = indexSearcher.doc(hits[i].doc);
			
			String question = doc.get("question");
			String answer = doc.get("answer");
			
			res[i][0] = question;
			res[i][1] = answer;
			
		}
		
		return res;
		
	}
	
	public void close() throws IOException {
		this.indexReader.close();
	}
	
	public static void main(String[] args) throws IOException, ParseException {
		//QuestionSearcher qs = new QuestionSearcher("questions_index");
		QuestionSearcher qs = new QuestionSearcher("indexer_service/src/main/resources/questions_index");
		qs.find("What Companies Will Issue Life Insurance To The Mentally Ill");
		
		qs.close();
	}
	
}
