# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:
# Started 7 May 2023 by zyteo
# Completed x May 2023

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


# -----------------------------------------------------------------------

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================


def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret


# ======================
# Data structure design
# ======================

# Problem 1


# TODO: NewsStory
# ●globally unique identifier (GUID) - a string
# ●title - a string●description - a string
# ●link to more content - a string
# ●pubdate - a datetime
# We want to store this information in an object that we can then pass around in the rest of our program. Your task, in this problem, is to write a class, NewsStory , starting with a constructor that takes ( guid, title, description, link, pubdate ) as argumentsand stores them appropriately. NewsStory also needs to contain the following methods:
# ●get_guid(self)
# ●get_title(self)
# ●get_description(self)
# ●get_link(self)
# ●get_pubdate(self)
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


# ======================
# Triggers
# ======================


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# PHRASE TRIGGERS


# Problem 2
# TODO: PhraseTrigger
# Implement a phrase trigger abstract class, PhraseTrigger .
# It should take in a string phraseas an argument to the class's constructor. This trigger should not be case-sensitive (it should treat "Intel" and "intel" as being equal).
# PhraseTrigger should be a subclass of Trigger . It has one new method,is_phrase_in , which takes in one string argument text.
# It returns True if the whole phrasephrase is present in text,
# False otherwise, as described in the above examples.
#  Thismethod should not be case-sensitive.
# Implement this method. Because this is an abstract class, we will not be directly instantiating any PhraseTriggers .
# PhraseTrigger should inherit its evaluate method from Trigger .
# We do this because nowwe can create subclasses of PhraseTrigger that use its is_phrase_in function.✦✦✦✦You are now ready to implement PhraseTrigger 's two subclasses: TitleTrigger andDescriptionTrigger .
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, text):
        # need to compare phrase to text
        # first convert both to lowercase
        # then split text into words
        # remove punctuation from text with replace
        # then join text back into a string
        # compare phrase to text
        # if phrase in text, return True
        # else return False
        phrase = self.phrase.lower()
        text = text.lower()
        text = text.split()
        # create a new list to store words
        new_text = []
        # get list of punctuation
        punctuation = string.punctuation
        for word in text:
            # check if there are alphabets between punctuation
            # if there are, remove punctuation and replace with space
            # else, remove punctuation
            # bee&$pop##@pie
            alphabet_sandwich_count = [0]
            current_type = None
            first_type = None
            changes = 0
            for index in range(len(word)):
                # for the very first index, set current type and first type
                if index == 0:
                    if word[index] in punctuation:
                        current_type = "punctuation"
                        first_type = "punctuation"
                        alphabet_sandwich_count[changes] += 1
                    else:
                        current_type = "alphabet"
                        first_type = "alphabet"
                        alphabet_sandwich_count[changes] += 1
                else:
                    if word[index] in punctuation:
                        if current_type == "punctuation":
                            alphabet_sandwich_count[changes] += 1
                        else:
                            changes += 1
                            current_type = "punctuation"
                            alphabet_sandwich_count.append(1)
                    else:
                        if current_type == "alphabet":
                            alphabet_sandwich_count[changes] += 1
                        else:
                            changes += 1
                            current_type = "alphabet"
                            alphabet_sandwich_count.append(1)
            # if there are more than 1 changes, then there are alphabets between punctuation
            if changes > 1:
                # now remove punctuation. check what first type is
                if first_type == "alphabet":
                    # make use of alphabet_sandwich_count to remove punctuation and replace with space
                    for i in range(len(alphabet_sandwich_count)):
                        if i % 2 == 0:
                            # even index means alphabet
                            # do nothing
                            pass
                        else:
                            # get the number of punctuation to remove
                            num_punctuation = alphabet_sandwich_count[i]
                            # get the index of the punctuation by summing up the previous numbers
                            index = sum(alphabet_sandwich_count[:i])
                            # remove the punctuation
                            word = word[:index] + " " + word[index + num_punctuation :]
                else:
                    if i % 2 == 0:
                        # if i = 0, replace with "" instead of " " as "$$test#pop" need to be "test pop"
                        if i == 0:
                            num_punctuation = alphabet_sandwich_count[i]
                            word = "" + word[num_punctuation :]
                        else:
                            # remove punctuation
                            num_punctuation = alphabet_sandwich_count[i]
                            index = sum(alphabet_sandwich_count[:i])
                            word = word[:index] + " " + word[index + num_punctuation :]
                    else:
                        # do nothing
                        pass
                word = word.split()
                for i in word:
                    new_text.append(i)
            else:
                # remove punctuation
                for i in punctuation:
                    if i in word:
                        word = word.replace(i, "")
                new_text.append(word)

        text = " ".join(new_text)
        if phrase in text:
            # split phrase into words, then check if each word is in text.
            # needs to be consecutive
            phrase = phrase.split()
            # get index of first word in phrase
            index = new_text.index(phrase[0])
            # check each word in phrase
            for word in phrase:
                if word == new_text[index]:
                    index += 1
                else:
                    return False
            return True
        else:
            return False


# Given some text, the trigger should fire only when each word in the phrase is present in its entirety and appears consecutively in the text, separated only by spaces or punctuation. The trigger should not be case sensitive. For example, a phrase trigger with the phrase "purple cow" should fire on the following text snippets:
# ●'PURPLE COW'
# ●'The purple cow is soft and cuddly.'
# ●'The farmer owns a really PURPLE cow.'
# ●'Purple!!! Cow!!!'
# ●'purple@#$%cow'
# ●'Did you see a purple cow?'
# But it should not fire on these text snippets:
# ●'Purple cows are cool!'
# ●'The purple blob over there is a cow.'
# ●'How now brown cow.'
# ●'Cow!!! Purple!!!'
# ●'purplecowpurplecowpurplecow'

# test phrase trigger
phrase = "Intel"
text = "Intel is a company"
phrase_trigger = PhraseTrigger(phrase)
# print(phrase_trigger.is_phrase_in(text))

phrase2 = "purple cow"
text2 = "Purple!!! Cow!!!"
phrase_trigger2 = PhraseTrigger(phrase2)
# print(phrase_trigger2.is_phrase_in(text2))

# all these should return True
text3 = "The purple cow is soft and cuddly."
text4 = "The farmer owns a really PURPLE cow."
text5 = "purple@#$%cow"  # need to account for this
text6 = "Did you see a purple     cow?"
# print("text3", phrase_trigger2.is_phrase_in(text3))
# print("text4", phrase_trigger2.is_phrase_in(text4))
# print("text5", phrase_trigger2.is_phrase_in(text5))
# print("text6", phrase_trigger2.is_phrase_in(text6))
# all these should return False
text7 = "Purple cows are cool!"
text8 = "The purple blob over there is a cow."
text9 = "How now brown cow."
text10 = "Cow!!! Purple!!!"
text11 = "purplecowpurplecowpurplecow"
# print("text7", phrase_trigger2.is_phrase_in(text7))
# print("text8", phrase_trigger2.is_phrase_in(text8))
# print("text9", phrase_trigger2.is_phrase_in(text9))
# print("text10", phrase_trigger2.is_phrase_in(text10))
# print("text11", phrase_trigger2.is_phrase_in(text11))

# Problem 3
# TODO: TitleTrigger

# Problem 4
# TODO: DescriptionTrigger

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6
# TODO: BeforeTrigger and AfterTrigger


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


# ======================
# Filtering
# ======================


# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories


# ======================
# User-Specified Triggers
# ======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, "r")
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith("//")):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines)  # for now, print it so you see what it contains!


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        # triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify="center")
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(
                    END,
                    "\n---------------------------------------------------------------\n",
                    "title",
                )
                cont.insert(END, newstory.get_description())
                cont.insert(
                    END,
                    "\n*********************************************************************\n",
                    "title",
                )
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=" ")
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
