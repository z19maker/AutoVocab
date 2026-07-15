from pathlib import Path
import csv

def check_file(str_file_path: str):
	file_path = Path(str_file_path)

	if not file_path.exists():
		print("file path does not exist")
		return False
	
	try:
		with open(file_path, 'rb') as f:
			first_four_bytes = f.read(4)
			is_mkv = first_four_bytes == b'\x1a\x45\xdf\xa3'
			if not is_mkv:
				f.seek(0)
				header = f.read(12)
				is_mp4 = (len(header) == 12
					and header[4:8] == b'ftyp')
				if not is_mp4:
					print("file is not an mkv or mp4 file")
					return False
			print("video file check complete!")
			return True

	except IOError:
		print("IOError")
		return False

def vocab_to_csv(vocab_dict: dict):
	# TODO: 
	# convert python dictionary into csv
	# no headers 
	# each key,value is a row
	csv_file_path = Path('deck.csv')
	with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		for key,value in vocab_dict.items():
			writer.writerow([key,value])

	return csv_file_path
