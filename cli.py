import click
import webbrowser

@click.command()
@click.option('--song', help='Selects the song to open')
@click.argument('browser', default='chromium')

# @click.argument('link', help='Selects the link to open')
def open_song(song, browser):
    if type(song).__name__ != 'str' or len(song) == 0:
        raise ValueError('Must provide a link')
    elif type(browser).__name__ != 'str' or len(browser) == 0:
        raise ValueError('Browser name must be a valid string')
    else:
        final_url = ''
        if song.startswith('http'):
            final_url = song
        else:
            final_url = "https://youtu.be/{}".format(song)
        webbrowser.get(browser).open_new_tab(final_url)

if __name__ == '__main__':
    open_song()
