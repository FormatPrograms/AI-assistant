This is my first "project" that I didn't steal.

This is an AI system designed to:
- Take mic input and convert it into an AI generated response.
- speak the generated response as TTS.
- preform any extra functions.


PI files:
- assistant_response.py
- pyspeak.py
- ____init____.py

Server files:
- assistant.py
- entgrak.py

Planned:
port this to windows, because on windows it basically makes my tts module redundant due to the fact that windows has better espeak voices than linux.
might just straight up make my gaming pc into a windows server.
might look into the programming of speech recogniton and find the optimal settings for my mic, or reverse engineer it and make it a little better for my system.
mobile compatability, probably will use the same tts as the pi (android is just linux for phones so theoretically the voices are the same)
preformance enhancement, it's a little slow to generate a response right now. so I'm thinking, instead of having the pi process the voice and play it. it just recieves 
a .mp3 plays it then deletes it.
