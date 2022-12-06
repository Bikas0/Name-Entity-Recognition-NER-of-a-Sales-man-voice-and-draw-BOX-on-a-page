def Name_Entity():
    import spacy
    from speech import Micro_voice
    NER = spacy.load("en_core_web_sm")
    text = Micro_voice()
    text1= NER(text)
    words = []
    for word in text1.ents:
        words.append(word.text)
    return words


