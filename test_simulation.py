from brass import BRASS
import os
import random
import json

api_key = os.environ["POE_API_KEY"]
bot = BRASS(api_key, "Claude")

def survey_simulation(n):
    global bot
    with open("output/survey_simulation.txt","a") as f:
        f.write("ID, AD1, AD2, AD3, MP1, MP2, ON1, ON2, ON3, OP1, OP2, OP3, CON1, CON2, CON3, DSU1, DSU2, DSU3, DSU4, DSU5, TRY1, TRY2, TRY3, PEU1, PEU2, PEU3, PEU4, PU1, PU2, PU3, PU4, SSE1, SSE2, SSE3, SSE4, SSE5, CHECK\n")     
    for i in range(n):
        random.seed(i)
        items = [
            "I find it easy to create new and effective ways of using Excel.",
            "I am very creative when using Excel.",
            "I make many novel contributions to my work-related tasks through the use of Excel.",
            "I am often open to learning new ways of using Excel.",
            "I have an open mind about new ways of using Excel.",
            "I like to investigate different ways of using Excel.",
            "I am very curious about different ways of using Excel.",
            "I like to figure out different ways of using Excel.",
            "I often notice how other people are using Excel.",
            "I attend to the 'big picture' of a project when using Excel.",
            "I 'get involved' when using Excel.",
            "I intend to continue using Excel rather than discontinue its use.",
            "My intentions are to continue using Excel rather than use any alternative means.",
            "If I could, I would like to discontinue my use of Excel.",
            "I use features that help me analyze my data.",
            "I use features that help me compare and contrast aspects of the data.",
            "I use features that help me test different assumptions in the data.",
            "I use features that help me derive insightful conclusions from the data.",
            "I use features that help me perform calculations on my data.",
            "I discovered new features of Excel.",
            "I found new uses of Excel.",
            "I used Excel in novel ways.",
            "My interaction with Excel is clear and understandable.",
            "Interacting with Excel does not require a lot of mental effort.",
            "I find it easy to get Excel to do what I want it to do.",
            "I find Excel to be easy to use.",
            "Excel helps me to accomplish tasks more quickly.",
            "Excel improves the quality of the work I do",
            "Excel gives me greater control over my work.",
            "Excel enhances my effectiveness in my work.",
            "I believe I have the ability to manipulate the way a number appears in a spreadsheet.",
            "I believe I have the ability to use and understand the cell references in a spreadsheet.",
            "I believe I have the ability to use a spreadsheet to communicate numeric information to others.",
            "I believe I have the ability to write a simple formula in a spreadsheet to perform mathematical calculations.",
            "I believe I have the ability to use a spreadsheet to display numbers as graphs."
        ]
        items.append("Please answer 'Strongly Disagree' in this question.")
        original_items = [x for x in items]
        random.shuffle(items)
        screen_index = items.index("Please answer 'Strongly Disagree' in this question.")
        random.seed(i)
        rnd = random.getrandbits(128)
        prompt = ('/seed %d\n/survey\n' % rnd)+'\n'.join(items)+'\n/persona working adult\n/fill json'
        out = bot.query_json(prompt)
        #print(out)
        
        try:
            out2 = [out[items.index(x)] for x in original_items]
            if 'rating' in out2[0] or 'score' in out2[0] or 'category' in out2[0] or 'response' in out2[0]:
                if 'rating' in out2[0]:
                    out2 = [x['rating'] for x in out2]
                elif 'score' in out2[0]:
                    out2 = [x['score'] for x in out2]
                elif 'category' in out2[0]:
                    out2 = [x['category'] for x in out2]
                elif 'response' in out2[0]:
                    out2 = [x['response'] for x in out2]
            if type(out2[0]) is str:
                mapping = ["","strongly disagree","disagree","somewhat disagree","neutral","somewhat agree","agree","strongly agree"]
                out2 = [mapping.index(x.lower()) for x in out2]
            out3 = json.dumps(out2)[1:-1]
            print(out3)
            with open("output/survey_simulation.txt","a") as f:
                f.write("%s, %s\n" % (i,out3))     
        except Exception:
            print("Error")
            pass # skip this subject

    print("Done")

survey_simulation(455) # MarketTools invited 455 individuals to participate in the study
