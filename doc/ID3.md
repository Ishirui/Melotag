# ID3 tags
The tags used to specify track info in mp3 files are called ***ID3 tags***. You can read more about them [here](https://en.wikipedia.org/wiki/ID3), [here](https://id3.org/Developer%20Information) and also most importantly [here](https://id3.org/id3v2.3.0)

One caveat is that they are *only* for mp3 files: FLACs, OGGs etc. use a different format.

# Implementation
To become format-agnostic, we will implement an abstract "track" class containing all the tags which we want to support - that list being based on the ID3 tags just below.
This will allow us to easily write "save" functions for saving all of this info to the different file formats without having to rewrite functions for each format.
But reading and writing tags, raw file manipulation will not be re-implemented here, we'll use libraries instead (this is Python !)

# Tag list

All tags specified in the ID3 standard can be found [here](https://id3.org/id3v2.3.0#Declared_ID3v2_frames). A lot aren't really useful, so we'll only support a subset:

- APIC (Attached Picture) *(cover art)*
- COMM (Comments)
- TALB (Album title)
- TIT2 (Track title)
- TIT3 (Track subtitle)
- IPLS (Involved people list) - authors, basically. Use instead of TPE1..4 ?
- TLAN (Language)
- PCNT (Play Counter)
- TBPM (BPM)
- TCOM (Composer)
- TEXT (Lyricist)
- TPUB (Publisher)
- TRCK (Track Number)
- TDAT (Date)


It might be cool to eventually support:

- EQUA (Equalization) - need to implement an actual equalizer !
- RVAD (Relative Volume Adjustment)
- RVRB (reverb) -- have to see if these 3 actually do anything in most media players
- SYLT (Synchronized lyric/text) - might not be to useful, since very tedious to do by hand
- USLT (Unsynchronized lyric/text transcription) - probably a safer bet
- TPE1..4 (Lead performer(s)/Soloist(s) ; Band/orchestra/accompaniment ; Conductor/performer refinement ; Interpreted, remixed, or otherwise modified by)

