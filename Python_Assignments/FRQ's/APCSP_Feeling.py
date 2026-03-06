Ask_Amount = int(input("How many students are responding?"))

responses = []

for i in range(Ask_Amount):
    responses.append(int((input("Rate your confidence from a scale of 1-5: "))))

def analyze_confidence(response_list):
    Total = 0
    for Ask_Amount in range(len(responses)):
        Total += responses[Ask_Amount]

    Average = Total / Ask_Amount

    if Average >= 4:
        return "Class is ready" + str(Average)
    elif Average <= 2:
        return "More practice is needed" + str(Average)
    else:
        return "Yall are cooked"+ str(Average)

print(analyze_confidence(responses))