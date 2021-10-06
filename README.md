# Kijiji-Monitor
A request based monitor for new Kijiji listings.

Scrapes the newest listings off the FIRST page of whatever Kijiji catergory URL it is set to monitor.

You must generate the website URLs yourself through the Kijiji website. Set up all your preferences and copy the link given by Kijiji by the website.


(Example)

https://www.kijiji.ca/b-nintendo-ds/city-of-london/pokemon/l5t72621750472?ll=31.686795%2C-23.012845&address=123+testing+lane+London+ON+H0+H0H+Canada&radius=50.0

Possible Errors
- The monitor may not pick up all new listings as it only scrapes the first page of the URL you give it. It will not work very well with very popular/broad preferences.
- The monitor may crash if a request takes too long to reach the website
