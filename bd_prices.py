#!/usr/bin/env python
"""scrape book prices from bookdepository.com"""
import argparse
import time

import requests
from bs4 import BeautifulSoup


def main(args: argparse.Namespace) -> None:
    """main entry point for the application."""
    base_url = 'https://www.bookdepository.com'

    with open(args.filename, 'rt') as f:
        paths = [path.strip() for path in f]

    for path in paths:
        url = f'{base_url}/{path}'

        r = requests.post(url, data={'selectCurrency': args.currency})

        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            print(f'got status_code {r.status_code}. Exiting.')
            # return a non-zero exit code
            return 1

        bs_obj = BeautifulSoup(r.text, 'html.parser')

        # extract the title, author and isbn13 from the html
        title = bs_obj.find('h1', {'itemprop': 'name'})
        author = bs_obj.find('span', {'itemprop': 'name'})
        isbn13 = url.rsplit('/')[-1]

        # extract the price
        sale_price = bs_obj.find('span', {'class': 'sale-price'})
        # some string formatting of the price
        price = format_price(sale_price.text)

        # display the results
        print(f'title: {title.text}')
        print(f'  author: {author.text.strip()}')
        print(f'  isbn13: {isbn13}')
        print(f'  price:  {price:.2f} {args.currency}')

        time.sleep(1)


def format_price(price: str) -> str:
    """Clean up the price scraped from the website."""
    if price[0] == '£':
        formatted_price = float(price[1:])
    elif price[:3] == 'US$':
        formatted_price = float(price[3:])
    elif price[-1] == '€':
        formatted_price = float(price[:-1].replace(',', '.'))
    else:
        raise ValueError('unsupported currency')

    return formatted_price


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='scrape book prices from bookdepository.com',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-f',
        '--filename',
        default='books.txt',
        help='filename containing the paths to books of interest',
    )
    parser.add_argument(
        '-c',
        '--currency',
        choices=['EUR', 'GBP', 'USD', 'CHF'],
        default='EUR',
        help='currency of the price to return',
        type=str.upper,
    )

    args = parser.parse_args()
    main(args)
