# Music Open Cli
Basically all you need to do is run the cli.py file with either a link, or something like aDaOgu2CQtI of https://www.youtube.com/watch?v=aDaOgu2CQtI, or the entire link, as value given to the song flag.

Basically,
```bash
python cli.py --song=https://www.youtube.com/watch?v=aDaOgu2CQtI
```
You could also, give a second argument for browser that python's webbrowser module would use. Something like this:
```bash
python cli.py song=https://www.youtube.com/watch?v=aDaOgu2CQtI mozilla
```
P.S. I personally use Chromium
You can run the clean-and-build script in bash to use pyinstaller to create a single executable file, the result of which would be found in 'dist'
You can rename this file to whatever you like, and as long as it's in your PATH, you can type up that command from wherever in your terminal (if you use MAC or Linux) and then use the program as described.

Aside from all this, keep hacking away.
