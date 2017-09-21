import bibtexparser
import os

with open('test.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)
for entry in bib_database.entries:
    print(entry['title'])
    print(entry['ID'])
    filename = '{}.md'.format(entry['ID'])
    file = open(filename, "w")
    file.write('+++' + os.linesep)
    if 'abstract' in entry:
        file.write('abstract = "{}"'.format(entry['abstract'].replace("$\\backslash$n", "").replace('\n', ' ')) + os.linesep)
    else:
        file.write('abstract = "{}"'.format(''.replace("$\\backslash$n", "").replace('\n', ' ')) + os.linesep)
    file.write('authors = ["{}"]'.format(entry['author'].replace('\n', ' ').replace(" and ", '", "')) + os.linesep)
    if ('month' in entry):
        file.write('date = "{} {}"'.format(entry['month'], entry['year']) + os.linesep)
    else:
        file.write('date = "{}"'.format(entry['year']) + os.linesep)
        
    file.write('type = "publication"' + os.linesep)
    file.write('math = true' + os.linesep)
    if 'journal' in entry:
        file.write('publication = "In {}"'.format(entry['journal'].replace('\n', ' ')) + os.linesep)
    elif 'booktitle' in entry:
        file.write('publication = "In {}"'.format(entry['booktitle'].replace('\n', ' ')) + os.linesep)
    elif 'book' in entry:
        file.write('publication = "In {}"'.format(entry['book'].replace('\n', ' ')) + os.linesep)
    else:
        file.write('publication = "In {}"'.format("") + os.linesep)
    file.write('title = "{}"'.format(entry['title'].replace('\n', ' ')) + os.linesep)
    file.write('url_code = ""'.format() + os.linesep)
    file.write('url_dataset = ""'.format() + os.linesep)
    if 'doi' in entry:
        file.write('doi = "{}"'.format(entry['doi']) + os.linesep)
    if 'url' in entry:
        file.write('url_pdf = "{}"'.format(entry['url']) + os.linesep)
    else:
        if 'doi' in entry:
            file.write('url_pdf = "https://doi.org/{}"'.format(entry['doi']) + os.linesep)
        else:
            file.write('url_pdf = ""' + os.linesep)
    file.write('url_project = ""' + os.linesep)
    file.write('url_slides = ""' + os.linesep)
    file.write('url_video = ""' + os.linesep)
    file.write('tags = [""]' + os.linesep)
    file.write('+++' + os.linesep)
    file.close() 