
from pathlib import Path

from faster_whisper import WhisperModel

print("loading model ... this only takes some time the first time. from then on the software loads it from storage.")
model = WhisperModel("small", device="cpu", compute_type="int8")


def transcribe(audio_file_path: Path):
	segments, info = model.transcribe(
		audio_file_path,
		language="ja",
	)
	
	transcript = "".join(segment.text for segment in segments)
	print(transcript)

	file = Path("transcript")
	file.write_text(transcript, encoding="utf-8")
	return file
