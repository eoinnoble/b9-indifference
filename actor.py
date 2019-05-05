import fnmatch
import json
import random
import os

from functools import reduce

from b9_tools import POSifiedText, RangeDict


class Actor(object):
    """
    An actor for whom arbitrary-length sentences and a following speaker can be generated.

    Attributes:
        source_text (list of list): a script comprised of a list of lists formatted [SPEAKER, line]
        name (str):                 speaker name, uppercase
        cast (list of str):         list of cast members you want in your new script
        line_nums (list of num):    all the line numbers from `source_text` in which `name` speaks
        text (str):                 all the lines from `source_text` that `name` speaks
        model (POSifiedText):       a markovify.Text model of `text` for generating sentences from
                                        relationships (RangeDict): used for working out the likely
                                        next speaker by `next_speaker`
        relationships_limit (num):  used as the upper random number limit by `choose_next_speaker`

    """

    def __init__(self, source_text, name, cast, state_size=2):
        self.source_text = source_text
        self.name = name
        self.cast = cast
        self.line_nums, self.text = zip(
            *[
                (line[0], line[1][1])
                for line in enumerate(self.source_text)
                if line[1][0] == self.name
            ]
        )
        self.model = self.get_or_generate_model(self.name, self.text, state_size)
        self.relationships, self.relationships_limit = (
            self.calculate_speaker_relationships()
        )

    @staticmethod
    def get_or_generate_model(name, text, state_size, scripts_location="/scripts/"):
        """
        Retrieve a stored model or generate a new one and store it

        Generating models can be a time-intensive process, especially during testing, but
        thankfully Markovify offers a `to_json()` method for its model objects. I have used a file
        naming convention of ACTOR_STATE-SIZE.JSON, but youcould use whatever you like as long as
        you provide the correct `pattern` to `find`. This method looks for a file of the right name
        or generates the model and saves it to the scripts folder as JSON. It returns a Markovify
        text model either way.

        :param name:             str, name of actor to return model for
        :param text:             list of str, text to train the model on
        :param state_size:       num, state size parameter for the model
        :param scripts_location: str, the folder name of where you're keeping the files
        :return:                 obj, Markovify text model
        """

        current_file_path = os.path.abspath(__file__)
        scripts_directory = os.path.split(current_file_path)[0] + scripts_location

        def find(pattern, path):
            """
            Finds the *first* instance of a file name in a single directory.

            :param pattern: str, file name pattern to search for
            :param path:    str, path to search
            :return:        list of str or empty list, any matching file name ends up in the list
            """
            result = []
            files = [
                f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
            ]
            for file in files:
                if fnmatch.fnmatch(file, pattern):
                    result.append(file)
                    break
            return result

        if find(name + "_" + str(state_size) + ".json", scripts_directory):
            with open(
                scripts_directory + name + "_" + str(state_size) + ".json"
            ) as json_data:
                model_json = json.load(json_data)
            return POSifiedText.from_json(model_json)
        else:
            model = POSifiedText(text, state_size=state_size)
            model_json = model.to_json()
            with open(
                scripts_directory + name + "_" + str(state_size) + ".json", "w"
            ) as json_data:
                json.dump(model_json, json_data, indent=4)
            return model

    def generate_sentence(self, sent_length):
        """
        Generate a sentence from `model` of a given length.

        :param sent_length: int, the maximum desired character length of the returned string
        :return:            str, the sentence string itself
        """
        return self.model.make_short_sentence(
            sent_length, tries=100  # Higher `state_size` will require more `tries`
        )

    def calculate_speaker_relationships(self):
        """
        Work out the likelihood of other `cast` members speaking after `name`.

        :return: RangeDict, ranges and possible speakers; and
                 int, maximum number for the `choose_next_speaker` random number
        """
        rels = {}
        rel_ranges = {}
        for line in self.line_nums:
            try:
                next_speaker = self.source_text[line + 1][0]
                if (
                    next_speaker in self.cast and next_speaker != self.name
                ):  # ignore speakers we don't care about
                    if next_speaker in rels.keys():
                        rels[next_speaker] += 1
                    else:
                        rels[next_speaker] = 1
            except IndexError:
                break

        total_rels = reduce((lambda x, y: x + y), rels.values())
        rel_counter = 0

        # We want a dict that looks like:
        # {
        #     range(0,10): "PICARD",
        #     […],
        #     range(n,`total_rels`): "WHOMEVER"
        # }
        for actor in rels.keys():
            rel_ranges[range(rel_counter, rel_counter + rels[actor])] = actor
            rel_counter += rels[actor]

        return (
            RangeDict(rel_ranges),
            total_rels,  # Need to pass back `total_rels` for `next_speaker`
        )

    def choose_next_speaker(self):
        """
        Decides who should speak next after our current speaker.

        :return: str, name of the person to speak next
        """
        random_num = random.randint(0, self.relationships_limit)
        return self.relationships[random_num]
