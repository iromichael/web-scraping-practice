# Countries of the World - Simple Scrape

Source: https://www.scrapethissite.com/pages/simple/

## What it does
Scrapes the page listing 250 countries and grabs name, capital, population, 
and area for each one. Saves it all to a CSV.

## How
Each country is inside its own `div.country`. Looped through each div and 
grabbed the name, capital, population, area from the tags inside it 
(h3.country-name, span.country-capital, etc). Built the DataFrame from a 
dict instead of rows this time.

## Things I practiced
- searching inside a specific tag instead of the whole page (avoids mixing 
  up data between countries)
- get_text(strip=True) for cleaning text
- to_csv with index=False