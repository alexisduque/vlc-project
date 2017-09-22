import bibtexparser
import os
import requests
import json
import sys
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding
from bibtexparser.customization import convert_to_unicode

# curl -LH "Accept: application/x-bibtex;q=1" https://doi.org/10.1126/science.169.3946.635
with open('test.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    #parser.customization = homogeneize_latex_encoding
    bib_database = bibtexparser.loads(bibtex_str, parser=parser)
    for entry in bib_database.entries:
        print(entry['title'])
        print(entry['ID'])
        filename = '{}.md'.format(entry['ID'])
        file = open(filename, "w")
        file.write('+++' + os.linesep)

        if 'doi' in entry:
            file.write('doi = "{}"'.format(entry['doi']) + os.linesep)
            # doi = entry['doi']
            # url = 'https://doi.org/10.1126/{}'.format(doi)
            # myResponse = requests.get(url, headers={'Accept': 'application/x-bibtex;q=1'}, verify=True)
            # if(myResponse.ok):
            #     result = str(myResponse.content, 'utf-8')
            #     bib_database = bibtexparser.loads(result, parser=parser)
            #     print(bib_database.entries)
            #     entry = bib_database.entries[0]

        if 'abstract' in entry:
            file.write('abstract = "{}"'.format(entry['abstract'].replace("$\\backslash$n", "").replace('\n', ' ')) + os.linesep)
        else:
            file.write('abstract = "{}"'.format(''.replace("$\\backslash$n", "").replace('\n', ' ')) + os.linesep)
        file.write('authors = ["{}"]'.format(entry['author'].replace('\n', ' ').replace(" and ", '", "')) + os.linesep)

        if ('month' in entry):
            file.write('date = "{} {}"'.format(entry['month'], entry['year']) + os.linesep)
        elif ('year' in entry):
            file.write('date = "{}"'.format(entry['year']) + os.linesep)
        else:
            file.write('date = "{}"'.format('' + os.linesep))
            
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