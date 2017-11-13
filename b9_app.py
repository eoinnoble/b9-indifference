from __future__ import print_function

import codecs
import os
import re

from bs4 import BeautifulSoup as Soup

import actor, script


current_file_path = os.path.abspath(__file__)
scripts_directory = os.path.split(current_file_path)[0] + "/scripts/"

# Get raw text as string, splitting each line into a two-item list of actor name and text
with open(scripts_directory + "source_scripts.txt") as f:
    all_tng_text = [line.split(" | ") for line in f.readlines()]

# Edit this as appropriate to add more people to the final output
cast = [
    "BEVERLY",
    "COMPUTER",
    "DATA",
    "DIRECTION",
    "GEORDI",
    "PICARD",
    "RIKER",
    "TROI",
    "WESLEY",
    "WORF"
]

if __name__ == "__main__":
    count = None
    while not count:
        count = input("Enter an integer wordcount greater than 1000: ")  # TODO: verify `count` is over 1000
        try:
            int(count)
            count = int(count)
            break
        except ValueError:
            print("%s isn’t an integer…" % count)
            count = None

    output = codecs.open(os.path.split(current_file_path)[0] + "/output/output.html", "w", "utf-8")

    tng_actors = {member: actor.Actor(all_tng_text, member, cast, 3) for member in cast}
    html = "<html lang='en'>\n    <head>\n        <title>B-9 Indifference</title>\n        " + \
           "<link href='styles.css' rel='stylesheet'/>\n    </head>\n    <body>"

    word_count = count
    script = script.Script(1000, tng_actors)
    while word_count > 0:
        episode_text = script.generate_episode()
        episode_length = len(list(filter(None, re.split(r'\s+', re.sub(r'<(.*?)>+', '', episode_text)))))
        html += episode_text
        word_count -= episode_length

    html += "</body>\n</html>"

    soup = Soup(html, 'html.parser')
    print(soup.prettify(), file=output)
    output.close()
