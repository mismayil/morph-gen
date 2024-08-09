#!/usr/bin/env python

import random
import re

import click


def generate_finnish_word():
    front_vowels = {"i", "ä", "ö", "y"}
    back_vowels = {"u", "a", "o"}
    neutral_vowels = {"e"}
    vowels = list(front_vowels | back_vowels | neutral_vowels)

    neutral_diphthongs = [
        "ee",
        "ei",
        "eu",
        "ey",
    ]
    front_diphthongs = [
        "ää",
        "äi",
        "äy",
        "ii",
        "iy",
        "iu",
        "öi",
        "öö",
        "öy",
        "yi",
        "yy",
    ]
    back_diphthongs = [
        "aa",
        "ai",
        "au",
        "oi",
        "oo",
        "ou",
        "ui",
        "uu",
    ]
    consonants = "ktpnsmlrhjv"
    syllable_patterns = ["v", "vv", "kv", "vk", "kvk"]
    syllable_pattern_weights = [0.1, 0.2, 0.2, 0.4, 0.1]

    word_syllables = []
    syllable_count = random.choice([2, 3, 4])

    vowel_type = random.choice(["front", "back", "neutral"])

    for syllable_id in range(syllable_count):

        if syllable_id != syllable_count - 1:
            patterns_to_choose_from = syllable_patterns
            syllable_pattern_weights = syllable_pattern_weights
        else:
            patterns_to_choose_from = ["k", "v"]
            syllable_pattern_weights = [0.5, 0.5]

        pattern = random.choices(
            patterns_to_choose_from, weights=syllable_pattern_weights, k=1
        )[0]
        syllable = ""

        for char in pattern:
            if char == "v":

                vowels_to_choose_from = list(
                    {
                        "front": front_vowels,
                        "back": back_vowels,
                        "neutral": neutral_vowels,
                    }[vowel_type]
                )

                # cannot choose sam vowel as previous syllable ends with

                if syllable_id > 0:
                    remove_this = word_syllables[syllable_id - 1][-1]
                    vowels_to_choose_from = [
                        v for v in vowels_to_choose_from if v != remove_this
                    ]

                    if len(vowels_to_choose_from) == 0:
                        vowels_to_choose_from = list(
                            {
                                "front": front_vowels,
                                "back": back_vowels,
                                "neutral": neutral_vowels,
                            }[vowel_type]
                        )

                diphthongs_to_choose_from = list(
                    {
                        "front": front_diphthongs,
                        "back": back_diphthongs,
                        "neutral": neutral_diphthongs,
                    }[vowel_type]
                )

                if random.random() < 0.1:
                    syllable += random.choice(diphthongs_to_choose_from)
                else:
                    syllable += random.choice(vowels_to_choose_from)
            else:
                syllable += random.choice(consonants)

        word_syllables.append(syllable)

    candidate_word = "".join(word_syllables)

    # if word contains triple vowel, redo the call to this function
    conditions = [re.search(r"[aeiouyäö]{3}", candidate_word)]

    if any(conditions):
        return generate_finnish_word()

    else:
        return candidate_word


@click.command()
@click.option("--n-words", "-n", type=int, default=10)
def main(n_words):
    for _ in range(n_words):
        print(generate_finnish_word())


if __name__ == "__main__":
    main()