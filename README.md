# Morse communicator
>A simple implementation of morse code for Pi (via gpiozero) and Arduino
***
## Pi version
Features:
- Beautiful hashtable
- Morse encodings are stored in standard format, _ = dah, . = dit
- Outputs to python console
- Message is provided by a simple string; change the string to change the message.
- Trivially adjustable time units
- Extendable encoding table; to add any character (unicode, numbers, capital letters, emoji) just add a single entry to the dict

## Arduino version
Features:
- Gnarly switch statement
- Outputs to serial terminal
- Message is provided by simple string, as above
- Trivially adjustable time units
- Time units can be specified in milliseconds, or words per minute
- Supports auditory output via a piezo speaker
- Trivially and individually adjustable tone frequencies - differentiate your dits and dahs by more than just their length

Note: If you want to use automatic Morse audio recognition, set the frequency on dit and dah to the same value.

Both files are fully commented, and readability was emphasized over size or operational efficiency since it's such a simple program. So they should be easy and fun to tweak if you want to add support for e.g. oscillators.
