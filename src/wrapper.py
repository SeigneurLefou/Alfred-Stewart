import sys

def info(txt):
	info_txt = {}
	info_txt["size"] = len(txt)
	tab_word = []
	inword = False
	for i in range(len(txt)):
		if inword == False and 32 < ord(txt[i]) and ord(txt[i]) != 127:
			inword = True
			tab_word.append(txt[i])
		elif inword == True and 32 < ord(txt[i]) and ord(txt[i]) != 127:
			tab_word[-1] += txt[i]
		elif inword == True:
			inword = False
	info_txt["list_word"] = tab_word
	tab_non_word = []
	inword = False
	for i in range(len(txt)):
		if inword == False and txt[i] == " ":
			inword = True
			tab_non_word.append(txt[i])
		elif inword == True and txt[i] == " ":
			 tab_non_word[-1] += txt[i]
		elif inword == True:
			inword = False
	info_txt["list_non_word"] = tab_non_word
	info_txt["num_word"] = len(tab_word)
	avg_size_word = 0
	for w in tab_word:
		avg_size_word += len(w)
	avg_size_word /= info_txt["num_word"]
	info_txt["avg_size_word"] = round(avg_size_word, 0)
	return info_txt

def text_warping(txt:str, line_size:int)->str:
    clr_txt = clear_txt(txt)
	info_txt = info(clr_txt)
	if len(clr_txt) <= line_size:
		return clr_txt
	num_word_line = int(sizeinfo_txt["avg_size_word"])
