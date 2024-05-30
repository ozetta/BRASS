from brass import BRASS
import os
import random
import json

api_key = os.environ["POE_API_KEY"]
bot = BRASS(api_key, "Claude")

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def sort_stability(n):
    correct_count = 0
    correct_rate = 0
    global bot
    PU_items = [
        "Using ChatGPT in my job would enable me to accomplish tasks more quickly.",
        "Using ChatGPT would improve my job performance.",
        "Using ChatGPT in my job would increase my productivity.",
        "Using ChatGPT would enhance my effectiveness on the job.",
        "Using ChatGPT would make it easier to do my job.",
        "I would find ChatGPT useful in my job."
    ]
    PEOU_items = [
        "Learning to operate ChatGPT would be easy for me.",
        "I would find it easy to get ChatGPT to do what I want it to do.",
        "My interaction with ChatGPT would be clear and understandable.",
        "I would find ChatGPT to be flexible to interact with.",
        "It would be easy for me to become skillful at using ChatGPT.",
        "I would find ChatGPT easy to use.",
    ]
        
    for i in range(n):
        random.seed(i)
        items = PU_items + PEOU_items    
        random.shuffle(items)
        prompt = '/sort "Perceived Usefulness" "Perceived Ease of Use"\n'+'\n'.join(items)+'\njson'
                
        out = bot.query_json(prompt)
        if out == None:
            out = {"Perceived Usefulness": [], "Perceived Ease of Use": []}
        common_pu = intersection(out["Perceived Usefulness"], PU_items)
        common_peou = intersection(out["Perceived Ease of Use"], PEOU_items)    
        rate = (len(common_pu) + len(common_peou)) / 12.0
        if set(out["Perceived Usefulness"]) == set(PU_items) and set(out["Perceived Ease of Use"]) == set(PEOU_items):
            correct = 1
        else:
            correct = 0
        with open("output/sort_stability.txt","a") as f:
            print(i,correct,rate)
            f.write("Seed %d: Correct = %d, Rate = %f\n" % (i,correct,rate))
        correct_count += correct
        correct_rate += rate

    with open("output/sort_stability.txt","a") as f:
        print(correct_count/float(n), correct_rate/float(n))
        f.write("\nAll correct rate = %f\nAverage correct rate = %f" % (correct_count/float(n), correct_rate/float(n)))

    print("Done")

def fill_stability(n):
    results = []
    errors = 0
    global bot
    random.seed(0)
    items = [
        "Using ChatGPT in my job would enable me to accomplish tasks more quickly.",
        "Using ChatGPT would improve my job performance.",
        "Using ChatGPT in my job would increase my productivity.",
        "Using ChatGPT would enhance my effectiveness on the job.",
        "Using ChatGPT would make it easier to do my job.",
        "I would find ChatGPT useful in my job.",
        "Learning to operate ChatGPT would be easy for me.",
        "I would find it easy to get ChatGPT to do what I want it to do.",
        "My interaction with ChatGPT would be clear and understandable.",
        "I would find ChatGPT to be flexible to interact with.",
        "It would be easy for me to become skillful at using ChatGPT.",
        "I would find ChatGPT easy to use.",
    ]
    items.append("Please answer 'Strongly Disagree' in this question.")
    random.shuffle(items)
    screen_index = items.index("Please answer 'Strongly Disagree' in this question.")
        
    for i in range(n):
        prompt = ('/seed %d\n/survey\n' % i)+'\n'.join(items)+'\n/persona student\n/fill json'
        out = bot.query_json(prompt)
        if out is None or len(out) != 13:
            errors += 1
        elif out[screen_index] != 1 and out[screen_index] != "Strongly Disagree" \
        and out[screen_index] != {"item": "Please answer 'Strongly Disagree' in this question.", "rating": 1} \
        and out[screen_index] != {"item": "Please answer 'Strongly Disagree' in this question.", "rating": "Strongly Disagree"}:
            errors += 1
        json_out = json.dumps(out)
        with open("output/fill_stability.txt","a") as f:
            print(i,json_out)
            f.write("Seed %d: %s\n" % (i,json_out))

        if json_out not in results:
            results.append(json_out)

    with open("output/fill_stability.txt","a") as f:
        print(len(results), errors)
        f.write("\nUnique entries: %d\nErrors: %d" % (len(results), errors))

    print("Done")

def fill2_stability(n):
    results = []
    errors = 0
    global bot
    random.seed(0)
    items = [
        "Using ChatGPT in my job would enable me to accomplish tasks more quickly.",
        "Using ChatGPT would improve my job performance.",
        "Using ChatGPT in my job would increase my productivity.",
        "Using ChatGPT would enhance my effectiveness on the job.",
        "Using ChatGPT would make it easier to do my job.",
        "I would find ChatGPT useful in my job.",
        "Learning to operate ChatGPT would be easy for me.",
        "I would find it easy to get ChatGPT to do what I want it to do.",
        "My interaction with ChatGPT would be clear and understandable.",
        "I would find ChatGPT to be flexible to interact with.",
        "It would be easy for me to become skillful at using ChatGPT.",
        "I would find ChatGPT easy to use.",
    ]
    items.append("Please answer 'Strongly Disagree' in this question.")
    random.shuffle(items)
    screen_index = items.index("Please answer 'Strongly Disagree' in this question.")
        
    for i in range(n):
        random.seed(i)
        rnd = random.getrandbits(128)
        prompt = ('/seed %d\n/survey\n' % rnd)+'\n'.join(items)+'\n/persona student\n/fill json'
        out = bot.query_json(prompt)
        if out is None or len(out) != 13:
            errors += 1
        elif out[screen_index] != 1 and out[screen_index] != "Strongly Disagree" \
        and out[screen_index] != {"item": "Please answer 'Strongly Disagree' in this question.", "rating": 1} \
        and out[screen_index] != {"item": "Please answer 'Strongly Disagree' in this question.", "rating": "Strongly Disagree"}:
            errors += 1
        json_out = json.dumps(out)
        with open("output/fill2_stability.txt","a") as f:
            print(i,rnd,json_out)
            f.write("Seed %d: %s\n" % (rnd,json_out))

        if json_out not in results:
            results.append(json_out)

    with open("output/fill2_stability.txt","a") as f:
        print(len(results), errors)
        f.write("\nUnique entries: %d\nErrors: %d" % (len(results), errors))

    print("Done")

def fill3_stability(n):
    results = []
    results2 = []
    errors = 0
    global bot
        
    for i in range(n):
        random.seed(i)
        items = [
            "Using ChatGPT in my job would enable me to accomplish tasks more quickly.",
            "Using ChatGPT would improve my job performance.",
            "Using ChatGPT in my job would increase my productivity.",
            "Using ChatGPT would enhance my effectiveness on the job.",
            "Using ChatGPT would make it easier to do my job.",
            "I would find ChatGPT useful in my job.",
            "Learning to operate ChatGPT would be easy for me.",
            "I would find it easy to get ChatGPT to do what I want it to do.",
            "My interaction with ChatGPT would be clear and understandable.",
            "I would find ChatGPT to be flexible to interact with.",
            "It would be easy for me to become skillful at using ChatGPT.",
            "I would find ChatGPT easy to use.",
        ]
        items.append("Please answer 'Strongly Disagree' in this question.")
        original_items = [x for x in items]
        random.shuffle(items)
        screen_index = items.index("Please answer 'Strongly Disagree' in this question.")
        random.seed(i)
        rnd = random.getrandbits(128)
        prompt = ('/seed %d\n/survey\n' % rnd)+'\n'.join(items)+'\n/persona student\n/fill json'
        out = bot.query_json(prompt)
        if out is None or len(out) != 13:
            errors += 1
        elif out[screen_index] != 1 and out[screen_index] != "Strongly Disagree" \
        and out[screen_index] != {"item": "Please answer 'Strongly Disagree' in this question.", "rating": 1} \
        and out[screen_index] != {"item": "Please answer 'Strongly Disagree' in this question.", "rating": "Strongly Disagree"}:
            errors += 1
        json_out = json.dumps(out)
        try:
            json_out2 = json.dumps([out[items.index(x)] for x in original_items])
        except Exception:
            json_out2 = None
        with open("output/fill3_stability.txt","a") as f:
            print(i,rnd,json_out,json_out2)
            f.write("Seed %d||%s||%s\n" % (rnd,json_out,json_out2))

        if json_out not in results:
            results.append(json_out)
            
        if json_out2 not in results2:
            results2.append(json_out2)
            
    with open("output/fill3_stability.txt","a") as f:
        print((len(results), len(results2), errors))
        f.write("\nUnique entries: %d\nUnique rearranged entries: %d\nErrors: %d" % (len(results), len(results2), errors))

    print("Done")

#sort_stability(100)
#fill_stability(100)
#fill2_stability(100)
fill3_stability(100)
