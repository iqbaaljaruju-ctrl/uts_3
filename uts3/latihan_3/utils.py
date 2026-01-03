def nilai_kelulusan(data):
	return sum(data) / len(data)

def parse_list(list_string):
	return list(map(int, list_string.split()))