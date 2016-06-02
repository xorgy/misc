#!/usr/bin/env python3
""" Fill in the blanks of random Cards Against Humanity questions with random Jeopardy answers
"""

from random import Random
random=Random()

jep={
  "description": "A sampling of 1000 Jeopardy questions and metadata. For the full dataset, see http://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/",
  "questions": [
    {
      "category": "DIPLOMACY",
      "air_date": "2000-10-13",
      "question": "'Term for a formal agreement; it's also a Honda'",
      "value": "$200",
      "answer": "Accord",
      "round": "Double Jeopardy!",
      "show_number": "3705"
    },
    {
      "category": "SEAS",
      "air_date": "1998-11-03",
      "question": "'Bab El Mandeb, Arabic for \"Gate of Tears\", connects the Gulf of Aden with this colorful sea'",
      "value": "$400",
      "answer": "Red Sea",
      "round": "Jeopardy!",
      "show_number": "3257"
    },
    {
      "category": "ZOOLOGY",
      "air_date": "2000-06-06",
      "question": "'This pet bird comes in 2 main types, depending on its singing: choppers & rollers'",
      "value": "$600",
      "answer": "Canaries",
      "round": "Double Jeopardy!",
      "show_number": "3642"
    },
    {
      "category": "ARGENTINA",
      "air_date": "2002-12-17",
      "question": "'Ushuaia, the world's southernmost city, lies on this island territory of Argentina'",
      "value": "$600",
      "answer": "Tierra del Fuego",
      "round": "Jeopardy!",
      "show_number": "4212"
    },
    {
      "category": "FASHION DESIGNERS",
      "air_date": "1992-10-26",
      "question": "'She was 86 when the Broadway musical about her premiered in 1969'",
      "value": "$400",
      "answer": "Coco Chanel",
      "round": "Jeopardy!",
      "show_number": "1871"
    },
    {
      "category": "THEY USED TO BE IN CHARGE",
      "air_date": "1999-09-16",
      "question": "'Benjamin Netanyahu'",
      "value": "$100",
      "answer": "Israel",
      "round": "Jeopardy!",
      "show_number": "3454"
    },
    {
      "category": "SAMS OF THE CINEMA",
      "air_date": "2006-05-18",
      "question": "'The last works he directed weren't Westerns but music videos starring Julian Lennon'",
      "value": "$1600",
      "answer": "Sam Peckinpah",
      "round": "Double Jeopardy!",
      "show_number": "5004"
    },
    {
      "category": "FOOD",
      "air_date": "2007-12-07",
      "question": "'Poblano is one type of this dark Mexican sauce made with chiles & chocolate'",
      "value": "$800",
      "answer": "mole",
      "round": "Double Jeopardy!",
      "show_number": "5350"
    },
    {
      "category": "THE BIRDS & THE BEES",
      "air_date": "2007-02-15",
      "question": "'It's a small, chunky brown bird with a short bill & a silent initial W'",
      "value": "$2000",
      "answer": "wren",
      "round": "Double Jeopardy!",
      "show_number": "5169"
    },
    {
      "category": "TUNNEL",
      "air_date": "2007-04-16",
      "question": "'The 11 1/2-mile tunnel between Bologna & Florence, Italy bears the name of this Italian mountain chain'",
      "value": "$1000",
      "answer": "the Apennines",
      "round": "Jeopardy!",
      "show_number": "5211"
    },
    {
      "category": "MOVIE STARS OLD & NEW",
      "air_date": "2004-07-15",
      "question": "'There was occasional talk of a comeback during her 49-year retirement from the screen'",
      "value": "$1600",
      "answer": "Greta Garbo",
      "round": "Double Jeopardy!",
      "show_number": "4589"
    },
    {
      "category": "\"HAL\"",
      "air_date": "2009-12-28",
      "question": "'Hebrew for \"praise God\", it's a shout of praise to God'",
      "value": "$200",
      "answer": "hallelujah",
      "round": "Jeopardy!",
      "show_number": "5821"
    },
    {
      "category": "YOU LOOK LIKE A GREEK GOD",
      "air_date": "2007-06-13",
      "question": "'His realm had 5 rivers: the Acheron, Cocytos, Lethe, Phlegethon & Styx'",
      "value": "$800",
      "answer": "Hades",
      "round": "Jeopardy!",
      "show_number": "5253"
    },
    {
      "category": "BALLET",
      "air_date": "1989-09-12",
      "question": "'\"Rond de jambe\" means a rotary movement of this body part, on the floor or in the air'",
      "value": "$400",
      "answer": "the leg",
      "round": "Double Jeopardy!",
      "show_number": "1152"
    },
    {
      "category": "WHAT'S ON \"TAP\"?",
      "air_date": "2011-12-02",
      "question": "'To place close together for comparison or contrast'",
      "value": "$2000",
      "answer": "to juxtapose",
      "round": "Double Jeopardy!",
      "show_number": "6260"
    },
    {
      "category": "ONE-NAMED PERSONALITIES",
      "air_date": "2009-09-22",
      "question": "'In 2002 this singer & other activists founded DATA, which stands for Debt, AIDS, Trade, Africa'",
      "value": "$400",
      "answer": "Bono",
      "round": "Double Jeopardy!",
      "show_number": "5752"
    },
    {
      "category": "FILING CHAPTER 11",
      "air_date": "2004-04-21",
      "question": "'Chapter 11 of this book begins, \"At the appointed time I returned to Miss Havisham's\"'",
      "value": "$800",
      "answer": "Great Expectations",
      "round": "Double Jeopardy!",
      "show_number": "4528"
    },
    {
      "category": "OUT WEST",
      "air_date": "2011-02-28",
      "question": "'From his time as a hunter of them in the Old West, it was the animal in the nickname of William F. Cody'",
      "value": "$200",
      "answer": "a buffalo",
      "round": "Jeopardy!",
      "show_number": "6096"
    },
    {
      "category": "TRANSPORTATION",
      "air_date": "2007-05-30",
      "question": "'Since 1899 these stalwart animals used in transport have served as the mascots of the Army Corps of Cadets'",
      "value": "$1,000",
      "answer": "mules",
      "round": "Double Jeopardy!",
      "show_number": "5243"
    },
    {
      "category": "BRITISH BANDS",
      "air_date": "2009-04-03",
      "question": "'The genesis of Genesis included this man singing lead; he left for the \"big time\" as a solo artist'",
      "value": "$800",
      "answer": "Peter Gabriel",
      "round": "Jeopardy!",
      "show_number": "5665"
    },
    {
      "category": "A FUNGUS AMONG US",
      "air_date": "2010-03-29",
      "question": "'Traditionally, dogs or pigs are used to detect these pricey fungi that come in black & white varieties'",
      "value": "$400",
      "answer": "truffles",
      "round": "Jeopardy!",
      "show_number": "5886"
    },
    {
      "category": "A PASSION FOR FASHION",
      "air_date": "2000-11-09",
      "question": "'He's the clothing designer who gave us Tommy Girl cologne'",
      "value": "$400",
      "answer": "Tommy Hilfiger",
      "round": "Double Jeopardy!",
      "show_number": "3724"
    },
    {
      "category": "TELEVISION",
      "air_date": "1990-05-16",
      "question": "'30 years ago she was Mary Stone on \"The Donna Reed Show\"; today she's Christine on \"Coach\"'",
      "value": "$500",
      "answer": "Shelley Fabares",
      "round": "Jeopardy!",
      "show_number": "1328"
    },
    {
      "category": "BATMAN TV VILLAINS",
      "air_date": "2009-07-23",
      "question": "'Julie Newmar, Eartha Kitt & Lee Meriwether as this purr-fect villain (not all at the same time)'",
      "value": "$400",
      "answer": "Catwoman",
      "round": "Jeopardy!",
      "show_number": "5744"
    },
    {
      "category": "STATE OF PLAY",
      "air_date": "2010-03-02",
      "question": "'Broncos,Rockies'",
      "value": "$600",
      "answer": "Colorado",
      "round": "Jeopardy!",
      "show_number": "5867"
    },
    {
      "category": "ESTIMATED PROPHET",
      "air_date": "2006-09-28",
      "question": "'This visionary Lebanese-American poet penned \"The Garden of the Prophet\"'",
      "value": "$1600",
      "answer": "Kahlil Gibran",
      "round": "Double Jeopardy!",
      "show_number": "5069"
    },
    {
      "category": "YELLOWSTONE NATIONAL PARK",
      "air_date": "2004-10-19",
      "question": "'(Sarah of the Clue Crew reads from Yellowstone National Park.)  This backbone of North America separating east- from west-flowing rivers cuts through the plateau of Yellowstone Park'",
      "value": "$1000",
      "answer": "the continental divide",
      "round": "Jeopardy!",
      "show_number": "4627"
    },
    {
      "category": "GAMES",
      "air_date": "1996-04-09",
      "question": "'In this game a person whose eyes are covered must determine a person's identity by feeling the face'",
      "value": "$400",
      "answer": "Blind Man\\'s Bluff",
      "round": "Jeopardy!",
      "show_number": "2682"
    },
    {
      "category": "IN PARIS",
      "air_date": "1999-04-14",
      "question": "'A Parisian must-see on anyone's list, this museum is the home of the Mona Lisa'",
      "value": "$200",
      "answer": "The Louvre",
      "round": "Jeopardy!",
      "show_number": "3373"
    },
    {
      "category": "POLITICAL IDIOMS",
      "air_date": "2006-07-25",
      "question": "'Used to describe a response made without thinking, its physical counterpart can take 1/20 second'",
      "value": None,
      "answer": "knee-jerk",
      "round": "Final Jeopardy!",
      "show_number": "5052"
    },
    {
      "category": "\"G.G.\"",
      "air_date": "2005-06-28",
      "question": "'Longtime Chicago Bear Harold \"Red\" Grange was also known by this \"spectral\" nickname'",
      "value": "$400",
      "answer": "the Galloping Ghost",
      "round": "Double Jeopardy!",
      "show_number": "4807"
    },
    {
      "category": "ARTISTS ON FILM",
      "air_date": "2000-02-28",
      "question": "'Anthony Quinn in \"Lust for Life\"'",
      "value": "$600",
      "answer": "Paul Gauguin",
      "round": "Double Jeopardy!",
      "show_number": "3571"
    },
    {
      "category": "I AM CURIOUS YELLOW",
      "air_date": "2002-03-12",
      "question": "'Only incorporated as a city in 1970, Yellowknife is the capital of this vast Canadian administrative region'",
      "value": "$1200",
      "answer": "the Northwest Territories",
      "round": "Double Jeopardy!",
      "show_number": "4042"
    },
    {
      "category": "FAMOUS SPEECHES",
      "air_date": "1992-05-28",
      "question": "'In 1859 he told a Va. courtroom, \"I never did intend murder, or...to excite or incite slaves to rebellion\"'",
      "value": "$1,000",
      "answer": "John Brown",
      "round": "Double Jeopardy!",
      "show_number": "1799"
    },
    {
      "category": "YOUNG ACTORS",
      "air_date": "2007-10-10",
      "question": "'She appeared in \"Santa Clause 3\" with brother Spencer before being nominated for an Oscar at age 10 in 2007'",
      "value": "$2000",
      "answer": "Abigail Breslin",
      "round": "Double Jeopardy!",
      "show_number": "5308"
    },
    {
      "category": "HAIL, HAIL ROCK 'N' ROLL",
      "air_date": "2000-05-10",
      "question": "'This Stevie Wonder hit is subtitled \"Everything's Alright\"'",
      "value": "$500",
      "answer": "\"Uptight\"",
      "round": "Jeopardy!",
      "show_number": "3623"
    },
    {
      "category": "THE RUSSIANS ARE COMING",
      "air_date": "2008-05-14",
      "question": "'The only son of Nicholas II, Alexis was the last male heir born to this royal family while it ruled Russia'",
      "value": "$1,000",
      "answer": "the Romanovs",
      "round": "Jeopardy!",
      "show_number": "5463"
    },
    {
      "category": "HALLS OF FAME",
      "air_date": "2003-03-10",
      "question": "'It opened in Cooperstown, New York in 1939'",
      "value": "$200",
      "answer": "Baseball Hall of Fame",
      "round": "Jeopardy!",
      "show_number": "4271"
    },
    {
      "category": "RIVER DEEP, MOUNTAIN HIGH",
      "air_date": "2004-12-08",
      "question": "'The names of this highest mountain in Western Europe & this highest mountain in the Pacific both mean \"White Mountain\"'",
      "value": "$1200",
      "answer": "Mont Blanc and Mauna Kea",
      "round": "Double Jeopardy!",
      "show_number": "4663"
    },
    {
      "category": "FRIENDS",
      "air_date": "2005-07-14",
      "question": "'Born in 1963, this former member of the Groundlings is the oldest of the 6 \"Friends\"'",
      "value": "$800",
      "answer": "Lisa Kudrow",
      "round": "Jeopardy!",
      "show_number": "4819"
    },
    {
      "category": "WARS",
      "air_date": "1984-11-29",
      "question": "'The material cost of this war was greater than all other wars put together'",
      "value": "$400",
      "answer": "World War II",
      "round": "Double Jeopardy!",
      "show_number": "59"
    },
    {
      "category": "GENESIS QUOTE FILL-IN",
      "air_date": "2011-02-03",
      "question": "'\"There were ____ in the earth in those days\"'",
      "value": "$800",
      "answer": "giants",
      "round": "Jeopardy!",
      "show_number": "6079"
    },
    {
      "category": "LEAVE 'EM LAUGHING",
      "air_date": "2007-09-12",
      "question": "'This term for an object of ridicule sounds like shares bought in a comedy club'",
      "value": "$800",
      "answer": "laughing stock",
      "round": "Double Jeopardy!",
      "show_number": "5288"
    },
    {
      "category": "GOOD PROVERBS",
      "air_date": "1999-06-11",
      "question": "'\"All good things must\" do this'",
      "value": "$200",
      "answer": "Come to an end",
      "round": "Jeopardy!",
      "show_number": "3415"
    },
    {
      "category": "U.S. STATES",
      "air_date": "1990-02-02",
      "question": "'3 of the top 10 U.S. cities in population are in this state'",
      "value": "$500",
      "answer": "Texas (Dallas, Houston, San Antonio)",
      "round": "Jeopardy!",
      "show_number": "1255"
    },
    {
      "category": "MI CASA ES SU CASA",
      "air_date": "2004-01-19",
      "question": "'From 1939 until his death in 1975 (yes, he's still dead) he lived in the palace of El Pardo just NW of Madrid'",
      "value": "$800",
      "answer": "Francisco Franco",
      "round": "Double Jeopardy!",
      "show_number": "4461"
    },
    {
      "category": "RULING WORDS",
      "air_date": "1987-12-10",
      "question": "'A gynocracy is government by women; this, from Greek for \"man\", is government by men'",
      "value": "$1000",
      "answer": "an androcracy",
      "round": "Double Jeopardy!",
      "show_number": "759"
    },
    {
      "category": "COLLEGES & UNIVERSITIES",
      "air_date": "1998-03-18",
      "question": "'Located in Pyongyang, North Korea's oldest university is named for this late Communist leader'",
      "value": "$1000",
      "answer": "Kim Il-sung",
      "round": "Double Jeopardy!",
      "show_number": "3128"
    },
    {
      "category": "WATERFALLS",
      "air_date": "1998-10-14",
      "question": "'Sherlock Holmes & Dr. Moriarty went over these Swiss falls; only Holmes survived'",
      "value": "$600",
      "answer": "Reichenbach Falls",
      "round": "Double Jeopardy!",
      "show_number": "3243"
    },
    {
      "category": "ECONOMICS",
      "air_date": "2007-10-31",
      "question": "'In 2005 Americans didn't put money away but spent all they earned & more, for the 1st negative rate of this since 1933'",
      "value": "$2000",
      "answer": "savings",
      "round": "Double Jeopardy!",
      "show_number": "5323"
    },
    {
      "category": "BODY LANGUAGE",
      "air_date": "2011-01-12",
      "question": "'(Jimmy of the Clue Crew stands in front of a diagram of a human skeleton) To attack where someone is most vulnerable is to go for one of these large veins here or here'",
      "value": "$1000",
      "answer": "go for the jugular",
      "round": "Jeopardy!",
      "show_number": "6063"
    },
    {
      "category": "GEEK SQUAD",
      "air_date": "2008-06-11",
      "question": "'(A Geek indicates a computer port.) Today it's easy connecting devices by using USB; older computers use 2 types of ports, parallel & this one'",
      "value": "$1000",
      "answer": "serial",
      "round": "Jeopardy!",
      "show_number": "5483"
    },
    {
      "category": "MEDICAL ABBREV.",
      "air_date": "2003-03-31",
      "question": "'A test used to diagnose diabetes:(please, no eating or drinking after midnight)'",
      "value": "$2000",
      "answer": "fasting blood sugar",
      "round": "Double Jeopardy!",
      "show_number": "4286"
    },
    {
      "category": "THE 17th CENTURY",
      "air_date": "1998-10-22",
      "question": "'The 1648 Peace of Westphalia ended a war that began on May 23 of this year'",
      "value": None,
      "answer": "1618 (when The Thirty Years\\' War began)",
      "round": "Final Jeopardy!",
      "show_number": "3249"
    },
    {
      "category": "LITERARY TRIVIA",
      "air_date": "1993-04-01",
      "question": "'Dew-of-june, an Indian heroine, appears in his novel \"The Pathfinder\"'",
      "value": "$400",
      "answer": "James Fenimore Cooper",
      "round": "Double Jeopardy!",
      "show_number": "1984"
    },
    {
      "category": "MOVIE CRITTERS",
      "air_date": "2006-06-28",
      "question": "'1972:\"Sounder\"'",
      "value": "$400",
      "answer": "a dog",
      "round": "Double Jeopardy!",
      "show_number": "5033"
    },
    {
      "category": "BILL PULLMAN FILMS",
      "air_date": "1997-10-13",
      "question": "'Though he lost Meg Ryan in \"Sleepless In Seattle\", he won Sandra Bullock's heart in this film'",
      "value": "$300",
      "answer": "While You Were Sleeping",
      "round": "Jeopardy!",
      "show_number": "3016"
    },
    {
      "category": "FAMOUS NAMES",
      "air_date": "1999-09-28",
      "question": "'In April 1999 Paul Simon took center field for the dedication of a monument to this man'",
      "value": None,
      "answer": "Joe DiMaggio",
      "round": "Final Jeopardy!",
      "show_number": "3462"
    },
    {
      "category": "CELEBRITY BIRTHDAYS",
      "air_date": "1997-06-30",
      "question": "'This Dane could tickle the ivories for Robert Loggia January 3, their mutual birthday'",
      "value": "$300",
      "answer": "Victor Borge",
      "round": "Jeopardy!",
      "show_number": "2971"
    },
    {
      "category": "ODE TO ENGLAND",
      "air_date": "1993-05-14",
      "question": "'William's protection against besiegers, it's now the home of the Beefeaters'",
      "value": "$1000",
      "answer": "the Tower of London",
      "round": "Double Jeopardy!",
      "show_number": "2015"
    },
    {
      "category": "\"U\"2",
      "air_date": "2007-06-29",
      "question": "'A small, cone-shaped structure at the back of the soft palate'",
      "value": "$2000",
      "answer": "a uvula",
      "round": "Double Jeopardy!",
      "show_number": "5265"
    },
    {
      "category": "HOW DO YOU WORK THIS THING?",
      "air_date": "2001-09-14",
      "question": "'Insert in drain; crank handle clockwise while moving wire to dislodge clog; hike up pants'",
      "value": "$400",
      "answer": "a snake",
      "round": "Double Jeopardy!",
      "show_number": "3915"
    },
    {
      "category": "2006 SPORTS LAUGHS",
      "air_date": "2007-06-14",
      "question": "'A U.K. company was vilified for marketing \"Little Hooliganz\", action figures of fans of this sport'",
      "value": "$1600",
      "answer": "soccer",
      "round": "Double Jeopardy!",
      "show_number": "5254"
    },
    {
      "category": "HISTORIC NAMES",
      "air_date": "1997-03-06",
      "question": "'In 1891 this ex-chancellor of Germany was elected to the Reichstag'",
      "value": "$200",
      "answer": "Otto Von Bismarck",
      "round": "Double Jeopardy!",
      "show_number": "2889"
    },
    {
      "category": "ALSO A VEGAS CASINO",
      "air_date": "2009-03-18",
      "question": "'A couple of owls'",
      "value": "$1000",
      "answer": "hooters",
      "round": "Jeopardy!",
      "show_number": "5653"
    },
    {
      "category": "THE \"BUC\"s",
      "air_date": "2009-05-22",
      "question": "'It's grain ground into flour, o-tay?'",
      "value": "$400",
      "answer": "buckwheat",
      "round": "Double Jeopardy!",
      "show_number": "5700"
    },
    {
      "category": "THE ADVENTURES OF HUCKLEBERRY FINN",
      "air_date": "2008-11-06",
      "question": "'The title adventures concern a young boy named Huckleberry Finn & an escaped slave of this name'",
      "value": "$200",
      "answer": "Jim",
      "round": "Jeopardy!",
      "show_number": "5559"
    },
    {
      "category": "CLASSICAL GAS",
      "air_date": "2011-12-09",
      "question": "'This French composer of \"Danse Macabre\" was writing music by the time he was 5'",
      "value": "$2000",
      "answer": "Camille Saint-Saëns",
      "round": "Double Jeopardy!",
      "show_number": "6265"
    },
    {
      "category": "BIG SCREEN BIO SUBJECTS",
      "air_date": "2004-10-27",
      "question": "'\"A Beautiful Mind\"'",
      "value": "$2000",
      "answer": "(John) Nash",
      "round": "Double Jeopardy!",
      "show_number": "4633"
    },
    {
      "category": "POETIC POTPOURRI",
      "air_date": "1997-03-31",
      "question": "'Dorothy Parker called her 1931 book of verse \"Death And\" these, 2 things Ben Franklin said were certainties'",
      "value": "$300",
      "answer": "Death and taxes",
      "round": "Jeopardy!",
      "show_number": "2906"
    },
    {
      "category": "A TOUR OF THE REAGAN LIBRARY",
      "air_date": "2003-05-13",
      "question": "'(Jimmy of the Clue Crew gives the clue.) In 1989 the Notre Dame football team presented Reagan with this man's letter sweater'",
      "value": "$1000",
      "answer": "George Gipp",
      "round": "Jeopardy!",
      "show_number": "4317"
    },
    {
      "category": "WHEN WAS THAT, PIERRE?",
      "air_date": "1998-12-04",
      "question": "'Tres tragique was this year when France was first occupied in World War II'",
      "value": "$100",
      "answer": "1940",
      "round": "Jeopardy!",
      "show_number": "3280"
    },
    {
      "category": "13-LETTER WORDS",
      "air_date": "2007-04-17",
      "question": "'En francais, s'il vous plait! This thick slice of tenderloin is broiled & served with potatoes & a bernaise sauce'",
      "value": "$1600",
      "answer": "chateaubriand",
      "round": "Double Jeopardy!",
      "show_number": "5212"
    },
    {
      "category": "DEATH IN POP",
      "air_date": "1998-02-03",
      "question": "'Mark Dinning sang about a \"Teen\" one; Peter Stampfel, about a \"Surfer\" one'",
      "value": "$600",
      "answer": "Angel",
      "round": "Double Jeopardy!",
      "show_number": "3097"
    },
    {
      "category": "\"M\"MMM GOOD",
      "air_date": "2005-02-11",
      "question": "'This popular leafy soul food side dish is an excellent source of vitamins A & C'",
      "value": "$2000",
      "answer": "mustard greens",
      "round": "Double Jeopardy!",
      "show_number": "4710"
    },
    {
      "category": "ANDY WARHOL",
      "air_date": "2000-12-18",
      "question": "'Andy's \"15 minutes of fame\" quote was once the motto of this magazine'",
      "value": "$600",
      "answer": "Interview",
      "round": "Double Jeopardy!",
      "show_number": "3751"
    },
    {
      "category": "SCIENCE",
      "air_date": "2008-11-12",
      "question": "'These were first seen in human cells in 1882; the exact number, 46, was determined in 1956'",
      "value": "$600",
      "answer": "chromosomes",
      "round": "Jeopardy!",
      "show_number": "5563"
    },
    {
      "category": "ALABAMMY BOUND",
      "air_date": "2011-04-14",
      "question": "'This city's News boasts the largest circulation of any Alabama newspaper'",
      "value": "$1200",
      "answer": "Birmingham",
      "round": "Double Jeopardy!",
      "show_number": "6129"
    },
    {
      "category": "SUPERHERO NAMES THROUGH PICTURES",
      "air_date": "2010-02-10",
      "question": "'X marks the spot, man, when this guy opens his peeper'",
      "value": "$200",
      "answer": "Cyclops",
      "round": "Jeopardy!",
      "show_number": "5853"
    },
    {
      "category": "FAMOUS TRIALS",
      "air_date": "2009-07-10",
      "question": "'Stabbed during his capture at Harpers Ferry, this abolitionist spent most of his 1859 trial lying on a cot'",
      "value": "$800",
      "answer": "John Brown",
      "round": "Double Jeopardy!",
      "show_number": "5735"
    },
    {
      "category": "BESTSELLERS",
      "air_date": "1999-07-09",
      "question": "'Neale Donald Walsch, author of \"Conversations with\" this being, says that anybody can have them'",
      "value": "$100",
      "answer": "God",
      "round": "Jeopardy!",
      "show_number": "3435"
    },
    {
      "category": "SCIENTISTS",
      "air_date": "1997-06-02",
      "question": "'While a professor at Stanford in 1970 he published \"Vitamin C And The Common Cold\"'",
      "value": "$600",
      "answer": "Linus Pauling",
      "round": "Double Jeopardy!",
      "show_number": "2951"
    },
    {
      "category": "BANDS OF THE '80S",
      "air_date": "1997-01-01",
      "question": "'The Proclaimers hit the U.S. charts when \"I'm Gonna Be (500 Miles)\" was featured in this Johnny Depp film'",
      "value": "$400",
      "answer": "Benny and Joon",
      "round": "Jeopardy!",
      "show_number": "2843"
    },
    {
      "category": "LIP GLOSS",
      "air_date": "2007-01-23",
      "question": "'Zyderm & Zyplast are types of these injections that you can get in your lips to feel more \"Hollywood\"'",
      "value": "$1000",
      "answer": "collagen injections",
      "round": "Jeopardy!",
      "show_number": "5152"
    },
    {
      "category": "TREES",
      "air_date": "1996-12-19",
      "question": "'It has cricket bat & weeping varieties'",
      "value": "$200",
      "answer": "Willow",
      "round": "Double Jeopardy!",
      "show_number": "2834"
    },
    {
      "category": "FOOD",
      "air_date": "1998-06-25",
      "question": "'Its history shows the French taking an Austrian crescent roll & making it with puff pastry, not bread dough'",
      "value": "$300",
      "answer": "Croissant",
      "round": "Jeopardy!",
      "show_number": "3199"
    },
    {
      "category": "TO YOUR HEALTH",
      "air_date": "2001-04-24",
      "question": "'Ballistic, static & contract-relax are the 3 main types of this pre-workout activity'",
      "value": "$400",
      "answer": "Stretching",
      "round": "Jeopardy!",
      "show_number": "3842"
    },
    {
      "category": "THE CONGRESS",
      "air_date": "1991-11-14",
      "question": "'Representing Massachusetts' 8th District, Joseph P. Kennedy is the son of this late New York senator'",
      "value": "$200",
      "answer": "Robert F. Kennedy",
      "round": "Double Jeopardy!",
      "show_number": "1659"
    },
    {
      "category": "ATHLETES",
      "air_date": "2005-04-22",
      "question": "'Once a star basketball player for USC, from 1997 to 2000 she coached the WNBA's Phoenix Mercury'",
      "value": "$2000",
      "answer": "Cheryl Miller",
      "round": "Double Jeopardy!",
      "show_number": "4760"
    },
    {
      "category": "POP MUSIC",
      "air_date": "1998-07-13",
      "question": "'This group's \"Night Fever\" stayed at No. 1 longer than any other single of 1978 -- 8 weeks'",
      "value": "$300",
      "answer": "Bee Gees",
      "round": "Jeopardy!",
      "show_number": "3211"
    },
    {
      "category": "HIGH SCHOOLS",
      "air_date": "1999-03-05",
      "question": "'In 1989 students at a Cambridge, Mass. school boycotted Coca-Cola to protest its ties to this formerly racist country'",
      "value": "$400",
      "answer": "South Africa",
      "round": "Double Jeopardy!",
      "show_number": "3345"
    },
    {
      "category": "FOREIGN FASHION",
      "air_date": "2001-03-13",
      "question": "'Before a Swede puts on his skor, these, he puts on his sockor'",
      "value": "$200",
      "answer": "Shoes",
      "round": "Double Jeopardy!",
      "show_number": "3812"
    },
    {
      "category": "CAMILLA",
      "air_date": "2001-12-06",
      "question": "'Camilla Parker Bowles was born Camilla Shand on July 17, 1947 in this world capital'",
      "value": "$200",
      "answer": "London",
      "round": "Jeopardy!",
      "show_number": "3974"
    },
    {
      "category": "YOGA",
      "air_date": "2000-09-04",
      "question": "'Though you won't see Rover in it, the position seen here is called \"downward facing\" this'",
      "value": "$600",
      "answer": "Dog",
      "round": "Double Jeopardy!",
      "show_number": "3676"
    },
    {
      "category": "TRANSPORTATION",
      "air_date": "1988-11-15",
      "question": "'Doing this comes from the Roman custom of offering a drink to the gods when launching a ship'",
      "value": "$4,000",
      "answer": "Breaking Champagne on the Prow",
      "round": "Double Jeopardy!",
      "show_number": "967"
    },
    {
      "category": "PHYSICAL SCIENCE",
      "air_date": "1999-04-28",
      "question": "'Solid water is ice; solid carbon dioxide has this 2-word name'",
      "value": "$100",
      "answer": "dry ice",
      "round": "Jeopardy!",
      "show_number": "3383"
    },
    {
      "category": "NOT TO BE CONFUSED",
      "air_date": "2011-10-04",
      "question": "'Compost is used as fertilizer; this dessert is fruit cooked slowly in a sugar syrup'",
      "value": "$400",
      "answer": "compote",
      "round": "Double Jeopardy!",
      "show_number": "6217"
    },
    {
      "category": "FAMILY VALUES",
      "air_date": "2010-12-24",
      "question": "'In 2008 & 2009 foundations of this Arkansas family's company claimed it gave $423 million in cash & in-kind gifts'",
      "value": "$200",
      "answer": "the Waltons",
      "round": "Jeopardy!",
      "show_number": "6050"
    },
    {
      "category": "ALPHABET SOUP",
      "air_date": "1984-09-13",
      "question": "'He's the heavyweight of the A-Team'",
      "value": "$200",
      "answer": "Mr. T",
      "round": "Double Jeopardy!",
      "show_number": "4"
    },
    {
      "category": "BUSINESS & INDUSTRY",
      "air_date": "2000-04-05",
      "question": "'In the 1970s, this white buck-shoed singer & his family endorsed the West Bend coffee maker'",
      "value": "$800",
      "answer": "Pat Boone",
      "round": "Double Jeopardy!",
      "show_number": "3598"
    },
    {
      "category": "LAST BUT NOT LEAST",
      "air_date": "2001-10-19",
      "question": "'This band gave its last concert with Jerry Garcia at Chicago's Soldier Field in 1995'",
      "value": "$200",
      "answer": "the Grateful Dead",
      "round": "Jeopardy!",
      "show_number": "3940"
    },
    {
      "category": "2- OR 11-LETTER WORDS",
      "air_date": "2010-11-12",
      "question": "'Every 3 years; make it an adverb to fit the category'",
      "value": "$2000",
      "answer": "triannually",
      "round": "Double Jeopardy!",
      "show_number": "6020"
    },
    {
      "category": "MILITARY LEADERS",
      "air_date": "1991-11-07",
      "question": "'Robert E. Lee's truce flag was delivered to this general in 1865; in 1876 he was killed at Little Big Horn'",
      "value": "$200",
      "answer": "George Custer",
      "round": "Double Jeopardy!",
      "show_number": "1654"
    },
    {
      "category": "ROCK & ROLL FRONTMEN",
      "air_date": "2008-04-16",
      "question": "'Roger Daltrey'",
      "value": "$400",
      "answer": "The Who",
      "round": "Jeopardy!",
      "show_number": "5443"
    },
    {
      "category": "HEALTH & MEDICINE",
      "air_date": "1998-09-07",
      "question": "'The pineal gland also makes this popular hormone used to remedy sleep disorder & jet lag'",
      "value": "$800",
      "answer": "Melatonin",
      "round": "Double Jeopardy!",
      "show_number": "3216"
    },
    {
      "category": "BIBLICAL TRANSPORTATION",
      "air_date": "1992-05-21",
      "question": "'In Genesis 6 God said it should be pitched within & without with pitch'",
      "value": "$400",
      "answer": "Noah\\'s Ark (the ark accepted)",
      "round": "Jeopardy!",
      "show_number": "1794"
    },
    {
      "category": "FILL IN THE BLANK-ISTAN",
      "air_date": "2001-07-16",
      "question": "'This country's 4 provinces are Baluchistan, the Northwest Frontier, Sindh, & Punjab'",
      "value": "$400",
      "answer": "Pakistan",
      "round": "Double Jeopardy!",
      "show_number": "3901"
    },
    {
      "category": "DANCE ORIGINS",
      "air_date": "2011-01-11",
      "question": "'Flamenco'",
      "value": "$200",
      "answer": "Spain",
      "round": "Jeopardy!",
      "show_number": "6062"
    },
    {
      "category": "MUSICAL COMPOSITIONS",
      "air_date": "2005-11-30",
      "question": "'Mozart's \"Hunt\", heard here, is this type of chamber piece'",
      "value": "$800",
      "answer": "a (string) quartet",
      "round": "Double Jeopardy!",
      "show_number": "4883"
    },
    {
      "category": "FRENCH BRED",
      "air_date": "2000-09-28",
      "question": "'On May 6, 1758 Arras, France hatched this politician who later hatched the Reign of Terror'",
      "value": "$400",
      "answer": "Robespierre",
      "round": "Jeopardy!",
      "show_number": "3694"
    },
    {
      "category": "SCIENCE FICTION",
      "air_date": "2006-02-02",
      "question": "'In Jules Verne's \"The Mysterious Island\", this reclusive captain dies & is buried at sea in his submarine'",
      "value": "$200",
      "answer": "Captain Nemo",
      "round": "Jeopardy!",
      "show_number": "4929"
    },
    {
      "category": "KIDDIE LIT CHARACTERS",
      "air_date": "1999-09-10",
      "question": "'In the Winnie-the-Pooh stories, this very small animal is the only \"ham\"'",
      "value": "$200",
      "answer": "Piglet",
      "round": "Jeopardy!",
      "show_number": "3450"
    },
    {
      "category": "INDUSTRY",
      "air_date": "2000-04-07",
      "question": "'It was the first car off a moving assembly line'",
      "value": "$200",
      "answer": "Model T",
      "round": "Double Jeopardy!",
      "show_number": "3600"
    },
    {
      "category": "SHAKESPEAREAN CHARACTERS",
      "air_date": "1993-11-30",
      "question": "'This king's corpse is carried on stage in the first scene of \"Henry VI, Part I\"'",
      "value": "$200",
      "answer": "Henry V",
      "round": "Double Jeopardy!",
      "show_number": "2127"
    },
    {
      "category": "FOUR!",
      "air_date": "1999-01-19",
      "question": "'Published in 1943, \"Four Quartets\" is considered by many to be this American-born poet's finest work'",
      "value": "$500",
      "answer": "T.S. Eliot",
      "round": "Jeopardy!",
      "show_number": "3312"
    },
    {
      "category": "APPLES",
      "air_date": "1997-04-16",
      "question": "'Voltaire first spread the story about this scientist & the falling apple'",
      "value": "$300",
      "answer": "Isaac Newton",
      "round": "Jeopardy!",
      "show_number": "2918"
    },
    {
      "category": "THE IDES OF MARCH",
      "air_date": "1999-03-15",
      "question": "'March 15, 1919:U.S. veterans of WWI meet in Paris & set up this \"American\" organization'",
      "value": "$300",
      "answer": "The American Legion",
      "round": "Jeopardy!",
      "show_number": "3351"
    },
    {
      "category": "THE SWINGIN' '60s",
      "air_date": "1999-12-27",
      "question": "'In January 1966 this general was inaugurated for his second term as president of France'",
      "value": "$1000",
      "answer": "Charles de Gaulle",
      "round": "Double Jeopardy!",
      "show_number": "3526"
    },
    {
      "category": "SNOOP DOGG",
      "air_date": "2008-09-22",
      "question": "'What we have here, Frank, is Snoop's \"Sensual Seduction\", heard on a 2008 episode of this Fla.-based crime show'",
      "value": "$400",
      "answer": "CSI: Miami",
      "round": "Jeopardy!",
      "show_number": "5526"
    },
    {
      "category": "AROUND WILLIAMSBURG",
      "air_date": "1998-12-10",
      "question": "'Williamsburg was made defensible & had fewer mosquitos than this early English settlement a few miles to the SW'",
      "value": "$600",
      "answer": "Jamestown",
      "round": "Double Jeopardy!",
      "show_number": "3284"
    },
    {
      "category": "GOD",
      "air_date": "2004-01-12",
      "question": "'Nebuchadnezzar told him, \"Your god is a god of gods, and a lord of kings\"'",
      "value": "$1200",
      "answer": "Daniel",
      "round": "Double Jeopardy!",
      "show_number": "4456"
    },
    {
      "category": "AS EASY AS A-B-C",
      "air_date": "2009-09-16",
      "question": "'Lewis Carroll coined this term for meaningless words or gibberish'",
      "value": "$800",
      "answer": "jabberwocky",
      "round": "Jeopardy!",
      "show_number": "5748"
    },
    {
      "category": "ANIMAL QUOTES",
      "air_date": "2002-11-22",
      "question": "'\"All right\", said this animal: \"and this time it vanished quite slowly, beginning with the end of the tail\"'",
      "value": "$600",
      "answer": "Cheshire Cat",
      "round": "Jeopardy!",
      "show_number": "4195"
    },
    {
      "category": "EXPLORERS",
      "air_date": "1990-11-14",
      "question": "'This explorer was about 60 when he died in Cuba in 1521, not too youthful'",
      "value": "$600",
      "answer": "Ponce de León",
      "round": "Double Jeopardy!",
      "show_number": "1428"
    },
    {
      "category": "MOVIE MUSICALS",
      "air_date": "2003-01-01",
      "question": "'Elsa Lanchester played Katie Nanna, the nanny who walks out on the Banks family at the beginning of this film'",
      "value": "$400",
      "answer": "Mary Poppins",
      "round": "Double Jeopardy!",
      "show_number": "4223"
    },
    {
      "category": "POLICE & THIEVES",
      "air_date": "2008-03-26",
      "question": "'This naval hero thought up his surname to hide from the British, who tried to arrest him as a pirate'",
      "value": "$1,000",
      "answer": "John Paul Jones",
      "round": "Double Jeopardy!",
      "show_number": "5428"
    },
    {
      "category": "SPORTS STARS",
      "air_date": "2004-02-05",
      "question": "'Special delivery for the Lakers, who signed this forward, \"The Mailman\", in 2003'",
      "value": "$400",
      "answer": "Karl Malone",
      "round": "Double Jeopardy!",
      "show_number": "4474"
    },
    {
      "category": "ISLANDS",
      "air_date": "2000-02-09",
      "question": "'Now 73, the woman seen here at age 17 calls this island nation home:(Queen Elizabeth II)'",
      "value": "$200",
      "answer": "Great Britain",
      "round": "Jeopardy!",
      "show_number": "3558"
    },
    {
      "category": "ISLANDS OF THE SOUTH PACIFIC",
      "air_date": "2008-07-03",
      "question": "'Legend says that the god Maui threw a fishhook into the sea from Samoa & brought up this current island kingdom'",
      "value": "$1600",
      "answer": "Tonga",
      "round": "Double Jeopardy!",
      "show_number": "5499"
    },
    {
      "category": "I'M IN HEAVEN",
      "air_date": "2002-11-19",
      "question": "'The death of this silent film idol, seen here, inspired the 1926 song \"There's a New Star in Heaven Tonight\"'",
      "value": "$800",
      "answer": "Rudolph Valentino",
      "round": "Jeopardy!",
      "show_number": "4192"
    },
    {
      "category": "NEW YORK LANDMARKS",
      "air_date": "2000-03-03",
      "question": "'This club's brief, glamorous life began in 1977 at 254 West 54th Street'",
      "value": "$700",
      "answer": "Studio 54",
      "round": "Double Jeopardy!",
      "show_number": "3575"
    },
    {
      "category": "WHAT THE \"H\"?",
      "air_date": "2007-09-26",
      "question": "'In the 18th century B.C., he wrote down his famous list of dos & don'ts'",
      "value": "$4,000",
      "answer": "Hammurabi",
      "round": "Double Jeopardy!",
      "show_number": "5298"
    },
    {
      "category": "NETWORKING",
      "air_date": "2011-03-21",
      "question": "'\"The Closer \"'",
      "value": "$1000",
      "answer": "TNT",
      "round": "Jeopardy!",
      "show_number": "6111"
    },
    {
      "category": "ANATOMY",
      "air_date": "1984-09-13",
      "question": "'Mark Anthony borrowed them, then bent them'",
      "value": "$200",
      "answer": "ears",
      "round": "Double Jeopardy!",
      "show_number": "4"
    },
    {
      "category": "SCIENCE",
      "air_date": "1997-06-19",
      "question": "'Human beings normally have 46 of these in most of their cells'",
      "value": "$200",
      "answer": "Chromosomes",
      "round": "Jeopardy!",
      "show_number": "2964"
    },
    {
      "category": "CHURCHES",
      "air_date": "2005-06-15",
      "question": "'At Ulm, Germany, here is the church & here is this structure, a towering 528 feet'",
      "value": "$200",
      "answer": "the steeple",
      "round": "Jeopardy!",
      "show_number": "4798"
    },
    {
      "category": "WORD ORIGINS",
      "air_date": "1998-09-30",
      "question": "'Originally, it referred to a boisterous, rude lad, not a young girl who behaves like a lad as it does now'",
      "value": "$500",
      "answer": "Tomboy",
      "round": "Jeopardy!",
      "show_number": "3233"
    },
    {
      "category": "TECH-KNOW",
      "air_date": "2011-03-04",
      "question": "'smugmug.com lets you share these & back them up'",
      "value": "$600",
      "answer": "pictures (or photographs)",
      "round": "Jeopardy!",
      "show_number": "6100"
    },
    {
      "category": "OLD EGYPT",
      "air_date": "1999-11-11",
      "question": "'This young lad took the -aton off his name & restored the old state religion Akhenaton had changed'",
      "value": "$600",
      "answer": "Tutankhamun",
      "round": "Double Jeopardy!",
      "show_number": "3494"
    },
    {
      "category": "FRENCH NAMES OF COUNTRIES",
      "air_date": "1997-07-08",
      "question": "'Liban'",
      "value": "$400",
      "answer": "Lebanon",
      "round": "Jeopardy!",
      "show_number": "2977"
    },
    {
      "category": "THE BIRD IS THE WORD",
      "air_date": "2005-01-10",
      "question": "'(Jimmy of the Clue Crew holds a pink disc.)  It's the general two-word term for a trap shooting target--live ones went out in the early 1900s'",
      "value": "$1000",
      "answer": "a clay pigeon",
      "round": "Jeopardy!",
      "show_number": "4686"
    },
    {
      "category": "JUST DESSERTS",
      "air_date": "2008-10-10",
      "question": "'One story about the origin of the name of this pie says its sweetness attracted a certain insect'",
      "value": "$800",
      "answer": "shoo-fly pie",
      "round": "Jeopardy!",
      "show_number": "5540"
    },
    {
      "category": "BODILY FLUIDS",
      "air_date": "2008-06-12",
      "question": "'When a woman's \"water breaks\", the sac that contains this fluid has ruptured'",
      "value": "$800",
      "answer": "amniotic fluid",
      "round": "Jeopardy!",
      "show_number": "5484"
    },
    {
      "category": "AFRICAN-AMERICANA",
      "air_date": "2007-01-15",
      "question": "'Frederick Douglass said this political party was the ship & everything else was the ocean'",
      "value": "$400",
      "answer": "the Republican Party",
      "round": "Jeopardy!",
      "show_number": "5146"
    },
    {
      "category": "WWII TRIVIA",
      "air_date": "1985-10-04",
      "question": "'The U.S. Navy had a ship whose sole purpose was to make this dessert'",
      "value": "$200",
      "answer": "ice cream",
      "round": "Jeopardy!",
      "show_number": "280"
    },
    {
      "category": "TREES",
      "air_date": "2011-09-21",
      "question": "'Acer rubrum is the scientific name for this colorful state tree of Rhode Island'",
      "value": "$2000",
      "answer": "the red maple",
      "round": "Double Jeopardy!",
      "show_number": "6208"
    },
    {
      "category": "ARTISTS",
      "air_date": "2006-12-27",
      "question": "'During his Rose Period, he often painted Harlequins & Saltimbanques'",
      "value": "$400",
      "answer": "Picasso",
      "round": "Double Jeopardy!",
      "show_number": "5133"
    },
    {
      "category": "TUTTI FRUITY",
      "air_date": "2002-09-11",
      "question": "'It's also known as a \"cooking banana\"'",
      "value": "$1200",
      "answer": "Plantain",
      "round": "Double Jeopardy!",
      "show_number": "4143"
    },
    {
      "category": "CHILD'S PLAY",
      "air_date": "2009-06-04",
      "question": "'A Dickens tale of child pickpockets & orphans came to the stage as this Tony-winning musical'",
      "value": "$600",
      "answer": "Oliver!",
      "round": "Jeopardy!",
      "show_number": "5709"
    },
    {
      "category": "THE ODYSSEY",
      "air_date": "1991-11-11",
      "question": "'This Greek messenger of the gods gives Odysseus an herb that protects him from Circe's spell'",
      "value": "$800",
      "answer": "Hermes",
      "round": "Double Jeopardy!",
      "show_number": "1656"
    },
    {
      "category": "LET'S GET TOGETHER",
      "air_date": "2003-03-11",
      "question": "'Another name for a costume ball; it's also in the title of a George Benson hit'",
      "value": "$800",
      "answer": "masquerade",
      "round": "Jeopardy!",
      "show_number": "4272"
    },
    {
      "category": "POTPOURRI",
      "air_date": "1989-12-21",
      "question": "'In-Mut-Too-Yah-Lat-Lat was the Indian name of this Nez Perce chief who would \"fight no more forever\"'",
      "value": "$600",
      "answer": "Chief Joseph",
      "round": "Double Jeopardy!",
      "show_number": "1224"
    },
    {
      "category": "THE CIVIL WAR",
      "air_date": "1998-12-31",
      "question": "'This grandson of the ninth president commanded troops in the Army of the Cumberland'",
      "value": "$600",
      "answer": "Benjamon Harrison",
      "round": "Double Jeopardy!",
      "show_number": "3299"
    },
    {
      "category": "ON THE STAGE",
      "air_date": "2001-09-24",
      "question": "'Based on Frances Hodgson Burnett's book, this musical is named for the \"secret\" place'",
      "value": "$600",
      "answer": "The Secret Garden",
      "round": "Double Jeopardy!",
      "show_number": "3921"
    },
    {
      "category": "AROUND THE U.S.A.",
      "air_date": "1999-06-24",
      "question": "'The Hotter 'N Hell Hundred Bicycle Ride is a summer event in this state's Wichita Falls'",
      "value": "$500",
      "answer": "Texas",
      "round": "Jeopardy!",
      "show_number": "3424"
    },
    {
      "category": "THE CRUSADES",
      "air_date": "1999-12-28",
      "question": "'This wife of Louis VII of France said if he went off to Jerusalem she'd get a divorce, so he dragged her along by force'",
      "value": "$600",
      "answer": "Eleanor of Aquitaine",
      "round": "Double Jeopardy!",
      "show_number": "3527"
    },
    {
      "category": "WHAT'S UP, CLOCK?",
      "air_date": "2006-12-01",
      "question": "'In a Mother Goose nursery rhyme, these 3 words precede \"the mouse ran up the clock\"'",
      "value": "$200",
      "answer": "hickory dickory dock",
      "round": "Jeopardy!",
      "show_number": "5115"
    },
    {
      "category": "MATH ABBREV. & SYMBOLS",
      "air_date": "2011-09-29",
      "question": "'Regarding sets, \"R\" refers to real numbers & \"Q\" refers to this group of numbers that also begins with 1'",
      "value": "$800",
      "answer": "rational numbers",
      "round": "Double Jeopardy!",
      "show_number": "6214"
    },
    {
      "category": "WAR STORIES",
      "air_date": "2007-05-24",
      "question": "'\"365 Days\", \"Born on the Fourth of July\"'",
      "value": "$1200",
      "answer": "Vietnam War",
      "round": "Double Jeopardy!",
      "show_number": "5239"
    },
    {
      "category": "I WROTE THAT!",
      "air_date": "2009-04-22",
      "question": "'\"Ottsy i Deti\", aka \"Fathers and Sons\"'",
      "value": "$2000",
      "answer": "Ivan Turgenev",
      "round": "Double Jeopardy!",
      "show_number": "5678"
    },
    {
      "category": "ENDS IN \"TH\"",
      "air_date": "2006-05-17",
      "question": "'This Minnesota city is the western terminus of the St. Lawrence Seaway'",
      "value": "$1200",
      "answer": "Duluth",
      "round": "Double Jeopardy!",
      "show_number": "5003"
    },
    {
      "category": "FUN IN THE \"SON\"",
      "air_date": "2004-04-15",
      "question": "'Also used in commercial fishing, it's known as echolocation in bats'",
      "value": "$800",
      "answer": "sonar",
      "round": "Double Jeopardy!",
      "show_number": "4524"
    },
    {
      "category": "THE FOREST",
      "air_date": "2006-03-22",
      "question": "'(Sarah of the Clue Crew reads from the World Forestry Center in Oregon.)  The Douglas fir is found in Oregon's forest, referred to as this mature 2-word term, often defined as being aged 150 to 200 years'",
      "value": "$2000",
      "answer": "old growth",
      "round": "Double Jeopardy!",
      "show_number": "4963"
    },
    {
      "category": "HAPPY BIRTHDAY, THE NEW YORK TIMES",
      "air_date": "2001-09-18",
      "question": "'2-word name for the section with headlines about \"Clues to the Cosmos\" & \"Plants as Pollution Sponges\"'",
      "value": "$600",
      "answer": "\"Science Times\"",
      "round": "Double Jeopardy!",
      "show_number": "3917"
    },
    {
      "category": "THE ANCIENTS SPEAK",
      "air_date": "2010-10-18",
      "question": "'This Greek lawmaker wrote about relieving citizens' debt, saying one \"who was enslaved is now free\"'",
      "value": "$2000",
      "answer": "Solon",
      "round": "Double Jeopardy!",
      "show_number": "6001"
    },
    {
      "category": "HUMAN PARASITES",
      "air_date": "1999-10-13",
      "question": "'These insects not only leave behind itchy welts, they may infect you with viral encephalitis'",
      "value": "$200",
      "answer": "Mosquitos",
      "round": "Jeopardy!",
      "show_number": "3473"
    },
    {
      "category": "I'M FUNEMPLOYED",
      "air_date": "2009-07-02",
      "question": "'Architecture is too staid; I want to design these, like Nitro at Six Flags'",
      "value": "$400",
      "answer": "roller coasters",
      "round": "Jeopardy!",
      "show_number": "5729"
    },
    {
      "category": "FRUITS & VEGETABLES",
      "air_date": "2001-01-11",
      "question": "'Sometimes served with cream or dipped in chocolate, these red fruits are also popular in a shortcake dish'",
      "value": "$200",
      "answer": "Strawberries",
      "round": "Double Jeopardy!",
      "show_number": "3769"
    },
    {
      "category": "LET'S TALK \"DIRTY\"",
      "air_date": "1998-01-26",
      "question": "'After leaving the Eagles in 1982, Don Henley went gold with this first solo hit'",
      "value": "$400",
      "answer": "\"Dirty Laundry\"",
      "round": "Jeopardy!",
      "show_number": "3091"
    },
    {
      "category": "A LITERARY TOUR",
      "air_date": "2003-01-29",
      "question": "'In Madrid, a plaque marks the house where this \"Don Quixote\" author lived & died'",
      "value": "$400",
      "answer": "Cervantes",
      "round": "Double Jeopardy!",
      "show_number": "4243"
    },
    {
      "category": "FAMOUS SCIENTISTS",
      "air_date": "1991-11-08",
      "question": "'Our main source of knowledge of Greek astronomy is his \"Almagest\", completed in the 2nd century'",
      "value": "$400",
      "answer": "Ptolemy",
      "round": "Double Jeopardy!",
      "show_number": "1655"
    },
    {
      "category": "AHD NEGATIVE PREFIXES",
      "air_date": "2009-04-22",
      "question": "'Before climactic'",
      "value": "$200",
      "answer": "anti-",
      "round": "Jeopardy!",
      "show_number": "5678"
    },
    {
      "category": "FINANCE",
      "air_date": "2007-11-15",
      "question": "'It's often set up by the wealthy for their kids, but California has a state children's one for poor folks'",
      "value": "$800",
      "answer": "a trust fund",
      "round": "Jeopardy!",
      "show_number": "5334"
    },
    {
      "category": "SAYS YOU",
      "air_date": "1999-01-04",
      "question": "'Abraham Lincoln said, \"The ballot is stronger than\" this'",
      "value": "$300",
      "answer": "The bullet",
      "round": "Jeopardy!",
      "show_number": "3301"
    },
    {
      "category": "2-LETTER WORDS",
      "air_date": "2003-03-25",
      "question": "'A person who has a selfish reason for doing something has this tool \"to grind\"'",
      "value": "$200",
      "answer": "ax",
      "round": "Jeopardy!",
      "show_number": "4282"
    },
    {
      "category": "'70s POP CULTURE",
      "air_date": "2005-12-20",
      "question": "'She was 13 when she became Broadway's original \"Annie\" in 1977'",
      "value": "$1600",
      "answer": "Andrea McArdle",
      "round": "Double Jeopardy!",
      "show_number": "4897"
    },
    {
      "category": "INTERNET FAVORITES",
      "air_date": "2010-02-04",
      "question": "'\"I'm On a Boat\" is one of many popular parody songs that started on this TV show & then went viral on the web'",
      "value": "$1600",
      "answer": "Saturday Night Live",
      "round": "Double Jeopardy!",
      "show_number": "5849"
    },
    {
      "category": "HOMOPHONIC PAIRS",
      "air_date": "2002-09-04",
      "question": "'The royal seat that was hurled'",
      "value": "$2000",
      "answer": "the thrown throne",
      "round": "Double Jeopardy!",
      "show_number": "4138"
    },
    {
      "category": "FAMILIAR PHRASES",
      "air_date": "2006-06-28",
      "question": "'The expression \"Banned in\" this city came from that city's enthusiastic censorship of books in the 1920s'",
      "value": "$600",
      "answer": "Boston",
      "round": "Jeopardy!",
      "show_number": "5033"
    },
    {
      "category": "MYTHOLOGY",
      "air_date": "1994-11-24",
      "question": "'With his own enchanting music, he was able to save the Argonauts from the Sirens'",
      "value": "$800",
      "answer": "Orpheus",
      "round": "Double Jeopardy!",
      "show_number": "2354"
    },
    {
      "category": "COLLEGE DEGREES",
      "air_date": "1991-12-20",
      "question": "'The field in which the honorary degree LL.D. is awarded'",
      "value": "$500",
      "answer": "law",
      "round": "Jeopardy!",
      "show_number": "1685"
    },
    {
      "category": "THAT'S SO RANDOM!",
      "air_date": "2004-11-12",
      "question": "'It's prohibited by the 5th Amendment, but you'll be facing it in the next round'",
      "value": "$600",
      "answer": "double jeopardy",
      "round": "Jeopardy!",
      "show_number": "4645"
    },
    {
      "category": "TV SHOWS IN OTHER WORDS",
      "air_date": "2004-06-29",
      "question": "'\"7 Plus 1 Completes the Need\"'",
      "value": "$600",
      "answer": "Eight Is Enough",
      "round": "Jeopardy!",
      "show_number": "4577"
    },
    {
      "category": "WEBSITES",
      "air_date": "2000-12-25",
      "question": "'At Ancestry.com you can build your own one of these & find out if you're on a main branch or just a twig'",
      "value": "$600",
      "answer": "family tree",
      "round": "Double Jeopardy!",
      "show_number": "3756"
    },
    {
      "category": "THE QUEEN'S ENGLISH",
      "air_date": "1990-03-19",
      "question": "'If you pinch a kipper you've stolen a fish; if you take a kip, you've done this'",
      "value": "$800",
      "answer": "taking a nap",
      "round": "Double Jeopardy!",
      "show_number": "1286"
    },
    {
      "category": "ACTORS & ACTRESSES",
      "air_date": "1997-05-09",
      "question": "'He played Michael Corleone in all 3 of Francis Ford Coppola's \"Godfather\" films'",
      "value": "$300",
      "answer": "Al Pacino",
      "round": "Jeopardy!",
      "show_number": "2935"
    },
    {
      "category": "COLLEGE BASKETBALL",
      "air_date": "2004-02-23",
      "question": "'Only 2 men have won 3 NCAA scoring titles -- Pete Maravich & this Cincinnati player known as the \"Big O\"'",
      "value": "$800",
      "answer": "Oscar Robertson",
      "round": "Jeopardy!",
      "show_number": "4486"
    },
    {
      "category": "FACE BOOK",
      "air_date": "2008-09-30",
      "question": "'A young woman named Latifa wrote the memoir \"My Forbidden Face: Growing Up Under\" this Afghan group'",
      "value": "$400",
      "answer": "the Taliban",
      "round": "Double Jeopardy!",
      "show_number": "5532"
    },
    {
      "category": "OSCAR IN THEIR FILM DEBUTS",
      "air_date": "2010-07-15",
      "question": "'Best Supporting Actress for \"On the Waterfront\" (1954)'",
      "value": "$2000",
      "answer": "Eva Marie Saint",
      "round": "Double Jeopardy!",
      "show_number": "5964"
    },
    {
      "category": "NEBRASKA: THE GOOD LIFE",
      "air_date": "2008-07-17",
      "question": "'Rub shoulders with Nebraska state legislators at Billy's restaurant on H Street in this capital'",
      "value": "$200",
      "answer": "Lincoln",
      "round": "Jeopardy!",
      "show_number": "5509"
    },
    {
      "category": "ART GAL-ERY",
      "air_date": "2007-11-12",
      "question": "'The stag shown here is by Rosa Bonheur, the first woman awarded the Grand Cross of this French medal'",
      "value": "$2,000",
      "answer": "the Legion of Honor",
      "round": "Double Jeopardy!",
      "show_number": "5331"
    },
    {
      "category": "EARS TO YOU!",
      "air_date": "2007-04-25",
      "question": "'As a friend of Walt Disney, Roy Williams was the first to put these on a hat'",
      "value": "$600",
      "answer": "(Mickey) Mouse ears",
      "round": "Jeopardy!",
      "show_number": "5218"
    },
    {
      "category": "REACH FOR THE STARS",
      "air_date": "1999-02-22",
      "question": "'Still familiar today, it's the 7-star constellation on the bottom of this ancient Chinese chart'",
      "value": "$400",
      "answer": "The Big Dipper",
      "round": "Double Jeopardy!",
      "show_number": "3336"
    },
    {
      "category": "TV SHOW OPENING NARRATIONS",
      "air_date": "2004-03-02",
      "question": "'\"Name: Richard Kimble.  Profession: Doctor of Medicine.  Destination: Death Row...\"'",
      "value": "$1000",
      "answer": "The Fugitive",
      "round": "Jeopardy!",
      "show_number": "4492"
    },
    {
      "category": "CROSSWORD CLUES \"O\"",
      "air_date": "2010-11-09",
      "question": "'To swing like a pendulum (9)'",
      "value": "$1200",
      "answer": "oscillate",
      "round": "Double Jeopardy!",
      "show_number": "6017"
    },
    {
      "category": "HISTORY THROUGH FOOTBALL",
      "air_date": "2007-05-10",
      "question": "'If you went to this European capital that existed only from 1949 to 1990, you'd definitely entered the \"red zone\"'",
      "value": "$400",
      "answer": "East Berlin",
      "round": "Double Jeopardy!",
      "show_number": "5229"
    },
    {
      "category": "LET'S GO WATERSKIING",
      "air_date": "2002-12-26",
      "question": "'The first national water ski championships were held in 1939 at this Long Island beach, also a theater site'",
      "value": "$800",
      "answer": "Jones Beach",
      "round": "Jeopardy!",
      "show_number": "4219"
    },
    {
      "category": "FOUR!",
      "air_date": "1999-01-19",
      "question": "'This set of concertos makes up the first part of Vivaldi's Opus 8'",
      "value": "$300",
      "answer": "The Four Seasons",
      "round": "Jeopardy!",
      "show_number": "3312"
    },
    {
      "category": "THE GARFIELD ERA",
      "air_date": "1993-06-30",
      "question": "'On April 5, 1881 the Treaty of Pretoria granted independence to this country'",
      "value": "$400",
      "answer": "South Africa",
      "round": "Jeopardy!",
      "show_number": "2048"
    },
    {
      "category": "'80s SONGS",
      "air_date": "2004-09-14",
      "question": "'This Pat Benatar song says, \"You come on like a flame, then you turn a cold shoulder\"'",
      "value": "$1600",
      "answer": "\"Fire And Ice\"",
      "round": "Double Jeopardy!",
      "show_number": "4602"
    },
    {
      "category": "FRENCH CLASS: THE BODY",
      "air_date": "2003-02-10",
      "question": "'If you're a nez-sayer, you're just referring to this body part'",
      "value": "$1600",
      "answer": "nose",
      "round": "Double Jeopardy!",
      "show_number": "4251"
    },
    {
      "category": "FROGS & TOADS",
      "air_date": "1997-10-24",
      "question": "'Group seen here, it took its name from a Monty Python skit: [video clue]'",
      "value": "$400",
      "answer": "Toad The Wet Sprocket",
      "round": "Jeopardy!",
      "show_number": "3025"
    },
    {
      "category": "MUSICMAKERS",
      "air_date": "2005-06-30",
      "question": "'In 1972 he \"and Mrs. Jones\" had a \"thing going on\"'",
      "value": "$1000",
      "answer": "Billy Paul",
      "round": "Jeopardy!",
      "show_number": "4809"
    },
    {
      "category": "COLLEGIATE SPORTS NICKNAMES",
      "air_date": "1999-07-22",
      "question": "'Texas A&M'",
      "value": "$200",
      "answer": "Aggies",
      "round": "Jeopardy!",
      "show_number": "3444"
    },
    {
      "category": "AIN'T THAT \"GRAND\"",
      "air_date": "1998-03-20",
      "question": "'This name for a railroad terminal at Park & 42nd is a synonym for frenzied activity'",
      "value": "$200",
      "answer": "Grand Central Station",
      "round": "Double Jeopardy!",
      "show_number": "3130"
    },
    {
      "category": "THE MOVIES",
      "air_date": "1997-06-26",
      "question": "'Glenn Close had a bit role as a male pirate in this 1991 Steven Spielberg fantasy about Peter Pan'",
      "value": "$100",
      "answer": "Hook",
      "round": "Jeopardy!",
      "show_number": "2969"
    },
    {
      "category": "CARTOONS",
      "air_date": "1998-01-14",
      "question": "'This \"sizzling\" star provided the voice of Balto, the heroic sled dog in a 1995 feature'",
      "value": "$500",
      "answer": "Kevin Bacon",
      "round": "Jeopardy!",
      "show_number": "3083"
    },
    {
      "category": "SOUNDS LIKE A NEW POKEMON",
      "air_date": "2010-07-09",
      "question": "'Melodeon's only power is to give enjoyment: it's a reed one of these'",
      "value": "$400",
      "answer": "an instrument",
      "round": "Jeopardy!",
      "show_number": "5960"
    },
    {
      "category": "THE BIBLE",
      "air_date": "1993-11-18",
      "question": "'In the book of Esther, he was hanged on the gallows that he had prepared for Mordecai'",
      "value": "$500",
      "answer": "Haman",
      "round": "Jeopardy!",
      "show_number": "2119"
    },
    {
      "category": "TRANSPORTATION",
      "air_date": "1988-12-02",
      "question": "'In 1783 Joseph & Jacques Montgolfier, sons of a French paper bag maker, invented this'",
      "value": "$600",
      "answer": "hot air balloon",
      "round": "Double Jeopardy!",
      "show_number": "980"
    },
    {
      "category": "STORY COLLECTIONS",
      "air_date": "2003-10-23",
      "question": "'If you like summer reruns, check out this 1837 Hawthorne collection (which was also reissued in 1842)'",
      "value": "$1600",
      "answer": "Twice-Told Tales",
      "round": "Double Jeopardy!",
      "show_number": "4399"
    },
    {
      "category": "1996 OLYMPIC GOLD MEDALISTS",
      "air_date": "1996-12-10",
      "question": "'Li Xiaoshuang became the first athlete from this country to win the men's all-around gold in gymnastics'",
      "value": "$100",
      "answer": "China",
      "round": "Jeopardy!",
      "show_number": "2827"
    },
    {
      "category": "ROCK MUSIC",
      "air_date": "1998-02-25",
      "question": "'In April of 1990 she began her worldwide \"Blond Ambition\" tour to promote her CD \"I'm Breathless\"'",
      "value": "$100",
      "answer": "Madonna",
      "round": "Jeopardy!",
      "show_number": "3113"
    },
    {
      "category": "ENGINEERING",
      "air_date": "1998-10-29",
      "question": "'The longest trip by rail you can take underwater is between these 2 countries'",
      "value": "$1,000",
      "answer": "England and France",
      "round": "Jeopardy!",
      "show_number": "3254"
    },
    {
      "category": "PLAY TIME",
      "air_date": "1998-03-16",
      "question": "'In this David Mamet play, Don Dubrow plans to steal a rare & valuable nickel'",
      "value": "$800",
      "answer": "American Buffalo",
      "round": "Double Jeopardy!",
      "show_number": "3126"
    },
    {
      "category": "SOUTH AMERICA",
      "air_date": "2001-05-11",
      "question": "'One of 2 landlocked countries in South America'",
      "value": None,
      "answer": "(1 of 2) Bolivia or Paraguay",
      "round": "Final Jeopardy!",
      "show_number": "3855"
    },
    {
      "category": "AUSTRALIA",
      "air_date": "2008-05-23",
      "question": "'An Australian sporting hero, Sir Donald Bradman is the only Aussie knighted for his services to this sport'",
      "value": "$600",
      "answer": "cricket",
      "round": "Jeopardy!",
      "show_number": "5470"
    },
    {
      "category": "\"J\" MART",
      "air_date": "2009-06-19",
      "question": "'He succeeded a daughter of Henry VIII in 1603'",
      "value": "$800",
      "answer": "James I",
      "round": "Jeopardy!",
      "show_number": "5720"
    },
    {
      "category": "9-LETTER WORDS",
      "air_date": "1997-11-26",
      "question": "'It describes a 2-House legislature'",
      "value": "$1000",
      "answer": "Bicameral",
      "round": "Double Jeopardy!",
      "show_number": "3048"
    },
    {
      "category": "THEATRE",
      "air_date": "2009-12-17",
      "question": "'\"To be or not to be\", Ralph Fiennes & more recently Jude Law have delivered the famous soliloquy as this Great Dane'",
      "value": "$200",
      "answer": "Hamlet",
      "round": "Jeopardy!",
      "show_number": "5814"
    },
    {
      "category": "A PLACE TO CALL HOME",
      "air_date": "2010-10-19",
      "question": "'From Greek words for \"living alone\", it's the place a monk calls home'",
      "value": "$800",
      "answer": "a monastery",
      "round": "Double Jeopardy!",
      "show_number": "6002"
    },
    {
      "category": "FASHIONABLE NAMES",
      "air_date": "1998-03-02",
      "question": "'This designer of Tommy jeans opened his flagship store in Beverly Hills in 1997'",
      "value": "$300",
      "answer": "Tommy Hifiger",
      "round": "Jeopardy!",
      "show_number": "3116"
    },
    {
      "category": "DISCOVERIES",
      "air_date": "2009-04-07",
      "question": "'By Newton--no, Leibniz--no, Newt--anyway, this branch of math'",
      "value": "$400",
      "answer": "calculus",
      "round": "Jeopardy!",
      "show_number": "5667"
    },
    {
      "category": "CROSSWORD CLUES \"Q\"",
      "air_date": "2008-03-27",
      "question": "'Where FBI agents train(8)'",
      "value": "$1600",
      "answer": "Quantico",
      "round": "Double Jeopardy!",
      "show_number": "5429"
    },
    {
      "category": "ANAGRAMMED CABINET DEPARTMENTS",
      "air_date": "2000-01-19",
      "question": "'To trap on trains'",
      "value": "$500",
      "answer": "Transportation",
      "round": "Jeopardy!",
      "show_number": "3543"
    },
    {
      "category": "RECONSTRUCTION",
      "air_date": "2007-03-01",
      "question": "'Reconstruction produced 2 black senators: Hiram Revels & Blanche Bruce, both from this state'",
      "value": "$1000",
      "answer": "Mississippi",
      "round": "Jeopardy!",
      "show_number": "5179"
    },
    {
      "category": "A TRIP TO LITERARY BRITAIN",
      "air_date": "1998-01-26",
      "question": "'Add a new twist to your London vacation & visit the home at 48 Doughty St. where he wrote \"Oliver Twist\"'",
      "value": "$200",
      "answer": "Charles Dickens",
      "round": "Double Jeopardy!",
      "show_number": "3091"
    },
    {
      "category": "GO SEE \"CAL\"",
      "air_date": "2007-06-26",
      "question": "'Ancient Roman name for the region of Scotland'",
      "value": "$2000",
      "answer": "Caledonia",
      "round": "Double Jeopardy!",
      "show_number": "5262"
    },
    {
      "category": "COLLEGE TEAM NICKNAMES",
      "air_date": "2007-07-23",
      "question": "'This University of Idaho nickname is from an old Germanic tribe whose name has come to mean troublemakers'",
      "value": "$1000",
      "answer": "Vandals",
      "round": "Jeopardy!",
      "show_number": "5281"
    },
    {
      "category": "4-LETTER VERBS",
      "air_date": "2001-05-15",
      "question": "'According to the title of a 1992 film \"White Men Can't\" do this'",
      "value": "$100",
      "answer": "Jump",
      "round": "Jeopardy!",
      "show_number": "3857"
    },
    {
      "category": "SCOTLAND",
      "air_date": "1988-01-12",
      "question": "'The weaver's cottage where this American steel king was born is part of a museum in Dunfermline'",
      "value": "$1000",
      "answer": "(Andrew) Carnegie",
      "round": "Double Jeopardy!",
      "show_number": "777"
    },
    {
      "category": "FUN WITH COLORS",
      "air_date": "2010-07-09",
      "question": "'This organization was founded in 1971; its efforts to save the whales gained worldwide attention'",
      "value": "$2000",
      "answer": "Greenpeace",
      "round": "Double Jeopardy!",
      "show_number": "5960"
    },
    {
      "category": "DUET TO ME ONE MORE TIME",
      "air_date": "2003-01-23",
      "question": "'\"Till I Loved You\", her hit song with Don Johnson, was written for the musical concept album \"Goya...A Life in Song\"'",
      "value": "$400",
      "answer": "Barbra Streisand",
      "round": "Jeopardy!",
      "show_number": "4239"
    },
    {
      "category": "WRITING FOR TV",
      "air_date": "2008-07-08",
      "question": "'Carol Barbee co-wrote the \"Why We Fight\" episode of this CBS show which fought its own cancellation (at least briefly)'",
      "value": "$800",
      "answer": "Jericho",
      "round": "Jeopardy!",
      "show_number": "5502"
    },
    {
      "category": "SCIENCE",
      "air_date": "1996-10-03",
      "question": "'Hirsutism is having more than the normal amount of this'",
      "value": "$100",
      "answer": "hair",
      "round": "Jeopardy!",
      "show_number": "2779"
    },
    {
      "category": "CELEBRITY MARRIAGES",
      "air_date": "1994-11-25",
      "question": "'Elizabeth Taylor converted to Judaism shortly before her 1959 marriage to this singer'",
      "value": "$400",
      "answer": "Eddie Fisher",
      "round": "Jeopardy!",
      "show_number": "2355"
    },
    {
      "category": "FAMOUS FAMILIES",
      "air_date": "2001-06-12",
      "question": "'Members of this family received a 1952 Pulitzer Prize, a 1954 Nobel & a 1979 Oscar nomination'",
      "value": None,
      "answer": "Hemingway (Ernest & his daughter Mariel)",
      "round": "Final Jeopardy!",
      "show_number": "3877"
    },
    {
      "category": "20th CENTURY STUFF",
      "air_date": "2001-07-17",
      "question": "'Noted gangster Pretty Boy Floyd's pretty boyhood was spent in this state's Cherokee Indian Territory'",
      "value": "$100",
      "answer": "Oklahoma",
      "round": "Jeopardy!",
      "show_number": "3902"
    },
    {
      "category": "CABLE CHANNELS",
      "air_date": "2010-10-15",
      "question": "'You can \"escape to chimp Eden\" on this channel'",
      "value": "$1000",
      "answer": "Animal Planet",
      "round": "Jeopardy!",
      "show_number": "6000"
    },
    {
      "category": "THIS & THAT",
      "air_date": "2012-01-13",
      "question": "'Greek myth says the goddess Eris not getting an invite to Peleus & Thetis' wedding feast helped lead to this war'",
      "value": "$400",
      "answer": "the Trojan War",
      "round": "Double Jeopardy!",
      "show_number": "6290"
    },
    {
      "category": "SAY CHEESE",
      "air_date": "1990-03-05",
      "question": "'According to legend, it was created when a shepherd left a piece of cheese in a cave for several weeks'",
      "value": "$500",
      "answer": "Roquefort",
      "round": "Jeopardy!",
      "show_number": "1276"
    },
    {
      "category": "THEY BITE, THEY STING",
      "air_date": "2001-01-31",
      "question": "'This mollusk captures its prey with its 8 arms, bites it with its beak & injects poison from its salivary glands'",
      "value": "$200",
      "answer": "the octopus",
      "round": "Double Jeopardy!",
      "show_number": "3783"
    },
    {
      "category": "VIRTUAL MEDICINE",
      "air_date": "2007-11-12",
      "question": "'(Sarah of the Clue Crew reads from the Carl J. Shapiro Simulation & Skills Center in Boston, MA.To ensure the passage of oxygen to the lungs, a tube is placed into this airway with care taken not to hit the esophagus behind it'",
      "value": "$800",
      "answer": "the trachea",
      "round": "Jeopardy!",
      "show_number": "5331"
    },
    {
      "category": "GEOLOGY",
      "air_date": "2006-06-13",
      "question": "'This \"table\" is the saturated area of bedrock; it tends to follow the contours of the land'",
      "value": "$1200",
      "answer": "the water table",
      "round": "Double Jeopardy!",
      "show_number": "5022"
    },
    {
      "category": "YOU NEED THERAPY",
      "air_date": "1999-02-02",
      "question": "'This \"therapy\" is drug treatment of infectious diseases like TB, as well as cancer'",
      "value": "$200",
      "answer": "Chemotherapy",
      "round": "Jeopardy!",
      "show_number": "3322"
    },
    {
      "category": "MOLDY OLDIES",
      "air_date": "2001-04-19",
      "question": "'\"Dandy\",\"Mrs. Brown You've Got A Lovely Daughter\"'",
      "value": "$300",
      "answer": "Herman\\'s Hermits",
      "round": "Jeopardy!",
      "show_number": "3839"
    },
    {
      "category": "WISH I'D SAID THAT",
      "air_date": "2004-09-24",
      "question": "'H.L. Mencken defined Puritanism as \"the haunting fear that someone, somewhere, may be\" this'",
      "value": "$1200",
      "answer": "happy",
      "round": "Double Jeopardy!",
      "show_number": "4610"
    },
    {
      "category": "___ OF ___",
      "air_date": "2006-09-22",
      "question": "'Edith Wharton won a Pulitzer Prize for this novel'",
      "value": "$200",
      "answer": "The Age of Innocence",
      "round": "Jeopardy!",
      "show_number": "5065"
    },
    {
      "category": "IN THE BOOKSTORE",
      "air_date": "2005-07-13",
      "question": "'This novel by Sue Monk Kidd about a 14-year-old southerner Lily Owen is a honey of a read'",
      "value": "$1600",
      "answer": "The Secret Life of Bees",
      "round": "Double Jeopardy!",
      "show_number": "4818"
    },
    {
      "category": "BIOLOGY",
      "air_date": "1997-02-11",
      "question": "'Some of these pituitary chemicals, like thyrotropin, affect other endocrine glands'",
      "value": "$600",
      "answer": "Hormones",
      "round": "Double Jeopardy!",
      "show_number": "2872"
    },
    {
      "category": "NO. 1 \"LOVE\" SONGS",
      "air_date": "2010-09-23",
      "question": "'The Captain & Tennille took this hopeful declaration to No. 1 in 1975'",
      "value": "$400",
      "answer": "\"Love Will Keep Us Together\"",
      "round": "Jeopardy!",
      "show_number": "5984"
    },
    {
      "category": "DREW BARRYMORE LOVES MUSIC",
      "air_date": "2007-12-07",
      "question": "'(Drew Barrymore gives the clue once more.) The ever-popular \"Evergreen\" has lyrics by Paul Williams & music by this singer who introduced it in \"A Star Is Born\"'",
      "value": "$600",
      "answer": "Barbra Streisand",
      "round": "Jeopardy!",
      "show_number": "5350"
    },
    {
      "category": "SHIPS",
      "air_date": "2006-04-07",
      "question": "'C.Y. Tung bought this ocean liner in 1970 with plans to convert her into the floating Seawise University'",
      "value": "$1000",
      "answer": "the Queen Elizabeth",
      "round": "Jeopardy!",
      "show_number": "4975"
    },
    {
      "category": "ENDS IN \"SS\"",
      "air_date": "2008-10-15",
      "question": "'Superstitious sailors have long believed that killing this large seabird brings bad luck'",
      "value": "$600",
      "answer": "an albatross",
      "round": "Jeopardy!",
      "show_number": "5543"
    },
    {
      "category": "SCHOOL PICTURE DAY",
      "air_date": "1999-09-10",
      "question": "'Before he was \"sent up the creek\", he was part of the Cheshire Academy'",
      "value": "$400",
      "answer": "James Van Der Beek",
      "round": "Double Jeopardy!",
      "show_number": "3450"
    },
    {
      "category": "KIDS IN SPORTS",
      "air_date": "2010-07-06",
      "question": "'11-year-old Ashlyn White won a 2009 U.S. youth title in this martial art in which you try to throw your opponent'",
      "value": "$1600",
      "answer": "judo",
      "round": "Double Jeopardy!",
      "show_number": "5957"
    },
    {
      "category": "COUNTRIES BY CAPITAL",
      "air_date": "2000-05-08",
      "question": "'In east Africa:Mogadishu'",
      "value": "$600",
      "answer": "Somalia",
      "round": "Double Jeopardy!",
      "show_number": "3621"
    },
    {
      "category": "A SLEEPY CATEGORY",
      "air_date": "2001-05-16",
      "question": "'He wrote, \"The woods are lovely, dark and deep.  But I have promises to keep, and miles to go before I sleep\"'",
      "value": "$400",
      "answer": "Robert Frost",
      "round": "Double Jeopardy!",
      "show_number": "3858"
    },
    {
      "category": "TOYS & GAMES",
      "air_date": "2001-04-16",
      "question": "'The world champion at this game gets $15,140, the amount of money in it'",
      "value": None,
      "answer": "Monopoly",
      "round": "Final Jeopardy!",
      "show_number": "3836"
    },
    {
      "category": "ALSO A PRESIDENTIAL NAME",
      "air_date": "2006-12-01",
      "question": "'Burn on, big river; in 1969 this city's Cuyahoga River actually caught fire'",
      "value": "$400",
      "answer": "Cleveland",
      "round": "Jeopardy!",
      "show_number": "5115"
    },
    {
      "category": "COMPLETES THE QUOTATION",
      "air_date": "2010-03-17",
      "question": "'\"Four score & 7 years ago our fathers brought forth, upon this continent, a new nation, conceived in _____\"'",
      "value": "$1200",
      "answer": "liberty",
      "round": "Double Jeopardy!",
      "show_number": "5878"
    },
    {
      "category": "AWARDS",
      "air_date": "1997-12-23",
      "question": "'This school's Hasty Pudding Club has been presenting its Woman of the Year Award since 1951'",
      "value": "$300",
      "answer": "Harvard",
      "round": "Jeopardy!",
      "show_number": "3067"
    },
    {
      "category": "BALLROOM BLITZ",
      "air_date": "2004-09-21",
      "question": "'An 18th century dance & a social ball are both called this, from a French word for \"petticoat\"'",
      "value": "$600",
      "answer": "a cotillion",
      "round": "Jeopardy!",
      "show_number": "4607"
    },
    {
      "category": "\"LONG\" JUMP",
      "air_date": "2004-10-07",
      "question": "'Its greatest use as a military weapon was during the Hundred Years' War; just ask the French at Crecy'",
      "value": "$800",
      "answer": "the longbow",
      "round": "Jeopardy!",
      "show_number": "4619"
    },
    {
      "category": "THE CIVIL WAR",
      "air_date": "1997-12-22",
      "question": "'This Confederate general's horse Traveller was originally named Jeff Davis'",
      "value": "$100",
      "answer": "Robert E. Lee",
      "round": "Jeopardy!",
      "show_number": "3066"
    },
    {
      "category": "OF \"RATH\"",
      "air_date": "2007-02-19",
      "question": "'On election night 2000, this newsman spouted lines like \"Bush will be madder than a rained-on rooster\"'",
      "value": "$800",
      "answer": "Dan Rather",
      "round": "Double Jeopardy!",
      "show_number": "5171"
    },
    {
      "category": "SIDE EFFECTS OF JEPOLAX",
      "air_date": "2006-07-14",
      "question": "'There are slight risks of acidosis, carcinoma & this sensation, from the Latin for \"choking chest pain\"'",
      "value": "$800",
      "answer": "angina",
      "round": "Jeopardy!",
      "show_number": "5045"
    },
    {
      "category": "NEEDFUL THINGS",
      "air_date": "1998-10-02",
      "question": "'Garlic & lime are found in this sauce that is essential to a classic Bloody Mary'",
      "value": "$400",
      "answer": "Worcestershire sauce",
      "round": "Jeopardy!",
      "show_number": "3235"
    },
    {
      "category": "JOURNALISM",
      "air_date": "2004-12-13",
      "question": "'It's the term for the first paragraph in a news story; a feature may have a delayed or indirect one'",
      "value": "$1000",
      "answer": "the lead",
      "round": "Jeopardy!",
      "show_number": "4666"
    },
    {
      "category": "U.S.A.",
      "air_date": "1990-03-08",
      "question": "'1 of the largest lakes in Minnesota, its name begins with the same 5 letters as Minnesota'",
      "value": "$1000",
      "answer": "Lake Minnetonka",
      "round": "Double Jeopardy!",
      "show_number": "1279"
    },
    {
      "category": "QUASI-RELATED PAIRS",
      "air_date": "1999-01-19",
      "question": "'\"The Nutcracker\" for example & Brat Pack actor Rob'",
      "value": "$400",
      "answer": "Suite & Lowe",
      "round": "Double Jeopardy!",
      "show_number": "3312"
    },
    {
      "category": "MAKING A GOOD IMPRESSIONIST",
      "air_date": "2002-12-03",
      "question": "'Painter of \"The Wave\", he was the father of French first wave filmmaker Jean'",
      "value": "$2000",
      "answer": "Pierre-Auguste Renoir",
      "round": "Double Jeopardy!",
      "show_number": "4202"
    },
    {
      "category": "EUROPEAN HISTORY",
      "air_date": "2006-03-09",
      "question": "'In 1991, republics of the former Soviet Union formed the CIS, which stands for this'",
      "value": "$2000",
      "answer": "the Commonwealth of Independent States",
      "round": "Double Jeopardy!",
      "show_number": "4954"
    },
    {
      "category": "LETTER MEN",
      "air_date": "2007-02-19",
      "question": "'He's the taller of the two gentlemen in the photo seen here'",
      "value": "$400",
      "answer": "P.T. Barnum",
      "round": "Jeopardy!",
      "show_number": "5171"
    },
    {
      "category": "___THE___",
      "air_date": "1990-02-26",
      "question": "'Witness Edison's invention, or come to an understanding of a situation'",
      "value": "$400",
      "answer": "See The Light",
      "round": "Jeopardy!",
      "show_number": "1271"
    },
    {
      "category": "STORES WITHOUT WALLS",
      "air_date": "1998-12-24",
      "question": "'You can buy tents & sleeping bags online at Idaho-based \"A Happy\" this'",
      "value": "$300",
      "answer": "Camper",
      "round": "Jeopardy!",
      "show_number": "3294"
    },
    {
      "category": "GREAT COMEBACKS WITH DAN PATRICK",
      "air_date": "2011-11-30",
      "question": "'(Dan Patrick reads the clue from his studio.)  A year after hitting .406, this Red Sox legend left to be a fighter pilot in WWII, came back, won the Triple Crown, left to fight in the Korean War, came back & was an All-Star'",
      "value": "$400",
      "answer": "Ted Williams",
      "round": "Jeopardy!",
      "show_number": "6258"
    },
    {
      "category": "THE KENNEDY CENTER",
      "air_date": "2006-01-11",
      "question": "'This American pianist who took Moscow (& the world) by storm in 1958 received a Kennedy Center honor in 2001'",
      "value": "$1000",
      "answer": "Van Cliburn",
      "round": "Jeopardy!",
      "show_number": "4913"
    },
    {
      "category": "BUSINESS & INDUSTRY",
      "air_date": "1997-06-16",
      "question": "'In 1996 companies that produce these consumables announced an end to their ban on TV & radio ads'",
      "value": "$200",
      "answer": "Liquor",
      "round": "Jeopardy!",
      "show_number": "2961"
    },
    {
      "category": "SPECIAL MONTHS",
      "air_date": "2009-10-12",
      "question": "'National UNICEF Day is observed during this month, National UNICEF Month'",
      "value": "$1,200",
      "answer": "October",
      "round": "Jeopardy!",
      "show_number": "5766"
    },
    {
      "category": "CLASSIC SITCOMS",
      "air_date": "2000-05-05",
      "question": "'This '70s character was given his last name because he talked ignorant nonsense'",
      "value": None,
      "answer": "Archie Bunker",
      "round": "Final Jeopardy!",
      "show_number": "3620"
    },
    {
      "category": "CITY HOMOPHONES",
      "air_date": "2010-12-24",
      "question": "'Helen's beau & Priam's son'",
      "value": "$400",
      "answer": "Paris",
      "round": "Double Jeopardy!",
      "show_number": "6050"
    },
    {
      "category": "ISMs",
      "air_date": "2000-02-10",
      "question": "'Manorialism was the economic basis of this system of political & military obligation in the Middle Ages'",
      "value": "$800",
      "answer": "Feudalism",
      "round": "Double Jeopardy!",
      "show_number": "3559"
    },
    {
      "category": "NAME THAT WESTERN",
      "air_date": "2005-01-03",
      "question": "'1991: \"Hi, Curly.  Killed anyone today?\"'",
      "value": "$800",
      "answer": "City Slickers",
      "round": "Double Jeopardy!",
      "show_number": "4681"
    },
    {
      "category": "WEIGHTS & MEASURES",
      "air_date": "1995-11-21",
      "question": "'Number of pecks in a bushel & a peck'",
      "value": "$1000",
      "answer": "5",
      "round": "Double Jeopardy!",
      "show_number": "2582"
    },
    {
      "category": "NEW YORK CITY HISTORY",
      "air_date": "2004-04-22",
      "question": "'Anger about the first one of these established by federal law spurred riots in July 1863'",
      "value": "$800",
      "answer": "a draft",
      "round": "Jeopardy!",
      "show_number": "4529"
    },
    {
      "category": "MEN OF SCIENCE",
      "air_date": "2010-02-16",
      "question": "'The flask that this British scientist invented in the 1890s was a predecessor of the Thermos'",
      "value": "$1600",
      "answer": "James Dewar",
      "round": "Double Jeopardy!",
      "show_number": "5857"
    },
    {
      "category": "STAMPS OF APPROVAL",
      "air_date": "2002-07-12",
      "question": "'These depicted on stamps include ones at Sandy Hook, New Jersey & Cape Hatteras, North Carolina'",
      "value": "$3,000",
      "answer": "lighthouses",
      "round": "Jeopardy!",
      "show_number": "4130"
    },
    {
      "category": "GAME SHOW FORMATS",
      "air_date": "2002-12-31",
      "question": "'2 contestants try to duplicate the answers given by 6 celebrities to funny fill-in-the-blank sentences'",
      "value": "$800",
      "answer": "The Match Game",
      "round": "Jeopardy!",
      "show_number": "4222"
    },
    {
      "category": "WOMEN ON U.S. STAMPS",
      "air_date": "2006-02-13",
      "question": "'1952:A famous seamstress & flagmaker'",
      "value": "$800",
      "answer": "Betsy Ross",
      "round": "Double Jeopardy!",
      "show_number": "4936"
    },
    {
      "category": "FASHIONABLE WORDS",
      "air_date": "2010-05-21",
      "question": "'Jackie Kennedy's iconic look included this classic round brimless hat'",
      "value": "$400",
      "answer": "pillbox",
      "round": "Jeopardy!",
      "show_number": "5925"
    },
    {
      "category": "MY LIFE OF \"E\"S",
      "air_date": "1998-09-14",
      "question": "'Instead of mere cream puffs, give me these oblong pastries with icing & a French name'",
      "value": "$200",
      "answer": "Eclairs",
      "round": "Jeopardy!",
      "show_number": "3221"
    },
    {
      "category": "POP MUSIC",
      "air_date": "2002-05-09",
      "question": "''70s classic heard here'",
      "value": "$400",
      "answer": "\"Walk On The Wild Side\"",
      "round": "Jeopardy!",
      "show_number": "4084"
    },
    {
      "category": "I WANNA BE...",
      "air_date": "2006-10-05",
      "question": "'...one of these, from the Greek for \"star sailor\", like John Glenn or Buzz Aldrin'",
      "value": "$800",
      "answer": "an astronaut",
      "round": "Double Jeopardy!",
      "show_number": "5074"
    },
    {
      "category": "\"E\" DAY",
      "air_date": "2011-03-28",
      "question": "'In Japan before WWII February 11 was celebrated as this large political unit day'",
      "value": "$2000",
      "answer": "Empire Day",
      "round": "Double Jeopardy!",
      "show_number": "6116"
    },
    {
      "category": "QUEEN ELIZABETH II",
      "air_date": "1999-02-05",
      "question": "'It's the Queen's royal family name & the name of one of her castles'",
      "value": "$200",
      "answer": "Windsor",
      "round": "Double Jeopardy!",
      "show_number": "3325"
    },
    {
      "category": "WHERE THE WILD THINGS ARE",
      "air_date": "1998-02-13",
      "question": "'Found in Central & South American forests, the spider monkey hangs from trees by this type of tail'",
      "value": "$200",
      "answer": "prehensile",
      "round": "Double Jeopardy!",
      "show_number": "3105"
    },
    {
      "category": "SPANS",
      "air_date": "2000-01-21",
      "question": "'Unlike many London sites, this bridge seen here is only about a century old:'",
      "value": "$400",
      "answer": "Tower Bridge",
      "round": "Double Jeopardy!",
      "show_number": "3545"
    },
    {
      "category": "MUSICAL THEATER",
      "air_date": "1998-09-11",
      "question": "'In France, this musical was known as \"Brillantine\"; in Mexico, it was \"Vaselina\"'",
      "value": None,
      "answer": "Grease",
      "round": "Final Jeopardy!",
      "show_number": "3220"
    },
    {
      "category": "WHEELS OF MISFORTUNE",
      "air_date": "2010-01-21",
      "question": "'Ford proclaimed the 1957 launch date of this car \"E-Day\"; let's say sales were disappointing'",
      "value": "$400",
      "answer": "the Edsel",
      "round": "Double Jeopardy!",
      "show_number": "5839"
    },
    {
      "category": "MAD MAGAZINE",
      "air_date": "2010-04-07",
      "question": "'Mad is under the corporate control of this comic book company that isn't based in Washington'",
      "value": "$800",
      "answer": "DC",
      "round": "Double Jeopardy!",
      "show_number": "5893"
    },
    {
      "category": "THE GREEK ALPHABET & MORE",
      "air_date": "2007-06-14",
      "question": "'This counter-terrorist military group headquartered at Fort Bragg is involved in hostage rescue'",
      "value": "$800",
      "answer": "Delta Force",
      "round": "Jeopardy!",
      "show_number": "5254"
    },
    {
      "category": "STRIVING FOR AN \"F\"",
      "air_date": "2011-02-17",
      "question": "'8-letter term meaning to exterminate pests using smoke'",
      "value": "$200",
      "answer": "fumigate",
      "round": "Jeopardy!",
      "show_number": "6089"
    },
    {
      "category": "GROOMING AIDS",
      "air_date": "2005-05-26",
      "question": "'To tighten your pores, you may use one of these, from the Latin for \"to draw together\"'",
      "value": "$400",
      "answer": "astringent",
      "round": "Jeopardy!",
      "show_number": "4784"
    },
    {
      "category": "A BUNCH OF STUFF",
      "air_date": "2008-06-19",
      "question": "'(Jimmy of the Clue Crew performs a science experiment.) Milk is a colloid, meaning a liquid with solid particles spread throughout; using vinegar, you can separate the solids, called curd, from the liquid, which is called this'",
      "value": "$400",
      "answer": "whey",
      "round": "Jeopardy!",
      "show_number": "5489"
    },
    {
      "category": "TRAVEL & TOURISM",
      "air_date": "1999-05-17",
      "question": "'This James Hoban-designed D.C. landmark, lit by electricity in 1891, will offer candlelight tours in December 1999'",
      "value": "$600",
      "answer": "the White House",
      "round": "Double Jeopardy!",
      "show_number": "3396"
    },
    {
      "category": "COMPOSERS",
      "air_date": "2007-05-25",
      "question": "'Beethoven said this great predecessor's name, which means \"brook\", should really be Meer, meaning \"sea\"'",
      "value": "$1200",
      "answer": "Bach",
      "round": "Double Jeopardy!",
      "show_number": "5240"
    },
    {
      "category": "SURVIVOR 12:  THE MUPPETS",
      "air_date": "2001-06-20",
      "question": "'Blaming all mishaps on an unseen mastodon-like creature, he outlasted the others to win $1 million'",
      "value": "$500",
      "answer": "Big Bird",
      "round": "Jeopardy!",
      "show_number": "3883"
    },
    {
      "category": "FAMOUS QUOTATIONS",
      "air_date": "2004-05-07",
      "question": "'According to the Declaration of Independence, \"All men are created\" this way'",
      "value": "$400",
      "answer": "equal",
      "round": "Double Jeopardy!",
      "show_number": "4540"
    },
    {
      "category": "YOU SAY MYANMAR, I SAY BURMA",
      "air_date": "2011-05-19",
      "question": "'Nearly 90% of Burmese practice this religion'",
      "value": "$600",
      "answer": "Buddhism",
      "round": "Jeopardy!",
      "show_number": "6154"
    },
    {
      "category": "IT'S LIKE, SHAKESPEARE, YOU KNOW?",
      "air_date": "2008-11-14",
      "question": "'What a drag!  She has to dress as a lawyer & be all like, \"Whatever!\" to save Antonio from Shylock'",
      "value": "$800",
      "answer": "Portia",
      "round": "Jeopardy!",
      "show_number": "5565"
    },
    {
      "category": "RIVER CITIES",
      "air_date": "1999-07-23",
      "question": "'1 of the 2 rivers at whose confluence the city of Montreal lies'",
      "value": "$500",
      "answer": "Ottawa or St. Lawrence",
      "round": "Jeopardy!",
      "show_number": "3445"
    },
    {
      "category": "YOU'RE FIRED!",
      "air_date": "2005-05-30",
      "question": "'In 1978 Handy Dan Hardware axed Arthur Blank-- but he did okay, co-founding this chain in Atlanta'",
      "value": "$2,200",
      "answer": "Home Depot",
      "round": "Jeopardy!",
      "show_number": "4786"
    },
    {
      "category": "GODZILLA",
      "air_date": "2006-03-28",
      "question": "'Apparently bored with his old conquests, in the 1998 version, Godzilla is intent on destroying this metropolis'",
      "value": "$800",
      "answer": "New York",
      "round": "Double Jeopardy!",
      "show_number": "4967"
    },
    {
      "category": "\"D-O\"",
      "air_date": "2011-12-29",
      "question": "'Small \"coins\" thrown from Mardi Gras floats'",
      "value": "$1600",
      "answer": "doubloons",
      "round": "Double Jeopardy!",
      "show_number": "6279"
    },
    {
      "category": "1979",
      "air_date": "1997-10-14",
      "question": "'Herman Tarnower & Nathan Pritikin rode the bestseller lists with books on doing this'",
      "value": "$200",
      "answer": "Dieting",
      "round": "Jeopardy!",
      "show_number": "3017"
    },
    {
      "category": "ORIGINAL PRANKSTA",
      "air_date": "2007-03-19",
      "question": "'In 1957 the British TV show \"Panorama\" reported on a bumper crop of this pasta grown in trees'",
      "value": "$1600",
      "answer": "spaghetti",
      "round": "Double Jeopardy!",
      "show_number": "5191"
    },
    {
      "category": "SINGERS ON FILM",
      "air_date": "1998-07-02",
      "question": "'\"Graffiti Bridge\", which he directed & starred in, was sort of a sequel to \"Purple Rain\"'",
      "value": "$1000",
      "answer": "Prince",
      "round": "Double Jeopardy!",
      "show_number": "3204"
    },
    {
      "category": "BOOKS",
      "air_date": "2004-03-05",
      "question": "'This book says, \"Monday burn Millay, Wednesday Whitman, Friday Faulkner...that's our official slogan\"'",
      "value": None,
      "answer": "Fahrenheit 451",
      "round": "Final Jeopardy!",
      "show_number": "4495"
    },
    {
      "category": "THE 4th",
      "air_date": "2002-07-03",
      "question": "'The 4th dimension according to the theory of relativity'",
      "value": "$400",
      "answer": "time",
      "round": "Jeopardy!",
      "show_number": "4123"
    },
    {
      "category": "MTM",
      "air_date": "2000-11-27",
      "question": "'(Hi, I'm Tyler Christopher of \"General Hospital\")  In 1984 as D.L. Brock he married Bobbie on \"G.H.\", in 1974 as Joe Gerard he married Rhoda on \"Rhoda\"'",
      "value": "$1000",
      "answer": "David Groh",
      "round": "Double Jeopardy!",
      "show_number": "3736"
    },
    {
      "category": "LETTER & LETTER",
      "air_date": "2004-01-12",
      "question": "'Charles Keating owned the Lincoln one that failed in the 1980s'",
      "value": "$800",
      "answer": "S&L",
      "round": "Jeopardy!",
      "show_number": "4456"
    },
    {
      "category": "TANK ARRAY",
      "air_date": "2009-11-17",
      "question": "'The U.S. Army's M-1 Abrams tank replaced the M-60 that bore the name of this tank commander'",
      "value": "$2000",
      "answer": "Patton",
      "round": "Double Jeopardy!",
      "show_number": "5792"
    },
    {
      "category": "HACKER CINEMA",
      "air_date": "2006-01-03",
      "question": "'In this 1999 film a character named for the god of dreams searches for the one who will destroy a computer world'",
      "value": "$600",
      "answer": "The Matrix",
      "round": "Jeopardy!",
      "show_number": "4907"
    },
    {
      "category": "U.S. HISTORY",
      "air_date": "1990-01-08",
      "question": "'Black Shawl was the wife of this Indian who helped lead the charge against Custer'",
      "value": "$200",
      "answer": "Crazy Horse",
      "round": "Jeopardy!",
      "show_number": "1236"
    },
    {
      "category": "THE ALPS",
      "air_date": "1999-11-24",
      "question": "'These features left over from the Ice Age include Maggiore, Constance & Como'",
      "value": "$800",
      "answer": "Lakes",
      "round": "Double Jeopardy!",
      "show_number": "3503"
    },
    {
      "category": "FIRST LADIES",
      "air_date": "1996-03-21",
      "question": "'During the 1960 presidential campaign, this Texan was called the Democrats' \"secret weapon\"'",
      "value": "$400",
      "answer": "Lady Bird Johnson",
      "round": "Double Jeopardy!",
      "show_number": "2669"
    },
    {
      "category": "TV MOVIES",
      "air_date": "2000-04-28",
      "question": "'This 1971 TV tearjerker told the story of a Chicago Bears running back & his battle with cancer'",
      "value": "$800",
      "answer": "Brian\\'s Song",
      "round": "Double Jeopardy!",
      "show_number": "3615"
    },
    {
      "category": "FOUNDERS",
      "air_date": "1998-06-03",
      "question": "'This Mass.-born businessman founded the Hawaiian Pineapple Company in 1901'",
      "value": "$600",
      "answer": "James Dole",
      "round": "Double Jeopardy!",
      "show_number": "3183"
    },
    {
      "category": "BANDS IN MOVIES",
      "air_date": "2010-05-25",
      "question": "'In 1968 The Monkees could be found in this film, also a body part'",
      "value": "$1600",
      "answer": "Head",
      "round": "Double Jeopardy!",
      "show_number": "5927"
    },
    {
      "category": "& NEVER THE TWAINS SHALL MEET",
      "air_date": "2005-06-22",
      "question": "'Mark first visited this city in 1872; in 1999 Shania played the Prince's Trust concert in Hyde Park there'",
      "value": "$1200",
      "answer": "London",
      "round": "Double Jeopardy!",
      "show_number": "4803"
    },
    {
      "category": "NO TIME TO TALK",
      "air_date": "2006-09-14",
      "question": "'This Scottish author of \"Kidnapped\" wrote, \"The cruelest lies are often told in silence\"'",
      "value": "$1000",
      "answer": "Robert Louis Stevenson",
      "round": "Jeopardy!",
      "show_number": "5059"
    },
    {
      "category": "THE NATIONAL PARK SYSTEM",
      "air_date": "2006-09-29",
      "question": "'The Wilcox House in Buffalo, N.Y., where he was sworn in as president, is designated a natl. historic site'",
      "value": "$600",
      "answer": "Teddy Roosevelt",
      "round": "Jeopardy!",
      "show_number": "5070"
    },
    {
      "category": "THE MIDDLE EAST",
      "air_date": "1999-09-29",
      "question": "'In 1967 this country lost the Golan Heights to Israel'",
      "value": "$400",
      "answer": "Syria",
      "round": "Double Jeopardy!",
      "show_number": "3463"
    },
    {
      "category": "BEFORE & AFTER",
      "air_date": "2009-11-26",
      "question": "'A recently surpassed all-time home run king turns into a \"killer\" vice president of the early 1800s'",
      "value": "$800",
      "answer": "Hank Aaron Burr",
      "round": "Double Jeopardy!",
      "show_number": "5799"
    },
    {
      "category": "PROPHET REPORT",
      "air_date": "2010-05-31",
      "question": "'Cassandra, a prophetess of Greek myth, also appears in this Shakespeare play'",
      "value": "$1,000",
      "answer": "Troilus and Cressida",
      "round": "Double Jeopardy!",
      "show_number": "5931"
    },
    {
      "category": "CROSSWORD CLUES \"M\"",
      "air_date": "2003-03-17",
      "question": "'Plaster condiment(7)'",
      "value": "$800",
      "answer": "mustard",
      "round": "Jeopardy!",
      "show_number": "4276"
    },
    {
      "category": "WOMEN",
      "air_date": "1986-02-05",
      "question": "'Her 1918 lunch with Robert Benchley at an Algonquin Hotel round table started a famous literary circle'",
      "value": "$400",
      "answer": "Dorothy Parker",
      "round": "Double Jeopardy!",
      "show_number": "368"
    },
    {
      "category": "AUSTRALIAN BUSINESS",
      "air_date": "2004-12-07",
      "question": "'In 2004 this corp. whose holdings include 20th Century Fox, announced plans to reincorporate in the U.S.'",
      "value": "$1000",
      "answer": "News Corp.",
      "round": "Jeopardy!",
      "show_number": "4662"
    },
    {
      "category": "LET'S ROCK!",
      "air_date": "2003-05-16",
      "question": "'\"My City of Ruins\" & other songs on this Bruce Springsteen CD relate in some way to the events of September 11, 2001'",
      "value": "$600",
      "answer": "\"The Rising\"",
      "round": "Jeopardy!",
      "show_number": "4320"
    },
    {
      "category": "CHEERS",
      "air_date": "2008-10-02",
      "question": "'This cocktail named for a motorcycle attachment is triple sec, brandy & lemon juice'",
      "value": "$800",
      "answer": "a sidecar",
      "round": "Jeopardy!",
      "show_number": "5534"
    },
    {
      "category": "CLASSIC CINEMA",
      "air_date": "2000-06-29",
      "question": "'1942:\"Major Strasser has been shot.  Round up the usual suspects.\"'",
      "value": "$100",
      "answer": "Casablanca",
      "round": "Jeopardy!",
      "show_number": "3659"
    },
    {
      "category": "TRAVEL & TOURISM",
      "air_date": "1995-12-08",
      "question": "'Lodgings in this capital city include the Hotel de L'annapurna & the Hotel Himalaya'",
      "value": "$1,200",
      "answer": "Katmandu",
      "round": "Double Jeopardy!",
      "show_number": "2595"
    },
    {
      "category": "FICTIONAL CHARACTERS",
      "air_date": "2000-02-15",
      "question": "'In \"Absalom! Absalom!\", it's the \"mythological\" name of Thomas Stupen's daughter, known as Clytie for short'",
      "value": "$1000",
      "answer": "Clytemnestra",
      "round": "Double Jeopardy!",
      "show_number": "3562"
    },
    {
      "category": "1967",
      "air_date": "2007-01-25",
      "question": "'In October, in a clash with army troops in Bolivia, this revolutionary leader was killed'",
      "value": "$600",
      "answer": "Che Guevara",
      "round": "Jeopardy!",
      "show_number": "5154"
    },
    {
      "category": "TUESDAY",
      "air_date": "1999-02-04",
      "question": "'Tuesday was Oscar-nominated for her role in this 1977 Diane Keaton film'",
      "value": "$800",
      "answer": "Looking For Mr. Goodbar",
      "round": "Double Jeopardy!",
      "show_number": "3324"
    },
    {
      "category": "AMERICAN AUTHORS",
      "air_date": "2009-05-08",
      "question": "'He reviewed films & TV for the New Republic before his first book, \"Goodbye, Columbus\", was published in 1959'",
      "value": "$2000",
      "answer": "Philip Roth",
      "round": "Double Jeopardy!",
      "show_number": "5690"
    },
    {
      "category": "THE WAR OF 1812",
      "air_date": "2006-09-28",
      "question": "'In this last major battle of the war, the British suffered about 2,000 casualties, including General Edward Pakenham'",
      "value": "$400",
      "answer": "the Battle of New Orleans",
      "round": "Jeopardy!",
      "show_number": "5069"
    },
    {
      "category": "CRUISE LINES",
      "air_date": "2008-10-09",
      "question": "'As Jerry Maguire, Tom tells Renee, \"You complete me\"; she says: \"Shut up, just shut up\", then this 5-word line'",
      "value": "$1200",
      "answer": "\"You had me at \\'hello\\'\"",
      "round": "Double Jeopardy!",
      "show_number": "5539"
    },
    {
      "category": "PRESIDENTIAL DEMISES",
      "air_date": "2001-02-27",
      "question": "'At 46 years, 177 days, he died at the youngest age of any president'",
      "value": "$100",
      "answer": "John F. Kennedy",
      "round": "Jeopardy!",
      "show_number": "3802"
    },
    {
      "category": "UP, UP & AWAY",
      "air_date": "2007-09-20",
      "question": "'There's a drawing of the first manned balloon flight as seen from Ben Franklin's place in this foreign city'",
      "value": "$400",
      "answer": "Paris",
      "round": "Double Jeopardy!",
      "show_number": "5294"
    },
    {
      "category": "LAST NAME'S THE SAME",
      "air_date": "2010-12-10",
      "question": "'South Carolina senator Lindsey & quarterback Otto'",
      "value": "$1000",
      "answer": "Graham",
      "round": "Jeopardy!",
      "show_number": "6040"
    },
    {
      "category": "JULY",
      "air_date": "1999-07-02",
      "question": "'Appropriately, it's what Canadians call the July 1 national holiday'",
      "value": "$200",
      "answer": "Canada Day",
      "round": "Double Jeopardy!",
      "show_number": "3430"
    },
    {
      "category": "DREAMS OF FIELDS",
      "air_date": "2010-06-01",
      "question": "'Britannica says this '30s film star was famed \"for his distinctive nasal voice... and his fondness for alcohol\"'",
      "value": "$800",
      "answer": "W.C. Fields",
      "round": "Double Jeopardy!",
      "show_number": "5932"
    },
    {
      "category": "POP MUSIC",
      "air_date": "1996-04-09",
      "question": "'His 1983 hit \"Beat It\" featured Eddie Van Halen on gutiar'",
      "value": "$200",
      "answer": "Michael Jackson",
      "round": "Jeopardy!",
      "show_number": "2682"
    },
    {
      "category": "COUNTRIES OF THE WORLD",
      "air_date": "2008-01-16",
      "question": "'This nation covers more than 6.5 million square miles in area'",
      "value": "$400",
      "answer": "Russia",
      "round": "Double Jeopardy!",
      "show_number": "5378"
    },
    {
      "category": "AT THE HOTEL",
      "air_date": "2001-06-12",
      "question": "'A mint placed here is a traditional sign you're in a high-class establishment'",
      "value": "$400",
      "answer": "On your pillow",
      "round": "Jeopardy!",
      "show_number": "3877"
    },
    {
      "category": "\"N\" THE MIDDLE",
      "air_date": "2011-06-23",
      "question": "'The Corinth one in Greece is only 3.9 miles long & has no locks'",
      "value": "$400",
      "answer": "a canal",
      "round": "Jeopardy!",
      "show_number": "6179"
    },
    {
      "category": "STATE CAPITAL NICKNAMES",
      "air_date": "1999-01-11",
      "question": "'It's the \"Queen on the James\" -- the James River, that is'",
      "value": "$800",
      "answer": "Richmond",
      "round": "Double Jeopardy!",
      "show_number": "3306"
    },
    {
      "category": "\"PARA\"GRAPHS",
      "air_date": "1997-09-05",
      "question": "'All the equipment used for a particular activity'",
      "value": "$1000",
      "answer": "Paraphernalia",
      "round": "Double Jeopardy!",
      "show_number": "2990"
    },
    {
      "category": "SONG SUNG \"BLUE\"",
      "air_date": "2005-06-24",
      "question": "'\"Sometimes I wonder what I'm a gonna do, but there ain't no cure for\" these'",
      "value": "$800",
      "answer": "the summertime blues",
      "round": "Double Jeopardy!",
      "show_number": "4805"
    },
    {
      "category": "PENINSULAS",
      "air_date": "2010-11-16",
      "question": "'The Adriatic, Ionian & Black Seas wash the shores of this peninsula'",
      "value": "$3,200",
      "answer": "the Balkan Peninsula",
      "round": "Double Jeopardy!",
      "show_number": "6022"
    },
    {
      "category": "\"SEX\" SELLS",
      "air_date": "2000-04-27",
      "question": "'The title to this 1962 runaway bestseller by Helen Gurley Brown was suggested to her by her husband'",
      "value": "$400",
      "answer": "\"Sex and the Single Girl\"",
      "round": "Double Jeopardy!",
      "show_number": "3614"
    },
    {
      "category": "THE 20th CENTURY",
      "air_date": "2008-09-25",
      "question": "'In 1973 members of AIM occupied this South Dakota village for 71 days to protest federal policies toward Indians'",
      "value": "$1200",
      "answer": "Wounded Knee",
      "round": "Double Jeopardy!",
      "show_number": "5529"
    },
    {
      "category": "AMERICAN BUSINESS",
      "air_date": "2006-07-24",
      "question": "'In 2006 Research In Motion settled its patent lawsuit with NTP over this portable wireless communications device'",
      "value": "$800",
      "answer": "a BlackBerry",
      "round": "Jeopardy!",
      "show_number": "5051"
    },
    {
      "category": "COUNTRIES OF THE WORLD",
      "air_date": "1997-01-01",
      "question": "'The Suez Canal divides the Asian & African portions of this country'",
      "value": "$400",
      "answer": "Egypt",
      "round": "Double Jeopardy!",
      "show_number": "2843"
    },
    {
      "category": "LIFE ON THE MISSISSIPPI",
      "air_date": "2000-02-10",
      "question": "'The Mississippi flows about 2,340 miles & empties into this body of water'",
      "value": "$200",
      "answer": "Gulf of Mexico",
      "round": "Double Jeopardy!",
      "show_number": "3559"
    },
    {
      "category": "BROADWAY",
      "air_date": "2007-02-15",
      "question": "'It's not easy for this \"Beauty and the Beast\" heroine to trip the light fantastic: her ball gown weighs more than 40 lbs.'",
      "value": "$400",
      "answer": "Belle",
      "round": "Double Jeopardy!",
      "show_number": "5169"
    },
    {
      "category": "WHO'S BUYING?",
      "air_date": "2010-12-23",
      "question": "'Wachovia, in 2008'",
      "value": "$2000",
      "answer": "Wells Fargo",
      "round": "Double Jeopardy!",
      "show_number": "6049"
    },
    {
      "category": "THE LANGUAGE OF PEACE",
      "air_date": "2011-05-18",
      "question": "'Pax'",
      "value": "$600",
      "answer": "Latin",
      "round": "Jeopardy!",
      "show_number": "6153"
    },
    {
      "category": "HOLIDAYS & OBSERVANCES",
      "air_date": "2003-05-01",
      "question": "'This symbol of Halloween may have originated in Medieval Scotland & was originally carved from a large turnip'",
      "value": "$400",
      "answer": "a jack-o\\'-lantern",
      "round": "Double Jeopardy!",
      "show_number": "4309"
    },
    {
      "category": "I THINK I LOVE SHOE",
      "air_date": "2011-12-29",
      "question": "'Have a unique fashion sense?  Into rubber sole? Then the shoe seen here, used in this sport, is for you'",
      "value": "$400",
      "answer": "bowling",
      "round": "Jeopardy!",
      "show_number": "6279"
    },
    {
      "category": "CAPITAL TOWNS",
      "air_date": "1998-12-24",
      "question": "'Elkhart in this state is the world capital of band instruments & RV manufacturing'",
      "value": "$600",
      "answer": "Indiana",
      "round": "Double Jeopardy!",
      "show_number": "3294"
    },
    {
      "category": "INTERNATIONAL MAIL",
      "air_date": "1996-10-07",
      "question": "'In Luxembourg they're only 4 digits long; in Brazil, 8'",
      "value": "$100",
      "answer": "a ZIP code",
      "round": "Jeopardy!",
      "show_number": "2781"
    },
    {
      "category": "THE ELEMENTS",
      "air_date": "2007-09-17",
      "question": "'When pronounced another way, this element is the top story on a newscast'",
      "value": "$800",
      "answer": "lead",
      "round": "Double Jeopardy!",
      "show_number": "5291"
    },
    {
      "category": "PSYCHOLOGY",
      "air_date": "2008-03-13",
      "question": "'Brought to the U.S. in the 1930s, this movement's name is German for \"pattern\" or \"shape\"'",
      "value": "$400",
      "answer": "gestalt",
      "round": "Double Jeopardy!",
      "show_number": "5419"
    },
    {
      "category": "SHERMANS",
      "air_date": "2006-05-30",
      "question": "'Sherman Minton was appointed to the U.S. Supreme Court in 1949 by this president'",
      "value": "$800",
      "answer": "Truman",
      "round": "Double Jeopardy!",
      "show_number": "5012"
    },
    {
      "category": "HISTORIC DOCUMENTS",
      "air_date": "1998-10-16",
      "question": "'Pope John XXIII addressed \"Pacem In Terris\", one of these letters, \"To all men of good will\"'",
      "value": "$600",
      "answer": "Papal encyclical",
      "round": "Double Jeopardy!",
      "show_number": "3245"
    },
    {
      "category": "MAURICE, BARRY OR ROBIN",
      "air_date": "2005-02-28",
      "question": "'Maeterlinck & Ravel'",
      "value": "$1000",
      "answer": "Maurice",
      "round": "Jeopardy!",
      "show_number": "4721"
    },
    {
      "category": "MEDICINAL PLANTS",
      "air_date": "2009-01-23",
      "question": "'From the Latin for \"little calendar\", it's a versatile antiseptic also taken internally'",
      "value": "$2000",
      "answer": "calendula",
      "round": "Double Jeopardy!",
      "show_number": "5615"
    },
    {
      "category": "TRIBUTE ALBUMS",
      "air_date": "2009-05-29",
      "question": "'Aerosmith covers \"Love Me Two Times\" on an album honoring this group's music'",
      "value": "$800",
      "answer": "the Doors",
      "round": "Double Jeopardy!",
      "show_number": "5705"
    },
    {
      "category": "GENESIS QUOTE FILL-IN",
      "air_date": "2011-02-03",
      "question": "'\"And God said, let us make man in our image, after our likeness: and let them have ____ over the fish of the sea\"'",
      "value": "$600",
      "answer": "dominion",
      "round": "Jeopardy!",
      "show_number": "6079"
    },
    {
      "category": "THIS SONG'S ALL WET!",
      "air_date": "2005-06-02",
      "question": "'The 2 title items in this Carpenters' tune, No. 2 in '71, \"always get me down\"'",
      "value": "$600",
      "answer": "\"Rainy Days And Mondays\"",
      "round": "Jeopardy!",
      "show_number": "4789"
    },
    {
      "category": "I'VE GOT THE POWER",
      "air_date": "2004-12-22",
      "question": "'As leader of the Baath party, he became dictator of a Middle Eastern country in 1979; in 2003 he was deposed'",
      "value": "$400",
      "answer": "Saddam Hussein",
      "round": "Jeopardy!",
      "show_number": "4673"
    },
    {
      "category": "ISLANDS OF THE SOUTHERN HEMISPHERE",
      "air_date": "2008-12-17",
      "question": "'Noted for its sea turtles, this volcanic island \"rises\" northwest of St. Helena in the South Atlantic'",
      "value": "$5,000",
      "answer": "Ascension Island",
      "round": "Double Jeopardy!",
      "show_number": "5588"
    },
    {
      "category": "YOU SANK MY BATTLESHIP!",
      "air_date": "2010-10-08",
      "question": "'A pocket battleship, the Graf this sank 9 British merchant ships before it was scuttled in 1939'",
      "value": "$2000",
      "answer": "Spee",
      "round": "Double Jeopardy!",
      "show_number": "5995"
    },
    {
      "category": "BRITISH POTPOURRI",
      "air_date": "1992-10-05",
      "question": "'In England it is appropriate to fly the Union Jack on April 23, this saint's day'",
      "value": "$500",
      "answer": "Saint George",
      "round": "Jeopardy!",
      "show_number": "1856"
    },
    {
      "category": "MR. X'S OBITUARY",
      "air_date": "2008-01-31",
      "question": "'He was in this military service, first ashore in the recapture of Guam on July 21, 1944'",
      "value": "$400",
      "answer": "the Marines",
      "round": "Jeopardy!",
      "show_number": "5389"
    },
    {
      "category": "NUTTY TV",
      "air_date": "2000-12-01",
      "question": "'Walnut Grove, Minnesota was the setting for this drama of the American West'",
      "value": "$400",
      "answer": "Little House on the Prairie",
      "round": "Jeopardy!",
      "show_number": "3740"
    },
    {
      "category": "\"GR\"!",
      "air_date": "2011-07-01",
      "question": "'Italy's Isle of Capri is famous for its \"blue\" one of these caves'",
      "value": "$400",
      "answer": "grotto",
      "round": "Jeopardy!",
      "show_number": "6185"
    },
    {
      "category": "CRIME RHYME TIME",
      "air_date": "2007-06-28",
      "question": "'A hip young delinquent'",
      "value": "$1000",
      "answer": "groovy juvie",
      "round": "Jeopardy!",
      "show_number": "5264"
    },
    {
      "category": "AMERICAN HISTORY",
      "air_date": "2004-01-15",
      "question": "'(Sofia of the Clue Crew at the Ronald Reagan Library)  This man awarded the Medal of Freedom to Ronald Reagan on January 13, 1993'",
      "value": "$800",
      "answer": "George H.W. Bush",
      "round": "Jeopardy!",
      "show_number": "4459"
    },
    {
      "category": "EUROPEAN CAPITALS",
      "air_date": "2004-09-09",
      "question": "'This capital lies on the Attica Plain surrounded by mountains including Parnes & Hymettus'",
      "value": "$800",
      "answer": "Athens",
      "round": "Jeopardy!",
      "show_number": "4599"
    },
    {
      "category": "TALKIN' TOLKIEN",
      "air_date": "2011-03-01",
      "question": "'Tolkien used this Old English word for \"monster\" as a synonym for \"goblin\"'",
      "value": "$1000",
      "answer": "orc",
      "round": "Jeopardy!",
      "show_number": "6097"
    },
    {
      "category": "BUSINESS & INDUSTRY",
      "air_date": "1987-04-24",
      "question": "'The largest grossing U.S. retail drug chain, it 1st put the ice cream in a chocolate malted milk'",
      "value": "$800",
      "answer": "Walgreens",
      "round": "Double Jeopardy!",
      "show_number": "620"
    },
    {
      "category": "BIG APPLE SAUCE",
      "air_date": "2001-05-22",
      "question": "'This island houses the inmates & staff of the New York City jail'",
      "value": "$800",
      "answer": "Rikers Island",
      "round": "Double Jeopardy!",
      "show_number": "3862"
    },
    {
      "category": "CRY \"UNCLE\"",
      "air_date": "1996-12-10",
      "question": "'In his famous recruitment poster, James Montgomery Flagg modeled this figure on himself'",
      "value": "$100",
      "answer": "Uncle Sam",
      "round": "Jeopardy!",
      "show_number": "2827"
    },
    {
      "category": "THROUGH THE LOOKING GLASS",
      "air_date": "2000-09-04",
      "question": "'Alice found this poem hard to understand even after she figured out that she had to hold it up to a mirror'",
      "value": "$1000",
      "answer": "\"Jabberwocky\"",
      "round": "Double Jeopardy!",
      "show_number": "3676"
    },
    {
      "category": "I LEARNED IT FROM WORLD BOOK",
      "air_date": "2009-10-22",
      "question": "'He \"was a shy, silent... Republican who led the U.S. during the boisterous Jazz Age\"'",
      "value": "$200",
      "answer": "Calvin Coolidge",
      "round": "Jeopardy!",
      "show_number": "5774"
    },
    {
      "category": "HYMNS & HERS",
      "air_date": "2006-10-27",
      "question": "'On a 1972 record she sings \"What a friend we have in Jesus\"; Rev. C.L. Franklin, her dad, is on the album too'",
      "value": "$400",
      "answer": "Aretha Franklin",
      "round": "Double Jeopardy!",
      "show_number": "5090"
    },
    {
      "category": "I HOP",
      "air_date": "2007-09-13",
      "question": "'This tiny insect pest, Pulex irritans, can leap more than 130 times its own height'",
      "value": "$1000",
      "answer": "flea",
      "round": "Jeopardy!",
      "show_number": "5289"
    },
    {
      "category": "\"D.C.\"",
      "air_date": "2002-10-31",
      "question": "'This team plays its home games in Texas Stadium'",
      "value": "$800",
      "answer": "Dallas Cowboys",
      "round": "Double Jeopardy!",
      "show_number": "4179"
    },
    {
      "category": "DOCTORS",
      "air_date": "1997-05-21",
      "question": "'In 1996 Renat Akchurin performed a 7-hour heart bypass operation on this Russian president'",
      "value": "$100",
      "answer": "Boris Yeltsin",
      "round": "Jeopardy!",
      "show_number": "2943"
    },
    {
      "category": "IS MIGHTIER THAN THE SWORD",
      "air_date": "2008-01-04",
      "question": "'The M60 type of this weapon is air-cooled, gas-operated & fires about 600 rounds per minute'",
      "value": "$400",
      "answer": "a machine gun",
      "round": "Jeopardy!",
      "show_number": "5370"
    },
    {
      "category": "A DAY AT THE HORSE RACES",
      "air_date": "2010-12-29",
      "question": "'At the far turn, it's my friend this horse now ridden by Alison Lohman, taking over for Roddy McDowall'",
      "value": "$800",
      "answer": "Flicka",
      "round": "Jeopardy!",
      "show_number": "6053"
    },
    {
      "category": "MARVELOUS",
      "air_date": "2007-01-30",
      "question": "'This alliterative super-villain could also have had a reality show called \"The Osborns\"'",
      "value": "$800",
      "answer": "the Green Goblin",
      "round": "Jeopardy!",
      "show_number": "5157"
    },
    {
      "category": "QUOTES",
      "air_date": "1991-01-17",
      "question": "'Mark Twain said this \"Parsifal\" composer's music \"is better than it sounds\"'",
      "value": "$400",
      "answer": "Richard Wagner",
      "round": "Jeopardy!",
      "show_number": "1474"
    },
    {
      "category": "I REALLY DIG YOU (UP)",
      "air_date": "1999-03-16",
      "question": "'In 1997 a made-up war record helped get M. Larry Lawrence buried at this Virginia cemetery -- briefly'",
      "value": "$200",
      "answer": "Arlington National Cemetery",
      "round": "Double Jeopardy!",
      "show_number": "3352"
    },
    {
      "category": "SUPER BOWL MVPs",
      "air_date": "2001-06-14",
      "question": "'XXVIII:Emmitt Smith'",
      "value": "$200",
      "answer": "Dallas Cowboys",
      "round": "Jeopardy!",
      "show_number": "3879"
    },
    {
      "category": "BODIES OF WATER",
      "air_date": "2007-10-08",
      "question": "'This British river that flows through London is also known as the Isis as it flows through Oxford'",
      "value": "$800",
      "answer": "the Thames",
      "round": "Double Jeopardy!",
      "show_number": "5306"
    },
    {
      "category": "UP & ATOM",
      "air_date": "2001-09-06",
      "question": "'Contrary to popular belief, the 28-year length of this for strontium 90 is not shared by a Twinkie'",
      "value": "$600",
      "answer": "the half-life",
      "round": "Double Jeopardy!",
      "show_number": "3909"
    },
    {
      "category": "QUOTES",
      "air_date": "1989-11-10",
      "question": "'England's James I called it \"Hateful to the nose, harmful to the brain, dangerous to the lungs\"'",
      "value": "$200",
      "answer": "Tobacco",
      "round": "Jeopardy!",
      "show_number": "1195"
    },
    {
      "category": "HAIKU GOES COUNTRY!",
      "air_date": "2007-05-02",
      "question": "'Hapsburgs' empire / Low-lying Neusiedler Lake / Hey, Schwarzenegger!'",
      "value": "$800",
      "answer": "Austria",
      "round": "Double Jeopardy!",
      "show_number": "5223"
    },
    {
      "category": "ALSO A BODY PART",
      "air_date": "2011-12-26",
      "question": "'(Jimmy of the Clue Crew spins the dreidel on the monitor.)  When it's your spin of the dreidel, hopefully you don't land on this 21st letter of the Hebrew alphabet, or you'll have to add to the pot'",
      "value": "$1000",
      "answer": "shin",
      "round": "Jeopardy!",
      "show_number": "6276"
    },
    {
      "category": "PITCHMEN",
      "air_date": "1998-12-31",
      "question": "'On the 70th anniversary of this brand in 1998, Mr. Whipple gave America permission to squeeze it'",
      "value": "$100",
      "answer": "the Charmin (bathroom tissue)",
      "round": "Jeopardy!",
      "show_number": "3299"
    },
    {
      "category": "SMALL ISLANDS",
      "air_date": "2007-03-20",
      "question": "'This atoll 1,300 miles NW of Honolulu, the site of a 1942 naval battle, is actually 2 small islands: Sand & Eastern'",
      "value": "$800",
      "answer": "Midway",
      "round": "Double Jeopardy!",
      "show_number": "5192"
    },
    {
      "category": "\"GRANT\"s & \"LEE\"s",
      "air_date": "1999-07-14",
      "question": "'The bill creating these colleges was signed into law by Abraham Lincoln'",
      "value": "$1000",
      "answer": "Land grant colleges",
      "round": "Double Jeopardy!",
      "show_number": "3438"
    },
    {
      "category": "LITERATURE",
      "air_date": "1998-12-10",
      "question": "'This character writes, \"Tom and me found the money that the robbers hid....we got six thousand dollars apiece\"'",
      "value": "$200",
      "answer": "Huckleberry Finn",
      "round": "Double Jeopardy!",
      "show_number": "3284"
    },
    {
      "category": "WORD ORIGINS",
      "air_date": "1998-02-24",
      "question": "'This state's name is from the Sioux for \"sky-tinted waters\"; maybe they meant the 10,000 lakes'",
      "value": "$200",
      "answer": "Minnesota",
      "round": "Double Jeopardy!",
      "show_number": "3112"
    },
    {
      "category": "COMMON BONDS",
      "air_date": "2010-12-22",
      "question": "'ICE, NIST'",
      "value": "$1200",
      "answer": "acronyms (of U.S. Government Agencies)",
      "round": "Double Jeopardy!",
      "show_number": "6048"
    },
    {
      "category": "SHAKESPEARE RETOOLED",
      "air_date": "2010-04-20",
      "question": "'In an attempt to come to grips with Shakespeare's \"Richard III\", this actor directed \"Looking for Richard\"'",
      "value": "$2000",
      "answer": "Al Pacino",
      "round": "Double Jeopardy!",
      "show_number": "5902"
    },
    {
      "category": "JOE MAMA",
      "air_date": "2005-01-05",
      "question": "'On Dec. 21, 1879 near Tbilisi, Georgia, Ekaterina Djugashvili gave birth to the future leader who went by this name'",
      "value": "$800",
      "answer": "Joseph Stalin",
      "round": "Double Jeopardy!",
      "show_number": "4683"
    },
    {
      "category": "PRINCE",
      "air_date": "2005-04-25",
      "question": "'The epithet of this prince, Richard II's father, probably refers to the color of his armor, not the terror he inspired'",
      "value": "$400",
      "answer": "(Edward) the Black Prince",
      "round": "Double Jeopardy!",
      "show_number": "4761"
    },
    {
      "category": "MR. OR MS. WILLIAMS",
      "air_date": "2000-05-04",
      "question": "'This devoted mom has been called the most famous Miss America of all time'",
      "value": "$1000",
      "answer": "Vanessa Williams",
      "round": "Double Jeopardy!",
      "show_number": "3619"
    },
    {
      "category": "FASHION FORWARD & BACKWARD",
      "air_date": "2009-03-23",
      "question": "'retro-housewife.com calls a '70s-style tunic in a '60s print a \"mippie\", a blend of mod & this word'",
      "value": "$400",
      "answer": "hippie",
      "round": "Jeopardy!",
      "show_number": "5656"
    },
    {
      "category": "GETTING SCIENTIFIC",
      "air_date": "2003-03-25",
      "question": "'(Sofia of the Clue Crew)  It's the process undergone by the moisture in your breath when it reaches cold air outside & becomes visible'",
      "value": "$2000",
      "answer": "condensation",
      "round": "Double Jeopardy!",
      "show_number": "4282"
    },
    {
      "category": "TOUGH HODGEPODGE",
      "air_date": "1999-06-24",
      "question": "'She choreographed the Jacksons' \"Torture\" video before becoming a singing star herself'",
      "value": "$200",
      "answer": "Paula Abdul",
      "round": "Double Jeopardy!",
      "show_number": "3424"
    },
    {
      "category": "BALLET",
      "air_date": "2003-11-10",
      "question": "'In 2003 the dance theatre of this N.Y. neighborhood presented the world premiere of \"St. Louis Woman: A Blues Ballet\"'",
      "value": "$1000",
      "answer": "Harlem",
      "round": "Jeopardy!",
      "show_number": "4411"
    },
    {
      "category": "DIVIDED BY A COMMON LANGUAGE",
      "air_date": "2007-01-25",
      "question": "'What the Brits call a jumper is a pullover one of these to an American'",
      "value": "$600",
      "answer": "sweater",
      "round": "Jeopardy!",
      "show_number": "5154"
    },
    {
      "category": "POINT IT OUT",
      "air_date": "1989-09-26",
      "question": "'In the sobriety test, you shut your eyes, put your arms out to your sides & touch this'",
      "value": "$200",
      "answer": "[your nose]",
      "round": "Jeopardy!",
      "show_number": "1162"
    },
    {
      "category": "WATER SPORTS",
      "air_date": "1984-12-07",
      "question": "'What an unlucky surfer has just experienced in this song'",
      "value": "$400",
      "answer": "a wipeout",
      "round": "Jeopardy!",
      "show_number": "65"
    },
    {
      "category": "THE AGE OF THE AQUARIUS",
      "air_date": "2010-02-10",
      "question": "'Send diamonds to this founder of a jewelry retailer--he'll be 198'",
      "value": "$1200",
      "answer": "Charles Louis Tiffany",
      "round": "Double Jeopardy!",
      "show_number": "5853"
    },
    {
      "category": "40 YEARS OF BARBIE",
      "air_date": "1999-07-09",
      "question": "'In celebration of Barbie's 40th anniversary, this \"costumer to the stars\" designed the doll seen here(\"Papillon Barbie\")'",
      "value": "$400",
      "answer": "Bob Mackie",
      "round": "Jeopardy!",
      "show_number": "3435"
    },
    {
      "category": "THE WIZARD",
      "air_date": "2010-03-11",
      "question": "'Nicol Williamson played Merlin in this magical 1981 film'",
      "value": "$1000",
      "answer": "Excalibur",
      "round": "Jeopardy!",
      "show_number": "5874"
    },
    {
      "category": "COOKIN' UP CATFISH",
      "air_date": "2007-06-29",
      "question": "'(Cheryl of the Clue Crew delivers the clue as she makes catfish at the Taylor Grocery in Mississippi.) One key ingredient in a good catfish fry coating is this sauce, developed in India but named for the English city where it was first bottled'",
      "value": "$600",
      "answer": "Worcesterchire",
      "round": "Jeopardy!",
      "show_number": "5265"
    },
    {
      "category": "PROSPERO",
      "air_date": "1999-01-18",
      "question": "'Prospero is the hero of the play \"The Tempest\", possibly the last by this playwright'",
      "value": "$200",
      "answer": "William Shakespeare",
      "round": "Double Jeopardy!",
      "show_number": "3311"
    },
    {
      "category": "THE 50 STATES",
      "air_date": "1988-11-11",
      "question": "'This state's capital lies on Cook Inlet, west of the Chugach Mountains'",
      "value": "$800",
      "answer": "Alaska",
      "round": "Double Jeopardy!",
      "show_number": "965"
    },
    {
      "category": "DURING DiMAGGIO'S HITTING STREAK",
      "air_date": "2001-10-10",
      "question": "'British & free French forces took Syria from this collaborationist French government'",
      "value": "$400",
      "answer": "Vichy",
      "round": "Jeopardy!",
      "show_number": "3933"
    },
    {
      "category": "SAVE THE PRINCE OF WALES",
      "air_date": "1999-07-08",
      "question": "'Charles honeymooned on this royal yacht that no longer rules the waves; it's been retired'",
      "value": "$1,500",
      "answer": "Britannia",
      "round": "Double Jeopardy!",
      "show_number": "3434"
    },
    {
      "category": "CIVIL WAR PEOPLE",
      "air_date": "2001-04-24",
      "question": "'Kate Clarke, mistress of this outlaw guerrilla leader, opened a brothel in St. Louis with the money he left her'",
      "value": "$800",
      "answer": "William Quantrill",
      "round": "Double Jeopardy!",
      "show_number": "3842"
    },
    {
      "category": "DESCRIBING THE NOVEL",
      "air_date": "2010-01-06",
      "question": "'Lockwood tells the tale, Yorkshire putting, Heathcliff is one wild cat'",
      "value": "$800",
      "answer": "Wuthering Heights",
      "round": "Jeopardy!",
      "show_number": "5828"
    },
    {
      "category": "ISLANDS",
      "air_date": "2004-09-17",
      "question": "'Named by Abel Tasman, Grotte Eylandt is the biggest island in this country's Gulf of Carpentaria'",
      "value": "$400",
      "answer": "Australia",
      "round": "Jeopardy!",
      "show_number": "4605"
    },
    {
      "category": "19th CENTURY BUSINESSMEN",
      "air_date": "2010-04-19",
      "question": "'By the time this Cleveland businessman retired in 1896, his company owned 3/4 of the USA's oil business'",
      "value": "$400",
      "answer": "(John D.) Rockefeller",
      "round": "Jeopardy!",
      "show_number": "5901"
    },
    {
      "category": "SPEECH",
      "air_date": "2001-10-26",
      "question": "'Read my lips -- the consonants M & B are phonetically this type of sound'",
      "value": "$2,000",
      "answer": "labial",
      "round": "Double Jeopardy!",
      "show_number": "3945"
    },
    {
      "category": "WORDS THAT SHOULD RHYME",
      "air_date": "2010-05-12",
      "question": "'Someone held against his will & the cost to mail a letter'",
      "value": "$400",
      "answer": "hostage & postage",
      "round": "Double Jeopardy!",
      "show_number": "5918"
    },
    {
      "category": "CROPS",
      "air_date": "2008-10-29",
      "question": "'To the Chinese, the 5 sacred grains are rice, wheat, barley, millet & this bean'",
      "value": "$1000",
      "answer": "soy",
      "round": "Jeopardy!",
      "show_number": "5553"
    },
    {
      "category": "TECHNOLOGY",
      "air_date": "2000-04-03",
      "question": "'In 1933 Marconi set up one of the first microwave radio systems, between Castel Gandolfo & this sovereign state'",
      "value": None,
      "answer": "Vatican City",
      "round": "Final Jeopardy!",
      "show_number": "3596"
    },
    {
      "category": "THE \"IGHT\" STUFF",
      "air_date": "2003-01-14",
      "question": "'Proverbially speaking, things \"out of\" this are \"out of mind\"'",
      "value": "$200",
      "answer": "sight",
      "round": "Jeopardy!",
      "show_number": "4232"
    },
    {
      "category": "ANTS",
      "air_date": "2005-07-06",
      "question": "'These insects also known as plant lice are captured & \"milked\" by many ants for the honeydew liquid they produce'",
      "value": "$5",
      "answer": "aphids",
      "round": "Double Jeopardy!",
      "show_number": "4813"
    },
    {
      "category": "2-LETTER TERMS",
      "air_date": "2000-03-20",
      "question": "'From Latin for \"thing\", it means \"with reference to\"'",
      "value": "$600",
      "answer": "re",
      "round": "Double Jeopardy!",
      "show_number": "3586"
    },
    {
      "category": "FRUITS & VEGETABLES",
      "air_date": "2009-01-13",
      "question": "'This shortcake staple is rich in Vitamin C, with about 90 milligrams per serving'",
      "value": "$800",
      "answer": "strawberries",
      "round": "Double Jeopardy!",
      "show_number": "5607"
    },
    {
      "category": "POETRY",
      "air_date": "1988-11-08",
      "question": "'In \"Ode on a Grecian Urn\" he asked, \"What men or gods are these?\"'",
      "value": "$800",
      "answer": "John Keats",
      "round": "Double Jeopardy!",
      "show_number": "962"
    },
    {
      "category": "NATURE",
      "air_date": "1994-05-23",
      "question": "'In 1845 the fungus disease phytophthora infestans rotted these vegetables all over Europe'",
      "value": "$100",
      "answer": "potatoes",
      "round": "Jeopardy!",
      "show_number": "2251"
    },
    {
      "category": "LEGAL LINGO",
      "air_date": "1999-02-18",
      "question": "'Acts that lower the dignity of the trial may bring a fine or a jail sentence if you're held in this'",
      "value": "$800",
      "answer": "Contempt of court",
      "round": "Double Jeopardy!",
      "show_number": "3334"
    },
    {
      "category": "K.K.",
      "air_date": "2005-05-18",
      "question": "'He was the majority stockholder in MGM until it was sold to Sony in 2005'",
      "value": "$800",
      "answer": "Kirk Kerkorian",
      "round": "Double Jeopardy!",
      "show_number": "4778"
    },
    {
      "category": "TRANSPORTATION",
      "air_date": "2004-12-27",
      "question": "'The name of this New York-Boston train combines \"acceleration\" & \"excellence\"'",
      "value": "$600",
      "answer": "the Acela",
      "round": "Jeopardy!",
      "show_number": "4676"
    },
    {
      "category": "PLANES, TRAINS & AUTOMOBILES",
      "air_date": "2005-03-11",
      "question": "'Count Andrenyi, Mrs. Hubbard & Col. Arbuthnot are among the suspects in this 1934 train-set novel'",
      "value": "$400",
      "answer": "Murder on the Orient Express",
      "round": "Double Jeopardy!",
      "show_number": "4730"
    },
    {
      "category": "RAIDERS",
      "air_date": "2008-12-24",
      "question": "'On raids, Ness' Untouchables welcomed members of this profession, even those from the Tribune'",
      "value": "$400",
      "answer": "the press (reporters accepted)",
      "round": "Double Jeopardy!",
      "show_number": "5593"
    },
    {
      "category": "COMMON BONDS",
      "air_date": "1989-11-06",
      "question": "'Helen Frankenthaler, Robert Rauschenberg & Roy Lichtenstein'",
      "value": "$400",
      "answer": "Artists",
      "round": "Jeopardy!",
      "show_number": "1191"
    },
    {
      "category": "VWLLSS NTNS",
      "air_date": "2010-10-12",
      "question": "'In the North Atlantic:  CLND'",
      "value": "$400",
      "answer": "Iceland",
      "round": "Jeopardy!",
      "show_number": "5997"
    },
    {
      "category": "IT'S ALL IN YOUR HEAD",
      "air_date": "2004-01-26",
      "question": "'It's the scientific name for the lower jaw'",
      "value": "$600",
      "answer": "mandible",
      "round": "Jeopardy!",
      "show_number": "4466"
    },
    {
      "category": "1987 OBITS",
      "air_date": "2005-11-28",
      "question": "'In February, a heart attack following gallbladder surgery claimed the life of this pop artist'",
      "value": "$400",
      "answer": "Andy Warhol",
      "round": "Jeopardy!",
      "show_number": "4881"
    },
    {
      "category": "EDUCATION",
      "air_date": "1991-07-19",
      "question": "'Founded in 1847, the Quincy Grammar School in this state was the USA's 1st graded elem. school'",
      "value": "$200",
      "answer": "Massachusetts",
      "round": "Double Jeopardy!",
      "show_number": "1605"
    },
    {
      "category": "CHOOSE YOUR WEAPON",
      "air_date": "2003-02-06",
      "question": "'The Gatling gun was the first practical one of these guns that fire a rapid, continuous stream of bullets'",
      "value": "$400",
      "answer": "machine gun",
      "round": "Jeopardy!",
      "show_number": "4249"
    },
    {
      "category": "TALES OF BRAVE ULYSSES",
      "air_date": "2004-11-05",
      "question": "'Ulysses devised this trick to induce the soldiers of Troy to open the city gates'",
      "value": "$400",
      "answer": "the Trojan horse",
      "round": "Jeopardy!",
      "show_number": "4639"
    },
    {
      "category": "KIDDY LIT",
      "air_date": "2004-06-24",
      "question": "'In the story by Alice Rice, it's where \"Mrs. Wiggs\" is \"of\"'",
      "value": "$1000",
      "answer": "the Cabbage Patch",
      "round": "Jeopardy!",
      "show_number": "4574"
    },
    {
      "category": "MATH, TEACHERS!",
      "air_date": "2011-05-03",
      "question": "'It's the greatest common factor of 18 & 24'",
      "value": "$800",
      "answer": "6",
      "round": "Double Jeopardy!",
      "show_number": "6142"
    },
    {
      "category": "PRESIDENTIAL MOMS",
      "air_date": "2001-05-17",
      "question": "'Sara Delano'",
      "value": "$400",
      "answer": "Franklin Delano Roosevelt",
      "round": "Double Jeopardy!",
      "show_number": "3859"
    },
    {
      "category": "FACES OF AMERICA",
      "air_date": "2006-10-10",
      "question": "'He instituted the ultimate top ten list as a part of his job'",
      "value": "$400",
      "answer": "J. Edgar Hoover",
      "round": "Jeopardy!",
      "show_number": "5077"
    },
    {
      "category": "AFRICAN CREATURES",
      "air_date": "2000-02-22",
      "question": "'Species of these in Africa include the puff adder & the gaboon viper'",
      "value": "$200",
      "answer": "Snakes",
      "round": "Jeopardy!",
      "show_number": "3567"
    },
    {
      "category": "DISNEY MOVIE TAGLINES",
      "air_date": "2006-09-15",
      "question": "'\"Awaken to a world of wonders\"'",
      "value": "$1000",
      "answer": "Sleeping Beauty",
      "round": "Jeopardy!",
      "show_number": "5060"
    },
    {
      "category": "POTPOURRI AROUND THE WORLD",
      "air_date": "2008-05-22",
      "question": "'Many Indian foods are accompanied by these popular relishes of spices & fruits often made from mangoes'",
      "value": "$1600",
      "answer": "chutneys",
      "round": "Double Jeopardy!",
      "show_number": "5469"
    },
    {
      "category": "\"N\"ATIONS OF THE WORLD",
      "air_date": "1998-06-15",
      "question": "'On the first Monday in June, this Kiwi country celebrates the Queen's birthday, the queen being Elizabeth'",
      "value": "$200",
      "answer": "New Zealand",
      "round": "Jeopardy!",
      "show_number": "3191"
    },
    {
      "category": "10-LETTER WORDS",
      "air_date": "2000-11-16",
      "question": "'From the Latin for \"growing up\", it's another term for a teen'",
      "value": "$500",
      "answer": "Adolescent",
      "round": "Jeopardy!",
      "show_number": "3729"
    },
    {
      "category": "NEPALESE HISTORY",
      "air_date": "2004-12-03",
      "question": "'Promulgated in 1990, the Nepali constitution is the only one in the world that makes this the state religion'",
      "value": "$600",
      "answer": "Hinduism",
      "round": "Jeopardy!",
      "show_number": "4660"
    },
    {
      "category": "HISTORICAL LAW & ORDER PLEAS",
      "air_date": "2007-02-23",
      "question": "'(Sam Waterston reads the clue.)  After the murder, you shouted \"Sic semper tyrannis!\"... Ballistics says it's your derringer, we've got Surratt--it's over'",
      "value": "$1200",
      "answer": "John Wilkes Booth",
      "round": "Double Jeopardy!",
      "show_number": "5175"
    },
    {
      "category": "\"X\" \"Q\"s ME",
      "air_date": "2010-05-20",
      "question": "'The name of this case used to carry your arrows might make you tremble'",
      "value": "$600",
      "answer": "a quiver",
      "round": "Jeopardy!",
      "show_number": "5924"
    },
    {
      "category": "5-LETTER WORDS",
      "air_date": "2007-12-17",
      "question": "'A type of star, sequoia or slalom'",
      "value": "$800",
      "answer": "giant",
      "round": "Double Jeopardy!",
      "show_number": "5356"
    },
    {
      "category": "THE WHITE HOUSE",
      "air_date": "2009-12-24",
      "question": "'The walls of the White House are this \"stone\", a type of sedimentary rock, that has been painted over'",
      "value": "$800",
      "answer": "sandstone",
      "round": "Double Jeopardy!",
      "show_number": "5819"
    },
    {
      "category": "PINEAPPLES",
      "air_date": "2011-05-27",
      "question": "'(Sarah of the Clue Crew reports from a pineapple plantation.Pineapple cultivation needs relatively little irrigation; with its reservoir formed in the leaves, the plant is a natural xerophyte--from the Greek \"xeros\", meaning this'",
      "value": "$800",
      "answer": "dry",
      "round": "Double Jeopardy!",
      "show_number": "6160"
    },
    {
      "category": "FASTER",
      "air_date": "2009-04-24",
      "question": "'Driving the Thrust SSC, Andy Green broke the land-speed record going 763 mph at Black Rock Desert in this state'",
      "value": "$400",
      "answer": "Nevada",
      "round": "Jeopardy!",
      "show_number": "5680"
    },
    {
      "category": "TECHNO LUST",
      "air_date": "2009-03-12",
      "question": "'This company has gone abbrev. happy with an HD XL DVR that records up to 150 hours of HDTV with THX'",
      "value": "$200",
      "answer": "TiVo",
      "round": "Jeopardy!",
      "show_number": "5649"
    },
    {
      "category": "THE ANIMAL KINGDOM",
      "air_date": "2000-05-30",
      "question": "'The USA's largest rodent, it has a flat tail that acts as a rudder in water'",
      "value": "$100",
      "answer": "Beaver",
      "round": "Jeopardy!",
      "show_number": "3637"
    },
    {
      "category": "GREAT MOMENTS IN TRAVEL",
      "air_date": "2004-07-19",
      "question": "'Johannes Badrutt, a St. Moritz hotel keeper, first convinced summer guests you could visit this country in winter, too'",
      "value": "$400",
      "answer": "Switzerland",
      "round": "Double Jeopardy!",
      "show_number": "4591"
    },
    {
      "category": "FACTS & FIGURES",
      "air_date": "2007-05-11",
      "question": "'Nothing to boast about, but the state with the most hazardous wast sites, more than 115, is this \"Garden State\"'",
      "value": "$800",
      "answer": "New Jersey",
      "round": "Double Jeopardy!",
      "show_number": "5230"
    },
    {
      "category": "MUSIC APPRECIATION",
      "air_date": "2001-05-16",
      "question": "'Of the 3 main voice classifications for male singers, this one is the highest'",
      "value": "$100",
      "answer": "Tenor",
      "round": "Jeopardy!",
      "show_number": "3858"
    },
    {
      "category": "CELEBS",
      "air_date": "2000-07-14",
      "question": "'This \"Men In Black\" star earned his \"Prince\" nickname in school due to his \"charming\" manner'",
      "value": "$100",
      "answer": "Will Smith",
      "round": "Jeopardy!",
      "show_number": "3670"
    },
    {
      "category": "BUSINESS",
      "air_date": "2007-06-14",
      "question": "'Future Michigan governor George Romney headed this merger-created car company from 1954 to 1962'",
      "value": "$800",
      "answer": "American Motors",
      "round": "Jeopardy!",
      "show_number": "5254"
    },
    {
      "category": "MEET YOU IN THE MIDDLE",
      "air_date": "2008-12-17",
      "question": "'No-wincomedy'",
      "value": "$600",
      "answer": "situation",
      "round": "Jeopardy!",
      "show_number": "5588"
    },
    {
      "category": "BUSINESS & INDUSTRY",
      "air_date": "2001-02-16",
      "question": "'This brokerage house uses the logo seen here'",
      "value": "$400",
      "answer": "Merrill Lynch",
      "round": "Jeopardy!",
      "show_number": "3795"
    },
    {
      "category": "THE LIVING EARTH",
      "air_date": "1997-05-07",
      "question": "'The only poisonous snake in Great Britain, the common adder belongs to this snake family'",
      "value": "$400",
      "answer": "Viper",
      "round": "Jeopardy!",
      "show_number": "2933"
    },
    {
      "category": "CREATURES OF NATURE",
      "air_date": "2010-07-20",
      "question": "'The peregrine type of this bird can reach speeds of 200 mph in a dive'",
      "value": "$400",
      "answer": "a falcon",
      "round": "Jeopardy!",
      "show_number": "5967"
    },
    {
      "category": "HISTORY OF THE WORLD PART 3",
      "air_date": "2000-12-04",
      "question": "'In 1598 Henry IV granted French Protestants religious freedom by issuing this edict'",
      "value": "$1000",
      "answer": "Edict of Nantes",
      "round": "Double Jeopardy!",
      "show_number": "3741"
    },
    {
      "category": "NAME THE OLYMPIC CITY",
      "air_date": "2002-09-24",
      "question": "'1984 winter games(a war zone in the 1990s)'",
      "value": "$1200",
      "answer": "Sarajevo",
      "round": "Double Jeopardy!",
      "show_number": "4152"
    },
    {
      "category": "EUROPE",
      "air_date": "2001-06-07",
      "question": "'We have the White House; this country's P.M. has the Chigi Palace or Palazzo Chigi'",
      "value": "$200",
      "answer": "Italy",
      "round": "Double Jeopardy!",
      "show_number": "3874"
    },
    {
      "category": "YANKEE MAGAZINE",
      "air_date": "2010-09-17",
      "question": "'A 1983 article on this yankee-style soup says long ago it was made with salt pork, not clams'",
      "value": "$400",
      "answer": "chowder",
      "round": "Double Jeopardy!",
      "show_number": "5980"
    },
    {
      "category": "A LITTLE \"R\" & \"R\"",
      "air_date": "2002-12-16",
      "question": "'This powerful African hound was originally bred to hunt lions'",
      "value": "$2000",
      "answer": "Rhodesian Ridgeback",
      "round": "Double Jeopardy!",
      "show_number": "4211"
    },
    {
      "category": "HAIR",
      "air_date": "2007-01-05",
      "question": "'In the 1974 picture seen here, Julius Erving sports this 4-letter hairstyle'",
      "value": "$1200",
      "answer": "an afro",
      "round": "Double Jeopardy!",
      "show_number": "5140"
    },
    {
      "category": "A MAGNUM OF CHAMPAGNE",
      "air_date": "1997-12-31",
      "question": "'Lerner & Loewe wrote \"The Night They Invented Champagne\" for this movie musical set in Gay Paree'",
      "value": "$200",
      "answer": "Gigi",
      "round": "Jeopardy!",
      "show_number": "3073"
    },
    {
      "category": "WHO CARRIED THE STATE?",
      "air_date": "2010-05-20",
      "question": "'Florida,2000'",
      "value": "$200",
      "answer": "George W. Bush",
      "round": "Jeopardy!",
      "show_number": "5924"
    },
    {
      "category": "COUNTRY SINGERS",
      "air_date": "1997-03-10",
      "question": "'Randy Traywick is the real name of this man who was a singer & a short order cook at the Nashville Palace'",
      "value": "$200",
      "answer": "Randy Travis",
      "round": "Jeopardy!",
      "show_number": "2891"
    },
    {
      "category": "HAIRSTYLES",
      "air_date": "1993-11-29",
      "question": "'A wedge-cut of the late '70s was named for this female skater, who popularized it at the Olympics'",
      "value": "$400",
      "answer": "Dorothy Hamill",
      "round": "Double Jeopardy!",
      "show_number": "2126"
    },
    {
      "category": "HISTORY",
      "air_date": "1990-11-16",
      "question": "'Called greatest Catholic missionary of modern times, he introduced Christianity into Japan in 1549'",
      "value": "$1000",
      "answer": "Francis Xavier",
      "round": "Double Jeopardy!",
      "show_number": "1430"
    },
    {
      "category": "A NOUN IS A PERSON, PLACE OR THING",
      "air_date": "2004-12-24",
      "question": "'Thing:Tolkien's evil version of a goblin'",
      "value": "$800",
      "answer": "an orc",
      "round": "Jeopardy!",
      "show_number": "4675"
    },
    {
      "category": "EPHEN STEPHEN",
      "air_date": "2004-02-25",
      "question": "'He was such a great poet that his unfinished \"Western Star\" won him a Pulitzer (his second) in 1944'",
      "value": "$2,000",
      "answer": "Stephen Vincent Benet",
      "round": "Double Jeopardy!",
      "show_number": "4488"
    },
    {
      "category": "FOREIGN FILM DIRECTORS",
      "air_date": "1996-12-11",
      "question": "'Shinobu Hashimoto co-wrote the scripts for his \"Rashomon\" & \"Seven Samurai\"'",
      "value": "$800",
      "answer": "Akira Kurosawa",
      "round": "Double Jeopardy!",
      "show_number": "2828"
    },
    {
      "category": "\"BIO\" SCIENCE",
      "air_date": "2006-09-13",
      "question": "'2 men at the U. of Washington's Department of this won the 1992 Nobel Prize for studying cell protein regulation'",
      "value": "$800",
      "answer": "biochemistry",
      "round": "Double Jeopardy!",
      "show_number": "5058"
    },
    {
      "category": "THIS MEANS WAR!",
      "air_date": "2000-10-16",
      "question": "'The USA's began in 1861, Angola's in 1975'",
      "value": "$100",
      "answer": "Civil War",
      "round": "Jeopardy!",
      "show_number": "3706"
    },
    {
      "category": "AMERICAN HISTORY",
      "air_date": "2002-09-17",
      "question": "'In 1901 the Senate ratified the Hay-Pauncefote Treaty, allowing the U.S. to build this in Central America'",
      "value": "$1200",
      "answer": "the Panama Canal",
      "round": "Double Jeopardy!",
      "show_number": "4147"
    },
    {
      "category": "BEFORE & AFTER",
      "air_date": "2004-01-19",
      "question": "'\"Culture Club\" lead singer who was \"The Father of His Country\"'",
      "value": "$400",
      "answer": "Boy George Washington",
      "round": "Double Jeopardy!",
      "show_number": "4461"
    },
    {
      "category": "UNAUTHORIZED BIOGRAPHIES",
      "air_date": "2000-12-20",
      "question": "'An unauthorized bio of Mark Wahlberg is titled \"Don't Call Me\" this'",
      "value": "$400",
      "answer": "Marky Mark",
      "round": "Jeopardy!",
      "show_number": "3753"
    },
    {
      "category": "ALSO A CANTERBURY TALES PILGRIM",
      "air_date": "2009-05-21",
      "question": "'It's what Bill Clinton could be called based on what he did for financier Marc Rich in 2001'",
      "value": "$1000",
      "answer": "pardoner",
      "round": "Jeopardy!",
      "show_number": "5699"
    },
    {
      "category": "SPOT THE POOCH",
      "air_date": "2007-02-01",
      "question": "'The choo choo,the chow chow'",
      "value": "$200",
      "answer": "the chow chow",
      "round": "Jeopardy!",
      "show_number": "5159"
    },
    {
      "category": "JANUARY 24",
      "air_date": "2000-01-24",
      "question": "'On Jan. 24, 1972 WWII soldier Shoichi Yokoi was found in the jungle of this island, a U.S. territory'",
      "value": "$1,000",
      "answer": "Guam",
      "round": "Double Jeopardy!",
      "show_number": "3546"
    },
    {
      "category": "CREAM",
      "air_date": "2004-11-05",
      "question": "'Captain Parker's in Yarmouth is a 2-time winner of Boston Harborfest's competition in this creamy soup'",
      "value": "$600",
      "answer": "clam chowder",
      "round": "Jeopardy!",
      "show_number": "4639"
    },
    {
      "category": "ATTACK OF THE THESAURUS",
      "air_date": "2002-09-16",
      "question": "'In kiddy lit Jack didn't kill the titan or the colossus, he killed this'",
      "value": "$800",
      "answer": "the giant",
      "round": "Double Jeopardy!",
      "show_number": "4146"
    },
    {
      "category": "CLASSICAL CLASSICS",
      "air_date": "2005-07-01",
      "question": "'This snoozer is listed as the composer's Opus 49, No. 4'",
      "value": "$600",
      "answer": "\"Brahms\\' Lullaby\"",
      "round": "Jeopardy!",
      "show_number": "4810"
    },
    {
      "category": "CROSSWORD CLUES \"F\"",
      "air_date": "2001-11-23",
      "question": "'British bad \"Guy\"(6)'",
      "value": "$1000",
      "answer": "Fawkes",
      "round": "Double Jeopardy!",
      "show_number": "3965"
    },
    {
      "category": "A DATE WITH HISTORY",
      "air_date": "2006-01-26",
      "question": "'On March 9, 1820 his daughter Maria became the first president's daughter married in the White House'",
      "value": "$1000",
      "answer": "James Monroe",
      "round": "Jeopardy!",
      "show_number": "4924"
    },
    {
      "category": "PITCHERS",
      "air_date": "1998-12-31",
      "question": "'This pitcher named for a U.S. president was played by Ronald Reagan in \"The Winning Team\"'",
      "value": "$1000",
      "answer": "Grover Cleveland Alexander",
      "round": "Double Jeopardy!",
      "show_number": "3299"
    },
    {
      "category": "SNOW WHITE'S FORGOTTEN DWARFS",
      "air_date": "1999-11-08",
      "question": "'Inferences made by this peachy-skinned dwarf are known as the same type of \"logic\"'",
      "value": "$400",
      "answer": "Fuzzy",
      "round": "Jeopardy!",
      "show_number": "3491"
    },
    {
      "category": "I'M HUNGARIAN",
      "air_date": "2006-09-18",
      "question": "'I'm a Hungarian actor & I was buried in the cape that I wore in one of my most memorable roles'",
      "value": "$800",
      "answer": "Bela Lugosi",
      "round": "Double Jeopardy!",
      "show_number": "5061"
    },
    {
      "category": "MEXICO",
      "air_date": "2004-06-23",
      "question": "'(Sarah of the Clue Crew sets down to  with four friends in the Yucatan Peninsula, Mexico.) In Mexico, you can enjoy the music of this type of band whose name may come from the word \"marriage\"'",
      "value": "$400",
      "answer": "mariachi",
      "round": "Double Jeopardy!",
      "show_number": "4573"
    },
    {
      "category": "LANDSCAPE CRUSADER",
      "air_date": "2006-04-19",
      "question": "'Shown here is her 1936 desert landscape entitled \"Summer Days\"'",
      "value": "$200",
      "answer": "(Georgia) O\\'Keeffe",
      "round": "Jeopardy!",
      "show_number": "4983"
    },
    {
      "category": "NURSERY RHYMES",
      "air_date": "1985-10-02",
      "question": "'Product reserved in bags for the master, the dame, & the little boy'",
      "value": "$500",
      "answer": "wool",
      "round": "Jeopardy!",
      "show_number": "278"
    },
    {
      "category": "WE GET LETTERS",
      "air_date": "2010-10-06",
      "question": "'On a treasure map, it \"marks the spot\"'",
      "value": "$200",
      "answer": "X",
      "round": "Jeopardy!",
      "show_number": "5993"
    },
    {
      "category": "HISTORIC VIRGINIA",
      "air_date": "2008-07-14",
      "question": "'Archaeologists visit Hopewell to dig at Kippax, once the home of Jane Rolfe Bolling, this historic woman's granddaughter'",
      "value": "$8,200",
      "answer": "Pocahontas",
      "round": "Double Jeopardy!",
      "show_number": "5506"
    },
    {
      "category": "POTENT POTABLES, SOUTHERN STYLE",
      "air_date": "2009-06-30",
      "question": "'A liqueur of this flavor (Kahlua, perhaps) gives that pretty muddy color to a Mississippi mud cocktail'",
      "value": "$800",
      "answer": "coffee",
      "round": "Jeopardy!",
      "show_number": "5727"
    },
    {
      "category": "THE MOVIES",
      "air_date": "1998-12-08",
      "question": "'Animators Bill Hanna & Joe Barbera had bit roles in this 1994 John Goodman film'",
      "value": "$200",
      "answer": "The Flintstones",
      "round": "Double Jeopardy!",
      "show_number": "3282"
    },
    {
      "category": "TV SERIES EPISODES",
      "air_date": "2003-03-28",
      "question": "'\"Musings of a Cigarette-Smoking Man\"'",
      "value": "$1000",
      "answer": "The X-Files",
      "round": "Jeopardy!",
      "show_number": "4285"
    },
    {
      "category": "CURRENT GOVERNORS",
      "air_date": "2001-01-23",
      "question": "'Tommy Thompson'",
      "value": "$800",
      "answer": "Wisconsin",
      "round": "Double Jeopardy!",
      "show_number": "3777"
    },
    {
      "category": "BEANS",
      "air_date": "1998-11-09",
      "question": "'It's the enumerative slang for an accountant or other financial exec'",
      "value": "$200",
      "answer": "beancounter",
      "round": "Jeopardy!",
      "show_number": "3261"
    },
    {
      "category": "AS \"IF\"!",
      "air_date": "2009-06-25",
      "question": "'To make a god of'",
      "value": "$800",
      "answer": "deify",
      "round": "Jeopardy!",
      "show_number": "5724"
    },
    {
      "category": "GUNS N' ROSES",
      "air_date": "2005-02-15",
      "question": "'He invented an electrically controlled naval mine as well as the 6-shooter'",
      "value": "$600",
      "answer": "(Samuel) Colt",
      "round": "Jeopardy!",
      "show_number": "4712"
    },
    {
      "category": "\"R-U\" SERIOUS?",
      "air_date": "2001-01-11",
      "question": "'Former president Gerald Ford's middle name'",
      "value": "$1000",
      "answer": "Rudolph",
      "round": "Double Jeopardy!",
      "show_number": "3769"
    },
    {
      "category": "SAY YOU WANT A REVOLUTION",
      "air_date": "2007-07-25",
      "question": "'It ended in 1917 with Nicholas II out on his czary...'",
      "value": "$400",
      "answer": "the Russian Revolution",
      "round": "Jeopardy!",
      "show_number": "5283"
    },
    {
      "category": "SONG LYRICS",
      "air_date": "2010-05-21",
      "question": "'Young Money (featuring Lloyd) just wants you to call him \"Mr.\" this \"I can make your bed rock\"'",
      "value": "$800",
      "answer": "Flintstone",
      "round": "Jeopardy!",
      "show_number": "5925"
    },
    {
      "category": "SIEGES",
      "air_date": "2006-12-04",
      "question": "'The book \"Besieged\" is subtitled \"...From Jericho to\" this city besieged by the Serbs in the 1990s'",
      "value": "$400",
      "answer": "Sarajevo",
      "round": "Double Jeopardy!",
      "show_number": "5116"
    },
    {
      "category": "A MINOR IN LITERATURE",
      "air_date": "2010-07-16",
      "question": "'In a classic story this little girl is sent to bring food & drink to her grandmother, but a wolf has gotten there first'",
      "value": "$200",
      "answer": "Little Red Riding Hood",
      "round": "Jeopardy!",
      "show_number": "5965"
    },
    {
      "category": "POETIC LICENSE",
      "air_date": "2007-11-12",
      "question": "'At university, this poetic lord developed a \"violent, though pure, love\" for young chorister John Edleston'",
      "value": "$600",
      "answer": "Byron",
      "round": "Jeopardy!",
      "show_number": "5331"
    },
    {
      "category": "AROUND THE DRUM KIT",
      "air_date": "2006-11-22",
      "question": "'(Sarah of the Clue Crew plays with cymbals.) The snowshoe, a cymbal set on the floor, moved up a bit and became the low boy, which moved up some more and became this'",
      "value": "$1200",
      "answer": "a high hat",
      "round": "Double Jeopardy!",
      "show_number": "5108"
    },
    {
      "category": "BEST ACTOR OSCAR WINNERS",
      "air_date": "2009-07-09",
      "question": "'1971:As \"Popeye\" Doyle'",
      "value": "$200",
      "answer": "Gene Hackman",
      "round": "Jeopardy!",
      "show_number": "5734"
    },
    {
      "category": "LITERARY EPITAPHS",
      "air_date": "1999-11-22",
      "question": "'Beloved father of Cordelia, less beloved father of Goneril & Regan'",
      "value": "$200",
      "answer": "King Lear",
      "round": "Double Jeopardy!",
      "show_number": "3501"
    },
    {
      "category": "SHE SELLS SEYCHELLES",
      "air_date": "2004-10-04",
      "question": "'Seychelles is an example of this grouping of a large number of islands on a vast sheet of sea'",
      "value": "$1600",
      "answer": "an archipelago",
      "round": "Double Jeopardy!",
      "show_number": "4616"
    },
    {
      "category": "ROCKET MAN",
      "air_date": "2006-04-11",
      "question": "'Apollo 8 astronauts Borman, Lovell & Anders were the first men to make this circuit & they made 10 of them'",
      "value": "$800",
      "answer": "a lunar orbit",
      "round": "Double Jeopardy!",
      "show_number": "4977"
    },
    {
      "category": "PRODUCTS",
      "air_date": "2009-01-23",
      "question": "'In 1909, 3 years before the blimps, Goodyear started making these for airplanes'",
      "value": "$200",
      "answer": "tires",
      "round": "Jeopardy!",
      "show_number": "5615"
    },
    {
      "category": "WORD\"Z\"",
      "air_date": "2008-03-10",
      "question": "'It's true! This city, the first colonial post in Mexico, was founded by Hernando Cortes in 1519'",
      "value": "$1600",
      "answer": "Veracruz",
      "round": "Double Jeopardy!",
      "show_number": "5416"
    },
    {
      "category": "LITERATURE",
      "air_date": "2008-06-30",
      "question": "'In Chaucer's \"The Canterbury Tales\" , this bawdy wife tells of her 5 husbands & her desire for a sixth'",
      "value": "$800",
      "answer": "the Wife of Bath",
      "round": "Jeopardy!",
      "show_number": "5496"
    },
    {
      "category": "STRANGE BUT TRUE",
      "air_date": "1998-06-24",
      "question": "'Some members of these Melanesian \"cults\" await consumer goods that will be sent by supernatural forces'",
      "value": "$400",
      "answer": "Cargo cults",
      "round": "Jeopardy!",
      "show_number": "3198"
    },
    {
      "category": "FAMOUS AMERICANS",
      "air_date": "2000-06-07",
      "question": "'Infamous 19th century actor seen here:'",
      "value": "$400",
      "answer": "John Wilkes Booth",
      "round": "Double Jeopardy!",
      "show_number": "3643"
    },
    {
      "category": "AH, SWEET MYTHTERY",
      "air_date": "2008-06-02",
      "question": "'The Myrmidons were this great hero's brutal cohorts in the Trojan War'",
      "value": "$800",
      "answer": "Achilles",
      "round": "Jeopardy!",
      "show_number": "5476"
    },
    {
      "category": "THAT'S JUST CLASSIC!",
      "air_date": "2005-06-06",
      "question": "'It's the classic passage of 19th century travelin' music heard here'",
      "value": "$800",
      "answer": "\"Ride of the Valkyrie\"",
      "round": "Double Jeopardy!",
      "show_number": "4791"
    },
    {
      "category": "STATE NICKNAMES",
      "air_date": "1998-02-16",
      "question": "'\"The Everglade State\"'",
      "value": "$100",
      "answer": "Florida",
      "round": "Jeopardy!",
      "show_number": "3106"
    },
    {
      "category": "TOE-KNEE",
      "air_date": "2003-01-30",
      "question": "'Inflammation of this tendon that pulls up the heel is common; rupture is a lot more serious'",
      "value": "$1200",
      "answer": "Achilles tendon",
      "round": "Double Jeopardy!",
      "show_number": "4244"
    },
    {
      "category": "SPORTS 2000",
      "air_date": "2000-09-15",
      "question": "'She dispatched sister Serena at Wimbledon & went on to defeat Lindsay Davenport for the title'",
      "value": "$400",
      "answer": "Venus Williams",
      "round": "Jeopardy!",
      "show_number": "3685"
    },
    {
      "category": "HISTORY ART",
      "air_date": "2002-12-20",
      "question": "'Delacroix, like Byron, sided with this people's fight to break free of Turkey, leading to his \"Massacre at Chios\"'",
      "value": "$1600",
      "answer": "Greeks",
      "round": "Double Jeopardy!",
      "show_number": "4215"
    },
    {
      "category": "BEFORE YOU WERE BORN",
      "air_date": "1997-04-30",
      "question": "'This made headlines when it crashed October 29, 1929; ask your broker, it's healthier now'",
      "value": "$600",
      "answer": "the Stock Market",
      "round": "Double Jeopardy!",
      "show_number": "2928"
    },
    {
      "category": "DOUBLE-LETTER GEOGRAPHY",
      "air_date": "2008-07-24",
      "question": "'This capital city was founded in 1840 on Lambton Harbour at the extreme south part of the North Island'",
      "value": "$400",
      "answer": "Wellington",
      "round": "Jeopardy!",
      "show_number": "5514"
    },
    {
      "category": "SPORTS",
      "air_date": "1997-03-06",
      "question": "'Fielding positions in this British game include wicketkeeper, square leg & gully'",
      "value": "$200",
      "answer": "Cricket",
      "round": "Jeopardy!",
      "show_number": "2889"
    },
    {
      "category": "FRUITS & VEGETABLES",
      "air_date": "1985-10-04",
      "question": "'Syrup originally made from pomegranates processed on the Caribbean island of Grenada'",
      "value": "$600",
      "answer": "grenadine",
      "round": "Double Jeopardy!",
      "show_number": "280"
    },
    {
      "category": "RONALD REAGAN",
      "air_date": "2006-09-18",
      "question": "'Presidential Chief of Staff Donald Regan was fired after hanging up on her'",
      "value": "$200",
      "answer": "Nancy Reagan",
      "round": "Jeopardy!",
      "show_number": "5061"
    },
    {
      "category": "PROHIBITION",
      "air_date": "1997-06-18",
      "question": "'Eliot Ness formed the \"Untouchables\" to rid this city of Al Capone'",
      "value": "$100",
      "answer": "Chicago",
      "round": "Jeopardy!",
      "show_number": "2963"
    },
    {
      "category": "PEOPLE WHO BECAME WORDS",
      "air_date": "1998-07-16",
      "question": "'Up on the highwire you might wear this bodysuit named for a famous 19th century trapeze artist'",
      "value": "$400",
      "answer": "Leotard",
      "round": "Double Jeopardy!",
      "show_number": "3214"
    },
    {
      "category": "DOGS",
      "air_date": "1994-11-16",
      "question": "'This gray hunting dog was formerly called a Weimar pointer'",
      "value": "$200",
      "answer": "Weimaraner",
      "round": "Double Jeopardy!",
      "show_number": "2348"
    },
    {
      "category": "MIDDLE NAMES",
      "air_date": "2006-03-28",
      "question": "'Founder of an oil company:Davison'",
      "value": "$400",
      "answer": "John D. Rockefeller",
      "round": "Jeopardy!",
      "show_number": "4967"
    },
    {
      "category": "VOCABULARY",
      "air_date": "2011-05-17",
      "question": "'A scarf for your neck, or a sound-deadener for your car'",
      "value": "$400",
      "answer": "a muffler",
      "round": "Double Jeopardy!",
      "show_number": "6152"
    },
    {
      "category": "MOVIE TAGLINES",
      "air_date": "1999-12-07",
      "question": "'1993:\"An adventure 65 million years in the making\"'",
      "value": "$600",
      "answer": "Jurassic Park",
      "round": "Double Jeopardy!",
      "show_number": "3512"
    },
    {
      "category": "POP MUSIC",
      "air_date": "1999-03-26",
      "question": "'Mark Knopfler & Neil Dorfsman produced this group's \"Money for Nothing\"'",
      "value": "$200",
      "answer": "Dire Straits",
      "round": "Double Jeopardy!",
      "show_number": "3360"
    },
    {
      "category": "COCKNEY RHYMING SLANG",
      "air_date": "1999-07-20",
      "question": "'A weasel and stoat is one of these, even if it isn't made from weasel or stoat'",
      "value": "$300",
      "answer": "Coat",
      "round": "Jeopardy!",
      "show_number": "3442"
    },
    {
      "category": "DON'T LOSE YOUR TRAIN OF THOUGHT",
      "air_date": "2004-02-27",
      "question": "'After touring the Coors Brewing Company, you may want to visit the Colorado Railroad Museum in this city'",
      "value": "$1000",
      "answer": "Golden",
      "round": "Jeopardy!",
      "show_number": "4490"
    },
    {
      "category": "IT'S \"ALL\"",
      "air_date": "2000-02-25",
      "question": "'November 1 on the Christian calendar'",
      "value": "$600",
      "answer": "All Saints Day",
      "round": "Double Jeopardy!",
      "show_number": "3570"
    },
    {
      "category": "NFL QBs OFF THE FIELD",
      "air_date": "2010-07-28",
      "question": "'In a mock \"United Way\" ad, this Colts QB berated kids on a football field & showed them how to break into a car'",
      "value": "$600",
      "answer": "Peyton Manning",
      "round": "Jeopardy!",
      "show_number": "5973"
    },
    {
      "category": "CATS",
      "air_date": "2004-05-19",
      "question": "'In the 1960s officials of the Ankara, Turkey zoo saved this pure breed from extinction'",
      "value": "$1000",
      "answer": "the Turkish Angora",
      "round": "Jeopardy!",
      "show_number": "4548"
    },
    {
      "category": "AN ENGLISH-SPORTS DICTIONARY",
      "air_date": "2006-05-15",
      "question": "'English: a newspaper story you saved;football: blocking below the waist from behind'",
      "value": "$400",
      "answer": "clipping",
      "round": "Jeopardy!",
      "show_number": "5001"
    },
    {
      "category": "WHAT'S NEXT?",
      "air_date": "2012-01-09",
      "question": "'Geologic time eras: Paleozoic, Mesozoic, this'",
      "value": "$2000",
      "answer": "Cenozoic",
      "round": "Double Jeopardy!",
      "show_number": "6286"
    },
    {
      "category": "WHO WANTS TO BE A LEGIONNAIRE?",
      "air_date": "2006-06-28",
      "question": "'Technically, it's the only country in the world that you can't be from to enlist in the French Foreign Legion'",
      "value": "$200",
      "answer": "France",
      "round": "Jeopardy!",
      "show_number": "5033"
    },
    {
      "category": "MUSICAL DUOS",
      "air_date": "1997-06-20",
      "question": "'In 1990 this \"Bridge Over Troubled Water\" duo was inducted into the Rock & Roll Hall of Fame'",
      "value": "$100",
      "answer": "Simon & Garfunkel",
      "round": "Jeopardy!",
      "show_number": "2965"
    },
    {
      "category": "CRAZY TOP 40 TUNES",
      "air_date": "2005-01-25",
      "question": "'\"But we're never gonna survive unless\" you name this artist who hit the Top 10 in 1991 with \"Crazy\"'",
      "value": "$1000",
      "answer": "Seal",
      "round": "Jeopardy!",
      "show_number": "4697"
    },
    {
      "category": "FICTION",
      "air_date": "2000-02-14",
      "question": "'Say a little prayer for this title character of a 1989 John Irving novel, who speaks in capital letters'",
      "value": "$400",
      "answer": "Owen Meany",
      "round": "Jeopardy!",
      "show_number": "3561"
    },
    {
      "category": "WHO'S WHO IN AMERICA",
      "air_date": "2006-06-16",
      "question": "'The Who's Who 60, an all-time list in the 60th Edition, incudes this \"aviator, b. Detroit, Feb. 4, 1902\"'",
      "value": "$400",
      "answer": "Charles Lindbergh",
      "round": "Double Jeopardy!",
      "show_number": "5025"
    },
    {
      "category": "SHAKESPEAREAN 1ST LINES",
      "air_date": "1986-11-04",
      "question": "'\"If music be the food of love, play on...\"'",
      "value": "$800",
      "answer": "Twelfth Night",
      "round": "Double Jeopardy!",
      "show_number": "497"
    },
    {
      "category": "OF ORDER",
      "air_date": "2011-03-09",
      "question": "'Animals, from slowest to fastest:peregrine falcon'",
      "value": "$400",
      "answer": "donkey, cheetah, peregrine falcon",
      "round": "Jeopardy!",
      "show_number": "6103"
    },
    {
      "category": "LITERARY LOCALES",
      "air_date": "1999-11-30",
      "question": "'1904:Never-Never-Land'",
      "value": "$200",
      "answer": "\"Peter Pan\"",
      "round": "Double Jeopardy!",
      "show_number": "3507"
    },
    {
      "category": "RHYME TIME",
      "air_date": "1997-05-19",
      "question": "'Amiable rodents'",
      "value": "$300",
      "answer": "Nice mice",
      "round": "Jeopardy!",
      "show_number": "2941"
    },
    {
      "category": "STARTS & ENDS WITH \"O\"",
      "air_date": "1997-07-04",
      "question": "'Shakespeare's moor'",
      "value": "$200",
      "answer": "Othello",
      "round": "Double Jeopardy!",
      "show_number": "2975"
    },
    {
      "category": "FIRST NOVELS",
      "air_date": "1998-01-12",
      "question": "'His first novel, \"Almayer's Folly\", is autobiographical, like \"Lord Jim\"'",
      "value": "$600",
      "answer": "Joseph Conrad",
      "round": "Double Jeopardy!",
      "show_number": "3081"
    },
    {
      "category": "SHORT STORIES",
      "air_date": "2000-04-12",
      "question": "'This mining camp's \"outcasts\" included a gambler, 2 prostitutes, a drunk & 2 young lovers'",
      "value": "$1000",
      "answer": "Poker Flat",
      "round": "Double Jeopardy!",
      "show_number": "3603"
    },
    {
      "category": "TV & FILM FOOD",
      "air_date": "2008-05-01",
      "question": "'The title character chugs raw eggs & punches slabs of beef in this 1976 Oscar winner'",
      "value": "$2000",
      "answer": "Rocky",
      "round": "Double Jeopardy!",
      "show_number": "5454"
    },
    {
      "category": "WHEN YOU WERE YOUNG",
      "air_date": "2008-09-19",
      "question": "'In 2000 Clinton became the first sitting president to visit this country since Nixon visited the troops in 1969'",
      "value": "$500",
      "answer": "Vietnam",
      "round": "Jeopardy!",
      "show_number": "5525"
    },
    {
      "category": "WHAT A SCOOP!",
      "air_date": "2007-11-29",
      "question": "'This treat of ice cream, syrups & other toppings was probably named for a day of the week'",
      "value": "$400",
      "answer": "a sundae",
      "round": "Double Jeopardy!",
      "show_number": "5344"
    },
    {
      "category": "YOU DO THE MATH!",
      "air_date": "2009-07-14",
      "question": "'Half a dozen centuries divided by 10 gives you this many years'",
      "value": "$400",
      "answer": "60",
      "round": "Double Jeopardy!",
      "show_number": "5737"
    },
    {
      "category": "WORLD LITERATURE",
      "air_date": "2001-06-04",
      "question": "'It consists of a story-telling contest to pass the time on a trip to the shrine of St. Thomas A Becket'",
      "value": "$200",
      "answer": "The Canterbury Tales",
      "round": "Double Jeopardy!",
      "show_number": "3871"
    },
    {
      "category": "POTENTATE POTABLES",
      "air_date": "2004-10-27",
      "question": "'The widget in this beer won a Queen's Award for technological advancement in 1991; stout work!'",
      "value": "$800",
      "answer": "Guinness",
      "round": "Double Jeopardy!",
      "show_number": "4633"
    },
    {
      "category": "ACTRESSES",
      "air_date": "2003-04-17",
      "question": "'She's mom to Kate Hudson'",
      "value": "$400",
      "answer": "Goldie Hawn",
      "round": "Double Jeopardy!",
      "show_number": "4299"
    },
    {
      "category": "\"M\"USIC",
      "air_date": "2002-10-14",
      "question": "'Last name of Louise & her sister Barbara, who \"was country when country wasn't cool\"'",
      "value": "$1200",
      "answer": "Mandrell",
      "round": "Double Jeopardy!",
      "show_number": "4166"
    },
    {
      "category": "ZODIAC SYMBOLS",
      "air_date": "2000-05-08",
      "question": "'This bovine is Zeus in disguise, which makes it Zeus in da skies'",
      "value": "$400",
      "answer": "Taurus",
      "round": "Double Jeopardy!",
      "show_number": "3621"
    },
    {
      "category": "THE \"ALP\"s",
      "air_date": "2008-04-25",
      "question": "'He has had 19 Top 40 hits as a soloist & with his band The Tijuana Brass'",
      "value": "$1200",
      "answer": "Herb Alpert",
      "round": "Double Jeopardy!",
      "show_number": "5450"
    },
    {
      "category": "CHARACTER IN JAMES FENIMORE COOPER",
      "air_date": "2011-11-23",
      "question": "'First & last name of the scout who's Cooper's most famous creation'",
      "value": "$400",
      "answer": "Natty Bumppo",
      "round": "Double Jeopardy!",
      "show_number": "6253"
    },
    {
      "category": "HELLO, DOLLY!",
      "air_date": "2002-12-13",
      "question": "'Arcola, Illinois, the birthplace of Johnny Gruelle, has a museum devoted to this rag doll duo he created'",
      "value": "$600",
      "answer": "Raggedy Ann & Andy",
      "round": "Jeopardy!",
      "show_number": "4210"
    },
    {
      "category": "NATIONAL HISTORIC LANDMARKS",
      "air_date": "2000-05-18",
      "question": "'You can stand with feet of clay, Henry Clay, at the reconstructed home where he lived from 1811 to 1852 in this state'",
      "value": "$800",
      "answer": "Kentucky",
      "round": "Double Jeopardy!",
      "show_number": "3629"
    },
    {
      "category": "COMPUTER PROGRAMS",
      "air_date": "2004-07-19",
      "question": "'Filemaker Pro is used for this type of application that stores & organizes information (like \"Jeopardy!\" clues)'",
      "value": "$800",
      "answer": "database",
      "round": "Double Jeopardy!",
      "show_number": "4591"
    },
    {
      "category": "\"DON'T\" YOU KNOW THIS SONG?",
      "air_date": "2006-04-21",
      "question": "'If you've given up, stop! & tell us this Tom Petty song that won the Best Special Effects MTV Music Video Award in '85'",
      "value": "$2000",
      "answer": "\"Don\\'t Come Around Here No More\"",
      "round": "Double Jeopardy!",
      "show_number": "4985"
    },
    {
      "category": "THERE'S SOMETHING ABOUT MARYLAND",
      "air_date": "1998-11-25",
      "question": "'Among U.S. racetracks, only Saratoga is older than this Preakness site, opened in 1870'",
      "value": "$800",
      "answer": "Pimlico Race Course",
      "round": "Double Jeopardy!",
      "show_number": "3273"
    },
    {
      "category": "CATS ALL, FOLKS",
      "air_date": "2003-04-30",
      "question": "'This Asian carnivore is the largest member of the cat family & the only big cat with striped fur'",
      "value": "$200",
      "answer": "tiger",
      "round": "Jeopardy!",
      "show_number": "4308"
    },
    {
      "category": "CHICKS WITH BICS",
      "air_date": "2003-01-29",
      "question": "'In 1994 this First Daughter published a seductive novel called \"Bondage\"'",
      "value": "$800",
      "answer": "Patti Davis",
      "round": "Jeopardy!",
      "show_number": "4243"
    },
    {
      "category": "AUSTRALIAN CAPITALS",
      "air_date": "2010-05-13",
      "question": "'It was named for William IV's wife, who was queen when it was founded in 1836'",
      "value": "$1600",
      "answer": "Adelaide",
      "round": "Double Jeopardy!",
      "show_number": "5919"
    },
    {
      "category": "MOVIE QUOTES",
      "air_date": "2006-04-28",
      "question": "'From 1978:\"...Nothing is over until we decide it is!  Was it over when the Germans bombed Pearl Harbor?...  No!\"'",
      "value": "$2000",
      "answer": "National Lampoon\\'s Animal House",
      "round": "Double Jeopardy!",
      "show_number": "4990"
    },
    {
      "category": "INTERNAL RHYMES",
      "air_date": "2011-03-21",
      "question": "'This adjective meaning unkempt & varied is often applied to disorganized armies or militias'",
      "value": "$1000",
      "answer": "ragtag",
      "round": "Jeopardy!",
      "show_number": "6111"
    },
    {
      "category": "MIND YOUR \"P\"s & \"Q\"s",
      "air_date": "1995-11-13",
      "question": "'It's an untrained person pretending to have medical knowledge'",
      "value": "$100",
      "answer": "Quack",
      "round": "Jeopardy!",
      "show_number": "2576"
    },
    {
      "category": "GEOGRAPHY \"B\"",
      "air_date": "2000-11-17",
      "question": "'The world's third-largest island, about 3/4 of it belongs to Indonesia'",
      "value": "$800",
      "answer": "Borneo",
      "round": "Double Jeopardy!",
      "show_number": "3730"
    },
    {
      "category": "MYTHOLOGY",
      "air_date": "1997-01-01",
      "question": "'The name of these creatures means \"Round-Eyed\"; they each had only one round eye'",
      "value": "$100",
      "answer": "Cyclops",
      "round": "Jeopardy!",
      "show_number": "2843"
    },
    {
      "category": "JACQUES IN THE BOX",
      "air_date": "2004-12-17",
      "question": "'Father Jacques Marquette & this cartographer explored the Mississippi River during June & July 1673'",
      "value": "$1600",
      "answer": "(Louis) Joliet",
      "round": "Double Jeopardy!",
      "show_number": "4670"
    },
    {
      "category": "SPORTS NICKNAMES",
      "air_date": "1996-12-23",
      "question": "'Hockey's \"The Great One\"'",
      "value": "$400",
      "answer": "Wayne Gretzky",
      "round": "Jeopardy!",
      "show_number": "2836"
    },
    {
      "category": "HAIR CARE HISTORY",
      "air_date": "2001-05-18",
      "question": "'Helene Curtis Inc. was the first to market this aerosol product in the 1950s'",
      "value": "$200",
      "answer": "Hair spray",
      "round": "Jeopardy!",
      "show_number": "3860"
    },
    {
      "category": "NEW YORK, NEW YORK",
      "air_date": "1998-12-01",
      "question": "'(VIDEO DAILY DOUBLE):It's the section of Central Park where you'd see the mosaic seen here (\"Imagine\")'",
      "value": "$1,000",
      "answer": "Strawberry Fields",
      "round": "Jeopardy!",
      "show_number": "3277"
    },
    {
      "category": "THE HAYES YEARS",
      "air_date": "1999-10-22",
      "question": "'10 members of this secret society of Irish immigrant coal workers were hanged on June 21, 1877'",
      "value": "$1000",
      "answer": "The Molly Maguires",
      "round": "Double Jeopardy!",
      "show_number": "3480"
    },
    {
      "category": "GAS",
      "air_date": "2003-10-09",
      "question": "'Used in WWI & against Iraq's Kurds, it's named for its smell'",
      "value": "$1200",
      "answer": "mustard gas",
      "round": "Double Jeopardy!",
      "show_number": "4389"
    },
    {
      "category": "20th CENTURY WOMEN",
      "air_date": "2003-01-02",
      "question": "'In August 1977 she opened her first cookie store in Palo Alto, California'",
      "value": "$200",
      "answer": "Debbi Fields",
      "round": "Jeopardy!",
      "show_number": "4224"
    },
    {
      "category": "IT'S ALL ABOUT \"U\"",
      "air_date": "2008-04-10",
      "question": "'Diva fashionista Wilhelmina Slater is the nemesis of this ABC title character'",
      "value": "$400",
      "answer": "Ugly Betty",
      "round": "Double Jeopardy!",
      "show_number": "5439"
    },
    {
      "category": "SODA POP QUIZ",
      "air_date": "2008-01-07",
      "question": "'Made originally from the roots of Smilax plants & similar to root beer, this sassy Old West treat is still served today'",
      "value": "$1000",
      "answer": "sarsaparilla",
      "round": "Jeopardy!",
      "show_number": "5371"
    },
    {
      "category": "CHARADES",
      "air_date": "2004-06-16",
      "question": "'(Cheryl for the Clue Crew makes a small \"C\" with her fingers.)  The gesture here means \"small word\", like this word followed by \"the Good Old Summertime\"'",
      "value": "$200",
      "answer": "in",
      "round": "Jeopardy!",
      "show_number": "4568"
    },
    {
      "category": "SPORTS NICKNAMES",
      "air_date": "2008-03-05",
      "question": "'In August 2005 this \"Siberian Siren\" became the first Russian ranked No. 1 in Women's tennis'",
      "value": "$800",
      "answer": "Maria Sharapova",
      "round": "Jeopardy!",
      "show_number": "5413"
    },
    {
      "category": "LITERARY SUBTITLES",
      "air_date": "2006-02-22",
      "question": "'Samuel Taylor Coleridge:\"A Vision in a Dream\"'",
      "value": "$2000",
      "answer": "Kubla Khan",
      "round": "Double Jeopardy!",
      "show_number": "4943"
    },
    {
      "category": "TOMMY ROT!",
      "air_date": "2000-09-22",
      "question": "'Like Norse warriors, this trombonist & bandleader is in Valhalla -- Valhalla, New York's Kensico Cemetery'",
      "value": "$400",
      "answer": "Tommy Dorsey",
      "round": "Jeopardy!",
      "show_number": "3690"
    },
    {
      "category": "LITERARY CHARACTERS' ADS",
      "air_date": "2009-10-09",
      "question": "'Young Russian count wanted for affair with married woman; open to pregnancy & train travel'",
      "value": "$800",
      "answer": "Anna Karenina",
      "round": "Double Jeopardy!",
      "show_number": "5765"
    },
    {
      "category": "CAT",
      "air_date": "2006-05-05",
      "question": "'Now endangered, these fast felines were once common in India where a Mogal emperor kept a thousand of them as hunting cats'",
      "value": "$400",
      "answer": "cheetah",
      "round": "Double Jeopardy!",
      "show_number": "4995"
    },
    {
      "category": "SCIENCE NEWS",
      "air_date": "2006-01-05",
      "question": "'Rocks on 4 continents were formed by the flow of this from an eruption that tore apart Pangaea'",
      "value": "$400",
      "answer": "lava",
      "round": "Double Jeopardy!",
      "show_number": "4909"
    },
    {
      "category": "OLYMPIC HISTORY",
      "air_date": "2001-07-03",
      "question": "'The first Olympic Torch Relay carried the flame from Olympia, Greece to this city, the 1936 host'",
      "value": "$400",
      "answer": "Berlin",
      "round": "Double Jeopardy!",
      "show_number": "3892"
    },
    {
      "category": "THE U.S. POPULATION",
      "air_date": "2000-09-25",
      "question": "'An August 1999 government report told of the strain on schools from the \"echo\" of this'",
      "value": None,
      "answer": "The \\\"Baby Boom\\\"",
      "round": "Final Jeopardy!",
      "show_number": "3691"
    },
    {
      "category": "STATES' MOST POPULOUS CITIES",
      "air_date": "2007-07-13",
      "question": "'Louisville,pop. 556,000'",
      "value": "$400",
      "answer": "Kentucky",
      "round": "Jeopardy!",
      "show_number": "5275"
    },
    {
      "category": "QUASI-RELATED PAIRS",
      "air_date": "2007-03-06",
      "question": "'Famed director of \"Sweeney Todd\" on Broadway & Haitian capital'",
      "value": "$1200",
      "answer": "Hal & Port Au Prince",
      "round": "Double Jeopardy!",
      "show_number": "5182"
    },
    {
      "category": "STAY-AT-HOME MOMS",
      "air_date": "2004-07-01",
      "question": "'We're sure this Ohioan's mother, Viola, was elated on July 20, 1969, but she kept her feet on the ground'",
      "value": "$800",
      "answer": "Neil Armstrong",
      "round": "Double Jeopardy!",
      "show_number": "4579"
    },
    {
      "category": "FEMALE FIRSTS",
      "air_date": "1998-02-17",
      "question": "'Bill Clinton thought of making Zoe Baird the first female attorney general but in the end it was this woman'",
      "value": "$100",
      "answer": "Janet Reno",
      "round": "Jeopardy!",
      "show_number": "3107"
    },
    {
      "category": "U.S. BAYS",
      "air_date": "2010-12-23",
      "question": "'Point Loma peninsula forms part of the entrance to this Southern California bay'",
      "value": "$1200",
      "answer": "San Diego",
      "round": "Double Jeopardy!",
      "show_number": "6049"
    },
    {
      "category": "THEY ALSO RAN",
      "air_date": "2008-04-16",
      "question": "'Born in Brooklyn in 1944, he was mayor of New York City from 1994 to 2002'",
      "value": "$200",
      "answer": "Rudy Giuliani",
      "round": "Jeopardy!",
      "show_number": "5443"
    },
    {
      "category": "VEHICLES",
      "air_date": "2005-07-05",
      "question": "'In 1965 Ralph Nader declared that this model from Chevrolet was \"Unsafe at Any Speed\"'",
      "value": "$2000",
      "answer": "the Corvair",
      "round": "Double Jeopardy!",
      "show_number": "4812"
    },
    {
      "category": "THE 76th ACADEMY AWARDS",
      "air_date": "2004-06-17",
      "question": "'She had a \"Monster\" night, taking home Best Actress Honors'",
      "value": "$600",
      "answer": "Charlize Theron",
      "round": "Jeopardy!",
      "show_number": "4569"
    },
    {
      "category": "MOVIE PREMIERES",
      "air_date": "2007-11-20",
      "question": "'(Kelly of the Clue Crew exits the theater doors at Radio City Music Hall, New York.)  Among movies that have premiered at Radio City Music Hall is \"To Kill a Mockingbird\", with an Oscar-winning performance by this man who was once an usher here'",
      "value": "$400",
      "answer": "Gregory Peck",
      "round": "Jeopardy!",
      "show_number": "5337"
    },
    {
      "category": "NEWS STORIES OF 1997",
      "air_date": "1997-12-31",
      "question": "'Dodger Wilton Guerrero was thrown out of a game June 1, 1997 for having this in his bat'",
      "value": "$200",
      "answer": "Cork",
      "round": "Double Jeopardy!",
      "show_number": "3073"
    },
    {
      "category": "COLLEGES & UNIVERSITIES",
      "air_date": "2010-09-24",
      "question": "'Its nickname was a slave term for the most powerful woman on a plantation'",
      "value": "$2000",
      "answer": "University of Mississippi",
      "round": "Double Jeopardy!",
      "show_number": "5985"
    },
    {
      "category": "VANITY",
      "air_date": "2006-03-31",
      "question": "'This Grammy, Oscar, Tony & Emmy winner famously prefers to be photographed from her left side'",
      "value": "$1000",
      "answer": "Barbra Streisand",
      "round": "Jeopardy!",
      "show_number": "4970"
    },
    {
      "category": "FAR-OUT CINEMA",
      "air_date": "2008-11-20",
      "question": "'In this M. Night Shyamalan film, aliens are good at scaring people; not so good with locked pantry doors or water'",
      "value": "$2000",
      "answer": "Signs",
      "round": "Double Jeopardy!",
      "show_number": "5569"
    },
    {
      "category": "POLITICIANS",
      "air_date": "1992-11-20",
      "question": "'From 1955-1961 this Texan was the Senate majority leader'",
      "value": "$400",
      "answer": "(Lyndon) Johnson",
      "round": "Double Jeopardy!",
      "show_number": "1890"
    },
    {
      "category": "ARTY FACTS",
      "air_date": "2007-04-13",
      "question": "'Bowler hats off to this Belgian painter who had his first exhibition in Brussels in 1927'",
      "value": "$1200",
      "answer": "(René) Magritte",
      "round": "Double Jeopardy!",
      "show_number": "5210"
    },
    {
      "category": "TBA",
      "air_date": "1999-01-06",
      "question": "'It's the animal name of the device I'm using here TO ANNOUNCE THE CLUE'",
      "value": "$200",
      "answer": "Bullhorn",
      "round": "Jeopardy!",
      "show_number": "3303"
    },
    {
      "category": "THE FIRTH OF FORTH",
      "air_date": "2002-07-03",
      "question": "'These people built the Antoine Wall from the Firth of Forth to the Firth of Clyde around 142 A.D.'",
      "value": "$1600",
      "answer": "the Romans",
      "round": "Double Jeopardy!",
      "show_number": "4123"
    },
    {
      "category": "THE MOVIES",
      "air_date": "1998-12-08",
      "question": "'In this 1969 film Robert Duvall told John Wayne, \"I call that bold talk for a one-eyed fat man\"'",
      "value": "$600",
      "answer": "True Grit",
      "round": "Double Jeopardy!",
      "show_number": "3282"
    },
    {
      "category": "SALUTE THE FLAGS",
      "air_date": "2003-02-05",
      "question": "'More people live under this flag than that of any other Central American country'",
      "value": "$2000",
      "answer": "Guatemala",
      "round": "Double Jeopardy!",
      "show_number": "4248"
    },
    {
      "category": "A DATE WITH DENSITY",
      "air_date": "2007-03-14",
      "question": "'This planet has a greater mean density than any of the others in our solar system'",
      "value": "$200",
      "answer": "Earth",
      "round": "Jeopardy!",
      "show_number": "5188"
    },
    {
      "category": "GUM",
      "air_date": "2005-02-07",
      "question": "'Its campaign using twins dates back to the 1930s'",
      "value": "$200",
      "answer": "Doublemint",
      "round": "Jeopardy!",
      "show_number": "4706"
    },
    {
      "category": "APOCALYPSE SOON?",
      "air_date": "2007-03-12",
      "question": "'In this Michael Crichton novel, a Scoop VII satellite returns to Earth with a deadly virus'",
      "value": "$1000",
      "answer": "The Andromeda Strain",
      "round": "Jeopardy!",
      "show_number": "5186"
    },
    {
      "category": "\"TRIX\" OF THE TRADE",
      "air_date": "2004-04-06",
      "question": "'Ms. Potter, the author'",
      "value": "$1200",
      "answer": "Beatrix",
      "round": "Double Jeopardy!",
      "show_number": "4517"
    },
    {
      "category": "DISEASES",
      "air_date": "2005-10-21",
      "question": "'Joint pain & fever are results of this 3-word blood disease occurring chiefly among African Americans'",
      "value": "$1600",
      "answer": "sickle-cell anemia",
      "round": "Double Jeopardy!",
      "show_number": "4855"
    },
    {
      "category": "PAPA JOHNS",
      "air_date": "2010-07-02",
      "question": "'One of his sons, John IV, wrote the memoir \"The Other Side Of Eden\"'",
      "value": "$3,000",
      "answer": "John Steinbeck",
      "round": "Double Jeopardy!",
      "show_number": "5955"
    },
    {
      "category": "\"SIDE\" EFFECTS",
      "air_date": "2004-03-22",
      "question": "'Show that includes \"Comedy Tonight\", \"Company\" & \"Send in the Clowns\"'",
      "value": "$2000",
      "answer": "Side by Side",
      "round": "Double Jeopardy!",
      "show_number": "4506"
    },
    {
      "category": "MEDICATIONS",
      "air_date": "2009-03-27",
      "question": "'It's the term for a disinfectant often applied topically, like Bactine'",
      "value": "$800",
      "answer": "an antiseptic",
      "round": "Jeopardy!",
      "show_number": "5660"
    },
    {
      "category": "LEGENDARY RHYME TIME",
      "air_date": "1999-04-19",
      "question": "'Bunyan's barroom fisticuffs'",
      "value": "$200",
      "answer": "Paul\\'s brawls",
      "round": "Double Jeopardy!",
      "show_number": "3376"
    },
    {
      "category": "\"EN\" THE BEGINNING",
      "air_date": "2002-05-10",
      "question": "'These peptide hormones in the brain reduce the sensation of pain'",
      "value": "$400",
      "answer": "endorphins",
      "round": "Double Jeopardy!",
      "show_number": "4085"
    },
    {
      "category": "\"DEEP\" DISH",
      "air_date": "2004-11-11",
      "question": "'Seen here, he was an endocrinologist before promoting Ayur Veda, an ancient form of holistic medicine'",
      "value": "$600",
      "answer": "Deepak Chopra",
      "round": "Jeopardy!",
      "show_number": "4644"
    },
    {
      "category": "ASTRONOMY",
      "air_date": "1987-11-17",
      "question": "'He discovered the four largest moons of Jupiter in 1610'",
      "value": "$200",
      "answer": "Galileo",
      "round": "Double Jeopardy!",
      "show_number": "737"
    },
    {
      "category": "LITERARY QUOTES",
      "air_date": "2009-02-18",
      "question": "'He wrote in \"Remembrance of Things Past\", \"The time which we have at our disposal every day is elastic\"'",
      "value": "$1200",
      "answer": "Marcel Proust",
      "round": "Double Jeopardy!",
      "show_number": "5633"
    },
    {
      "category": "WOMEN IN SPORTS",
      "air_date": "1998-10-06",
      "question": "'She & husband Bart Conner run a gymnastics academy in Norman, Oklahoma that rates a perfect 10'",
      "value": "$400",
      "answer": "Nadia Comaneci",
      "round": "Double Jeopardy!",
      "show_number": "3237"
    },
    {
      "category": "INVENTIONS",
      "air_date": "1985-11-22",
      "question": "'1st credited to Hans Lippershey in 1608, it was Galileo, in 1609, who first used it to look up'",
      "value": "$400",
      "answer": "the telescope",
      "round": "Double Jeopardy!",
      "show_number": "315"
    },
    {
      "category": "LITERARY SEVENS",
      "air_date": "2009-12-25",
      "question": "'Lawrence of Arabia's wartime memoirs, published in 1926, were called \"Seven Pillars of\" this'",
      "value": "$400",
      "answer": "Wisdom",
      "round": "Double Jeopardy!",
      "show_number": "5820"
    },
    {
      "category": "STARS OF THE SCREEN",
      "air_date": "2003-04-04",
      "question": "'This young American superstar has an Italian first name, but a German middle one, Wilhelm'",
      "value": "$1000",
      "answer": "Leonardo DiCaprio",
      "round": "Jeopardy!",
      "show_number": "4290"
    },
    {
      "category": "OH, HENRY!",
      "air_date": "2001-10-16",
      "question": "'Trying to reconcile free & slave states in the 1800s, he was the architect of the Missouri Compromise'",
      "value": "$600",
      "answer": "Henry Clay",
      "round": "Double Jeopardy!",
      "show_number": "3937"
    },
    {
      "category": "SPORTS",
      "air_date": "1994-05-23",
      "question": "'The insignia of this National League baseball team features a mountain peak'",
      "value": "$400",
      "answer": "the (Colorado) Rockies",
      "round": "Jeopardy!",
      "show_number": "2251"
    },
    {
      "category": "JUST CHUTE ME",
      "air_date": "2011-06-08",
      "question": "'In 1485 this Italian designed a parachute; over 500 years later, Adrian Nicholas made a jump using that design'",
      "value": "$200",
      "answer": "Leonardo",
      "round": "Jeopardy!",
      "show_number": "6168"
    },
    {
      "category": "ON THE RADIO",
      "air_date": "2010-02-17",
      "question": "'\"Sober\" was a 2009 hit for this woman whose hair color no longer matches her name'",
      "value": "$800",
      "answer": "Pink",
      "round": "Double Jeopardy!",
      "show_number": "5858"
    },
    {
      "category": "WHAT'S THE MARTYR WITH YOU?",
      "air_date": "2009-05-18",
      "question": "'When the French Revolution began in 1789, he painted its leaders & martyrs; \"The Death of Marat\" is an example'",
      "value": "$1600",
      "answer": "(Jacques-Louis) David",
      "round": "Double Jeopardy!",
      "show_number": "5696"
    },
    {
      "category": "PEOPLE",
      "air_date": "1993-11-16",
      "question": "'As a child, he billed himself as \"Davino, the Boy Magician\"; now he uses this Dickens name'",
      "value": "$200",
      "answer": "David Copperfield",
      "round": "Jeopardy!",
      "show_number": "2117"
    },
    {
      "category": "NOTABLE NAMES",
      "air_date": "1997-01-02",
      "question": "'As Chopin could tell you, it was the pen name of Amandine Aurore Lucie Dupin'",
      "value": "$1000",
      "answer": "George Sand",
      "round": "Double Jeopardy!",
      "show_number": "2844"
    },
    {
      "category": "THE LONDON STAGE",
      "air_date": "2008-12-23",
      "question": "'In 2007 these studious \"Boys\" were back in town in Alan Bennett's play at Wyndham's Theatre'",
      "value": "$2000",
      "answer": "The History Boys",
      "round": "Double Jeopardy!",
      "show_number": "5592"
    },
    {
      "category": "MIDDLE NAME, PLEASE",
      "air_date": "2003-02-19",
      "question": "'Simon Legree creator'",
      "value": "$800",
      "answer": "(Harriet) Beecher (Stowe)",
      "round": "Double Jeopardy!",
      "show_number": "4258"
    },
    {
      "category": "TV FRIENDS",
      "air_date": "1997-11-12",
      "question": "'He's the friend Matt LeBlanc plays on \"Friends\"'",
      "value": "$300",
      "answer": "Joey Tribbiani",
      "round": "Jeopardy!",
      "show_number": "3038"
    },
    {
      "category": "1996",
      "air_date": "1996-12-16",
      "question": "'This CBS News show finally aired its interview with former tobacco executive Jeffrey Wigand'",
      "value": "$200",
      "answer": "\"60 Minutes\"",
      "round": "Jeopardy!",
      "show_number": "2831"
    },
    {
      "category": "IN & AROUND LONDON",
      "air_date": "2000-05-05",
      "question": "'Shopping in London?  You may head to stores named Marks & Spencer or Fortnum & this'",
      "value": "$800",
      "answer": "Mason",
      "round": "Double Jeopardy!",
      "show_number": "3620"
    },
    {
      "category": "SNL ALUMNI",
      "air_date": "1998-09-16",
      "question": "'She plays Dr. Mary Albright on TV's \"3rd Rock From The Sun\"'",
      "value": "$200",
      "answer": "Jane Curtin",
      "round": "Jeopardy!",
      "show_number": "3223"
    },
    {
      "category": "SATIRE",
      "air_date": "1997-10-10",
      "question": "'This pair's 1881 comic opera \"Patience\" parodies aesthetes like Oscar Wilde'",
      "value": "$200",
      "answer": "Gilbert & Sullivan",
      "round": "Jeopardy!",
      "show_number": "3015"
    },
    {
      "category": "THE KOSOVO SITUATION",
      "air_date": "1999-10-06",
      "question": "'Throughout 1998 Serb forces battled the KLA, an abbreviation for this'",
      "value": "$400",
      "answer": "Kosovo Liberation Army",
      "round": "Double Jeopardy!",
      "show_number": "3468"
    },
    {
      "category": "CALIFORNIA CITIES",
      "air_date": "1990-01-12",
      "question": "'The world's largest known almond processing center as well as the governor's mansion are in this city'",
      "value": "$100",
      "answer": "Sacramento",
      "round": "Jeopardy!",
      "show_number": "1240"
    },
    {
      "category": "THE PLACE TO \"B\"",
      "air_date": "2011-02-23",
      "question": "'It's the westernmost & third largest of Canada's provinces'",
      "value": "$600",
      "answer": "British Columbia",
      "round": "Jeopardy!",
      "show_number": "6093"
    },
    {
      "category": "BODIES OF WATER",
      "air_date": "1997-05-19",
      "question": "'The Aleutian Islands separate the Pacific Ocean from this sea'",
      "value": "$600",
      "answer": "Bering Sea",
      "round": "Double Jeopardy!",
      "show_number": "2941"
    },
    {
      "category": "BOOK SERIES",
      "air_date": "1999-09-09",
      "question": "'This cat from \"Sabrina\" has his own series of \"Tails\"'",
      "value": "$800",
      "answer": "Salem",
      "round": "Double Jeopardy!",
      "show_number": "3449"
    },
    {
      "category": "PEOPLE WITH MUPPET NAMES",
      "air_date": "1998-10-13",
      "question": "'A host of \"Break The Bank\", he's best known as the former singing host of the Miss America pageant'",
      "value": "$400",
      "answer": "Bert Parks",
      "round": "Double Jeopardy!",
      "show_number": "3242"
    },
    {
      "category": "\"P\"s ON EARTH",
      "air_date": "2004-12-16",
      "question": "'While exploring the Arkansas River in 1806, he discovered the Colorado Peak named for him'",
      "value": "$1200",
      "answer": "Zebulon Pike",
      "round": "Double Jeopardy!",
      "show_number": "4669"
    },
    {
      "category": "LETTER AFTER P",
      "air_date": "1999-09-17",
      "question": "'In the symbol of an element used to fuel reactors -- its atomic number is 94'",
      "value": "$1000",
      "answer": "u (Plutonium)",
      "round": "Double Jeopardy!",
      "show_number": "3455"
    },
    {
      "category": "WHAT A YEAR!",
      "air_date": "1999-01-26",
      "question": "'In this year, \"Rock Around The Clock\" was recorded, Roger Bannister beat the clock & Henri Matisse clocked out'",
      "value": "$400",
      "answer": "1954",
      "round": "Jeopardy!",
      "show_number": "3317"
    },
    {
      "category": "\"PAY\" UP",
      "air_date": "2011-01-18",
      "question": "'It sounds positive, but it can also be the act of taking revenge'",
      "value": "$800",
      "answer": "payback",
      "round": "Double Jeopardy!",
      "show_number": "6067"
    },
    {
      "category": "PRESIDENTIAL FACEBOOK PAGES",
      "air_date": "2009-09-29",
      "question": "'Hometown: Lamar, Missouri;Religious Views: Baptist'",
      "value": "$200",
      "answer": "Truman",
      "round": "Jeopardy!",
      "show_number": "5757"
    },
    {
      "category": "SONNETS & SONNETEERS",
      "air_date": "2010-05-19",
      "question": "'John Milton wrote a sonnet about this Lord Protector under whom he served as Secretary of Foreign Languages'",
      "value": "$800",
      "answer": "Oliver Cromwell",
      "round": "Double Jeopardy!",
      "show_number": "5923"
    },
    {
      "category": "THE \"UNDER\" WORLD",
      "air_date": "2005-01-28",
      "question": "'Abolitionist \"railroad\"'",
      "value": "$400",
      "answer": "underground",
      "round": "Jeopardy!",
      "show_number": "4700"
    },
    {
      "category": "UPDATED LITERATURE?",
      "air_date": "2008-10-01",
      "question": "'Jake Barnes gets a prescription for Viagra & settles down with Lady Brett Ashley'",
      "value": "$800",
      "answer": "The Sun Also Rises",
      "round": "Jeopardy!",
      "show_number": "5533"
    },
    {
      "category": "AMERICAN HISTORY",
      "air_date": "1997-07-08",
      "question": "'On Dec. 23, 1921 President Harding pardoned this Socialist so that he could have Christmas dinner with his wife'",
      "value": "$500",
      "answer": "Eugene Victor Debs",
      "round": "Jeopardy!",
      "show_number": "2977"
    },
    {
      "category": "HISPANIC AMERICANS",
      "air_date": "1997-10-27",
      "question": "'Seen here, this model \"flowered\" as a personality on MTV & MTV Latino:'",
      "value": "$1,500",
      "answer": "Daisy Fuentes",
      "round": "Double Jeopardy!",
      "show_number": "3026"
    },
    {
      "category": "POLITICS",
      "air_date": "2003-02-26",
      "question": "'You're on this \"wing\" if you support traditional values & the conservative party line'",
      "value": "$200",
      "answer": "right-wing",
      "round": "Jeopardy!",
      "show_number": "4263"
    },
    {
      "category": "THE GREAT DEPRESSION",
      "air_date": "2003-06-26",
      "question": "'Some say the 1930 tariff named for these 2 politicians made the Depression worse & helped spread it overseas'",
      "value": "$1000",
      "answer": "Smoot & Hawley",
      "round": "Jeopardy!",
      "show_number": "4349"
    },
    {
      "category": "INVASIONS",
      "air_date": "2002-10-17",
      "question": "'Within hours of an August 1990 invasion, this country had complete control of one of its neighbors'",
      "value": "$400",
      "answer": "Iraq",
      "round": "Double Jeopardy!",
      "show_number": "4169"
    },
    {
      "category": "MED. ABBREV.",
      "air_date": "2004-12-14",
      "question": "'2 of the 3 illnesses for which a DPT vaccination provides immunity'",
      "value": "$400",
      "answer": "diphtheria and pertussis (also, tetanus)",
      "round": "Double Jeopardy!",
      "show_number": "4667"
    },
    {
      "category": "GETTING KNOTTY",
      "air_date": "2002-11-11",
      "question": "'(Cheryl of the Clue Crew reports)  This non-slipping knot takes its name from the line attached to the front part of a boat'",
      "value": "$1600",
      "answer": "bowline",
      "round": "Double Jeopardy!",
      "show_number": "4186"
    },
    {
      "category": "HOCKEY",
      "air_date": "1998-03-30",
      "question": "'A depiction of Long Island appears on the logo of this NHL team'",
      "value": "$200",
      "answer": "the Islanders",
      "round": "Double Jeopardy!",
      "show_number": "3136"
    },
    {
      "category": "DANGEROUS SCIENCE",
      "air_date": "1998-02-23",
      "question": "'He looked for a safe way to handle nitroglycerin after an 1864 explosion killed his brother'",
      "value": "$400",
      "answer": "Alfred Nobel",
      "round": "Double Jeopardy!",
      "show_number": "3111"
    },
    {
      "category": "'90s TRENDS",
      "air_date": "1999-05-28",
      "question": "'This adornment has been seen on Cher, Dennis Rodman & the 5,000-year-old \"Iceman\" found in 1991'",
      "value": None,
      "answer": "tattoos",
      "round": "Final Jeopardy!",
      "show_number": "3405"
    },
    {
      "category": "ROAMIN' WITH THE ROMANS",
      "air_date": "1999-01-05",
      "question": "'By 240 B.C. a roamin' Roman could ease on down this road all the \"way\" to Brindisi'",
      "value": "$400",
      "answer": "The Appian Way",
      "round": "Double Jeopardy!",
      "show_number": "3302"
    },
    {
      "category": "THE MOVIES",
      "air_date": "2000-06-06",
      "question": "'In this Christmas 1999 release Winona Ryder had a holly Jolie time with Angelina in the mental institute'",
      "value": "$200",
      "answer": "Girl, Interrupted",
      "round": "Jeopardy!",
      "show_number": "3642"
    },
    {
      "category": "STARTS WITH 2 VOWELS",
      "air_date": "2009-07-01",
      "question": "'A trapeze artist'",
      "value": "$2,000",
      "answer": "an aerialist",
      "round": "Double Jeopardy!",
      "show_number": "5728"
    },
    {
      "category": "COOKING",
      "air_date": "1997-11-27",
      "question": "'Pour beaten eggs slowly into simmering broth to make this Chinese dish'",
      "value": "$300",
      "answer": "egg drop soup",
      "round": "Jeopardy!",
      "show_number": "3049"
    },
    {
      "category": "OLD HAT",
      "air_date": "2001-04-19",
      "question": "'It's the Andalusian gypsy dance style performed by wearers of these hats'",
      "value": "$300",
      "answer": "Flamenco",
      "round": "Jeopardy!",
      "show_number": "3839"
    },
    {
      "category": "HISTORY",
      "air_date": "1999-04-22",
      "question": "'In 897 Pope Stephen VI had his predecessor Formosus exhumed, put on trial & thrown into this river'",
      "value": "$500",
      "answer": "Tiber",
      "round": "Jeopardy!",
      "show_number": "3379"
    },
    {
      "category": "SKULL",
      "air_date": "2008-10-17",
      "question": "'The skull seen here belongs to this creature, Ursus maritimus'",
      "value": "$200",
      "answer": "the polar bear",
      "round": "Jeopardy!",
      "show_number": "5545"
    },
    {
      "category": "CROSSWORD CLUES \"G\"",
      "air_date": "1998-10-26",
      "question": "'Sand, or \"True\" nerve            (4)'",
      "value": "$800",
      "answer": "Grit",
      "round": "Double Jeopardy!",
      "show_number": "3251"
    },
    {
      "category": "FOUND IN MONGOLIA",
      "air_date": "2010-09-22",
      "question": "'Mongolia's annual Naadam festival includes archery, wrestling & the racing of   these animals'",
      "value": "$200",
      "answer": "horses",
      "round": "Jeopardy!",
      "show_number": "5983"
    },
    {
      "category": "12-LETTER WORDS",
      "air_date": "2006-07-17",
      "question": "'This curry-flavored soup takes its name from the Tamil for \"pepper water\"'",
      "value": "$600",
      "answer": "mulligatawny",
      "round": "Jeopardy!",
      "show_number": "5046"
    },
    {
      "category": "FUN WITH PROBABILITY",
      "air_date": "2007-10-03",
      "question": "'The probability of the first card dealt being an ace is 4 in 52, so the probability of the second card being an ace is 1 in this number'",
      "value": "$2000",
      "answer": "17",
      "round": "Double Jeopardy!",
      "show_number": "5303"
    },
    {
      "category": "WORLD LIT",
      "air_date": "2000-11-22",
      "question": "'\"The Art of the Impossible\" is a collection of writings by this Czech playwright & president'",
      "value": "$200",
      "answer": "Vaclav Havel",
      "round": "Double Jeopardy!",
      "show_number": "3733"
    },
    {
      "category": "'70s THEATER",
      "air_date": "1986-02-07",
      "question": "'A \"Babe on Broadway\" in 1941 film, it wasn't until 1979's \"Sugar Babies\" he made a real Broadway debut'",
      "value": "$400",
      "answer": "Mickey Rooney",
      "round": "Double Jeopardy!",
      "show_number": "370"
    },
    {
      "category": "REQUIRED READING",
      "air_date": "2000-10-03",
      "question": "'In works of mythology, Ajax was one of the heroes of this country in the Trojan War'",
      "value": "$500",
      "answer": "Greece",
      "round": "Jeopardy!",
      "show_number": "3697"
    },
    {
      "category": "CITY SONGS",
      "air_date": "2010-07-22",
      "question": "'Sinatra:\"Bet your bottom dollar you lose the blues in\" this city, this city, \"the town... Billy Sunday could not shut down\"'",
      "value": "$400",
      "answer": "Chicago",
      "round": "Jeopardy!",
      "show_number": "5969"
    },
    {
      "category": "THE QUOTABLE FRANKLIN",
      "air_date": "1989-11-06",
      "question": "'These \"fell great oaks\"'",
      "value": "$200",
      "answer": "Little Srokes",
      "round": "Jeopardy!",
      "show_number": "1191"
    },
    {
      "category": "THE QUOTABLE MAO",
      "air_date": "2006-04-24",
      "question": "'\"Weapons are an important factor in war, but not the decisive one; it is\" this \"and not materials that counts\"'",
      "value": "$1600",
      "answer": "man",
      "round": "Double Jeopardy!",
      "show_number": "4986"
    },
    {
      "category": "AMERICAN CUISINE",
      "air_date": "1997-12-29",
      "question": "'A favorite in New England, red flannel hash gets its color from these red veggies'",
      "value": "$400",
      "answer": "Beets",
      "round": "Jeopardy!",
      "show_number": "3071"
    },
    {
      "category": "HOLIDAYS & OBSERVANCES",
      "air_date": "2006-04-17",
      "question": "'The Punxsutawney Spirit was the first newspaper to print news about the observance of this holiday in 1886'",
      "value": "$600",
      "answer": "Groundhog Day",
      "round": "Jeopardy!",
      "show_number": "4981"
    },
    {
      "category": "BIBLICAL PAINTINGS",
      "air_date": "2010-03-19",
      "question": "'(Sarah of the Clue Crew shows a painting on the monitor.)  In a 17th-century painting, Isaac, now blind in his old age, is blessing Jacob, who, you'll notice, is wearing gloves to hide the fact that he isn't this hairier brother'",
      "value": "$2000",
      "answer": "Esau",
      "round": "Double Jeopardy!",
      "show_number": "5880"
    },
    {
      "category": "THE AGE OF REASON",
      "air_date": "2001-01-04",
      "question": "'The ideas of deism are usually represented by God making one of these & then just letting it run'",
      "value": "$400",
      "answer": "Watch",
      "round": "Jeopardy!",
      "show_number": "3764"
    },
    {
      "category": "WHAT A CARD!",
      "air_date": "2008-09-09",
      "question": "'Founded in 1938, this company developed Bazooka Bubble Gum & paired it with baseball trading cards'",
      "value": "$2000",
      "answer": "Topps",
      "round": "Double Jeopardy!",
      "show_number": "5517"
    },
    {
      "category": "LATIN CLASS",
      "air_date": "1998-02-17",
      "question": "'Descartes thought therefore he knew this first person singular form of the verb \"to be\"'",
      "value": "$600",
      "answer": "Sum",
      "round": "Double Jeopardy!",
      "show_number": "3107"
    },
    {
      "category": "BOOKS & AUTHORS",
      "air_date": "2010-11-08",
      "question": "'This Khaled Hosseini novel is about Amir, who flees Kabul for America'",
      "value": "$600",
      "answer": "The Kite Runner",
      "round": "Jeopardy!",
      "show_number": "6016"
    },
    {
      "category": "BROTHERS & SISTERS",
      "air_date": "1984-09-20",
      "question": "'In the Bible, Aaron was this brother's mouthpiece in dealing with Pharaoh'",
      "value": "$400",
      "answer": "Moses",
      "round": "Double Jeopardy!",
      "show_number": "9"
    },
    {
      "category": "RHYME TIME",
      "air_date": "2011-06-20",
      "question": "'An odd-looking Vandyke or goatee'",
      "value": "$400",
      "answer": "a weird beard",
      "round": "Double Jeopardy!",
      "show_number": "6176"
    },
    {
      "category": "A MURDER INVESTIGATION",
      "air_date": "2010-11-29",
      "question": "'(Kyra Sedgwick delivers the clue.)  If 2 or more murders have a similar type of victim & weapon, you might be dealing with one of these, a term popularized by Robert Ressler of the FBI'",
      "value": "$800",
      "answer": "a serial killer",
      "round": "Jeopardy!",
      "show_number": "6031"
    },
    {
      "category": "\"DE\" ARTS",
      "air_date": "2005-03-07",
      "question": "'The son of a surgeon, this director brought some gore to the screen in \"Carrie\" & \"Scarface\"'",
      "value": "$200",
      "answer": "(Brian) De Palma",
      "round": "Jeopardy!",
      "show_number": "4726"
    },
    {
      "category": "THE AMERICAN REVOLUTION",
      "air_date": "2006-02-08",
      "question": "'Formerly Fort Carillon, it was captured by Ethan Allen & others May 10, 1775'",
      "value": "$2000",
      "answer": "Fort Ticonderoga",
      "round": "Double Jeopardy!",
      "show_number": "4933"
    },
    {
      "category": "THE JIMMY CARTER EXPERIENCE",
      "air_date": "2005-02-28",
      "question": "'Cool under \"Fire\" during a 7-year Navy career, Carter served on the Seawolf, this type of vessel'",
      "value": "$600",
      "answer": "a (nuclear) submarine",
      "round": "Jeopardy!",
      "show_number": "4721"
    },
    {
      "category": "COLLEGIATE SPORTS NICKNAMES",
      "air_date": "1999-07-22",
      "question": "'Michigan State'",
      "value": "$500",
      "answer": "Spartans",
      "round": "Jeopardy!",
      "show_number": "3444"
    },
    {
      "category": "NYPD",
      "air_date": "2005-04-06",
      "question": "'(Sarah of the Clue Crew reports from outside an NYPD station.)  On the narrow streets of Lower Manhattan police drive Piaggios, from the makers of this Italian scooter that debuted in 1946'",
      "value": "$600",
      "answer": "the Vespa",
      "round": "Jeopardy!",
      "show_number": "4748"
    },
    {
      "category": "REMEMBERING ARTHUR MILLER",
      "air_date": "2005-03-18",
      "question": "'This scathingly personal drama portrayed Marilyn Monroe as a singer named Maggie'",
      "value": "$1600",
      "answer": "After the Fall",
      "round": "Double Jeopardy!",
      "show_number": "4735"
    },
    {
      "category": "ENTERTAINING JOHNS",
      "air_date": "2005-12-09",
      "question": "'A one-time gag writer for Red Skelton, he was reportedly the highest-paid TV star at his peak in the 1980s'",
      "value": "$400",
      "answer": "Johnny Carson",
      "round": "Double Jeopardy!",
      "show_number": "4890"
    },
    {
      "category": "THIS MOVIE IS A DISASTER!",
      "air_date": "2005-09-12",
      "question": "'Dustin Hoffman fights a deadly African virus that has spread to America'",
      "value": "$1200",
      "answer": "Outbreak",
      "round": "Double Jeopardy!",
      "show_number": "4826"
    },
    {
      "category": "SKY HIGH",
      "air_date": "2009-02-02",
      "question": "'The Sheraton Hotelat 500 Canal Street'",
      "value": "$800",
      "answer": "New Orleans",
      "round": "Jeopardy!",
      "show_number": "5621"
    },
    {
      "category": "FLOAT LIKE A BUTTERFLY...",
      "air_date": "2010-02-24",
      "question": "'Seen here are scores of these butterflies at their winter camp in Michoacan, Mexico'",
      "value": "$800",
      "answer": "monarchs",
      "round": "Double Jeopardy!",
      "show_number": "5863"
    },
    {
      "category": "COLLEGE TEAM NICKNAMES",
      "air_date": "2003-04-11",
      "question": "'(I'm Kurt Warner.) The team at my alma mater, Northern Iowa, is these big, fierce black cats'",
      "value": "$200",
      "answer": "Panthers",
      "round": "Jeopardy!",
      "show_number": "4295"
    },
    {
      "category": "SYMPHONIES ON FILM",
      "air_date": "2008-12-05",
      "question": "'In 1998's \"Serengeti Symphony\", the title nature reserve in this country is shown with only music & natural sound'",
      "value": "$1200",
      "answer": "Tanzania",
      "round": "Double Jeopardy!",
      "show_number": "5580"
    },
    {
      "category": "WRITERS",
      "air_date": "1992-11-12",
      "question": "'\"Scientific American\" was one of the magazines that reviewed his novel, \"Gravity's Rainbow\"'",
      "value": "$1,000",
      "answer": "Thomas Pynchon",
      "round": "Double Jeopardy!",
      "show_number": "1884"
    },
    {
      "category": "MISSING ELEMENTS",
      "air_date": "2009-01-15",
      "question": "'Methanol:OH'",
      "value": "$2000",
      "answer": "carbon",
      "round": "Double Jeopardy!",
      "show_number": "5609"
    },
    {
      "category": "RHYME TIME",
      "air_date": "2008-05-21",
      "question": "'A fake foot covering'",
      "value": "$800",
      "answer": "a mock sock",
      "round": "Double Jeopardy!",
      "show_number": "5468"
    },
    {
      "category": "NOTED AFRICAN AMERICANS",
      "air_date": "2002-09-04",
      "question": "'In 1993 she became the second Black American elected to serve in the U.S. Senate since Reconstruction'",
      "value": "$1600",
      "answer": "Carol Moseley Braun",
      "round": "Double Jeopardy!",
      "show_number": "4138"
    },
    {
      "category": "\"BOR\"-ING",
      "air_date": "2000-07-21",
      "question": "'Last name of the ruthless German seen here'",
      "value": "$500",
      "answer": "Bormann (Martin)",
      "round": "Jeopardy!",
      "show_number": "3675"
    },
    {
      "category": "TELEVISION",
      "air_date": "1999-06-23",
      "question": "'This Buddy Ebsen series had a Nielsen average of 39.1 for 1963-64, the highest season rating from 1960 to today'",
      "value": "$1000",
      "answer": "The Beverly Hillbillies",
      "round": "Double Jeopardy!",
      "show_number": "3423"
    },
    {
      "category": "ISLAND COUNTRIES",
      "air_date": "2000-06-26",
      "question": "'In 1998 Pope John Paul II concluded his visit to this country with a mass at the Plaza de la Revolucion'",
      "value": "$200",
      "answer": "Cuba",
      "round": "Jeopardy!",
      "show_number": "3656"
    },
    {
      "category": "PEOPLE",
      "air_date": "2003-07-08",
      "question": "'As a partner in a law firm in Arkansas, she earned a higher salary than her husband, then the state's governor'",
      "value": "$800",
      "answer": "Hillary Rodham Clinton",
      "round": "Double Jeopardy!",
      "show_number": "4357"
    },
    {
      "category": "POLITICAL QUOTES",
      "air_date": "1990-09-03",
      "question": "'Completes \"If the British Empire and its Commonwealth last for 1,000 years, men will still say...\"'",
      "value": "$400",
      "answer": "this was their finest hour",
      "round": "Jeopardy!",
      "show_number": "1376"
    },
    {
      "category": "CAPITAL CITY HOTELS",
      "air_date": "2001-06-21",
      "question": "'Hostel La Macarena & Hostel Cervantes'",
      "value": "$600",
      "answer": "Madrid",
      "round": "Double Jeopardy!",
      "show_number": "3884"
    },
    {
      "category": "WHICH BIBLE BOOK?",
      "air_date": "2011-06-17",
      "question": "'\"A wise son maketh a glad father:  but a foolish son is the heaviness of his mother\"'",
      "value": "$600",
      "answer": "Proverbs",
      "round": "Jeopardy!",
      "show_number": "6175"
    },
    {
      "category": "SAMUEL L. JACKSON",
      "air_date": "2008-02-28",
      "question": "'In 1995 Sam's Zeus Carver had a rough day with Bruce Willis in this sequel'",
      "value": "$1200",
      "answer": "Die Hard with a Vengeance (or Die Hard 3)",
      "round": "Double Jeopardy!",
      "show_number": "5409"
    },
    {
      "category": "RHYMING BRANDS",
      "air_date": "2004-04-30",
      "question": "'One slogan said, \"Me-Hee for\" this chocolate drink'",
      "value": "$400",
      "answer": "Yoo-Hoo",
      "round": "Jeopardy!",
      "show_number": "4535"
    },
    {
      "category": "PREFIXES",
      "air_date": "2012-01-02",
      "question": "'\"Anti-\" means \"against; \"ante-\" means this'",
      "value": "$1,200",
      "answer": "before",
      "round": "Jeopardy!",
      "show_number": "6281"
    },
    {
      "category": "NATIONAL HISTORIC SITES",
      "air_date": "2005-01-06",
      "question": "'A site near Walla Walla commemorates the role of Marcus & Narcissa Whitman in establishing part of this trail'",
      "value": "$200",
      "answer": "the Oregon Trail",
      "round": "Jeopardy!",
      "show_number": "4684"
    },
    {
      "category": "THE DEVIL",
      "air_date": "2008-02-01",
      "question": "'It's what the Devil wears in the title of Lauren Weisberger's fashion industry novel'",
      "value": "$400",
      "answer": "Prada",
      "round": "Jeopardy!",
      "show_number": "5390"
    },
    {
      "category": "21st CENTURY MUSIC",
      "air_date": "2002-11-14",
      "question": "'In 2001 Alicia Keys won an MTV Award for Best New Artist in a Video with this song'",
      "value": "$1000",
      "answer": "\"Fallin\\'\"",
      "round": "Jeopardy!",
      "show_number": "4189"
    },
    {
      "category": "PETS",
      "air_date": "1990-11-05",
      "question": "'The Birman & the Balinese are long-haired breeds of these'",
      "value": "$400",
      "answer": "cats",
      "round": "Jeopardy!",
      "show_number": "1421"
    },
    {
      "category": "UNREAL ESTATE",
      "air_date": "2010-01-12",
      "question": "'Bearing a close resemblance to William Randolph Hearst's San Simeon, it's Citizen Kane's mansion'",
      "value": "$1000",
      "answer": "Xanadu",
      "round": "Jeopardy!",
      "show_number": "5832"
    },
    {
      "category": "FAMILIAR PHRASES",
      "air_date": "1997-04-23",
      "question": "'Long ago this was \"as good as an ell\"; now it's \"as good as a mile\"'",
      "value": "$200",
      "answer": "A miss",
      "round": "Jeopardy!",
      "show_number": "2923"
    },
    {
      "category": "BOOKS OF THE BIBLE",
      "air_date": "2001-12-07",
      "question": "'This book talks about \"A time to love, and a time to hate; a time of war, and a time of peace\"'",
      "value": "$1200",
      "answer": "Ecclesiastes",
      "round": "Double Jeopardy!",
      "show_number": "3975"
    },
    {
      "category": "FOREIGN WORDS & PHRASES",
      "air_date": "1990-05-16",
      "question": "'This Italian word is a musical direction for something you must play; it's obligatory'",
      "value": "$400",
      "answer": "Obligato",
      "round": "Double Jeopardy!",
      "show_number": "1328"
    },
    {
      "category": "THE FLAGPOLE",
      "air_date": "2002-07-04",
      "question": "'Originally a flagpole was just a straight one of these cut, trimmed & treated'",
      "value": "$400",
      "answer": "a tree trunk",
      "round": "Double Jeopardy!",
      "show_number": "4124"
    },
    {
      "category": "CROSSWORD CLUES \"V\"",
      "air_date": "2009-05-26",
      "question": "'Short, pointed beard(7)'",
      "value": "$1200",
      "answer": "Vandyke",
      "round": "Double Jeopardy!",
      "show_number": "5702"
    },
    {
      "category": "ANIMAL ANAGRAMS",
      "air_date": "1998-07-15",
      "question": "'Verna has a pet one perching just above her chamber door'",
      "value": "$600",
      "answer": "Raven (Verna)",
      "round": "Double Jeopardy!",
      "show_number": "3213"
    },
    {
      "category": "BORN TO RUN",
      "air_date": "2006-03-22",
      "question": "'At the 1936 Berlin games, he ran a 10.3 in the 100 meters, tying the Olympic record'",
      "value": "$200",
      "answer": "Jesse Owens",
      "round": "Jeopardy!",
      "show_number": "4963"
    },
    {
      "category": "NOT TO BE CONFUSED: ACTING EDITION",
      "air_date": "2009-01-13",
      "question": "'William Daniels was a snooty doc on \"St. Elsewhere\" & Anthony Daniels played this snooty character in \"Star Wars\"'",
      "value": "$400",
      "answer": "C-3PO",
      "round": "Double Jeopardy!",
      "show_number": "5607"
    },
    {
      "category": "NAME THE POET",
      "air_date": "2007-02-19",
      "question": "'\"His pride had cast him out from heaven, with all his host of rebel angels\"'",
      "value": "$400",
      "answer": "Milton",
      "round": "Double Jeopardy!",
      "show_number": "5171"
    },
    {
      "category": "\"C\"OMEDIANS",
      "air_date": "2003-03-07",
      "question": "'Some of his \"Seven Words You Can't Say on TV\" are now said on TV, especially cable'",
      "value": "$400",
      "answer": "George Carlin",
      "round": "Jeopardy!",
      "show_number": "4270"
    },
    {
      "category": "GOING COUNTRY",
      "air_date": "2003-04-30",
      "question": "'It's the largest country in the Caribbean & it's only about 90 miles south of Florida'",
      "value": "$1200",
      "answer": "Cuba",
      "round": "Double Jeopardy!",
      "show_number": "4308"
    },
    {
      "category": "\"ERE\"Y WORDS",
      "air_date": "2010-10-20",
      "question": "'In Greek mythology, one must pass through this dark region of the underworld to reach Hades'",
      "value": "$2000",
      "answer": "Erebus",
      "round": "Double Jeopardy!",
      "show_number": "6003"
    },
    {
      "category": "WEST ON THE MAP",
      "air_date": "1990-05-02",
      "question": "'Since 1967 Israel has occupied a controversial area on the West Bank of this river'",
      "value": "$600",
      "answer": "The Jordan River",
      "round": "Double Jeopardy!",
      "show_number": "1318"
    },
    {
      "category": "& THE AWARD GOES TO...",
      "air_date": "2008-05-06",
      "question": "'Awards for this art form include the Cesar, the Palme d'Or & the Golden Lion'",
      "value": "$200",
      "answer": "film",
      "round": "Jeopardy!",
      "show_number": "5457"
    },
    {
      "category": "POPULATIONS",
      "air_date": "2002-09-19",
      "question": "'Of 2 million, 20 million or 200 million, the number closest to the population of Native Americans in the U.S.A.'",
      "value": "$400",
      "answer": "2 million",
      "round": "Double Jeopardy!",
      "show_number": "4149"
    },
    {
      "category": "RECENT MOVIES",
      "air_date": "2002-09-18",
      "question": "'The tagline to this 2002 sequel was \"This summer a Little goes a long way\"'",
      "value": "$800",
      "answer": "Stuart Little",
      "round": "Jeopardy!",
      "show_number": "4148"
    },
    {
      "category": "COMING TO A CLOTHES",
      "air_date": "2001-06-11",
      "question": "'Hyphenated name for the style of jacket seen here:'",
      "value": "$200",
      "answer": "Double-breasted",
      "round": "Jeopardy!",
      "show_number": "3876"
    },
    {
      "category": "\"I\" DO",
      "air_date": "2005-12-01",
      "question": "'This vomit-inducing syrup originally came from the root of a South American shrub'",
      "value": "$1000",
      "answer": "ipecac",
      "round": "Jeopardy!",
      "show_number": "4884"
    },
    {
      "category": "\"D\" FACTO",
      "air_date": "2007-03-23",
      "question": "'2-word term for the group of cells for prisoners awaiting execution'",
      "value": "$800",
      "answer": "death row",
      "round": "Double Jeopardy!",
      "show_number": "5195"
    },
    {
      "category": "11-LETTER WORDS",
      "air_date": "2010-05-10",
      "question": "'Unplanned or without premeditation, like some combustion'",
      "value": "$400",
      "answer": "spontaneous",
      "round": "Double Jeopardy!",
      "show_number": "5916"
    },
    {
      "category": "1979",
      "air_date": "1997-10-14",
      "question": "'Noted falls in 1979 included the Shah of Iran's after 37 years & this space station's after 34,980 orbits'",
      "value": "$300",
      "answer": "Skylab",
      "round": "Jeopardy!",
      "show_number": "3017"
    },
    {
      "category": "WORLD GEOGRAPHY",
      "air_date": "1997-12-08",
      "question": "'Natives of this largest island call it Kalaallit Nunaat'",
      "value": "$300",
      "answer": "Greenland",
      "round": "Jeopardy!",
      "show_number": "3056"
    },
    {
      "category": "IT'S ALL IN YOUR HEAD",
      "air_date": "2004-01-26",
      "question": "'Bicuspids are also known as pre-these & are permanent grinding teeth'",
      "value": "$400",
      "answer": "molars",
      "round": "Jeopardy!",
      "show_number": "4466"
    },
    {
      "category": "SUPERSTITIONS",
      "air_date": "1996-09-02",
      "question": "'For a bride, a coin in here ensures future wealth & perhaps a painful walk down the aisle'",
      "value": "$400",
      "answer": "her shoe",
      "round": "Jeopardy!",
      "show_number": "2756"
    },
    {
      "category": "YUL TIDE FILMS",
      "air_date": "1997-12-26",
      "question": "'In \"The Buccaneer\", Yul portrayed this buccaneer during the Battle of New Orleans'",
      "value": "$1000",
      "answer": "Jean Lafitte",
      "round": "Double Jeopardy!",
      "show_number": "3070"
    },
    {
      "category": "U.S. GEOGRAPHY",
      "air_date": "2008-10-20",
      "question": "'Of the non-state U.S. territories, areas & districts, the only one that is larger in area than the smallest state'",
      "value": None,
      "answer": "Puerto Rico",
      "round": "Final Jeopardy!",
      "show_number": "5546"
    },
    {
      "category": "MEN IN BLACK",
      "air_date": "1998-05-19",
      "question": "'An alien on \"Star Trek:  Voyager\", Jennifer Lien is the voice of this human MIB agent in the cartoon series'",
      "value": "$800",
      "answer": "\"L\"",
      "round": "Double Jeopardy!",
      "show_number": "3172"
    },
    {
      "category": "\"J\"EOGRAPHY",
      "air_date": "2006-04-17",
      "question": "'Until the '60s, French was the official language of this British island in the English Channel'",
      "value": "$1600",
      "answer": "Jersey",
      "round": "Double Jeopardy!",
      "show_number": "4981"
    },
    {
      "category": "INNOVATORS",
      "air_date": "2002-12-19",
      "question": "'George Ballas invented the powered plant-cutting tool known by this alliterative name'",
      "value": "$600",
      "answer": "Weed Whacker",
      "round": "Jeopardy!",
      "show_number": "4214"
    },
    {
      "category": "MY FAVORITE THINGS",
      "air_date": "2011-07-12",
      "question": "'\"Rain drops on roses and whiskers on\" these young animals'",
      "value": "$200",
      "answer": "kittens",
      "round": "Jeopardy!",
      "show_number": "6192"
    },
    {
      "category": "BODIES OF WATER",
      "air_date": "2011-12-09",
      "question": "'At its northern end, this \"colorful\" sea branches into the Gulf of Suez on the west & the Gulf of Aqaba on the east'",
      "value": "$400",
      "answer": "the Red",
      "round": "Jeopardy!",
      "show_number": "6265"
    },
    {
      "category": "STIFLE YOURSELF EDICT",
      "air_date": "2001-06-28",
      "question": "'After Charles V, this priest is the next person mentioned by name in the 1521 edict of the Diet of Worms'",
      "value": "$200",
      "answer": "Martin Luther",
      "round": "Double Jeopardy!",
      "show_number": "3889"
    },
    {
      "category": "THE COUNTRY HE RULED",
      "air_date": "2011-09-19",
      "question": "'John III Sobieski:1674 to 1696'",
      "value": "$1200",
      "answer": "Poland",
      "round": "Double Jeopardy!",
      "show_number": "6206"
    },
    {
      "category": "ROBERT LOUIS STEVENSON",
      "air_date": "2002-10-03",
      "question": "'\"The Silverado Squatters\" was an 1883 tale about Stevenson's experiences in one of these camps in California'",
      "value": "$800",
      "answer": "mining camp",
      "round": "Jeopardy!",
      "show_number": "4159"
    },
    {
      "category": "UNREAL ESTATE",
      "air_date": "1997-10-23",
      "question": "'Mildendo, a metropolis in this country in \"Gulliver's Travels\" was only 500 feet square'",
      "value": "$200",
      "answer": "Lilliput",
      "round": "Jeopardy!",
      "show_number": "3024"
    },
    {
      "category": "CANADA",
      "air_date": "2003-06-10",
      "question": "'This peak, Canada's highest point, was named for the founder of the Geological Survey of Canada'",
      "value": "$2000",
      "answer": "Mount Logan",
      "round": "Double Jeopardy!",
      "show_number": "4337"
    },
    {
      "category": "BEER BASH!",
      "air_date": "1998-09-25",
      "question": "'This Bavarian city is famous for its pale lager & was the site of the 1923 Beer Hall Putsch'",
      "value": "$1,000",
      "answer": "Munich",
      "round": "Jeopardy!",
      "show_number": "3230"
    },
    {
      "category": "THE OSCARS",
      "air_date": "1995-11-22",
      "question": "'2 of the 5 actors before Tom Hanks to win 2 Best Actor Oscars'",
      "value": None,
      "answer": "(2 of 5) Marlon Brando, Gary Cooper, Dustin Hoffman, Fredric March & Spencer Tracy",
      "round": "Final Jeopardy!",
      "show_number": "2583"
    },
    {
      "category": "ON THE \"MAT\"",
      "air_date": "2004-05-31",
      "question": "'This prefix is from the Greek for \"blood\"'",
      "value": "$2000",
      "answer": "hemato- (or hemat-)",
      "round": "Double Jeopardy!",
      "show_number": "4556"
    },
    {
      "category": "MYTHOLOGY",
      "air_date": "1990-03-19",
      "question": "'This goddess of wisdom was said to have sprung forth fully grown from the brain of her father, Zeus'",
      "value": "$200",
      "answer": "Athena",
      "round": "Double Jeopardy!",
      "show_number": "1286"
    },
    {
      "category": "\"OY\" TO THE WORLD",
      "air_date": "2010-07-01",
      "question": "'Developed in 1923, its the yummy hybrid edible seen here'",
      "value": "$1200",
      "answer": "a boysenberry",
      "round": "Double Jeopardy!",
      "show_number": "5954"
    },
    {
      "category": "NAMES BY THE NUMBER",
      "air_date": "1999-01-15",
      "question": "'Dopey, Sleepy, Doc, Bashful, Happy, Sneezy & Grumpy'",
      "value": "$200",
      "answer": "The Seven Dwarfs",
      "round": "Double Jeopardy!",
      "show_number": "3310"
    },
    {
      "category": "NAMES IN THE NEWS",
      "air_date": "1990-01-22",
      "question": "'If you were invited to Tangier for a $2 mil. weekend birthday bash in August '89, it was probably his'",
      "value": "$400",
      "answer": "Malcolm Forbes",
      "round": "Jeopardy!",
      "show_number": "1246"
    },
    {
      "category": "CELEB L.L.s",
      "air_date": "2002-09-25",
      "question": "'She was the first woman to have a country album certified gold'",
      "value": "$800",
      "answer": "Loretta Lynn",
      "round": "Double Jeopardy!",
      "show_number": "4153"
    },
    {
      "category": "CELEBRITY MEMOIRS",
      "air_date": "2011-10-10",
      "question": "'This country star called her 2011 memoir \"From This Moment On\", also the name of one of her hit songs'",
      "value": "$1000",
      "answer": "Shania Twain",
      "round": "Jeopardy!",
      "show_number": "6221"
    },
    {
      "category": "THERE'S A SUCKER...",
      "air_date": "2003-03-24",
      "question": "'This company says it's answered over 25,000 letters asking how many licks it takes to get to the center of its famous pop'",
      "value": "$400",
      "answer": "Tootsie Roll",
      "round": "Jeopardy!",
      "show_number": "4281"
    },
    {
      "category": "GREASE",
      "air_date": "2010-04-22",
      "question": "'Every March brings the national day named for this sometimes-greasy treat'",
      "value": "$400",
      "answer": "a corndog",
      "round": "Jeopardy!",
      "show_number": "5904"
    },
    {
      "category": "MUSICIANS",
      "air_date": "2010-03-23",
      "question": "'After a near-death experience, this singer converted to the Islamic faith and took a new name:  Yusuf Islam'",
      "value": "$200",
      "answer": "Cat Stevens",
      "round": "Jeopardy!",
      "show_number": "5882"
    },
    {
      "category": "GIMME AN \"H\"",
      "air_date": "2008-06-30",
      "question": "'In Greek myth, she's the goddess of the hearth'",
      "value": "$2000",
      "answer": "Hestia",
      "round": "Double Jeopardy!",
      "show_number": "5496"
    },
    {
      "category": "HODGEPODGE",
      "air_date": "2009-02-09",
      "question": "'In poker, 3 & 5 of hearts, 10 of clubs, jack of hearts, king of hearts is called a busted this'",
      "value": "$400",
      "answer": "a flush",
      "round": "Jeopardy!",
      "show_number": "5626"
    },
    {
      "category": "ORGANIZATIONS",
      "air_date": "2003-01-30",
      "question": "'Its slogan is \"When You Can't Breathe, Nothing Else Matters\"'",
      "value": "$2,300",
      "answer": "American Lung Association",
      "round": "Double Jeopardy!",
      "show_number": "4244"
    },
    {
      "category": "RITA HAYWORTH",
      "air_date": "2000-04-24",
      "question": "'Born Margarita Cansino, Rita shared her middle name with this Bizet opera temptress'",
      "value": "$200",
      "answer": "Carmen",
      "round": "Double Jeopardy!",
      "show_number": "3611"
    },
    {
      "category": "OFFICIAL STATE STUFF",
      "air_date": "2010-02-18",
      "question": "'Minnesota's state butterfly is this one with bright orange & black wings'",
      "value": "$400",
      "answer": "a monarch",
      "round": "Jeopardy!",
      "show_number": "5859"
    },
    {
      "category": "19th CENTURY LITERARY CHARACTERS",
      "air_date": "2010-11-18",
      "question": "'Alice questions reality after these 2 say she's only a character in the Red King's dream; ooo, 19th century \"Inception\"!'",
      "value": "$1600",
      "answer": "Tweedledee and Tweedledum",
      "round": "Double Jeopardy!",
      "show_number": "6024"
    },
    {
      "category": "FLOWERS",
      "air_date": "2008-10-16",
      "question": "'The lady's slipper is the official flower of this Canadian island province'",
      "value": "$800",
      "answer": "Prince Edward Island",
      "round": "Double Jeopardy!",
      "show_number": "5544"
    },
    {
      "category": "TAKE THE KIDS!",
      "air_date": "2000-05-24",
      "question": "'The Polynesian Cultural Center on the north shore of this island is famous for canoe pageants & luaus'",
      "value": "$400",
      "answer": "Oahu",
      "round": "Jeopardy!",
      "show_number": "3633"
    },
    {
      "category": "UNSEEN TV FACES",
      "air_date": "2007-02-20",
      "question": "'We never saw the face of this Yankees owner on \"Seinfeld\"; it was really Larry David voicing the part'",
      "value": "$800",
      "answer": "Steinbrenner",
      "round": "Jeopardy!",
      "show_number": "5172"
    },
    {
      "category": "2008 OBITS",
      "air_date": "2009-05-26",
      "question": "'A Russian nobelist, he shuffled off this mortal gulag at age 89'",
      "value": "$2000",
      "answer": "Solzhenitsyn",
      "round": "Double Jeopardy!",
      "show_number": "5702"
    },
    {
      "category": "POTPOURRI",
      "air_date": "2008-07-16",
      "question": "'(Kelly of the Clue Crew  tries to sell you a cell from Sony Headquarters in Tokyo, Japan.) The W44S multimedia phone combines Sony's multimedia, like digital TV, with the phone technology of Ericsson, based in this country'",
      "value": "$400",
      "answer": "Sweden",
      "round": "Jeopardy!",
      "show_number": "5508"
    },
    {
      "category": "THE \"PEN\"",
      "air_date": "2008-01-04",
      "question": "'This antibiotic is effective against certain spirochetes'",
      "value": "$200",
      "answer": "penicillin",
      "round": "Jeopardy!",
      "show_number": "5370"
    },
    {
      "category": "\"EASY\"",
      "air_date": "1984-12-12",
      "question": "''30s domestic comedy radio show featuring Goodman Ace & wife, Jane'",
      "value": "$1000",
      "answer": "Easy Aces",
      "round": "Double Jeopardy!",
      "show_number": "68"
    },
    {
      "category": "BORN & DIED",
      "air_date": "2007-10-30",
      "question": "'A profile of this film director says he was born in Britain in 1899 & died in Los Angeles in 1980'",
      "value": "$600",
      "answer": "Alfred Hitchcock",
      "round": "Jeopardy!",
      "show_number": "5322"
    },
    {
      "category": "DID YOU NOTICE?",
      "air_date": "1987-04-06",
      "question": "'Number of bends in a standard paper clip'",
      "value": "$600",
      "answer": "3",
      "round": "Double Jeopardy!",
      "show_number": "606"
    },
    {
      "category": "WORLD OF FOOD",
      "air_date": "2005-06-30",
      "question": "'Adobo & sinigang'",
      "value": "$2000",
      "answer": "the Philippines",
      "round": "Double Jeopardy!",
      "show_number": "4809"
    },
    {
      "category": "THE NEW YORK TIMES OBITUARIES",
      "air_date": "2001-02-23",
      "question": "'In April 1976 the Times said this billionaire died \"as mysteriously as he had lived\"'",
      "value": "$200",
      "answer": "Howard Hughes",
      "round": "Double Jeopardy!",
      "show_number": "3800"
    },
    {
      "category": "\"ROOM\"",
      "air_date": "2009-10-19",
      "question": "'Starting in this office area is a proverbial entry point for many in Hollywood'",
      "value": "$600",
      "answer": "the mailroom",
      "round": "Jeopardy!",
      "show_number": "5771"
    },
    {
      "category": "FIRST LADIES",
      "air_date": "1997-04-07",
      "question": "'She called her autobiography \"First Lady from Plains\"'",
      "value": "$200",
      "answer": "Rosalynn Carter",
      "round": "Double Jeopardy!",
      "show_number": "2911"
    },
    {
      "category": "SOUNDTRACKS BY SONGS",
      "air_date": "1999-10-27",
      "question": "'1988:\"Kokomo\"'",
      "value": "$1000",
      "answer": "Cocktail",
      "round": "Double Jeopardy!",
      "show_number": "3483"
    },
    {
      "category": "THEIR FIRST FEATURE FILMS",
      "air_date": "2005-10-19",
      "question": "'Falling off a chair at her audition helped her win the role of the klutzy princess in \"The Princess Diaries\"'",
      "value": "$600",
      "answer": "(Anne) Hathaway",
      "round": "Jeopardy!",
      "show_number": "4853"
    },
    {
      "category": "SCIENCE GUYS",
      "air_date": "2002-06-05",
      "question": "'He's the \"Science Guy\" seen here'",
      "value": "$200",
      "answer": "Bill Nye",
      "round": "Jeopardy!",
      "show_number": "4103"
    },
    {
      "category": "ACADEMIC DEGREES",
      "air_date": "2010-11-19",
      "question": "'If you're into acting or photography, you may want a B.F.A., which stands for this'",
      "value": "$200",
      "answer": "Bachelor of Fine Arts",
      "round": "Jeopardy!",
      "show_number": "6025"
    },
    {
      "category": "ON BOARD GAME BOARDS",
      "air_date": "2009-06-03",
      "question": "'Millionaire Estates,Pay Day!'",
      "value": "$1000",
      "answer": "Life",
      "round": "Jeopardy!",
      "show_number": "5708"
    },
    {
      "category": "OREGONE",
      "air_date": "2000-06-14",
      "question": "'A grand hotel on what's now this city's Pioneer Courthouse Square became a parking lot in the '50s'",
      "value": "$400",
      "answer": "Portland",
      "round": "Double Jeopardy!",
      "show_number": "3648"
    },
    {
      "category": "THE BIBLE",
      "air_date": "1990-01-29",
      "question": "'This gospel writer was a tax collector at Capernaum when Jesus 1st met him'",
      "value": "$700",
      "answer": "Matthew",
      "round": "Jeopardy!",
      "show_number": "1251"
    },
    {
      "category": "SUPERSTITIONS",
      "air_date": "1999-11-24",
      "question": "'It's said if these itch, you're about to get a kiss, so pucker up!'",
      "value": "$200",
      "answer": "Lips",
      "round": "Jeopardy!",
      "show_number": "3503"
    },
    {
      "category": "WORLD HISTORY",
      "air_date": "1989-11-03",
      "question": "'The 1st great building of the Acropolis was this one built between 447-438 B.C.'",
      "value": "$400",
      "answer": "The Parthenon",
      "round": "Jeopardy!",
      "show_number": "1190"
    },
    {
      "category": "CITIES BY HOTEL",
      "air_date": "2001-05-29",
      "question": "'The Fairmont, after which James Brolin's TV \"Hotel\" was modeled'",
      "value": "$400",
      "answer": "San Francisco",
      "round": "Jeopardy!",
      "show_number": "3867"
    },
    {
      "category": "FAN TOM",
      "air_date": "2005-04-19",
      "question": "'Since childhood, this author of \"I Am Charlotte Simmons\" has been a huge fan of a book called \"Honey Bear\"'",
      "value": "$600",
      "answer": "(Tom) Wolfe",
      "round": "Jeopardy!",
      "show_number": "4757"
    },
    {
      "category": "PRESIDENTIAL FINAL MOMENTS",
      "air_date": "2001-09-10",
      "question": "'The end finally came for this Pres. in Elberon, New Jersey from blood posioning after being shot'",
      "value": "$800",
      "answer": "Garfield",
      "round": "Double Jeopardy!",
      "show_number": "3911"
    },
    {
      "category": "\"CEL\"EBRITY WORDS",
      "air_date": "2010-04-16",
      "question": "'The basement, or last place in the standings of a sports league'",
      "value": "$400",
      "answer": "the cellar",
      "round": "Double Jeopardy!",
      "show_number": "5900"
    },
    {
      "category": "FUNNY MEN",
      "air_date": "1999-07-20",
      "question": "'This onetime Vaudevillian & star of \"Modern Times\" was knighted in 1975'",
      "value": "$800",
      "answer": "Charlie Chaplin",
      "round": "Double Jeopardy!",
      "show_number": "3442"
    },
    {
      "category": "U.S. GEOGRAPHY",
      "air_date": "1997-06-12",
      "question": "'This river that winds through Wyoming, Idaho & Oregon is the main tributary of the Columbia River'",
      "value": "$300",
      "answer": "Snake River",
      "round": "Jeopardy!",
      "show_number": "2959"
    },
    {
      "category": "ALMOST ASSASSINATED",
      "air_date": "2005-10-25",
      "question": "'September 5, 1975 while greeting a crowd in Sacramento, California'",
      "value": "$1200",
      "answer": "Ford",
      "round": "Double Jeopardy!",
      "show_number": "4857"
    },
    {
      "category": "LITERATURE",
      "air_date": "1996-01-12",
      "question": "'It begins, \"In the ancient city of London....A boy was born to a poor family of the name of Canty....\"'",
      "value": "$1,000",
      "answer": "\"The Prince And The Pauper\"",
      "round": "Double Jeopardy!",
      "show_number": "2620"
    },
    {
      "category": "YUCATAN LINES",
      "air_date": "2004-09-15",
      "question": "'Cancun is a popular spot for this \"seasonal\" trip, as in the 2003 film \"The Real Cancun\"'",
      "value": "$400",
      "answer": "spring break",
      "round": "Double Jeopardy!",
      "show_number": "4603"
    },
    {
      "category": "MUSICAL WORDS",
      "air_date": "2010-03-26",
      "question": "'(Kelly of the Clue Crew performs a science experiment.)  Electricity will only light the fluorescent bulb to where I put my hand, because like copper or an orchestra leader, my body is acting as this'",
      "value": "$800",
      "answer": "a conductor",
      "round": "Jeopardy!",
      "show_number": "5885"
    },
    {
      "category": "CLASSY CLASSICAL CLASSICS",
      "air_date": "2006-05-23",
      "question": "'You're \"rite\" on the money if you know the controversial music heard here is by this composer'",
      "value": "$600",
      "answer": "Stravinsky",
      "round": "Jeopardy!",
      "show_number": "5007"
    },
    {
      "category": "RECONSTRUCTION",
      "air_date": "2007-03-01",
      "question": "'The Freedman's Bureau aided in establishing black colleges, including this Washington, D.C. school'",
      "value": "$600",
      "answer": "Howard",
      "round": "Jeopardy!",
      "show_number": "5179"
    },
    {
      "category": "1898",
      "air_date": "1998-07-08",
      "question": "'In 1898, he turned in \"The Turn of the Screw\" to his publisher'",
      "value": "$400",
      "answer": "Henry James",
      "round": "Jeopardy!",
      "show_number": "3208"
    },
    {
      "category": "FAMOUS NAMES",
      "air_date": "2007-11-22",
      "question": "'In the 19th century he created a new type of reference work, a dictionary named from the Greek word for \"treasury\"'",
      "value": None,
      "answer": "Roget",
      "round": "Final Jeopardy!",
      "show_number": "5339"
    },
    {
      "category": "\"CUS\" WORDS",
      "air_date": "2000-11-28",
      "question": "'Notable early bloomers seen here:'",
      "value": "$500",
      "answer": "Crocuses",
      "round": "Jeopardy!",
      "show_number": "3737"
    },
    {
      "category": "FRENCH NOVELISTS",
      "air_date": "2010-11-19",
      "question": "'This Guy, a master of the short story, also wrote 6 novels, including \"Bel-Ami\" & \"Pierre et Jean\"'",
      "value": "$1600",
      "answer": "Guy de Maupassant",
      "round": "Double Jeopardy!",
      "show_number": "6025"
    },
    {
      "category": "MUSIC & LITERATURE",
      "air_date": "1998-10-13",
      "question": "'This \"Messiah\" composer set Dryden's poem \"Ode For St. Cecilia's Day\" to music'",
      "value": "$200",
      "answer": "George F. Handel",
      "round": "Jeopardy!",
      "show_number": "3242"
    },
    {
      "category": "AIRPORTS",
      "air_date": "2007-01-08",
      "question": "'Poland's largest airport is located in Warsaw & named for this composer'",
      "value": "$1000",
      "answer": "Chopin",
      "round": "Jeopardy!",
      "show_number": "5141"
    },
    {
      "category": "4X4",
      "air_date": "2004-10-13",
      "question": "'Take an archaic version of a second person pronoun & add beach grains to make this number'",
      "value": "$200",
      "answer": "thousand",
      "round": "Jeopardy!",
      "show_number": "4623"
    },
    {
      "category": "PAUNCH SHOPS",
      "air_date": "2010-07-02",
      "question": "'Hit a Grand Slam Slugger with hash browns at one of these restaurants & you've knocked in 85% of your RDV of fat'",
      "value": "$800",
      "answer": "Denny\\'s",
      "round": "Jeopardy!",
      "show_number": "5955"
    },
    {
      "category": "CONTINENTAL DRIFTING",
      "air_date": "2007-07-10",
      "question": "'(Jon of the Clue Crew stands in front of an ancient globe) Meaning \"all earth\", it's the term Alfred Wegener gave to an historic, theoretical supercontinent'",
      "value": "$1600",
      "answer": "Pangaea",
      "round": "Double Jeopardy!",
      "show_number": "5272"
    },
    {
      "category": "COLLEGE ATHLETICS",
      "air_date": "1998-05-08",
      "question": "'From 1962 through 1997, this North Carolina men's basketball coach had an NCAA record 879 wins'",
      "value": "$400",
      "answer": "Dean Smith",
      "round": "Jeopardy!",
      "show_number": "3165"
    },
    {
      "category": "MOVIE TITLE PAIRS",
      "air_date": "2005-07-08",
      "question": "'1973:Kris Kristofferson'",
      "value": "$800",
      "answer": "Pat Garrett and Billy the Kid",
      "round": "Double Jeopardy!",
      "show_number": "4815"
    },
    {
      "category": "\"CEL\"EBRITY WORDS",
      "air_date": "2010-04-16",
      "question": "'This clear wrap used to package food was developed from a failed attempt to invent stain-proof tablecloths'",
      "value": "$1200",
      "answer": "cellophane",
      "round": "Double Jeopardy!",
      "show_number": "5900"
    },
    {
      "category": "DISNEY FILMS BY SONGS",
      "air_date": "1999-04-22",
      "question": "'\"Spoonful of Sugar\" & \"Chim-Chim-Cheree\"'",
      "value": "$200",
      "answer": "Mary Poppins",
      "round": "Jeopardy!",
      "show_number": "3379"
    },
    {
      "category": "U.S. CRIME STATISTICS",
      "air_date": "1998-09-23",
      "question": "'Of 1 in 20, 1 in 50 or 1 in 100, the average number of people who will serve time in their lifetime'",
      "value": "$300",
      "answer": "1 in 20",
      "round": "Jeopardy!",
      "show_number": "3228"
    },
    {
      "category": "ON- & OFF-SCREEN ROMANCES",
      "air_date": "1998-03-13",
      "question": "'Yves Montand & this blond sex symbol took the title of their 1960 film \"Let's Make Love\" literally'",
      "value": "$500",
      "answer": "Marilyn Monroe",
      "round": "Jeopardy!",
      "show_number": "3125"
    },
    {
      "category": "THE CIVIL WAR",
      "air_date": "1992-10-13",
      "question": "'This famous Mary's diary, published in 1905, gives an inside view of Confederate leaders'",
      "value": "$1000",
      "answer": "Mary Chestnut",
      "round": "Double Jeopardy!",
      "show_number": "1862"
    },
    {
      "category": "CARMEN",
      "air_date": "2002-03-11",
      "question": "'In Act II the handsome Escamillo enters to the \"song\" named for these bullfighters'",
      "value": "$1600",
      "answer": "the toreadors",
      "round": "Double Jeopardy!",
      "show_number": "4041"
    },
    {
      "category": "SCREEN SIRENS",
      "air_date": "1999-06-22",
      "question": "'She debuted in 1957's \"A Face in the Crowd\" & is seen here 2 years later in \"Anatomy of a Murder\"'",
      "value": "$800",
      "answer": "Lee Remick",
      "round": "Double Jeopardy!",
      "show_number": "3422"
    },
    {
      "category": "TEENS IN LITERATURE",
      "air_date": "1999-02-25",
      "question": "'When this Jane Austen novel begins, Elinor Dashwood, the eldest daughter, is \"only nineteen\"'",
      "value": "$400",
      "answer": "\"Sense and Sensibility\"",
      "round": "Jeopardy!",
      "show_number": "3339"
    },
    {
      "category": "MATHEMATICIANS",
      "air_date": "2002-09-04",
      "question": "'He discovered the law of universal gravitation as well as a new way to calculate curves'",
      "value": "$400",
      "answer": "Newton",
      "round": "Double Jeopardy!",
      "show_number": "4138"
    },
    {
      "category": "FUN WITH OPERA",
      "air_date": "2008-09-29",
      "question": "'Composer Mario Castelnuovo-Tedesco went \"Wilde\" & turned this Oscar Wilde play into a 1962 opera'",
      "value": "$600",
      "answer": "The Importance of Being Earnest",
      "round": "Jeopardy!",
      "show_number": "5531"
    },
    {
      "category": "ADAPTATIONS",
      "air_date": "1998-06-12",
      "question": "'This Bogart-Bergman film is better remembered than its source, the play \"Everybody Comes to Rick's\"'",
      "value": "$400",
      "answer": "Casablanca",
      "round": "Double Jeopardy!",
      "show_number": "3190"
    },
    {
      "category": "CHRONICLES",
      "air_date": "1999-10-06",
      "question": "'Livy's \"Ab Urbe Condita\", or \"History From the Founding of the City\", is about this city'",
      "value": "$400",
      "answer": "Rome",
      "round": "Jeopardy!",
      "show_number": "3468"
    },
    {
      "category": "STRUCTURES",
      "air_date": "2005-12-05",
      "question": "'The U.S. Air Force Museum's Cold War gallery is, appropriately, in a 200,000-square-foot one of these'",
      "value": "$800",
      "answer": "a hangar",
      "round": "Double Jeopardy!",
      "show_number": "4886"
    },
    {
      "category": "SONGS FROM MUSICALS",
      "air_date": "2002-09-02",
      "question": "'\"I Hope I Get It\"'",
      "value": "$2000",
      "answer": "A Chorus Line",
      "round": "Double Jeopardy!",
      "show_number": "4136"
    },
    {
      "category": "BETTER KNOWN AS...",
      "air_date": "1999-01-18",
      "question": "'Movie star Walter Matuschanskayasky'",
      "value": "$200",
      "answer": "Walter Matthau",
      "round": "Jeopardy!",
      "show_number": "3311"
    },
    {
      "category": "CINCO DE MAYO",
      "air_date": "2011-06-17",
      "question": "'The name of this fried-fish-friendly mayo-based sauce containing capers & pickles is likely derived from a word for \"hell\"'",
      "value": "$1200",
      "answer": "tartar sauce",
      "round": "Double Jeopardy!",
      "show_number": "6175"
    },
    {
      "category": "\"B\" PLUS",
      "air_date": "2008-05-23",
      "question": "'The alpha factor measures a stock's own volatility; this Greek letter compares it to the entire market'",
      "value": "$200",
      "answer": "beta",
      "round": "Jeopardy!",
      "show_number": "5470"
    },
    {
      "category": "TV STARS",
      "air_date": "2000-12-11",
      "question": "'John Lithgow appeared as a Broadway director in this autobiographical Bob Fosse film'",
      "value": "$1000",
      "answer": "All That Jazz",
      "round": "Double Jeopardy!",
      "show_number": "3746"
    },
    {
      "category": "1994",
      "air_date": "1995-07-05",
      "question": "'Los Angeles was hit by a major one January 17'",
      "value": "$100",
      "answer": "an earthquake",
      "round": "Jeopardy!",
      "show_number": "2513"
    },
    {
      "category": "STATE OF THE UNION",
      "air_date": "2012-01-10",
      "question": "'This union state's 6th regiment was nicknamed the Minutemen; its 20th was the Harvard regiment'",
      "value": "$200",
      "answer": "Massachusetts",
      "round": "Jeopardy!",
      "show_number": "6287"
    },
    {
      "category": "QUOTATIONS",
      "air_date": "2000-10-03",
      "question": "'This talk show host said, \"I admire, respect & adore authors\" when she was honored for her book club'",
      "value": "$600",
      "answer": "Oprah",
      "round": "Double Jeopardy!",
      "show_number": "3697"
    },
    {
      "category": "ISLANDS IN THE SEA",
      "air_date": "2011-03-11",
      "question": "'Nunivak'",
      "value": "$2,500",
      "answer": "the Bering Sea",
      "round": "Double Jeopardy!",
      "show_number": "6105"
    },
    {
      "category": "OFFAL FRENCH FOOD",
      "air_date": "2007-01-05",
      "question": "'In the French dish pieds et paquets, the paquets are packets of sheep's tripe & the pieds are these sheep extremities'",
      "value": "$800",
      "answer": "feet (hooves accepted)",
      "round": "Jeopardy!",
      "show_number": "5140"
    },
    {
      "category": "PRIMETIME TV",
      "air_date": "2006-01-18",
      "question": "'It was the profession of Ray Barone on the CBS sitcom \"Everybody Loves Raymond\"'",
      "value": "$2000",
      "answer": "sportswriter",
      "round": "Double Jeopardy!",
      "show_number": "4918"
    },
    {
      "category": "SHAKESPEARE'S PLAYS WITHIN PLAYS",
      "air_date": "1998-07-08",
      "question": "'While disguised as a boy, this heroine of \"As You Like It\" improvises a scene'",
      "value": "$800",
      "answer": "Rosalind",
      "round": "Double Jeopardy!",
      "show_number": "3208"
    },
    {
      "category": "MARVEL COMICS HEROES",
      "air_date": "2004-07-07",
      "question": "'\"The Incredible\"'",
      "value": "$400",
      "answer": "the Hulk",
      "round": "Double Jeopardy!",
      "show_number": "4583"
    },
    {
      "category": "FRENCH LITERATURE",
      "air_date": "2003-06-24",
      "question": "'Bored by her doctor husband, this title character has affairs with Leon Dupuis & Rodolphe Boulanger'",
      "value": "$1600",
      "answer": "Madame Bovary",
      "round": "Double Jeopardy!",
      "show_number": "4347"
    },
    {
      "category": "HOME RUN SLUGGERS",
      "air_date": "1996-11-26",
      "question": "'On July 27, 1974 in the only game he ever pitched, Dodger Rex Hudson gave up this man's 726th home run'",
      "value": "$200",
      "answer": "Hank Aaron",
      "round": "Jeopardy!",
      "show_number": "2817"
    },
    {
      "category": "A WORK OF PHILOSOPHY",
      "air_date": "2007-02-23",
      "question": "'Karl Marx was heavily influenced by this German's \"Phenomenology of Mind\"'",
      "value": "$2000",
      "answer": "Hegel",
      "round": "Double Jeopardy!",
      "show_number": "5175"
    },
    {
      "category": "OPRAH'S BOOK CLUB",
      "air_date": "2001-12-05",
      "question": "'One of Oprah's picks for 2000 was \"Daughter of Fortune\" by this Chilean author'",
      "value": "$800",
      "answer": "Isabel Allende",
      "round": "Double Jeopardy!",
      "show_number": "3973"
    },
    {
      "category": "VERB-OTEN",
      "air_date": "2001-12-10",
      "question": "'You can do it to property, to \"the show\" or to second base'",
      "value": "$600",
      "answer": "steal",
      "round": "Jeopardy!",
      "show_number": "3976"
    },
    {
      "category": "LITERARY PAIRS",
      "air_date": "2004-10-06",
      "question": "'They \"dined on mince and slices of quince which they ate with a runcible spoon\"'",
      "value": "$400",
      "answer": "the Owl & the Pussycat",
      "round": "Double Jeopardy!",
      "show_number": "4618"
    },
    {
      "category": "GRAMMAR",
      "air_date": "2006-12-25",
      "question": "'The sentence \"Harold and Kumar go to White Castle\" has a plural compound one of these'",
      "value": "$800",
      "answer": "a subject",
      "round": "Double Jeopardy!",
      "show_number": "5131"
    },
    {
      "category": "TV BARS & RESTAURANTS",
      "air_date": "1996-01-11",
      "question": "'On this sitcom you may find the Crane brothers having coffee at Cafe Nervosa'",
      "value": "$400",
      "answer": "\"Frasier\"",
      "round": "Jeopardy!",
      "show_number": "2619"
    },
    {
      "category": "GEOGRAPHY",
      "air_date": "1995-07-07",
      "question": "'A smaller canal connecting to this river brings fresh water to the Suez Canal'",
      "value": "$200",
      "answer": "the Nile",
      "round": "Double Jeopardy!",
      "show_number": "2515"
    },
    {
      "category": "ROCK & ROLL",
      "air_date": "1997-02-25",
      "question": "'Led by Sting, they disbanded after the release of \"Synchronicity\", their fifth & most successful album'",
      "value": "$200",
      "answer": "The Police",
      "round": "Jeopardy!",
      "show_number": "2882"
    },
    {
      "category": "WORD ORIGINS",
      "air_date": "1986-02-10",
      "question": "'Weapon said to have been the size of a pomegranate & filled with \"seeds\" of gunpowder'",
      "value": "$1,000",
      "answer": "a hand grenade",
      "round": "Double Jeopardy!",
      "show_number": "371"
    },
    {
      "category": "QUOTATIONS",
      "air_date": "2004-03-31",
      "question": "'In \"Bartlett's\", Daniel Webster's \"I still live\" is listed as these'",
      "value": "$800",
      "answer": "his last words",
      "round": "Double Jeopardy!",
      "show_number": "4513"
    },
    {
      "category": "POTENT POTABLES",
      "air_date": "2008-01-18",
      "question": "'In cockney rhyming slang, this liquor is a \"gay & frisky\"'",
      "value": "$800",
      "answer": "whiskey",
      "round": "Double Jeopardy!",
      "show_number": "5380"
    },
    {
      "category": "THEOLOGY",
      "air_date": "2008-11-27",
      "question": "'\"Hasidic Derashot\" is a course at JTS, this \"theological seminary\"'",
      "value": "$1200",
      "answer": "Jewish Theological Seminary",
      "round": "Double Jeopardy!",
      "show_number": "5574"
    },
    {
      "category": "NEW WORDS IN THE OED",
      "air_date": "2008-12-09",
      "question": "'A denial, in Pig Latin'",
      "value": "$800",
      "answer": "ixnay",
      "round": "Jeopardy!",
      "show_number": "5582"
    },
    {
      "category": "FOREIGN-BORN LEADERS",
      "air_date": "2008-11-04",
      "question": "'Adolf Hitler was born in this country in 1889'",
      "value": "$800",
      "answer": "Austria",
      "round": "Double Jeopardy!",
      "show_number": "5557"
    },
    {
      "category": "FILMS OF THE '80s",
      "air_date": "1997-12-22",
      "question": "'In this 1983 musical Barbra Streisand disguises herself as a boy to study the Talmud'",
      "value": "$400",
      "answer": "Yentl",
      "round": "Double Jeopardy!",
      "show_number": "3066"
    },
    {
      "category": "HOLIDAYS & OBSERVANCES",
      "air_date": "2007-04-27",
      "question": "'The half-mile route for this annual event begins at Santo Domingo Street in Pamplona'",
      "value": "$600",
      "answer": "the Running of the Bulls",
      "round": "Jeopardy!",
      "show_number": "5220"
    },
    {
      "category": "THE SOUTH",
      "air_date": "1993-02-05",
      "question": "'In 1926 the Rockefellers began restoring the historic area of this colonial capital of Virginia'",
      "value": "$400",
      "answer": "Williamsburg",
      "round": "Jeopardy!",
      "show_number": "1945"
    },
    {
      "category": "SATURDAY NIGHT LIVES",
      "air_date": "2001-06-19",
      "question": "'For 2 seasons Don Novello appeared regularly on the show as this \"Father\"'",
      "value": "$400",
      "answer": "Father Guido Sarducci",
      "round": "Jeopardy!",
      "show_number": "3882"
    },
    {
      "category": "NAMED FOR THEIR LOOKS",
      "air_date": "2009-07-14",
      "question": "'Baseball players know the infield is shaped like this gem, which gives the field its name'",
      "value": "$200",
      "answer": "a diamond",
      "round": "Jeopardy!",
      "show_number": "5737"
    },
    {
      "category": "POETS",
      "air_date": "2006-03-28",
      "question": "'The Library of Congress' 2005 exhibit on him had a section titled \"Wound Dresser in the Civil War\"'",
      "value": None,
      "answer": "Walt Whitman",
      "round": "Final Jeopardy!",
      "show_number": "4967"
    },
    {
      "category": "MISHEARD LYRICS",
      "air_date": "2002-10-17",
      "question": "'The Four Tops:\"Ain't no woman like a one-eyed goat\"'",
      "value": "$400",
      "answer": "\\'Ain\\'t No Woman (Like the One I\\'ve Got)\"",
      "round": "Jeopardy!",
      "show_number": "4169"
    },
    {
      "category": "BELIEFS",
      "air_date": "2005-07-05",
      "question": "'Think \"fast\": the name of this month in the Islamic calendar is from the Arabic for \"to be scorched\"'",
      "value": "$2,000",
      "answer": "Ramadan",
      "round": "Double Jeopardy!",
      "show_number": "4812"
    },
    {
      "category": "WELL, IT'S NOT SHAKESPEARE",
      "air_date": "2011-05-13",
      "question": "'Last name of Daphne, who is addition to novels wrote plays like \"September Tide\"'",
      "value": "$2000",
      "answer": "du Maurier",
      "round": "Double Jeopardy!",
      "show_number": "6150"
    },
    {
      "category": "\"TRIC\"s",
      "air_date": "2007-10-31",
      "question": "'One of these can be \"red light\" or \"of Columbia\"'",
      "value": "$800",
      "answer": "district",
      "round": "Jeopardy!",
      "show_number": "5323"
    },
    {
      "category": "GROUPS",
      "air_date": "2006-10-25",
      "question": "'In law, a panel is a list of this group's members--that's why they're \"impaneled\"'",
      "value": "$600",
      "answer": "a jury",
      "round": "Jeopardy!",
      "show_number": "5088"
    },
    {
      "category": "RHYME TIME",
      "air_date": "1999-09-13",
      "question": "'Seat you sit on in a Parisian park'",
      "value": "$600",
      "answer": "French bench",
      "round": "Double Jeopardy!",
      "show_number": "3451"
    },
    {
      "category": "BRUTUS",
      "air_date": "2007-09-25",
      "question": "'During the Roman Civil War, Brutus sided with this man but was later pardoned by Julius Caesar--Oops!'",
      "value": "$1000",
      "answer": "Pompey",
      "round": "Jeopardy!",
      "show_number": "5297"
    },
    {
      "category": "MIDWEST CITIES",
      "air_date": "1998-09-29",
      "question": "'A copy of the Gettysburg Address is displayed in this city's old state capital building'",
      "value": "$300",
      "answer": "Springfield, Illinois",
      "round": "Double Jeopardy!",
      "show_number": "3232"
    },
    {
      "category": "ANAGRAMMED STATE CAPITALS",
      "air_date": "1999-05-26",
      "question": "'Males'",
      "value": "$200",
      "answer": "Salem",
      "round": "Jeopardy!",
      "show_number": "3403"
    },
    {
      "category": "WISH SUPERSTITIONS",
      "air_date": "1993-12-22",
      "question": "'\"I wish I may, I wish I might, have the wish I wish tonight\" is said upon seeing one of these'",
      "value": "$300",
      "answer": "a star",
      "round": "Jeopardy!",
      "show_number": "2143"
    },
    {
      "category": "THE PEABODY AWARDS",
      "air_date": "2007-03-13",
      "question": "'Baltimore reporter John Sherman won a Peabody for investigating pollution in this bay'",
      "value": "$1200",
      "answer": "Chesapeake Bay",
      "round": "Double Jeopardy!",
      "show_number": "5187"
    },
    {
      "category": "COOKING ON TV",
      "air_date": "1997-10-30",
      "question": "'After she cooked an omelette on a book review show, WGBH created \"The French Chef\" for her'",
      "value": "$100",
      "answer": "Julia Child",
      "round": "Jeopardy!",
      "show_number": "3029"
    },
    {
      "category": "WHAT'S NEW?",
      "air_date": "2004-06-21",
      "question": "'In 2003 Edith Grossman served up a new translation of this Cervantes work'",
      "value": "$400",
      "answer": "Don Quixote",
      "round": "Jeopardy!",
      "show_number": "4571"
    },
    {
      "category": "OCCUPATIONAL WEAR",
      "air_date": "2009-01-01",
      "question": "'This Ray-Ban style was designed for military pilots in the 1930s'",
      "value": "$400",
      "answer": "aviators",
      "round": "Jeopardy!",
      "show_number": "5599"
    },
    {
      "category": "CARIBBEAN CUISINE",
      "air_date": "2001-01-02",
      "question": "'In Aruba, you'll have fun eating funchi, a side dish made from this kind of meal'",
      "value": "$400",
      "answer": "Corn meal",
      "round": "Double Jeopardy!",
      "show_number": "3762"
    },
    {
      "category": "YOU'RE A SUPERHERO",
      "air_date": "2007-03-26",
      "question": "'This group gained their superpowers after being exposed to cosmic radiation during a space flight'",
      "value": "$800",
      "answer": "The Fantastic Four",
      "round": "Double Jeopardy!",
      "show_number": "5196"
    },
    {
      "category": "PROPHECIES & PREDICTIONS",
      "air_date": "1990-05-03",
      "question": "'Attributed to the apostle John, this prophetic work is the last book of the New Testament'",
      "value": "$400",
      "answer": "Revelation/The Apocalypse",
      "round": "Double Jeopardy!",
      "show_number": "1319"
    },
    {
      "category": "TELL ME EVERYTHING",
      "air_date": "2010-04-16",
      "question": "'Your average garden variety of this creature moves at about .03 miles per hour'",
      "value": "$200",
      "answer": "a snail",
      "round": "Jeopardy!",
      "show_number": "5900"
    },
    {
      "category": "COSMOPOLITAN",
      "air_date": "1999-04-16",
      "question": "'With over 50 independent countries, this continent has more than any other'",
      "value": "$500",
      "answer": "Africa",
      "round": "Jeopardy!",
      "show_number": "3375"
    },
    {
      "category": "OLD TESTAMENT",
      "air_date": "1989-11-08",
      "question": "'He said, “Divide the living child in two & give half to the one (mother) & half to the other”'",
      "value": "$200",
      "answer": "Solomon",
      "round": "Jeopardy!",
      "show_number": "1193"
    },
    {
      "category": "TOURNAMENT",
      "air_date": "2005-05-16",
      "question": "'Sir Lionel is killed during a tournament in this musical but is later miraculously revived'",
      "value": "$600",
      "answer": "Camelot",
      "round": "Jeopardy!",
      "show_number": "4776"
    },
    {
      "category": "WHERE DID MY MUSTACHE GO?",
      "air_date": "2001-10-01",
      "question": "'This governor wants to appeal to young punks when he gets back into pro wrestling'",
      "value": "$500",
      "answer": "Jesse Ventura",
      "round": "Jeopardy!",
      "show_number": "3926"
    },
    {
      "category": "MEDICAL TERMS",
      "air_date": "1995-09-25",
      "question": "'It's the network of nerve fibers & ganglia at the upper part of the back of the abdomen'",
      "value": "$800",
      "answer": "solar plexus",
      "round": "Double Jeopardy!",
      "show_number": "2541"
    },
    {
      "category": "THE CARS",
      "air_date": "2002-11-28",
      "question": "'I can't see the sun; this Mitsubishi is blocking it'",
      "value": "$1,000",
      "answer": "an Eclipse",
      "round": "Jeopardy!",
      "show_number": "4199"
    },
    {
      "category": "BEFORE & AFTER",
      "air_date": "2005-09-15",
      "question": "'Lady tennis legend is grouchy with the press & gets compared to an arthropod with delicious legs as...'",
      "value": "$1600",
      "answer": "Billie Jean King Crab",
      "round": "Double Jeopardy!",
      "show_number": "4829"
    },
    {
      "category": "AMERICANA",
      "air_date": "2011-07-05",
      "question": "'Woody Guthrie wrote this song that spans \"from the redwood forest to the gulf stream waters\"'",
      "value": "$1600",
      "answer": "\"This Land Is Your Land\"",
      "round": "Double Jeopardy!",
      "show_number": "6187"
    },
    {
      "category": "EXTREMELY YOUTHFUL POLITICIANS",
      "air_date": "2009-09-16",
      "question": "'We wonder if this guy seen here still has that shirt'",
      "value": "$200",
      "answer": "Obama",
      "round": "Jeopardy!",
      "show_number": "5748"
    },
    {
      "category": "AMAZING SPORTS RECORDS",
      "air_date": "2005-11-11",
      "question": "'In this key job, preparing horses, Ben Jones brought a record 6 horses to the Kentucky Derby winner's circle'",
      "value": "$2000",
      "answer": "trainer",
      "round": "Double Jeopardy!",
      "show_number": "4870"
    },
    {
      "category": "WRITTEN BY ANONYMOUS",
      "air_date": "2009-04-27",
      "question": "'The '70s novel \"Go Ask\" her is the alleged diary of a teenage girl whose life descends into drug use'",
      "value": "$400",
      "answer": "Alice",
      "round": "Double Jeopardy!",
      "show_number": "5681"
    },
    {
      "category": "BLESSED ARE THE PEACEMAKERS",
      "air_date": "1998-03-23",
      "question": "'At his 1969 inaugural he said, \"The greatest honor history can bestow is the title of peacemaker\"'",
      "value": "$600",
      "answer": "Richard Nixon",
      "round": "Double Jeopardy!",
      "show_number": "3131"
    },
    {
      "category": "CHINA TOWNS",
      "air_date": "1998-12-11",
      "question": "'The city of Dali is famous not for surrealist art, but for these Buddhist temple structures'",
      "value": "$200",
      "answer": "Pagodas",
      "round": "Jeopardy!",
      "show_number": "3285"
    },
    {
      "category": "NICKEL & DIMED",
      "air_date": "2012-01-05",
      "question": "'The Buffalo head nickel was also called this type; John Big Tree was a model for it'",
      "value": "$800",
      "answer": "an Indian nickel",
      "round": "Double Jeopardy!",
      "show_number": "6284"
    },
    {
      "category": "MY BOD",
      "air_date": "2000-02-09",
      "question": "'Descartes called this gland \"the seat of the rational soul\"; scientists still aren't sure what it does'",
      "value": "$800",
      "answer": "Pineal gland",
      "round": "Double Jeopardy!",
      "show_number": "3558"
    },
    {
      "category": "EDIBLE RHYME TIME",
      "air_date": "2005-01-06",
      "question": "'A Scottish cap made from Hormel's \"spiced ham\"'",
      "value": "$1000",
      "answer": "a Spam tam",
      "round": "Jeopardy!",
      "show_number": "4684"
    },
    {
      "category": "18th CENTURY SCIENTISTS",
      "air_date": "2009-02-26",
      "question": "'This N. European said his grave-stone should be inscribed Princeps botanicorum, \"prince of botanists\"'",
      "value": None,
      "answer": "Carolus Linnaeus",
      "round": "Final Jeopardy!",
      "show_number": "5639"
    },
    {
      "category": "ANATOMY",
      "air_date": "1990-03-08",
      "question": "'The only mobile bone of the face'",
      "value": "$200",
      "answer": "Mandible",
      "round": "Double Jeopardy!",
      "show_number": "1279"
    },
    {
      "category": "OLYMPIC MASCOTS",
      "air_date": "1999-03-31",
      "question": "'One of the symbols used at the 1968 games in this city was a red jaguar'",
      "value": "$800",
      "answer": "Mexico City",
      "round": "Double Jeopardy!",
      "show_number": "3363"
    },
    {
      "category": "ONLINE INSULTS",
      "air_date": "2007-07-26",
      "question": "'Provoking people in an online forum could get you this moniker, like the nemesis of the Billy Goats Gruff'",
      "value": "$1200",
      "answer": "troll",
      "round": "Double Jeopardy!",
      "show_number": "5284"
    },
    {
      "category": "OPERA WOMEN",
      "air_date": "2009-01-26",
      "question": "'This title character is actually the daughter of King Amonasro of Ethiopia'",
      "value": "$400",
      "answer": "Aida",
      "round": "Double Jeopardy!",
      "show_number": "5616"
    },
    {
      "category": "\"J\" WALKING",
      "air_date": "2001-11-06",
      "question": "'(Sofia of the Clue Crew rides a carousel at the Santa Monica Pier.)  In the 1600s an early type of carousel was used to train noblemen in this sport that uses lances'",
      "value": "$500",
      "answer": "jousting",
      "round": "Jeopardy!",
      "show_number": "3952"
    },
    {
      "category": "THEY PICKED UP THE CHEKHOV",
      "air_date": "2006-07-26",
      "question": "'This playwright adapted several Chekhov stories for his play \"The Good Doctor\" (Hint: Marsha Mason was in it)'",
      "value": "$400",
      "answer": "Neil Simon",
      "round": "Double Jeopardy!",
      "show_number": "5053"
    },
    {
      "category": "COUNTRY SINGERS WHO ACT",
      "air_date": "2003-03-27",
      "question": "'This blonde trained Sylvester Stallone to be a country singer in \"Rhinestone\"'",
      "value": "$200",
      "answer": "Dolly Parton",
      "round": "Jeopardy!",
      "show_number": "4284"
    },
    {
      "category": "KIDDY LIT",
      "air_date": "2008-03-10",
      "question": "'In this poem, the hero is instructed to shun the frumious Bandersnatch'",
      "value": "$400",
      "answer": "Jabberwocky",
      "round": "Jeopardy!",
      "show_number": "5416"
    },
    {
      "category": "ZOOLOGY",
      "air_date": "2000-04-21",
      "question": "'Rodents native to this continent include the cavy, coypu & capybara'",
      "value": "$200",
      "answer": "South America",
      "round": "Jeopardy!",
      "show_number": "3610"
    },
    {
      "category": "AUTHOR'S MAIDEN NAMES",
      "air_date": "2005-06-27",
      "question": "'Laura Wilder'",
      "value": "$800",
      "answer": "Ingalls",
      "round": "Double Jeopardy!",
      "show_number": "4806"
    },
    {
      "category": "BACKWORDS",
      "air_date": "2005-05-12",
      "question": "'Liam likes to sort this'",
      "value": "$400",
      "answer": "mail (Liam)",
      "round": "Jeopardy!",
      "show_number": "4774"
    },
    {
      "category": "THE LUCK OF THE \"IRISH\"",
      "air_date": "1999-03-17",
      "question": "'Fine examples of this include Tullamore Dew, Old Bushmills & Jameson Distillery Reserve'",
      "value": "$200",
      "answer": "Irish whiskey",
      "round": "Jeopardy!",
      "show_number": "3353"
    },
    {
      "category": "YOU DESERVE A SHOWBIZ AWARD!",
      "air_date": "2005-06-06",
      "question": "'Starting in 1972, the ACT awards were handed out for achievement in television aimed at this demographic'",
      "value": "$1200",
      "answer": "children",
      "round": "Double Jeopardy!",
      "show_number": "4791"
    },
    {
      "category": "MAN IN SPACE",
      "air_date": "1988-01-15",
      "question": "'Halley's Comet was met in 1986 by this country's Suisei & Sakigake spacecrafts'",
      "value": "$200",
      "answer": "Japan",
      "round": "Double Jeopardy!",
      "show_number": "780"
    },
    {
      "category": "LADIES' DAY",
      "air_date": "2007-10-23",
      "question": "'Rina Messenger, Miss Universe of 1976, saw service in this country's army'",
      "value": "$2000",
      "answer": "Israel",
      "round": "Double Jeopardy!",
      "show_number": "5317"
    },
    {
      "category": "HONEST AL TREBEK'S USED CARS",
      "air_date": "2006-03-15",
      "question": "'Never mind this carmaker's Jetta--I see you top down, stone cold chillin' in its model called the Thing'",
      "value": "$600",
      "answer": "Volkswagen",
      "round": "Jeopardy!",
      "show_number": "4958"
    },
    {
      "category": "LET'S GRAB SOME SEAFOOD",
      "air_date": "2006-07-04",
      "question": "'The rock type of this is easily distinguishable from the Maine; all 10 of its legs are about the same size'",
      "value": "$200",
      "answer": "a lobster",
      "round": "Jeopardy!",
      "show_number": "5037"
    },
    {
      "category": "CAVING",
      "air_date": "1997-03-10",
      "question": "'Cavers use special dyes to track the flow of these'",
      "value": "$200",
      "answer": "(Underground) Rivers",
      "round": "Jeopardy!",
      "show_number": "2891"
    },
    {
      "category": "SOLD!",
      "air_date": "2010-02-02",
      "question": "'I give you a goat, you rethatch my hut & we're using this 6-letter \"system\"'",
      "value": "$600",
      "answer": "barter",
      "round": "Jeopardy!",
      "show_number": "5847"
    },
    {
      "category": "MARLIN",
      "air_date": "2006-12-29",
      "question": "'Marlin Firearms of North Haven, Connecticut manufactures these in 12 & 20 gauge varieties'",
      "value": "$200",
      "answer": "shotguns",
      "round": "Jeopardy!",
      "show_number": "5135"
    },
    {
      "category": "LITERARY ISLAND HOPPING",
      "air_date": "2010-12-10",
      "question": "'Amity is a city, not an island, in this Peter Benchley thriller; it is on Long Island, however'",
      "value": "$400",
      "answer": "Jaws",
      "round": "Double Jeopardy!",
      "show_number": "6040"
    },
    {
      "category": "COLLEGE ATHLETICS",
      "air_date": "2008-12-09",
      "question": "'Northwestern University's women have won 4 consecutive championships in this sport, Canada's national summer sport'",
      "value": "$1000",
      "answer": "lacrosse",
      "round": "Jeopardy!",
      "show_number": "5582"
    },
    {
      "category": "ACTRESSES",
      "air_date": "1998-02-25",
      "question": "'Her first name honors the playwriting partner of Russel Crouse, her father'",
      "value": "$400",
      "answer": "Lindsey Crouse",
      "round": "Double Jeopardy!",
      "show_number": "3113"
    },
    {
      "category": "THE HISTORY CHANNEL",
      "air_date": "2004-01-07",
      "question": "'The name of these people was later applied to German soldiers'",
      "value": "$400",
      "answer": "the Huns",
      "round": "Double Jeopardy!",
      "show_number": "4453"
    },
    {
      "category": "3-NAMED CELEBRITIES",
      "air_date": "2000-12-13",
      "question": "'In the 1995 movie \"Nixon\", this \"Frasier\" co-star played John Dean'",
      "value": "$100",
      "answer": "David Hyde Pierce",
      "round": "Jeopardy!",
      "show_number": "3748"
    },
    {
      "category": "FOOD AKA",
      "air_date": "2010-03-08",
      "question": "'Checkerberry is also called mountain this, the beverage it's often boiled to make'",
      "value": "$400",
      "answer": "tea",
      "round": "Jeopardy!",
      "show_number": "5871"
    },
    {
      "category": "THE MUSES",
      "air_date": "2010-11-09",
      "question": "'Melpomene is the muse of tragedy & her sister Thalia, of this'",
      "value": "$400",
      "answer": "comedy",
      "round": "Double Jeopardy!",
      "show_number": "6017"
    },
    {
      "category": "THE MIDWEST",
      "air_date": "1990-04-18",
      "question": "'Minnesota city that's home to the world famous Mayo Clinic'",
      "value": "$400",
      "answer": "Rochester",
      "round": "Jeopardy!",
      "show_number": "1308"
    },
    {
      "category": "HISTORIC NAMES",
      "air_date": "1997-04-02",
      "question": "'While serving as New York governor, this first chief justice signed a bill ending slavery in that state'",
      "value": "$600",
      "answer": "John Jay",
      "round": "Double Jeopardy!",
      "show_number": "2908"
    },
    {
      "category": "SIDESHOW CINEMA",
      "air_date": "2005-04-29",
      "question": "'This 1960 Disney flick starring Kevin Corcoran in the title role was subtitled \"Or Ten Weeks with a Circus\"'",
      "value": "$2000",
      "answer": "Toby Tyler",
      "round": "Double Jeopardy!",
      "show_number": "4765"
    },
    {
      "category": "AIRLINES",
      "air_date": "2007-03-21",
      "question": "'It's the airline whose familiar logo is seen here'",
      "value": "$600",
      "answer": "Alaska Airlines",
      "round": "Jeopardy!",
      "show_number": "5193"
    },
    {
      "category": "WE'RE WORLD CHAMPS",
      "air_date": "2001-03-22",
      "question": "'Lasse Kjus,Alberto Tomba'",
      "value": "$1000",
      "answer": "skiing",
      "round": "Double Jeopardy!",
      "show_number": "3819"
    },
    {
      "category": "CAR TUNES",
      "air_date": "2003-04-18",
      "question": "'In 1984 Sammy Hagar sang, \"Write me up a 125, post my face wanted dead or alive...I can't drive\" this speed'",
      "value": "$200",
      "answer": "55",
      "round": "Jeopardy!",
      "show_number": "4300"
    },
    {
      "category": "SPELLING",
      "air_date": "2005-10-12",
      "question": "'Put your thoughts in order as you spell...'",
      "value": "$2000",
      "answer": "C-H-R-O-N-O-L-O-G-I-C-A-L",
      "round": "Double Jeopardy!",
      "show_number": "4848"
    },
    {
      "category": "ON THE MENU",
      "air_date": "2008-10-08",
      "question": "'An Outback appetizer:Bloomin' this'",
      "value": "$800",
      "answer": "Onions",
      "round": "Jeopardy!",
      "show_number": "5538"
    },
    {
      "category": "AGRIBUSINESS",
      "air_date": "2008-10-13",
      "question": "'In 1966 Robert Mondavi started the first major winery in this valley since Prohibition'",
      "value": "$400",
      "answer": "the Napa Valley",
      "round": "Jeopardy!",
      "show_number": "5541"
    },
    {
      "category": "MOVIE PHONE",
      "air_date": "2004-04-19",
      "question": "'She played squeaky clean Jan, who shared a party line with playboy Rock Hudson in \"Pillow Talk\"'",
      "value": "$400",
      "answer": "Doris Day",
      "round": "Jeopardy!",
      "show_number": "4526"
    },
    {
      "category": "HOLD THE MAYO CLINIC",
      "air_date": "2001-07-11",
      "question": "'In 1950 Mayo doctors Edward Kendall & Philip Hench won the Nobel Prize for their work with this steroid'",
      "value": "$600",
      "answer": "Cortizone",
      "round": "Double Jeopardy!",
      "show_number": "3898"
    },
    {
      "category": "THE \"C\"ROSSWORD PUZZLE",
      "air_date": "2005-03-15",
      "question": "'Used in atomic clocks, it melts at 83.3 degrees F.(6)'",
      "value": "$1000",
      "answer": "cesium",
      "round": "Jeopardy!",
      "show_number": "4732"
    },
    {
      "category": "HARRIET",
      "air_date": "2008-04-11",
      "question": "'Since he was unmarried, his niece Harriet Lane acted as his First Lady'",
      "value": "$1600",
      "answer": "Buchanan",
      "round": "Double Jeopardy!",
      "show_number": "5440"
    },
    {
      "category": "TEENS IN HISTORY",
      "air_date": "1999-11-12",
      "question": "'This \"Good King\" of Christmas carol fame was a teenage ruler of Bohemia'",
      "value": "$600",
      "answer": "Wenceslas",
      "round": "Double Jeopardy!",
      "show_number": "3495"
    },
    {
      "category": "COUNTRIES IN FRENCH",
      "air_date": "2005-02-28",
      "question": "'La Coree du Nord'",
      "value": "$600",
      "answer": "North Korea",
      "round": "Jeopardy!",
      "show_number": "4721"
    },
    {
      "category": "THEY PLAYED JESSE JAMES",
      "air_date": "2004-06-22",
      "question": "'This co-star of 2003's \"Open Range\" played Jesse in a 1972 film'",
      "value": "$2000",
      "answer": "(Robert) Duvall",
      "round": "Double Jeopardy!",
      "show_number": "4572"
    },
    {
      "category": "TECHNOLOGY",
      "air_date": "1990-04-18",
      "question": "'The USSR lost contact with its Phobos 2 craft before it landed on Phobos, a moon of this planet'",
      "value": "$400",
      "answer": "Mars",
      "round": "Jeopardy!",
      "show_number": "1308"
    },
    {
      "category": "PEOPLE",
      "air_date": "2003-03-25",
      "question": "'In 2002 this former Clinton cabinet member ran for governor of Florida'",
      "value": "$400",
      "answer": "Janet Reno",
      "round": "Jeopardy!",
      "show_number": "4282"
    },
    {
      "category": "RECONSTRUCTION",
      "air_date": "2000-04-05",
      "question": "'The 1876 exposition celebrating this helped reconcile North & South'",
      "value": "$400",
      "answer": "Centennial",
      "round": "Double Jeopardy!",
      "show_number": "3598"
    },
    {
      "category": "SIDESHOW CINEMA",
      "air_date": "2005-04-29",
      "question": "'In \"You Can't Cheat an Honest Man\", he played circus owner Larson E. Whipsnade'",
      "value": "$800",
      "answer": "W.C. Fields",
      "round": "Double Jeopardy!",
      "show_number": "4765"
    },
    {
      "category": "GOAT-POURRI",
      "air_date": "2010-09-20",
      "question": "'Crippled beggar Sammy Smalls, who traveled in a goat cart, inspired a title character of this opera set on Catfish Row'",
      "value": "$2000",
      "answer": "Porgy and Bess",
      "round": "Double Jeopardy!",
      "show_number": "5981"
    },
    {
      "category": "WAKE UP!",
      "air_date": "2009-11-13",
      "question": "'Breakfast is only served until 9, & I know you crave this \"colorful\" dish of spuds fried & pressed into a patty'",
      "value": "$400",
      "answer": "hash browns",
      "round": "Jeopardy!",
      "show_number": "5790"
    },
    {
      "category": "BIG RIVER",
      "air_date": "1999-02-01",
      "question": "'In one theory, the name of this Pennsylvania river comes from Suckahanee, \"water\"'",
      "value": "$400",
      "answer": "Susquehanna",
      "round": "Double Jeopardy!",
      "show_number": "3321"
    },
    {
      "category": "JEWELRY",
      "air_date": "1986-02-04",
      "question": "'A gem carved in relief, or the kind of appearance Alfred Hitchcock made in his movies'",
      "value": "$400",
      "answer": "a cameo",
      "round": "Jeopardy!",
      "show_number": "367"
    },
    {
      "category": "GOOD \"BY\"",
      "air_date": "2008-01-08",
      "question": "'A secondary substance made from the manufacture of something else'",
      "value": "$800",
      "answer": "a byproduct",
      "round": "Jeopardy!",
      "show_number": "5372"
    },
    {
      "category": "CATCH HER",
      "air_date": "2008-04-14",
      "question": "'Evelyn \"Billie\" Frechette was the moll of this 1930s bank robber & recounted their lives together in a jail confession'",
      "value": "$2,000",
      "answer": "(John) Dillinger",
      "round": "Double Jeopardy!",
      "show_number": "5441"
    },
    {
      "category": "NEWSPAPER HISTORY",
      "air_date": "2011-10-26",
      "question": "'In 1896 the Dow Jones Industrial Average officially appeared in print for the first time in this newspaper'",
      "value": "$400",
      "answer": "The Wall Street Journal",
      "round": "Double Jeopardy!",
      "show_number": "6233"
    },
    {
      "category": "HELLO MOTHER",
      "air_date": "2004-11-09",
      "question": "'Proverbially, necessity is its mother'",
      "value": "$400",
      "answer": "invention",
      "round": "Double Jeopardy!",
      "show_number": "4642"
    },
    {
      "category": "HOW COME?",
      "air_date": "2001-07-03",
      "question": "'Come to the park in your sulky to participate in this type of racing, seen here'",
      "value": "$300",
      "answer": "Harness racing",
      "round": "Jeopardy!",
      "show_number": "3892"
    },
    {
      "category": "\"STOP\" & \"GO\"",
      "air_date": "2010-12-28",
      "question": "'It's called the \"peach of the tropics\"'",
      "value": "$200",
      "answer": "a mango",
      "round": "Jeopardy!",
      "show_number": "6052"
    }
  ]
}



questions=["_?  There's an app for that.","Why can't I sleep at night?","What's that smell?","I got 99 problems but _ ain't one.","Maybe she's born with it.  Maybe it's _.","What's the next Happy Meal&copy; toy?","Anthropologists have recently discovered a primitive tribe that worships _.","It's a pity that kids these days are all getting involved with _.","During Picasso's often-overlooked Brown Period, he produced hundreds of paintings of _.","Alternative medicine is now embracing the curative powers of _.","And the Academy Award for _ goes to _.","What's that sound?","What ended my last relationship?","MTV's new reality show features eight washed-up celebrities living with _.","I drink to forget _.","I'm sorry professor, but I couldn't complete my homework because of _.","What is Batman's guilty pleasure?","This is the way the world ends <br> This is the way the world ends <br> Not with a bang but with _.","What's a girl's best friend?","TSA guidelines now prohibit _ on airplanes.","_.  That's how I want to die.","For my next trick, I will pull _ out of _.","In the new Disney Channel Original Movie, Hannah Montana struggles with _ for the first time.","_ is a slippery slope that leads to _.","What does Dick Cheney prefer?","Dear Abby, I'm having some trouble with _ and would like your advice.","Instead of coal, Santa now gives the bad children _.","What's the most emo?","In 1,000 years when paper money is but a distant memory, _ will be our currency.","What's the next superhero/sidekick duo?","In M. Night Shyamalan's new movie, Bruce Willis discovers that _ had really been _ all along.","A romantic, candlelit dinner would be incomplete without _.","_.  Becha can't have just one!","White people like _.","_.  High five, bro.","Next from J.K. Rowling: Harry Potter and the Chamber of _.","BILLY MAYS HERE FOR _.","In a world ravaged by _, our only solace is _.","War!  What is it good for?","During sex, I like to think about _.","What are my parents hiding from me?","What will always get you laid?","In L.A. County Jail, word is you can trade 200 cigarettes for _.","What did I bring back from Mexico?","What don't you want to find in your Chinese food?","What will I bring back in time to convince people that I am a powerful wizard?","How am I maintaining my relationship status?","_.  It's a trap!","Coming to Broadway this season, _: The Musical.","While the United States raced the Soviet Union to the moon, the Mexican government funneled millions of pesos into research on _.","After the earthquake, Sean Penn brought _ to the people of Haiti.","Next on ESPN2, the World Series of _.","Step 1: _.  Step 2: _.  Step 3: Profit.","Rumor has it that Vladimir Putin's favorite dish is _ stuffed with _.","But before I kill you, Mr. Bond, I must show you _.","What gives me uncontrollable gas?","What do old people smell like?","The class field trip was completely ruined by _.","When Pharaoh remained unmoved, Moses called down a Plague of _.","What's my secret power?","What's there a ton of in heaven?","What would grandma find disturbing, yet oddly charming?","I never truly understood _ until I encountered _.","What did the U.S. airdrop to the children of Afghanistan?","What helps Obama unwind?","What did Vin Diesel eat for dinner?","_: good to the last drop.","Why am I sticky?","What gets better with age?","_: kid-tested, mother-approved.","What's the crustiest?","What's Teach for America using to inspire inner city students to succeed?","Studies show that lab rats navigate mazes 50% faster after being exposed to _.","Life for American Indians was forever changed when the White Man introduced them to _.","Make a haiku.","I do not know with what weapons World War III will be fought, but World War IV will be fought with _.","Why do I hurt all over?","What am I giving up for Lent?","In Michael Jackson's final moments, he thought about _.","In an attempt to reach a wider audience, the Smithsonian Museum of Natural History has opened an interactive exhibit on _.","When I am President of the United States, I will create the Department of _.","Lifetime&copy; presents _, the story of _.","When I am a billionaire, I shall erect a 50-foot statue to commemorate _.","When I was tripping on acid, _ turned into _.","That's right, I killed _.  How, you ask?  _.","What's my anti-drug?","_ + _ = _.","What never fails to liven up the party?","What's the new fad diet?","Major League Baseball has banned _ for giving players an unfair advantage.","My plan for world domination begins with _.","The CIA now interrogates enemy agents by repeatedly subjecting them to _.","Dear Sir or Madam, We regret to inform you that the Office of _ has denied your request for _","In Rome, there are whisperings that the Vatican has a secret room devoted to _.","Science will never explain _.","When all else fails, I can always masturbate to _.","I learned the hard way that you can't cheer up a grieving friend with _.","In its new tourism campaign, Detroit proudly proclaims that it has finally eliminated _.","An international tribunal has found _ guilty of _.","The socialist governments of Scandinavia have declared that access to _ is a basic human right.","In his new self-produced album, Kanye West raps over the sounds of _.","What's the gift that keeps on giving?","Next season on Man vs. Wild, Bear Grylls must survive in the depths of the Amazon with only _ and his wits.","When I pooped, what came out of my butt?","In the distant future, historians will agree that _ marked the beginning of America's decline.","In a pinch, _ can be a suitable substitute for _.","What has been making life difficult at the nudist colony?","Michael Bay's new three-hour action epic pits _ against _.","And I would have gotten away with it, too, if it hadn't been for _.","What brought the orgy to a grinding halt?","During his midlife crisis, my dad got really into _.","_ would be woefully incomplete without _.","My new favorite porn star is Joey &#34;_&#34; McGee.","Before I run for president, I must destroy all evidence of my involvement with _.","This is your captain speaking. Fasten your seatbelts and prepare for _.","In his newest and most difficult stunt, David Blaine must escape from _.","The Five Stages of Grief: denial, anger, bargaining, _, and acceptance.","My mom freaked out when she looked at my browser history and found _.com/_.","I went from _ to _, all thanks to _.","Members of New York's social elite are paying thousands of dollars just to experience _.","This month's Cosmo: &#34;Spice up your sex life by bringing _ into the bedroom.&#34;","Little Miss Muffet Sat on a tuffet, Eating her curds and _.","If God didn't want us to enjoy _, he wouldn't have given us _.","My country, 'tis of thee, sweet land of _.","After months of debate, the Occupy Wall Street General Assembly could only agree on &#34;More _!&#34;","I spent my whole life working toward _, only to have it ruined by _.","Next time on Dr. Phil: How to talk to your child about _.","Only two things in life are certain: death and _.","Everyone down on the ground! We don't want to hurt anyone. We're just here for _.","The healing process began when I joined a support group for victims of _.","The votes are in, and the new high school mascot is _.","Charades was ruined for me forever when my mom had to act out _.","Before _, all we had was _.","Tonight on 20/20: What you don't know about _ could kill you.","You haven't truly lived until you've experienced _ and _ at the same time.","D&D 4.0 isn't real D&D because of the _.","It's a D&D retroclone with _ added.","Storygames aren't RPGs because of the _.","The Slayer's Guide to _.","Worst character concept ever: _, but with _.","Alightment: Chaotic _","It's a D&D retroclone with _ added.","What made the paladin fall? _","The portal leads to the quasi-elemental plane of _.","The Temple of Elemental _.","Pathfinder is basically D&D _ Edition.","_ : The Storytelling Game.","People are wondering why Steve Jackson published GURPS _.","Linear Fighter, Quadratic _.","You start with 1d4 _ points.","Back when I was 12 and I was just starting playing D&D, the game had _.","Big Eyes, Small _.","In the grim darkness of the future there is only _.","My innovative new RPG has a stat for _.","A true gamer has no problem with _.","Elminster cast a potent _ spell and then had sex with _.","The Deck of Many _.","You are all at a tavern when _ approach you.","For the convention I cosplayed as Sailor Moon, except with _.","The worst part of Grave of the Fireflies is all the _.","In the Evangelion remake, Shinji has to deal with _.","Worst anime convention purchase ever? _.","While powering up Vegeta screamed, _!","You evaded my _ attack. Most impressive.","I downloaded a doujin where _ got into _.","The magical girl found out that the Power of Love is useless against _.","The Japanese government has spent billions of yen researching _.","In the dubbed version they changed _ into _.","_ is Best Pony.","The _ of Haruhi Suzumiya.","The new thing in Akihabara is fetish cafes where you can see girls dressed up as _.","Your drill can pierce _!","Avatar: The Last _ bender.","In the name of _ Sailor Moon will punish you!","No harem anime is complete without _.","My boyfriend's a _ now.","The _ of _ has left me in despair!","_.tumblr.com","Somehow they made a cute mascot girl out of _.","Haruko hit Naoto in the head with her bass guitar and _ came out.","After blacking out during New year's Eve, I was awoken by _.","This holiday season, Tim Allen must overcome his fear of _ to save Christmas.","Jesus is _.","Every Christmas, my uncle gets drunk and tells the story about _.","What keeps me warm during the cold, cold, winter?","On the third day of Christmas, my true love gave to me: three French hens, two turtle doves, and _.","Wake up, America. Christmas is under attack by secular liberals and their _.","We got the third rope, now where's the fourth?","Tonights main event, _ vs. _.","Tackle, Dropdown, _.","Christopher Daniels is late on his _.","Instead of booking _, they should have booked _.","Genius is 10% inspiration, 90% _.","They found _ in the dumpster behind _.","The best thing I ever got for Christmas was _.","There's no crying in _.","Mastodon! Pterodactyl! Triceratops! Sabretooth Tiger! _!","Don't eat the _.","He did _ with the _!?!","SOOOOO hot, want to touch the _.","Stop looking at me _!","I'm cuckoo for _ puffs.","Silly rabbit, _ are for kids.","Between love and madness lies _.","Instead of chess, the Grim Reaper now gambles for your soul with a game of _.","My father gave his life fighting to protect _ from _.","Why is my throat sore?","_ sparked a city-wide riot that only ended with _.","I’m very sorry Mrs. Smith, but Little Billy has tested positive for _.","Instead of beating them, Chris Brown now does _ to women.","Instead of cutting, trendy young emo girls now engage in _.","The definition of rock bottom is gambling away _.","The Mayan prophecies really heralded the coming of _ in 2012.","The next US election will be fought on the key issues of _ against _.","When I was 10 I wrote to Santa wishing for _.","Where or How I met my last signifigant other: _.","_, Never leave home without it.","_. This is my fetish.","David Icke's newest conspiracy theory states that _ caused _.","I did _ so you don't have to!","I need your clothes, your bike, and _.","In a new Cold War retro movie, the red menace tries to conquer the world through the cunning use of _.","In college, our lecturer made us write a report comparing _ to _.","In The Hangover part 3, those four guys have to deal with _, _, and _.","My zombie survival kit includes food, water, and _.","The way to a man's heart is through _.","What was the theme of my second wedding?","What's the newest Japanese craze to head West?","Everybody loves _.","I can only express myself through _.","My new porn DVD was completely ruined by the inclusion of _","My three wishes will be for _, _, and _.","The latest horrifying school shooting was inspired by _.","I got fired because of my not-so-secret obsession over _.","My new favourite sexual position is _","A successful job interview begins with a firm handshake and ends with _.","Lovin' you is easy 'cause you're _.","My life is ruled by a vicious cycle of _ and _.","The blind date was going horribly until we discovered our shared interest in _.","_. Awesome in theory, kind of a mess in practice.","I'm not like the rest of you. I'm too rich and busy for _.","In the seventh circle of Hell, sinners must endure _ for all eternity.","_: Hours of fun. Easy to use. Perfect for _!","What left this stain on my couch?","Call the law offices of Goldstein & Goldstein, because no one should have to tolerate _ in the workplace.","When you get right down to it, _ is just _.","Turns out that _-Man was neither the hero we needed nor wanted.","As part of his daily regimen, Anderson Cooper sets aside 15 minutes for _.","Money can't buy me love, but it can buy me _.","With enough time and pressure, _ will turn into _.","And what did you bring for show and tell?","During high school, I never really fit in until I found _ club.","Hey, baby, come back to my place and I'll show you _.","After months of practice with _, I think I'm finally ready for _.","To prepare for his upcoming role, Daniel Day-Lewis immersed himself in the world of _.","Finally! A service that delivers _ right to your door.","My gym teacher got fired for adding _ to the obstacle course.","Having problems with _? Try _!","As part of his contract, Prince won't perform without _ in his dressing room.","Listen, son. If you want to get involved with _, I won't stop you. Just steer clear of _.","I just met you and this is crazy, but here's _, so _ maybe","It's only _ if you get caught!","_: The Next Generation","Terminator 4: _","Disney presents _ on ice!","_. The other white meat.","A _ a day keeps the _ away.","I'm sweating like a _ at a _.","I love the smell of _ in the morning.","You're not gonna believe this, but _.","_. All the cool kids are doing it.","So I was _ in my cubicle at work, and suddenly _!","Baskin Robbins just added a 32nd flavor: _!","I can drive and ____ at the same time.","_ ain't nothin' to fuck wit'!"]

q=random.choice(questions)
if(q.find("_")==-1):
	q=q+" _"
while(q.find("_")!=-1):
	item=random.choice(jep["questions"])
	q=q.replace("_", item["answer"], 1)
print(q)
