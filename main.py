dictionary_file = "./lemmad.txt"
output_file = "./domains.txt"

tlds = {
    ".edu", ".eu", ".eus", ".gal", ".info", ".int", ".krd",
    ".mobi", ".org", ".pro", ".tel", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".ar", ".as",
    ".at", ".au", ".ba", ".bd", ".be", ".bf", ".bh", ".bi", ".bo", ".bs",
    ".bt", ".de", ".do", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".fi", ".ga", ".ge", ".gi", ".gu", ".hk", ".hm",
    ".hn", ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".ir", ".is", ".it", ".je", ".jo", ".ke",
    ".ki", ".la", ".lb", ".li", ".lt", ".lu", ".lv", ".ma", ".me", ".mm", ".mo", ".mp", ".ms", ".na", ".ne", ".ng",
    ".ni", ".no", ".nu", ".om", ".pa", ".pe", ".ps", ".re", ".ro", ".rs", ".ru", ".sa", ".se", ".si", ".sk", ".sn",
    ".so", ".st", ".su", ".sv", ".tk", ".tl", ".to", ".tt", ".tv", ".ug", ".uk", ".us", ".va", ".ve", ".vi", ".vu"}

replacements = {"ä": "a", "ö": "o", "õ": "o", "ü": "u"}

def format_url(word: str, tld: str):
    domain_name = word.replace(tld, "")
    return f"{domain_name}.{tld}"

def replace_special_chars(text: str):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

with open(dictionary_file) as df:
    for line in df:
        line = replace_special_chars(line.strip().split(" ")[0])
        matches = [format_url(line, tld[1:]) for tld in tlds if line.endswith(tld[1:])]
        with open (output_file, "a") as of:
            [of.write(match.lower() + "\n") for match in matches]