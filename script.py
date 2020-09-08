import random
import re
import textwrap


class Script(object):
    """
    Generates a script of a certain length, using a variety of cast members.

    Attributes:
        stardate (str):                     date for use in the script, changed by
                                                `increment_stardate`
        length (int):                       desired length of the script
        cast (dict of {str name: `Actor`}): `Actor` instances to be used in the script
        lines_per_ep (int):                 number of lines per "episode", defaults to 1000

    """

    def __init__(self, length, cast, lines_per_ep=1000):
        self.length = length
        self.cast = cast
        self.lines_per_ep = lines_per_ep
        self.stardate = "42353.7"  # The stardate of the first episode of Star Trek: The Next Generation

    def increment_stardate(self):
        """
        Return a stardate for use in the script.

        According to https://en.wikipedia.org/wiki/Stardate, for The Next Generation era:
            A stardate is a five-digit number followed by a decimal point and one more digit.
            Example: "41254.7." The first two digits of the stardate are always "41." The 4 stands
            for 24th century, the 1 indicates first season. The additional three leading digits
            will progress unevenly during the course of the season from 000 to 999. The digit
            following the decimal point is generally regarded as a day counter.

        The stardate of the first episode of season one is 42353.7 according to the scripts, but
        we'll try to adhere to the rest of the rationale for them.

        :return: str, a stardate
        """

        new_stardate = "4"
        additional_digits = int(self.stardate[1:5])
        additional_digits += random.randint(
            20, 50  # Need to be careful not to cause this number to be >4 digits
        )
        day = random.randint(1, 7)
        return f"{new_stardate}{str(additional_digits)}.{str(day)}"

    def generate_episode(self):
        """
        Generates an "episode" for our script.

        This method builds a block of HTML, starting with a `stardate`, and fills it with random
        speakers, who speak a random number of sentences before being followed by a random speaker.
        This continues until `lines_per_ep` is hit, at which point `increment_stardate` is called
        to change the `stardate`.

        :return: str, the episode text
        """

        html = textwrap.dedent(
            f"""\
            <div class='stardate-bar'>
                <div class='stardate-text'>{self.stardate}</div>
                <div class='bar-separator'></div>
            </div>
            """
        )
        next_speaker = None

        while (
            len(list(filter(None, re.split(r"\s+", re.sub(r"<(.*?)>+", "", html)))))
            < self.lines_per_ep
        ):
            next_speaker = next_speaker or random.choice(list(self.cast.keys()))
            # DIRECTION text gets special visual treatment
            if next_speaker == "DIRECTION":
                html += "<p class='direction'>"
                for i in range(0, random.randint(1, 4)):
                    html += (
                        self.cast[next_speaker].generate_sentence(
                            random.randint(100, 150)
                        )
                        + " "
                    )
                html += "</p>\n    "
            else:
                html += textwrap.dedent(
                    f"""\
                    <p class='speaker'>
                        <span class='speaker-name'>{next_speaker}:</span>
                        <span class='speaker-lines'>
                    """
                )
                for i in range(0, random.randint(1, 4)):
                    html += (
                        self.cast[next_speaker].generate_sentence(
                            random.randint(100, 150)
                        )
                        + " "
                    )
                html += "</span></p>\n    "
            next_speaker = self.cast[next_speaker].choose_next_speaker()

        self.stardate = self.increment_stardate()
        return html
