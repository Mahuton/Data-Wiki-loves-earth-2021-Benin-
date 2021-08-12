#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
import json

#r = requests.get('https://api.github.com/events')
limit = 50
files_list = []
next_page2 = True
nexts = []
file_concat  = ''
next_page = ''

def get_pages():
    """get files in category wiki loves earth 21 in Benin"""
    global next_page
    global next_page2
    global file_concat
    payload = {
        'action': 'query',
        'list': 'categorymembers',
        'format':'json',
        'cmtitle': 'Category:Images_from_Wiki_Loves_Earth_2021_in_Benin',
        'cmcontinue': next_page,
        'cmlimit': limit}
    r = requests.get('https://commons.wikimedia.org/w/api.php', params=payload)
    y = json.loads(r.text)
    if 'continue' in y:
        print(y['continue']['cmcontinue'])
        next_page = y['continue']['cmcontinue']
    else:
        next_page2 = False
        
    cat_members = y['query']['categorymembers']
    for elts in cat_members:
        files_list.append(elts['title'])


def get_user():
    """ Get users  from files """
    global file_concat
    for j in files_list:
        file_concat+=j+ '|'
    files = file_concat[:-1]
    payload2 = {
    'action': 'query',
    'titles': files,
    'format':'json',
    'prop': 'imageinfo',
    'iiprop':'url|user'}
    
    r2 = requests.get('https://commons.wikimedia.org/w/api.php', params=payload2)
    response = json.loads(r2.text)
    if 'query' in response:
        for i in response['query']['pages']:
            title = imageinfos = response['query']['pages'][i]['title']
            #print(title)
            try:
                g = open('files.txt', 'a')
                g.write(title + '\n')
                g.close()
            except UnicodeEncodeError:
                print(title)

            if 'Category:' not in title: 
                imageinfos = response['query']['pages'][i]['imageinfo']
                for j in imageinfos:
                    user = j['user']
                    url = j['url']
                    #print(user)
                    try:
                        f = open('user.txt', 'a')
                        f.write(user + '\n')
                        f.close()
                        
                        h = open('urls.txt', 'a')
                        h.write(url + '\n')
                        h.close()
                        
                        del files_list[:]
                        file_concat  = ''
                    except UnicodeEncodeError:
                        print(user)

def main():
    counter = 0
    while next_page2 == True:
        print(counter)
        get_pages()
        get_user()
        counter+=1
    
# Call main function
if __name__ == '__main__':
    main()
    
    