import json


gameVar = 0
count = 0
scenario = 0

while gameVar == 0:
    with open('data/scene.json') as fp:
        data = json.loads(fp.read())

        try:
            data['parts']['scenarios'][scenario]['scenario']
        except:
            if IndexError:
                print(
                    'You have managed to escape the mansion, and been granted the help you needed. From here on, your life could only improve... Congratulations')
                exit()

        print("You have unlocked Scenario {}. Congratulations on surviving.".format(scenario + 1))

        print("\n", data['parts']['story'][0]['Scenario{}'.format(scenario)])

        answer = input(f"""
-------------------------------------------------------------------------------------
A choice presents itself... What will {name} choose?

{data['parts']['scenarios'][scenario]['scenario']}
[A] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionA'][0]}
[B] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionB'][0]}
[C] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionC'][0]}

Beware:  Sometimes your choice may be lethal to {name}, and submitting something else will always be lethal.
-------------------------------------------------------------------------------------
""").lower()


        def answered(result):
            if result == "False":
                print(data['parts']['scenarios'][scenario]['Death'].replace("NAME", name))
                exit()
            if result == "True":
                pass

            if result == "follow" and data['parts']['scenarios'][scenario]['followup'] != "null":
                fanswer = input(f"""
{data['parts']['scenarios'][scenario]['followup'][0]['Story']}

-------------------------------------------------------------------------------------
A follow-up choice presents itself... What will {name} choose?

{data['parts']['scenarios'][scenario]['followup'][0]['Question']}
[A] {data['parts']['scenarios'][scenario]['followup'][0]['DecisionA'][0]}            
[B] {data['parts']['scenarios'][scenario]['followup'][0]['DecisionB'][0]}

Beware:  Sometimes your choice may be lethal to {name}, and submitting something else will always be lethal.
-------------------------------------------------------------------------------------
            """).lower()
                if fanswer == "a":
                    fresult = data['parts']['scenarios'][scenario]['followup'][0]['DecisionA'][1]
                    if fresult == "False":
                        print(data['parts']['scenarios'][scenario]['followup'][0]['Death'].replace("NAME", name))
                        exit()
                    else:
                        pass
                if fanswer == "b":
                    fresult = data['parts']['scenarios'][scenario]['followup'][0]['DecisionB'][1]
                    if fresult == "False":
                        print(data['parts']['scenarios'][scenario]['followup'][0]['Death'].replace("NAME", name))
                        exit()
                    else:
                        pass
            else:
                pass


        if answer == "stop":
            print("User has requested to abort the game, Exiting...")
            exit()
        elif answer == "a":
            result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionA'][1]
            answered(result)
        elif answer == "b":
            result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionB'][1]
            answered(result)
        elif answer == "c":
            result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionC'][1]
            answered(result)
        else:
            today = datetime.datetime.now()
            print(
                f"You have decided to do nothing. This, clearly was not a good idea as you have starved of hunger.\nRest in Peace {name}, 1993-{today.strftime('%Y')}")
            exit()

        scenario += 1