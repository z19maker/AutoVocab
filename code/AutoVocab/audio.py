from pathlib import Path

from ffmpeg import FFmpeg

def extract_audio(mkv_file_path: Path):

	suffix = ".m4a" if mkv_file_path.suffix.lower() == ".mp4" else ".mka"
	audio_file_path = mkv_file_path.with_suffix(suffix)

	(
		FFmpeg()
		.input(str(mkv_file_path))
		.output(
			str(audio_file_path),
			vn=None,
			c="copy",
			y=None
		)
		.execute()
	)
	
	return audio_file_path
