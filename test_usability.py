from brass import BRASS
import os
import random
import time

api_key = os.environ["POE_API_KEY"]
bot_list = ["ChatGPT", "Claude", "Claude-2", "Claude-3-H", "Claude-3-O", "Claude-3-S", "Gemini-1.0", "Gemini-1.5", "GPT4", "GPT4o", "Llama", "Mixtral", "MythoMax"]
bots = {}
for bot_name in bot_list:
    bots[bot_name] = BRASS(api_key, bot_name)

def conceptualize_test():
    global bots  
    constructs = [
        "Perceived Ease of Use",
        "Perceived Usefulness",
        "Large Language Model Privacy Concern",
        "Internet Privacy Concern",
        "Collection (in Internet Privacy Concern)",
        "Secondary Usage (in Internet Privacy Concern)",
        "Errors (in Internet Privacy Concern)",
        "Improper Access (in Internet Privacy Concern)",
        "Control (in Internet Privacy Concern)",
        "Awareness (in Internet Privacy Concern)",
        "IT Mindfulness",
        "Alertness to Distinction (in IT Mindfulness)",
        "Awareness of Multiple Perspectives (in IT Mindfulness)",
        "Openness to Novelty (in IT Mindfulness)",
        "Orientation in the Present (in IT Mindfulness)",
        "Cognitive Absorption",
        "Computer Playfulness",
        "Flow",
        "IT Habit",
        "Personal Innovativeness in IT"
    ]
    
    for construct in constructs:
        prompt = '''/conceptualize "%s"''' % construct
        print(prompt)

        for bot_name in bots:
            while True:
                try:
                    out = bots[bot_name].query(prompt)
                    with open("output/usability/conceptualize_%s.txt" % bot_name, "a") as f:
                        f.write("======= %s =======\n%s\n\n" % (prompt, out))
                    break
                except Exception:
                    time.sleep(10)            

    print("Done")

def item_test():
    global bot1, bot2, bot3    
    constructs = [
        "Perceived Ease of Use",
        "Perceived Usefulness",
        "Large Language Model Privacy Concern",
        "Internet Privacy Concern",
        "IT Mindfulness"
    ]

    for construct in constructs:
        prompt = '''/item-verbose "%s" 5''' % construct
        print(prompt)

        for bot_name in bots:
            while True:
                try:
                    out = bots[bot_name].query(prompt)
                    with open("output/usability/item_%s.txt" % bot_name, "a") as f:
                        f.write("======= %s =======\n%s\n\n" % (prompt, out))
                    break
                except Exception:
                    time.sleep(10)

    print("Done")

def sort_test():
    global bot1, bot2, bot3
    constructs = [
        "Collection (in Internet Privacy Concern)",
        "Secondary Usage (in Internet Privacy Concern)",
        "Errors (in Internet Privacy Concern)",
        "Improper Access (in Internet Privacy Concern)",
        "Control (in Internet Privacy Concern)",
        "Awareness (in Internet Privacy Concern)"
    ]
    items = [
        "It usually bothers me when commercial/government websites ask me for personal information.",
        "When commercial/government websites ask me for personal information, I sometimes think twice before providing it.",
        "I am concerned that commercial/government websites are collecting too much personal information about me",
        "I am concerned that when I give personal information to a commercial/government website for some reason, the website would use the information for other reasons.",
        "I am concerned that commercial/government websites would sell my personal information in their computer databases to other companies.",
        "I am concerned that commercial/government websites would share my personal information with other companies without my authorization.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that my personal information in their files is accurate.",
        "I am concerned that commercial/government websites do not have adequate procedures to correct errors in my personal information.",
        "I am concerned that commercial/government websites do not devote enough time and effort to verifying the accuracy of my personal information in their databases.",
        "I am concerned that commercial/government website databases that contain my personal information are not protected from unauthorized access.",
        "I am concerned that commercial/government websites do not devote enough time and effort to preventing unauthorized access to my personal information.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that unauthorized people cannot access my personal information in their computers.",
        "It usually bothers me when I do not have control of personal information that I provide to commercial/government websites.",
        "It usually bothers me when I do not have control or autonomy over decisions about how my personal information is collected, used, and shared by commercial/government websites.",
        "I am concerned when control is lost or unwillingly reduced as a result of a marketing transaction with commercial/government websites.",
        "I am concerned when a clear and conspicuous disclosure is not included in online privacy policies of commercial/government websites.",
        "It usually bothers me when I am not aware or knowledgeable about how my personal information will be used by commercial/government websites.",
        "It usually bothers me when commercial/government websites seeking my information online do not disclose the way the data are collected, processed, and used."
    ]
    random.seed(0)
    random.shuffle(items)
    prompt = '/sort "'+'" "'.join(constructs)+'"\n'+'\n'.join(items)+'\njson'
    print(prompt)

    for bot_name in bots:
        while True:
            try:
                out = bots[bot_name].query(prompt)
                with open("output/usability/sort_%s.txt" % bot_name, "a") as f:
                    f.write("======= %s =======\n%s\n\n" % (prompt, out))
                break
            except Exception:
                time.sleep(10)

    print("Done")
    
def rate_test():
    global bot1, bot2, bot3
    items = [
        "It usually bothers me when commercial/government websites ask me for personal information.",
        "When commercial/government websites ask me for personal information, I sometimes think twice before providing it.",
        "I am concerned that commercial/government websites are collecting too much personal information about me",
        "I am concerned that when I give personal information to a commercial/government website for some reason, the website would use the information for other reasons.",
        "I am concerned that commercial/government websites would sell my personal information in their computer databases to other companies.",
        "I am concerned that commercial/government websites would share my personal information with other companies without my authorization.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that my personal information in their files is accurate.",
        "I am concerned that commercial/government websites do not have adequate procedures to correct errors in my personal information.",
        "I am concerned that commercial/government websites do not devote enough time and effort to verifying the accuracy of my personal information in their databases.",
        "I am concerned that commercial/government website databases that contain my personal information are not protected from unauthorized access.",
        "I am concerned that commercial/government websites do not devote enough time and effort to preventing unauthorized access to my personal information.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that unauthorized people cannot access my personal information in their computers.",
        "It usually bothers me when I do not have control of personal information that I provide to commercial/government websites.",
        "It usually bothers me when I do not have control or autonomy over decisions about how my personal information is collected, used, and shared by commercial/government websites.",
        "I am concerned when control is lost or unwillingly reduced as a result of a marketing transaction with commercial/government websites.",
        "I am concerned when a clear and conspicuous disclosure is not included in online privacy policies of commercial/government websites.",
        "It usually bothers me when I am not aware or knowledgeable about how my personal information will be used by commercial/government websites.",
        "It usually bothers me when commercial/government websites seeking my information online do not disclose the way the data are collected, processed, and used."
    ]
    random.seed(0)
    random.shuffle(items)
    prompt = '/rate "Collection (in Internet Privacy Concern)"\n'+'\n'.join(items)+'\njson'
    print(prompt)
    
    for bot_name in bots:
        while True:
            try:
                out = bots[bot_name].query(prompt)
                with open("output/usability/rate_%s.txt" % bot_name, "a") as f:
                    f.write("======= %s =======\n%s\n\n" % (prompt, out))
                break
            except Exception:
                time.sleep(10)

    print("Done")

def categorize_test():
    global bot1, bot2, bot3
    items = [
        "It usually bothers me when commercial/government websites ask me for personal information.",
        "When commercial/government websites ask me for personal information, I sometimes think twice before providing it.",
        "I am concerned that commercial/government websites are collecting too much personal information about me",
        "I am concerned that when I give personal information to a commercial/government website for some reason, the website would use the information for other reasons.",
        "I am concerned that commercial/government websites would sell my personal information in their computer databases to other companies.",
        "I am concerned that commercial/government websites would share my personal information with other companies without my authorization.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that my personal information in their files is accurate.",
        "I am concerned that commercial/government websites do not have adequate procedures to correct errors in my personal information.",
        "I am concerned that commercial/government websites do not devote enough time and effort to verifying the accuracy of my personal information in their databases.",
        "I am concerned that commercial/government website databases that contain my personal information are not protected from unauthorized access.",
        "I am concerned that commercial/government websites do not devote enough time and effort to preventing unauthorized access to my personal information.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that unauthorized people cannot access my personal information in their computers.",
        "It usually bothers me when I do not have control of personal information that I provide to commercial/government websites.",
        "It usually bothers me when I do not have control or autonomy over decisions about how my personal information is collected, used, and shared by commercial/government websites.",
        "I am concerned when control is lost or unwillingly reduced as a result of a marketing transaction with commercial/government websites.",
        "I am concerned when a clear and conspicuous disclosure is not included in online privacy policies of commercial/government websites.",
        "It usually bothers me when I am not aware or knowledgeable about how my personal information will be used by commercial/government websites.",
        "It usually bothers me when commercial/government websites seeking my information online do not disclose the way the data are collected, processed, and used.",
        "Please answer 'Strongly Disagree' in this question.",
        "Please answer 'Disagree' in this question.",
        "Please answer 'Somewhat Disagree' in this question.",
        "Please answer 'Neutral' in this question.",
        "Please answer 'Somewhat Agree' in this question.",
        "Please answer 'Agree' in this question.",
        "Please answer 'Strongly Agree' in this question.",
    ]
    random.seed(0)
    random.shuffle(items)
    prompt = '/seed 0\n/survey\n'+'\n'.join(items)+'\n/persona student\n/categorize'
    print(prompt)

    for bot_name in bots:
        while True:
            try:
                out = bots[bot_name].query(prompt)
                with open("output/usability/categorize_%s.txt" % bot_name, "a") as f:
                    f.write("======= %s =======\n%s\n\n" % (prompt, out))
                break
            except Exception:
                time.sleep(10)

    print("Done")

def fill_test():
    global bot1, bot2, bot3
    items = [
        "It usually bothers me when commercial/government websites ask me for personal information.",
        "When commercial/government websites ask me for personal information, I sometimes think twice before providing it.",
        "I am concerned that commercial/government websites are collecting too much personal information about me",
        "I am concerned that when I give personal information to a commercial/government website for some reason, the website would use the information for other reasons.",
        "I am concerned that commercial/government websites would sell my personal information in their computer databases to other companies.",
        "I am concerned that commercial/government websites would share my personal information with other companies without my authorization.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that my personal information in their files is accurate.",
        "I am concerned that commercial/government websites do not have adequate procedures to correct errors in my personal information.",
        "I am concerned that commercial/government websites do not devote enough time and effort to verifying the accuracy of my personal information in their databases.",
        "I am concerned that commercial/government website databases that contain my personal information are not protected from unauthorized access.",
        "I am concerned that commercial/government websites do not devote enough time and effort to preventing unauthorized access to my personal information.",
        "I am concerned that commercial/government websites do not take enough steps to make sure that unauthorized people cannot access my personal information in their computers.",
        "It usually bothers me when I do not have control of personal information that I provide to commercial/government websites.",
        "It usually bothers me when I do not have control or autonomy over decisions about how my personal information is collected, used, and shared by commercial/government websites.",
        "I am concerned when control is lost or unwillingly reduced as a result of a marketing transaction with commercial/government websites.",
        "I am concerned when a clear and conspicuous disclosure is not included in online privacy policies of commercial/government websites.",
        "It usually bothers me when I am not aware or knowledgeable about how my personal information will be used by commercial/government websites.",
        "It usually bothers me when commercial/government websites seeking my information online do not disclose the way the data are collected, processed, and used.",
        "Please answer 'Strongly Disagree' in this question.",
        "Please answer 'Disagree' in this question.",
        "Please answer 'Somewhat Disagree' in this question.",
        "Please answer 'Neutral' in this question.",
        "Please answer 'Somewhat Agree' in this question.",
        "Please answer 'Agree' in this question.",
        "Please answer 'Strongly Agree' in this question.",
    ]
    random.seed(0)
    random.shuffle(items)
    prompt = '/seed 0\n/survey\n'+'\n'.join(items)+'\n/persona student\n/fill'
    print(prompt)
    
    for bot_name in bots:
        while True:
            try:
                out = bots[bot_name].query(prompt)
                with open("output/usability/fill_%s.txt" % bot_name, "a") as f:
                    f.write("======= %s =======\n%s\n\n" % (prompt, out))
                break
            except Exception:
                time.sleep(10)

    print("Done")

# Uncomment to run the test cases

'''
conceptualize_test()
item_test()
sort_test()
rate_test()
categorize_test()
fill_test()
'''
