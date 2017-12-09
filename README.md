# chart_success.py
A script to evaluate the chart success of an artist, writer or producer on a billboard chart over the years. 

The simple metric calculated is as follows: A no. 1 song is valued as 100, a no. 2 song is valued as 99, etc., a no. 100 song is valued as 1. All song values of each chart of each year are added together.

A more accurate version of this which also thakes the artists into account is implemented in [calculate-chart-success-2](https://github.com/3ngthrust/calculate-chart-success-2).

Usage
-----
1. Create a list of all the songs the person you want to evaluate worked on. Go to the discography of this person on Wikipedia. Select the whole table with the songs (Ctrl+C). Copy the table to libre office (Ctrl+V). Select the column with the song titles in libre office. Copy them (Ctrl+C) in libre and paste them into an an editor. Remove empty lines (Regex to find the lines: ^\n) and ". The result should be a list like the example 'songs_max_martin_02_12_17' here.

2. Adapt the year until the charts are fetched and the address of the text file in chart_success.py and run the script

3. Plot the results, a example is provided in visualisation.py

Dependencies
------------
This script uses [billboard.py](https://github.com/guoguo12/billboard-charts) from [guoguo12](https://github.com/guoguo12). 

Example
-------
All the songs Max Martin contributed to (according to his Wikipedia discography writer and/or producer) are listed in 'songs_max_martin_02_12_17'. (Duplicates do not matter, since they are removed in the script.) 

![](https://raw.githubusercontent.com/3ngthrust/calculate-chart-success/master/Max_Martin_Chart_Success.png)

The value for 1995 should be zero, but three identically named songs from other artists 'Creep' (TLC), 'I Believe' (Robson & Jerome) and 'I kissed a girl' (Jill Sobule) are counted as seen in 'output_max_martin_02_12_17'. Because of reused song titles occasional extra points have to be expected.
