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
	info_txt["num_non_word"] = len(tab_non_word)
	avg_size_word = 0
	for w in tab_word:
		avg_size_word += len(w)
	avg_size_word /= info_txt["num_word"]
	info_txt["avg_size_word"] = round(avg_size_word, 0)
	avg_size_non_word = 0
	for w in tab_non_word:
		avg_size_non_word += len(w)
	avg_size_non_word /= info_txt["num_non_word"]
	info_txt["avg_size_non_word"] = round(avg_size_non_word, 0)
	return info_txt
    
def tab_to_space(txt, tab=4):
    clr_txt = ""
    nb_space = 0
    pos = 0
    for cc in txt:
        if cc == '\t':
            nb_space = tab - (pos % tab)
            clr_txt += ' ' * nb_space
            pos += nb_space
        else:
            clr_txt += cc
            pos += 1
    return clr_txt

def text_wrapping(txt:str, line_size:int)->str:
    clr_txt = tab_to_space(txt)
    if len(clr_txt) <= line_size:
	    return [clr_txt]
    info_txt = info(clr_txt)
    num_word = 1
    while (info_txt["avg_size_word"] * (num_word + 1) + info_txt["avg_size_non_word"] * num_word) < line_size:
        num_word += 1
    wrapped_text = [""]
    counter = 1
    for i in range(info_txt["num_word"]):
        wrapped_text[-1] += info_txt["list_word"][i]
        if counter < num_word and i < len(info_txt["list_non_word"]):
            wrapped_text[-1] += info_txt["list_non_word"][i]
        else:
            wrapped_text.append("")
            counter = 0
        counter += 1
    wrapped_text.pop()
    return wrapped_text

def complete_space(tab_line):
    len_max = 0
    tab_line_space = tab_line
    for line in tab_line:
        if len(line) > len_max:
            len_max = len(line)
    for i in range(len(tab_line)):
        while len(tab_line_space[i]) < len_max:
            tab_line_space[i] += ' '
    return tab_line_space
            
def treated_text(txt, nb = 80):
    wrap = text_wrapping(txt, nb)
    spc = complete_space(wrap)
    return spc
