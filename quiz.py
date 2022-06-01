import random

History_of_SG = [
    ['Which treaty formally established the status of Singapore as a British colony?', ['Anglo-Dutch Treaty', 'Treaty of  Temasek', 'Treaty of Singapore', 'Straits Settlement Treaty']],
    ['When did Singapore gain independence?', ['August 1965', 'October 1964', 'September 1967', 'March 1966']],
    ['Besides Singapore, which were the other two settlements that together formed the Straits Settlements?', ['Malacca and Penang', 'Malacca and Johor', 'Johor and Perak', 'Penang and Perak']],
    ['Racial Harmony Day is commemorated because of this event?', ['Communal Riots (1964)', 'Maria Hertogh Riots (1950)', 'Little India Riots (2013)', 'Hock Lee Bus Riots (1955)']],
    ['Which year was Singapore’s Founding Prime Minister, Mr Lee Kuan Yew, born?', ['1923', '1945', '1956', '1939']],
    ['Which former President of Singapore was a former diplomat and served as the Ambassador to the United States from 1990 to 1996?', ['Mr S. R. Nathan', 'Mr Ong Teng Cheong', 'Mr Yusof Ishak', 'Mr Tony Tan']],
    ['What is the theme of Singapore’s 2021 National Day Parade?', ['Together, our Singapore Spirit', 'A Stronger Singapore', 'The Road Ahead', 'We are Singapore']],
    ["Who was the first Prime Minister of Singapore?", ['Lee Kuan Yew', 'Goh Chok Tong', 'Goh Keng Swee', 'Lee Hsien Long']],
    ["What do the five stars on the Singapore National Flag represent?", ['Democracy, peace, progress, justice and equality', 'Democracy, peace, progress, justice and equanimity ', 'Democracy, peace, progress, justice and efficiency', 'Democracy, peace, performance, justice and equality']],
    ["A small island state itself, Singapore is surrounded by a plethora of mini islands. How many offshore islands are there?", ['64 ', '59', '75', '82']],
    ["Which of the following is not cited in Singapore’s National Pledge?", ['pledge ourselves as one united family ', 'Regardless of race, language or religion', 'happiness, prosperity and progress', 'a democratic society, based on justice and equality']],
    ["Where was singapore's first national day parade held at?", ['The Padang ', 'The Float @ Marina Bay', 'National Stadium ', 'Tampines Hub']],
    ["Singapore’s National Anthem, Majulah Singapura, was composed by Zubir Said in which year?", ['1958', '1965', '1959', '1957']],
    ["How many SEA games medals did our athletes win in 2022 Vietnam SEA games in total?", ['164 ', '446', '63', '174']],
    ["Who is Singapore’s First Olympian?", ['Lloyd Valberg (high jump)', 'Tan Howe Liang (Weightlifting)', 'Joscelin Yeo (Swimming)', 'Feng Tian Wei (table tennis)']],
    ["Which of the following policies helps bring people of different races together?", ['Housing policy ', 'Transport policy', 'Economic policy', 'Finance policy', 'Immigrant policy']],
]

History_of_NS = [
    ["When was the National Service (admendment) Bill ", ['14 March 1967', '23 April 1967', '14 March 1965', '23 April 1965']],
    ["Who started National Service in Singapore?", ['Goh Keng Swee', 'Goh Chok Tong', 'Goh Beng Kwan', 'Lee Kuan Yew']],
    ["Conscription model of National Service models which country?", ['Isreal', 'Egypt', 'USA', 'UK']],
    ["How Long is National Service in Singapore?", ['2 years', '1.8 years', '1.9 years', '2.5 years']],
    ["What is the RSAF logo made up of?", ['Red Lion Head within a Roundel ', 'Blue Lion Head within a Roundel', 'Red Lion Head within a Crest', 'Blue Lion Head within a Crest']],
    ["Who is the current Chief of Air Force?", ['Kelvin khong Boon Leng ', 'Hoo Cher Mou', 'Ng Chee Meng ', 'Ng Chee Khern']],
    ["What was Minister Gan Siow Huang’s role when she first joined the RSAF", ['Air Traffic Controller (AWO)', 'Pilot', 'Weapon System Officer', 'Ground based air defence (AWO)']],
    ["Singapore’s Self-image in security terms has been represented by __", ['A dolphin', 'A lion', 'A snake', 'A bee']]
]

History_of_163 = [
    ["What is the maximum effective range of the I-HAWK System?", ['40Km', '50Km', '60Km', '30Km']],
    ["When was 163 sqn founded?", ['1982', '1984', '1983', '1985']],
    ["What is 163 sqn motto?", ['Above the Best', 'Above the Rest', 'Above All', 'Above you']],
    ["When was the I-HAWK missile system commissioned in Singapore?", ['1979', '1970', '1980', '1981']],
    ["When did the Aster-30 Missile system start air defence operations in Singapore?", ['Aug 2020 ', 'Sep 2020', 'July 2020', 'June 2020']],
    ["Who was the first CO of 163 sqn?", ['MAJ LIM BUCK SIAH', 'MAJ LEE BUCK SIAH', 'MAJ LEE BUCK SIAN', 'MAJ LIM BOO SIAN']],
    ["Who was the first CC of 163 sqn?", ['1WO JOHN TAN', '1WO BOB TAN', '1WO ALEX TAN', '1WO DAVID TAN']],
    ["What is 163 sqn mascot?", ['Hawk', 'Eagle', 'Donkey', 'Arrow']],
    ["When was 163 sqn relocated to LCK camp II?", ['SEP 1987', 'JUN 1983', 'FEB 1990', 'APR 1979']],
    ["When was the Vuelo officially opened?", ['18 July 2012', '15 July 2012', '16 July 2012', '17 July 2012']]
]

Fun_fact = [
    [
        "",
        "", 
        "", 
        "",
        "He was a 4th generation Chinese Singaporean, born at 92 Kampong Java Road",
        "He was the 6th president of Singapore",
        "It was a nod to Singaporeans’ unity and can-do spirit that has kept the country strong amid the COVID-19 pandemic",
        "He was known as Harry Lee, stopped using the name after leaving Cambridge",
        "The crescent moon represents a young nation on the ascendant, and the 5 stars stand for the nation’s ideals",
        "This includes Sentosa — a popular island resort with myriad attractions—and havens for nature lovers like Pulau Ubin, St John's Island and Sisters' Islands",
        "Initially penned by Mr S Rajaratnam in 1966, the Pledge was written against the backdrop of racial riots in the '50s and '60s",
        "held in 1966, and still remains as an iconic landmark in Singapore’s landscape",
        "By law, the anthem must be sung with Malay lyrics, but there are authorised translations of the lyrics of the anthem in Singapore's three other official languages: English, Mandarin and Tamil",
        "placing 5th overall with 47 Gold, 46 Silvers, 71 Bronze medals",
        "on 29 Jul 1948, he became the first Singaporean to represent Singapore at the 14th Olympic games held in london",
        "under the Ethnic integration policy, different races are immersed together"
    ],
    [
        "",
        "",
        "",
        "",
        "It expresses courage, strength and resolve with 5 flow manes representing the nation’s 5 beliefs",
        "He has an MBA with Honours from Switzerland",
        "He direct RSAF air operations, and control RSAF aircraft as well as Ground-Based Air Defence weapon systems",
        "This is an important form of deterrence against potential aggressors",
        "",
        "",
        "Singapore has changed its 'poison shrimp' posture since the 1980s to the current 'dolphin' strategy – an allusion to agility, intelligence, and quick reflexes that allow it to be friendly but can yet kill when provoked"

    ],
    [
        "",
        "163 sqn was founded in May 1982 to take on the responsibility of the newly acquired Improved Homing All-the-Way Killer (I-HAWK)",
        "'Above the Best' is the modus operandi adopted by 163 sqn. It is an attitude, a work ethic which is as demanding as it is uncompromising. Simply put, we are not content with just being above the rest, we also strive to better ourselves continually",
        "It met the RSAF’s Medium range air defence requirements",
        "It is a Medium-range Surface-to-Air Missile (MSAM) system capable of engaging and intercepting a wide spectrum of air threats",
        "MAJ LIM BUCK SIAH was the CO of our sqn from 3 May 1982 to 30 Jun 1983",
        "1WO JOHN TAN was the CC of our sqn from 1 Oct 1983 to 24 Jul 1988. Wait a second, was there a CC from May 1982 to Oct 1983...",
        "The hawk is the mascot of 163 sqn. It symbolises tenacity, determination and the focused will to achieve success in all its missions",
        "In order to overcome the spatial constraints, a new premise was constructed off Lim Chu Kang Road and 163 sqn was relocated to LCK camp II in Sep 1987",
        "Vuelo means flight in Spanish. It signifies the flight that 163 sqn has taken thus far as their heritage. It was officially opened by MG HOO CHER MOU (CAF) on 18 Jul 2012"
    ]
]

section1 = [
    ["What is 1 + 1?", ["2"*59, "1", "3", "4", "5"]],
    ["What is 1 + 2?", ["3", "2", "1", "4", "5"]],
    ["What is 1 + 3?", ["4", "2", "3", "1", "5"]],
    ["What is 1 + 4?", ["5", "2", "3", "4", "1"]],
    ["What is 1 + 0?", ["1", "2", "3", "4", "5"]]
]

section2 = [
    ["What is 5 - 1?", ["4", "1", "2", "3", "5"]],
    ["What is 5 - 2?", ["3", "1", "2", "4", "5"]],
    ["What is 5 - 3?", ["2", "1", "4", "3", "5"]],
    ["What is 5 - 4?", ["1", "4", "2", "3", "5"]],
    ["What is 5 - 0?", ["5", "1", "2", "3", "4"]]    
]

section3 = [
    ["What is 4 * 1?", ["4", "1", "2", "3", "5"]],
    ["What is 3 * 1?", ["3", "1", "2", "4", "5"]],
    ["What is 2 * 1?", ["2", "1", "4", "3", "5"]],
    ["What is 1 * 1?", ["1", "4", "2", "3", "5"]],
    ["What is 5 * 1?", ["5", "1", "2", "3", "4"]]
]

def quiz(n):
    if n == 1:
        x = random.randrange(len(History_of_SG))
        quiz = History_of_SG[x]
    elif n == 2:
        x = random.randrange(len(History_of_NS))
        quiz = History_of_NS[x]
    else:
        x = random.randrange(len(History_of_163))
        quiz = History_of_163[x]

    return quiz[0], quiz[1][0], random.sample(quiz[1], len(quiz[1])), str(x)

def ff(n, x):
    return Fun_fact[n-1][int(x)]

'''
if __name__ == "__main__":
    # f = open("temp.txt", "w")

    for i in range(len(History_of_SG)):
        # line = ""
        for j in History_of_SG[i]:
            if j == "":
                print('-')
                # line += "-\n"
            else:
                print(j)
                # line += str(j) + "\n"
        print()
        # line += "\n"
        # f.write(line)
    
    for i in range(len(History_of_NS)):
        # line = ""
        for j in History_of_NS[i]:
            if j == "":
                print('-')
                # line += "-\n"
            else:
                print(j)
                # line += str(j) + "\n"
        print()
        # line += "\n"
        # f.write(line)

    for i in range(len(History_of_163)):
        # line = ""
        for j in History_of_163[i]:
            if j == "":
                print('-')
                # line += "-\n"
            else:
                print(j)
                # line += str(j) + "\n"
        print()
        # line += "\n"
        # f.write(line)
    
    # f.close()
'''