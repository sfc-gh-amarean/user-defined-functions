#!/usr/bin/env python

import sys

def greetings(name):
  greet = f"Hello, {name}! How are you doing today? Welcome Valo Team to our Demo!"
  return greet

if __name__ == "__main__":
  name = "Aria Marean"
  if len(sys.argv) > 1:
      name = sys.argv[1] 
  greetings(name)
