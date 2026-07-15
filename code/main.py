#!/usr/bin/env python3
import argparse 
from pathlib import Path

from AutoVocab.utils import check_file, vocab_to_csv
from AutoVocab.audio import extract_audio
from AutoVocab.transcribe import transcribe
from AutoVocab.vocabulary import make_vocab
from AutoVocab.translate import ja_to_en

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file", type=str, help="input mkv or mp4 file path")
	args = parser.parse_args()
	print("checking mkv file...")
	str_file_path = args.file
	print("Provided file path:\t", str_file_path)
	if check_file(str_file_path):
		mkv_file_path = Path(str_file_path)
		print("video file checked.")
		print("extracting audio...")
		audio_file_path = extract_audio(mkv_file_path)
		print("audio extracted.")
		print("creating transcript...")
		transcription_file_path = transcribe(audio_file_path)
		print("transcript made.")
		print("turning transcription into vocabulary list...")
		vocab = make_vocab(transcription_file_path)
		print("vocabulary list created")
		print("translating japanese to english")
		complete_vocab = ja_to_en(vocab)
		print("turning vocabulary list into anki deck")
		anki_file_path = vocab_to_csv(complete_vocab)
		print("process complete. the anki deck has been saved to full_path_to_anki_deck")

main()
