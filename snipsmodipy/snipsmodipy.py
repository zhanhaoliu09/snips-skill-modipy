# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib2
import pprint
import json
from snipsskill-core import login
commandList = {'play' : '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}',
            'get_state' : '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.get_state"}',
            'pause' : '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.pause"}',
            'stop' : '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.stop"}',
            'next' : '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.next"}',
            'previous' : '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.previous"}', 
            'find' : '{"jsonrpc": "2.0", "id": 1, "method": "core.library.search", "params" : {%s} } ',
            'describe' : '{"jsonrpc": "2.0", "id": 1, "method": "core.describe"}'
    
}

def request(url, data):
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    print(type(f))
    pp = pprint.PrettyPrinter(indent=4)
    for x in f:
        d = json.loads(x)
        pp.pprint(d)
    f.close()

def play(url):
    request(url, commandList['play'])
    
def get_state(url):
    request(url, commandList['get_state'])    

def pause(url):
    request(url, commandList['pause'])   
    
def stop(url):
    request(url, commandList['stop'])
    
def skip_track(url):
    request(url, commandList['next']) 
    
def previous_track(url):
    request(url, commandList['next'])

def repeat(url):
    pass

def search_playlist(url, params):
    print(commandList['find'] % (params))
    request(url, commandList['find'] % (params))

class SnipsModipy(object):
    def __init__(self, url):
        self.url = url
        
    def playMusic(self):
        print('play')
        play(self.url)
        
    def pauseMusic(self):
        pause(self.url)
        
    def stopMusic(self):
        print('stop')
        stop(self.url)
    
    def next(self):
        skip_track(self.url)
        
    def previous(self):
        previous_track(self.url)

    def find(self, artist = None, genre = None):
        params = ''
        if (artist != None):
            params += '"artist" : ["%s"]' % artist
        if (genre != None):
            params += '"genre" : ["%s"]' % genre
        print(params)
        search_playlist(self.url, params)
        
        

