package ir;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field.Store;
import org.apache.lucene.document.StoredField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.IndexWriterConfig.OpenMode;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

public class QuestionIndexer {

	private IndexWriter indexer;
	
	public QuestionIndexer(String indexDirPath, boolean createNew) 
			throws IOException {
		
		java.nio.file.Path indexDirectoryPath = java.nio.file.Paths.get(indexDirPath);
		Directory indexDir = FSDirectory.open(indexDirectoryPath);
		
		Analyzer analyzer = new StandardAnalyzer();
		
		IndexWriterConfig iwc = new IndexWriterConfig(analyzer);
		
		if (createNew) {
			iwc.setOpenMode(OpenMode.CREATE);
		}
		else {
			iwc.setOpenMode(OpenMode.APPEND);
		}
		
		this.indexer = new IndexWriter(indexDir, iwc);
		
	}
	
	public void indexQuestion(String question, String answer) throws IOException {
		
		Document doc = new Document();
		
		doc.add(new TextField("question", question, Store.YES));
		doc.add(new StoredField("answer", answer));
		
		indexer.addDocument(doc);
		
	}
	
	public void finishIndexing() throws IOException {
		indexer.close();
	}
	
	public void indexQuestionAnswerPairs(String fPath) throws IOException {
		
		BufferedReader br = new BufferedReader(new FileReader(fPath));
		
		String line = null;
		
		while ((line = br.readLine()) != null) {
			line = line.trim();
			
			if (line.equals("")) {
				continue;
			}
			
			String[] pair = line.split(",");
			
			if (pair.length != 2) {
				continue;
			}
						
			this.indexQuestion(pair[0], pair[1]);
			
		}
		
		br.close();
		
	}
	
	public static void main(String[] args) throws IOException {
		
		QuestionIndexer qi = new QuestionIndexer("indexer_service/src/main/resources/questions_index", true);

		qi.indexQuestionAnswerPairs("indexer_service/src/main/resources/QnA.csv");//ispravljena putanja
		
		qi.finishIndexing();
		
	}
	
}
