def cutFile():
    text_area.event_generate("<<Cut>>")
def copyFile():
    text_area.event_generate("<<Copy>>")
def pasteFile():
    text_area.event_generate("<<Paste>>")