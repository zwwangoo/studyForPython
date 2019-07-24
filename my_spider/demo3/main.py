import os
from search import get_detail_url, get_search_result
from gene import get_page, parse_page


def main():
    info = get_detail_url(get_search_result('brca1'))
    item = next(info)
    print(item)
    if os.path.exists('transcripts-{}.txt'.format(item['name'])):
        return
    transcripts = parse_page(get_page(item['url']))
    with open('transcripts-{}.txt'.format(item['name']), 'w+') as f:
        for transcript in transcripts:
            f.write('\n' + str(transcript))


if __name__ == '__main__':
    main()
