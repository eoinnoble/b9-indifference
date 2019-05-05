import codecs
import os
import re
import textwrap

from bs4 import BeautifulSoup as Soup

import actor
import script

# Edit this as appropriate to add more people to the final output
CAST = [
    "BEVERLY",
    "COMPUTER",
    "DATA",
    "DIRECTION",
    "GEORDI",
    "PICARD",
    "RIKER",
    "TROI",
    "WESLEY",
    "WORF",
]
CURRENT_FILE_PATH = os.path.abspath(__file__)
SCRIPTS_DIRECTORY = f"{os.path.split(CURRENT_FILE_PATH)[0]}/scripts/"


# Get raw text as string, splitting each line into a two-item list of actor name and text
with open(SCRIPTS_DIRECTORY + "source_scripts.txt") as f:
    all_tng_text = [line.split(" | ") for line in f.readlines()]

if __name__ == "__main__":
    word_count = 0
    while word_count <= 1000:
        word_count = input("Enter an integer wordcount greater than 1000: ")
        try:
            word_count = int(word_count)
            if word_count > 1000:
                break
        except ValueError:
            print(f"{word_count} isn’t an integer…")
            word_count = 0

    with codecs.open(
        f"{os.path.split(CURRENT_FILE_PATH)[0]}/output/output.html", "w", "utf-8"
    ) as output:

        tng_actors = {
            member: actor.Actor(all_tng_text, member, CAST, 3) for member in CAST
        }
        script = script.Script(1000, tng_actors)

        html = textwrap.dedent(
            """\
            <html lang='en'>
                <head>
                    <title>B-9 Indifference</title>
                    <meta charset='UTF-8'>
                    <link href='styles.css' rel='stylesheet'/>
                </head>
                <body>
            """
        )

        while word_count > 0:
            episode_text = script.generate_episode()
            episode_length = len(
                list(
                    filter(
                        None, re.split(r"\s+", re.sub(r"<(.*?)>+", "", episode_text))
                    )
                )
            )
            html += episode_text
            word_count -= episode_length

        html += textwrap.dedent(
            """
            </body>
            </html>
            """
        )

        soup = Soup(html, "html.parser")
        print(soup.prettify(), file=output)
