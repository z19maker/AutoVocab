from pathlib import Path

from janome.tokenizer import Tokenizer 

t = Tokenizer()

def make_vocab(transcription_file_path: Path):
	def read_file_content(file_path: Path) -> str:
		return file_path.read_text(encoding="utf-8")

	content = read_file_content(transcription_file_path)

	tokens = t.tokenize(content)
	vocab = [token.surface for token in tokens if token.part_of_speech.split(",")[0] in ("名詞", "動詞", "形容詞", "形容動詞", "副詞")]
	return vocab
