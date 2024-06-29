#!/usr/bin/env python

import random


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
    syllable_patterns = ["vv", "kv", "vk", "kvk"]

    word_syllables = []
    syllable_count = random.choice([2, 3, 4, 5])

    for syllable_id in range(syllable_count):
        patterns_to_choose_from = (
            syllable_patterns if syllable_id != syllable_count - 1 else ["vv", "kv"]
        )
        pattern = random.choice(patterns_to_choose_from)
        syllable = ""

        if "v" in pattern:
            random_vowel = random.choice(vowels)

            if random_vowel in front_vowels:
                vowel_type = "front"
            elif random_vowel in back_vowels:
                vowel_type = "back"
            else:
                vowel_type = "neutral"

        for char in pattern:
            if char == "v":

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

                if random.random() < 0.15:
                    syllable += random.choice(diphthongs_to_choose_from)
                else:
                    syllable += random.choice(vowels_to_choose_from)
            else:
                syllable += random.choice(consonants)
        word_syllables.append(syllable)

    return "".join(word_syllables)


# Test the function

if __name__ == "__main__":
    for _ in range(10):
        print(generate_finnish_word())
