# The Missing 11th of the Month

This is the code behind a [blog post](http://drhagen.com/blog/the-missing-11th-of-the-month/) detailing why the 11th of the month (January 11th, February 11th, etc.) appears less often than other days of the month as pondered in an [xkcd comic](https://xkcd.com/1140/).

# Dependencies

* [matplotlib](http://github.com/matplotlib/matplotlib)
* [pandas](http://github.com/pydata/pandas)
* [requests](http://github.com/kennethreitz/requests)
* [scipy](https://www.scipy.org/) (small section)

# Usage

Run `summarize_data.py` to produce the graphs found in the blog post.

If you do not trust the associated .csv files or simply want to see how the data is fetched from the database, check out `fetch_and_save.py`. Note that you cannot run this entire file at once or Google will cut your IP address off for a while.

# License

All code is made available under the MIT license. See license.txt.

The getngrams.py file comes from [Matt Nicklay](https://github.com/econpy/google-ngrams) and is also available under an MIT license. See license_getngrams.txt.
