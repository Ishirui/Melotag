# Melotag
In-depth, remotely accessible tag editor for music libraries.

This project is still *very much* a work in progress: most of the features described below will not be available for a while.

# Concept

This tool is meant to be an in-depth way of tagging and customizing music and audio libraries: album names and art, genre, titles...
Tools like MP3Tag already fill this role, but often lack features I would like to implement here:
  - Regex-based tagging: pull info like title or track number from the filename
  - Remote edition: I stream most of my music from my Plex media server, which doesn't let me *modify* the tags of my music.I would like this tool to feature a web interface for uploading and tagging music from a remote client.
  - Filesystem integration: automatically sort tracks in the library based on their tags. For example, every track could be found at the path root/Artist/Album/tracktitle.mp3. *Note: Multi-Artist albums might make this difficult*
  - Multi-platform: as I mentioned, the idea is for it to primarily be a server-based, web-accessed app. But I also would like to have dedicated mobile and desktop clients.
  
Eventually, the project could also move to be a dedicated music playback platform, kind of like Plex but only for music (especially since Plex isn't great for music on mobile...)

# Roadmap

- [] Scripts for basic edition
- [] Basic UI
- [] Advanced features: Regex-based tagging, filesystem integration...
- [] Dockerization, basic web interface
- [] Improve the web interface
- [] Probably other stuff including huge refactors along the way but hey, we'll see.

# Architecture

Python for the scripts, as it's what I know best. 
For the web-based stuff, I might just do a basic front-end in Vanilla JS, maybe React for the most advanced one. I could then use React native for the mobile app and Electron for the desktop. Might also be a good idea to transition the backend to Node at that point. Or maybe keep the Python and use Django ? ¯\_(ツ)_/¯


# Note

This is my first "large-scale" programming project, and one of my first web-based ones. The code will probably terrible, and the architectural choices even worse. 
This is also something I'm doing for fun, and primarily for me (since i could really use something like that !).
Please don't diss me, but please do offer criticism and/or advice ! It would really help me out 😊
