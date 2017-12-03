#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 3ngthrust
"""

import billboard
import time

def get_song_set(txtlink):
    # File with a list of songs is converted to a set (no duplicates).
    f = open(txtlink)
    song_str_list = f.read().split('\n')
    song_str_list = [str.lower(s) for s in song_str_list]
    return set(song_str_list)

def return_value(song_str, chart):                                         
    # Run through one chart and return the "value" of the song in this chart.
    for chart_pos, song in enumerate(chart):                              
        if song_str == str.lower(song.title):
            print(song_str + ' ' + str(100-chart_pos))
            # Top cart_pos is 0 -> top position returns 100. 
            # Last position in the hot 100 returns 1.
            return 100-chart_pos
        
    # If the song isnt in the chart the returned value is 0
    return 0
 
    
if __name__ == "__main__":

    # Load the set of songs
    song_str_set = get_song_set('songs_max_martin_02_12_17')
    
    # Calculate the value of the artist
    
    # Init
    values_per_year = dict()
    chart = billboard.ChartData('hot-100')
    year = int(chart.date[:4])
    
    # Check the charts when the artist was active
    while year >= 1995:
        print(chart.date)        
        print(year)
        
        for song_str in song_str_set:
            value = return_value(song_str, chart)
            
            if value:
                if year in values_per_year:
                    values_per_year[year] = values_per_year[year] + value
                else:
                    values_per_year[year] = value

        # Get older chart
        older_chart = billboard.ChartData('hot-100', date=chart.previousDate)
        while len(older_chart)!=100:
            print('Could not download the chart, trying agian in 2 seconds.')
            time.sleep(2)
            older_chart = billboard.ChartData('hot-100', date=chart.previousDate)
            
        chart = older_chart
        year = int(chart.date[:4])
    

    print(values_per_year)
