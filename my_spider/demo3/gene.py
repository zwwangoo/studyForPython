import requests
from lxml import etree

url = 'https://www.ensembl.org/Homo_sapiens/Transcript/Summary?db=core;g=ENSG00000166845;r=18:54358585-54382032;t=ENST00000300091'  # noqa


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; '
        'en-us) AppleWebKit/534.50 (KHTML, like Gecko) '
        'Version/5.1 Safari/534.50',

    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_page(text):
    html = etree.HTML(text)
    table = html.xpath('//table[@id="transcripts_table"]')[0]
    rows = table.xpath('tbody/tr')

    for row in rows:
        transcript = dict()
        name = row.xpath('td[1]/text()')
        transcript['name'] = name[0]

        transcript_id = row.xpath('td[2]/a/text()')
        transcript['transcript_id'] = transcript_id[0]

        bp = row.xpath('td[3]/text()')
        transcript['bp'] = bp[0]

        protein = row.xpath('td[4]/a/text()')
        if not protein:
            protein = row.xpath('td[4]/text()')
        transcript['protein'] = protein[0] if protein else ''

        biotype = row.xpath(
            'td[6]/div/div/text()',
        )
        if not biotype:
            biotype = row.xpath(
                'td[6]/div/div/span/text()',
            )

        transcript['biotype'] = biotype[0] if biotype else ''

        ccds = row.xpath('td[7]/a/text()')
        transcript['ccds'] = ccds[0] if ccds else ''

        uniprot = row.xpath('td[8]/a/text()')
        transcript['uniprot'] = uniprot[0] if uniprot else ''

        refseq_match = row.xpath('td[9]/a/text()')
        transcript['refseq_match'] = refseq_match[0] if refseq_match else ''

        flags = row.xpath('td[10]/span/span[contains(@class, "ht")]/text()')
        transcript['flags'] = [flag for flag in flags]

        yield transcript


for transcript in parse_page(get_page(url)):
    print(transcript)
