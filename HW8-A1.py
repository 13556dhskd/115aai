import sys


lines = sys.stdin.read().splitlines()
if lines:
	index = 0
	n = int(lines[index].strip())
	index += 1
	playlist = lines[index].split()[:n] if index < len(lines) else []
	index += 1
	q = int(lines[index].strip())
	index += 1

	for _ in range(q):
		line = lines[index].strip()
		index += 1
		parts = line.split(maxsplit=1)
		command = parts[0]

		if command.upper() in ("REVERSE", "反向"):
			playlist.reverse()
		elif command.upper() == "ADD":
			if len(parts) > 1:
				playlist.append(parts[1])
		elif command.upper() == "REMOVE":
			if len(parts) > 1 and parts[1] in playlist:
				playlist.remove(parts[1])
		elif command.startswith("添加"):
			name = parts[1] if len(parts) > 1 else command[2:]
			if name:
				playlist.append(name)
		elif command.startswith(("去除", "移除")):
			prefix = "去除" if command.startswith("去除") else "移除"
			name = parts[1] if len(parts) > 1 else command[len(prefix):]
			if name in playlist:
				playlist.remove(name)

	print(len(playlist))
	print(" ".join(playlist) if playlist else "EMPTY")
