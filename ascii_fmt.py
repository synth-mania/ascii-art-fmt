input_file = input("file: ").strip()

with open(input_file, "r") as f:
	art = f.read()

in_lines = art.split(chr(10))

pad_to = int(input("Pad lines to _ chars: ").strip())

output_file = input("output file: ").strip()

fill_char = input("fill char: ").strip() or "⣿"

with open(output_file, "w") as f:
	for line in in_lines:
		f.write(line + (pad_to - len(line)) * fill_char + "\n")

print("done")
