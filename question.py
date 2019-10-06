import random

class question:
    def __init__(self, prompt, answer, wrong_answers):
        self.prompt = prompt
        self.answer = answer
        self.wrong_answers = wrong_answers

question_prompts = [
    "We are currently in what century?",
    "What is the current year we are living in?",
    "What color are bananas?",
    "What color are strawberries?",
    "You go to a doctor when you are?",
    "When do you go to an auto mechanic?",
    "1+0 = ?",
    "2+3=?",
    "0*1 = ?",
    "-1*0=?",
    "Who is the current president of the United States?",
    "Who is the current president of Croatia?",
    "How many continents are there?",
    "How many oceans are there?",
    "Which continent is the least populated?",
    "Which continent is the most populated?",
    "What is square root of 81?",
    "What is 7 to the power of 2?",
    "What is the Capital of Australia?",
    "What is the Capital of Canada?",
    "What is heavier, 100 kilos of feather or 100 kilos of rocks",
    "If you overtake second runner, you are?",
    "Which gas is the most present in the air?",
    "What is the fastest animal on the planet?",
    "How many planets are in Solar System?",
    "What is the name of our galaxy?",
    "What year did the World War 1 end?",
    "What year did the World War 2 begin?",
    "Who composed the 4 seasons?",
    "Who composed the Moonlight Sonata?"
]

right_answers = [
    "21st",
    "2019.",
    "Yellow",
    "Red",
    "Sick",
    "When you have a broken vehicle",
    "1",
    "5",
    "0",
    "0",
    "Donald Trump",
    "Kolinda Grabar Kitarovic",
    "7",
    "5",
    "Antarctica",
    "Asia",
    "9",
    "49",
    "Canberra",
    "Ottawa",
    "Same",
    "Second",
    "Nitrogen",
    "Cheetah",
    "9",
    "The Milky Way",
    "1918.",
    "1939.",
    "Vivaldi",
    "Beethoven"
]

wrong_answers = [
    ["1st", "20st", "9st", "21st"],
    ["1919.", "2018.", "50.", "2019."],
    ["White", "Purple", "Black", "Yellow"],
    ["Blue", "Green", "Yellow", "Red"],
    ["Hungry", "Happy", "Sleepy",  "Sick"],
    ["When you are sick", "When you are sad", "When you are bored", "When you have a broken vehicle"],
    ["0", "-1", "2", "1"],
    ["4", "6", "3", "5"],
    ["1", "-1", "10", "0"],
    ["-1", "1", "-10", "0"],
    ["Barack Obama", "George W. Bush", "John F. Kennedy",  "Donald Trump"],
    ["Stipe Mesic", "Franjo Tudman", "Ivo Josipovic", "Kolinda Grabar Kitarovic"],
    ["6", "8", "2", "7"],
    ["3", "4", "6", "5"],
    ["Europe", "Australia", "North America", "Antarctica"],
    ["Europe", "South America", "Africa", "Asia"],
    ["8", "10", "7", "9"],
    ["47", "36", "64", "49"],
    ["Sydney", "Perth", "Melbourne", "Canberra"],
    ["Vancouver", "Toronto", "Quebec", "Ottawa"],
    ["100 kilos of feather", "100 kilos of rocks", "Impossible to tell", "Same"],
    ["First", "Third", "I am confused", "Second"],
    ["Oxygen", "Helium", "Argon",  "Nitrogen"],
    ["Horse", "Leopard", "Turtle", "Cheetah"],
    ["7", "8", "6", "9"],
    ["Our galaxy", "Solar System", "Black Hole", "The Milky Way"],
    ["1919.", "1917.", "1914.", "1918."],
    ["1945.", "1941.", "2019.", "1939."],
    ["Mozart", "Handel", "Bach", "Vivaldi"],
    ["Chopin", "Mozart", "Wagner", "Beethoven"]
]

pitanja = [None] * 15
for i in range(15):
    j = random.randint(i*2, i*2+1)
    random.shuffle(wrong_answers[j])
    pitanja[i] = question(question_prompts[j], right_answers[j], wrong_answers[j])
