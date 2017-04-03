# lru-cache

To run this program type have python 2.7 installed & type `python main.py` into your terminal.

Begin by initializing the cache size by enter 'SIZE <n>', where n is the number of items the cache can store.
If n is invalid, the program will respond with 'ERROR' and terminate.

Set items with a line giving the key and value, separated by a space, 
the program will respond with 'SET OK'.

Invalid 'SET's will receive a response of 'ERROR' yet the program will continue.

Get items with a line giving the key requested, the program will respond with the previously stored value, for example “GOT foo”. If the the key is not in the cache, it will reply with “NOTFOUND”.

Enter 'EXIT' to terminate.
