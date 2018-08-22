# bookdepository-prices

An application to read a list of books of interest, and fetch their prices from BookDepository.

## Usage

```
usage: bd_prices.py [-h] [-f FILENAME] [-c {EUR,GBP,USD,CHF}]
```

Optional arguments | Description
:----------------- | :----------
`-f,--filename`    | filename containing the paths to books of interest (default: books.txt)
`-c, --currency`   | choice of `{EUR,GBP,USD,CHF}`. currency of the price to return (default: EUR)

## Example output

```
$ python bd_prices.py
title: Python Testing with pytest
  author: Brian Okken
  isbn13: 9781680502404
  price:  29.81 EUR
title: Python for Data Analysis, 2e
  author: Wes McKinney
  isbn13: 9781491957660
  price:  30.45 EUR
title: Automate The Boring Stuff With Python
  author: Al Sweigart
  isbn13: 9781593275990
  price:  20.11 EUR
```

## Configuration

Create a plaintext file containing the `paths` of books of interest from [bookdepository.com](https://www.bookdepository.com).

The `path` is the part after the final `/` in `https://www.bookdepository.com/`.

For example, to get the price for "Python Testing with pytest" by Brian Okken:

* Get the URL for this book
  * `https://www.bookdepository.com/Python-Testing-with-pytest/9781680502404`
* Take note of the `path`
  * `Python-Testing-with-pytest/9781680502404`
* Paste the path into a plaintext file named `books.txt` (or another name of your choice)

An example [`books.txt`](books.txt) is shown below (and also included in this repository):

```
$ cat books.txt
Python-Testing-with-pytest/9781680502404
Python-for-Data-Analysis-2e-Wes-McKinney/9781491957660
Automate-Boring-Stuff-With-Python-Al-Sweigart/9781593275990
```

## Motivation

Prices on BookDepository tend to fluctuate, and so instead of manually having to keep an eye on the prices of many books, this application displays the prices easily, in a single location.

## TODO

- [ ] More robust URL handling in `books.txt`
- [ ] Store a price history database
