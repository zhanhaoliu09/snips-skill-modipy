# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib2

def request(url, data):
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    for x in f:
        print(x)
    f.close()

def play(url):
    data = '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.play"}'
    request(url, data)
    
def get_state(url):
    data = '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.get_state"}'
    request(url, data)    

def pause(url):
    data = '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.pause"}'
    request(url, data)   
    
def stop(url):
    data = '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.stop"}'
    request(url, data)
    
def skip_track(url):
    data = '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.next"}'
    request(url, data) 
    
def previous_track(url):
    data = '{"jsonrpc": "2.0", "id": 1, "method": "core.playback.previous"}'
    request(url, data)

def repeat(url):
    pass

def search_playlist(url):
    pass

class SnipsModipy(object):
    def __init__(self, url):
        self.url = url
        
    def playMusic(self):
        play(self.url)
        
    def pauseMusic(self):
        pause(self.url)
        
    def stopMusic(self):
        stop(self.url)
    
    def next(self):
        skip_track(self.url)
        
    def previous(self):
        previous_track(self.url)
        
        

