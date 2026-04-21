# Sprint 3: Quantitative Evaluation

The Sprint 3 Quantitative Evaluation will document the measureable performance of the ClearPath AI system across 10 evaluation cases. For each case, it will present fresh rerun results comparing the baseline summary and the ADHD-focused summary using exact metrics, including compliance score, reading level, average sentence length, and average paragraph length. It will also note any ADHD rule failures and include a failure-case analysis for any summary that remains below 80% compliance after three attempts. Overall, this file is meant to provide clear, data-driven evidence that the system's ADHD-focused output is more structurally compliant and easier to read than the baseline output, while also showing where improvements may still be needed.


## Input 1: Microbiology Textbook

### Source
https://assets.openstax.org/oscms-prodcms/media/documents/Microbiology-WEB.pdf

### Original Input
Visible light consists of electromagnetic waves that behave like other waves. Hence, many of the properties of light that are relevant to microscopy can be understood in terms of light’s behavior as a wave. An important property of light waves is the wavelength, or the distance between one peak of a wave and the next peak. The height of each peak (or depth of each trough) is called the amplitude. In contrast, the frequency of the wave is the rate of vibration of the wave, or the number of wavelengths within a specified time period.


### Baseline Summary Attempt 1
Visible light is composed of electromagnetic waves that exhibit wave-like properties, which are crucial for understanding microscopy. Key characteristics of light waves include:
- **Wavelengths:** The distance between consecutive peaks of a wave.
- **Amplitude:** The height of the peaks or depth of the troughs.
- **Frequency:** The rate of vibration, indicating how many wavelngths occur in a given time period.

### Baseline Summary Attempt 2
Visible light is composed of electromagnetic waves that exhibit wave-like properties, which are crucial for understanding microscopy. Key characteristics of light waves include wavelength (the distance between consecutive peaks), amplitude (the height of peaks or depth of troughs), and frequency (the rate of vibration or number of wavelengths in a given time period).

### Baseline Summary Attempt 3
Visible light is composed of electromagnetic waves that exhibit wave-like properties, which are crucial for understanding microscopy. Key characteristics of light waves include wavelength (the distance between consecutive peaks), amplitude (the height of peaks or depth of troughs), and frequency (the rate of vibration or the number of wavelengths in a given time period).

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understanding the properties of visible light.
- Learn how light behaves as a wave.
- Identify key terms related to light waves.

**Key Concepts:**
- Light consists of electromagnetic waves.
- Wavelength is the distance between wave peaks.
- Amplitude is the height of wave peaks of depth of troughs.
- Frequency is the rate of wave vibrations.
- Light's wave properties are important for microscopy.

**Recall Questions:**
1. What is the wavelength of a light wave?
2. How does amplitude relate to light waves?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the properties of visible light.
- Learn how light behaves as a wave.
- Identify key terms related to light waves.

**Key Concepts:**
- Visible light is made of electromagnetic waves.
- Light behaves like other types of waves.
- Wavelength is the distance between wave peaks.
- Amplitude is the height of the wave peaks.
- Frequency is the rate of wave vibrations.

**Recall Questions:**
1. What is the wavelength of a light wave?
2. How does amplitude relate to light waves?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand the properties of visible light.
- Learn about light waves and their behavior.
- Identify key terms related to light waves.

**Key Concepts:**
- Visible light is made of electromagnetic waves.
- Light behaves like other types of waves.
- Wavelength is the distnace between wave peaks.
- Amplitude is the height of the wave peaks.
- Frequency is how often the wave vibrates in a time period.

**Recall Questions:**
1. What is the distance between one peak of a wave and the next called?
2. How is amplitude defined in light waves?


### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 11.2236       | 15.25               | 30.5                 | 40%              |
| 2        | 15.8959       | 26.5                | 53                   | 30%              |
| 3        | 15.9178       | 27                  | 54                   | 30%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 5.5364        | 7.5833              | 15.1667              | 100%             |
| 2        | 4.9856        | 7.5                 | 15                   | 100%             |
| 3        | 5.3317        | 8.3333              | 14.2857              | 100%             |

---

## Input Case 2: Python Textbook

### Source
https://www.kea.nu/files/textbooks/humblepy/pythoncrashcourse.pdf

### Original Input
For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True. Then, all our other tests (to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.


### Baseline Summary Attempt 1
In programming, a flag is a variable used to control the execution of a program based on certain conditions. The program runs while the flag is set to True and stops when an event changes the flag to False. This approach simplifies the overall while statement to check only the flag's status, while other conditions that may alter the flag can be managed separately within the program.

### Baseline Summary Attempt 2
In programming, a flag is a variable used to control the execution of a proram based on certain conditions. The program runs while the flag is set to True and stops when the flag is set to False due to specific events. This approach simplifies the overall while statement to a single condition--checking if the flag is True--while allowing other conditions that may change the flag's value to be organized within the program. 

### Baseline Summary Attempt 3
In programming, a flag is a variable that indicates whether a program should continue running based on certain conditions. The program operates while the flag is set to True and stops when an event changes the flag to False. Consequently, the main while loop only needs to check the flag's status, while other conditions that may alter the flag can be managed separately within the program.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand the concept of a flag in programming.
- Learn how to control program execution with a flag.
- Recognize how to organize conditions in a program.

**Key Concepts:**
- A flag is a variable that signals if a program runs.
- Programs run while the falg is True.
- The program stops when the flag is set to False.
- Only one condition checks if the flag is True.
- Other tests can determine when to change the flag.

**Recall Questions:**
1. What is the purpose of a flag in a program?
2. How does a program know when to stop running?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the concept of a flag in programming.
- Learn how to control program execution with a flag.
- Identify how to organize conditions in a program.

**Key Concepts:**
- A flag is a variable that signals if a program runs.
- The program runs while the flag is True.
- The program stops when the flag is set to False.
- Only one condition checks if the flag is True.
- Other events can change the flag's value.

**Recall Questions:**
1. What is the purpose of a flag in programming?
2. How does the flag affect programming execution?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand the concept of a flag in programming.
- Learn how to control program execution using a flag.
- Recognize how to organize conditions in a program.

**Key Concepts:**
- A flag is a variable that signals if a program runs.
- Programs cna run while the flag is True.
- The program stop swhen the flag is set to False.
- Only one conditions checks if the flag is True.
- Other conditions can be organized to set the flag to False.

**Recall Questions:**
1. What is the purposed of a flag in programming?
2. How does a program know when to stop running?


### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 10.9081       | 22.3333             | 67                   | 30%              |
| 2        | 11.8425       | 24.3333             | 73                   | 30%              |
| 3        | 11.0476       | 22                  | 66                   | 30%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 4.5009        | 9.0833              | 18.1667              | 100%             |
| 2        | 5.1917        | 8.75                | 15                   | 100%             |
| 3        | 4.9475        | 9.25                | 15.8571              | 100%             |

---

## Input Case 3: Napolean Bonaparte Biography

### Source
https://www.history.com/articles/napoleon

### Original Input
Napoleon Bonaparte (1769-1821), also known as Napoleon I, was a French military leader and emperor who conquered much of Europe in the early 19th century. Born on the island of Corsica, Napoleon rapidly rose through the ranks of the military during the French Revolution (1789-1799). After seizing political power in France in a 1799 coup d’état, he crowned himself emperor in 1804. Shrewd, ambitious and a skilled military strategist, Napoleon successfully waged war against various coalitions of European nations and expanded his empire. However, after a disastrous French invasion of Russia in 1812, Napoleon abdicated the throne two years later and was exiled to the island of Elba. In 1815, he briefly returned to power in his Hundred Days campaign. After a crushing defeat at the Battle of Waterloo, he abdicated once again and was exiled to the remote island of Saint Helena, where he died at 51.


### Baseline Summary Attempt 1
Napoleon Bonaparte (1769-1821), a French military leader and emperor, rose to prominence during the French Revolution and seized power in a 1799 coup, becoming emperor in 1804. Known for his military strategy, he expanded his empire through wars against European coalitions. However, after a failed invasion of Russia in 1812, he abdicated in 1814 and was exiled to Elba. He returned to power for a brief period in 1815 during the Hundred Days but was defeated at the Battle of Waterloo. Subsequently, he was exiled to Saint Helena, where he died at the age of 51.

### Baseline Summary Attempt 2
Napoleon Bonaparte (1769-1821), also known as Napoleon I, was a prominent French military leader and emperor who expanded his empire across much of Europe in the early 19th century. Born in Corsica, he rose through military ranks during the French Revolution and seized power in a 1799 coup, becoming emperor in 1804. Renowned for his strategic prowess, he successfully fought against various European coalitions. However, his 1812 invasion of Russia ended disastrously, leading to his abdication in 1814 and exile to Elba. He returned briefly to power in 1815 during the Hundred Days but was defeated at the Battle of Waterloo, resulting in his second abdication and exile to Saint Helena, where he died at age 51.

### Baseline Summary Attempt 3
Napoleon Bonaparte (1769-1821), also known as Napoleon I, was a significant French military leader and emperor who expanded his empire across Europe in the early 19th century. Born in Corsica, he rose through the military ranks during the French Revolution and seized power in a 1799 coup, becoming emperor in 1804. Noted for his strategic skills, he fought successfully against various European coalitions. However, his 1812 invasion of Russia was a failure, leading to his abdication in 1814 and exile to Elba. He returned to power briefly in 1815 during the Hundred Days but was defeated at the Battle of Waterloo, resulting in his second abdication and exile to Saint Helena, where he died at 51.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand Napoleon Bonaparte's rise and fall.
- Identify key events in his life.
- Recognize his impact on Europe.

**Key Concepts:**
- Napoleon was born in Corsica in 1769.
- He became a military leader during the French Revolution.
- He crowned himself emperor of France in 1804.
- His invasion of Russia in 1812 led to his downfall.
- He was exiled to Elba and then Saint Helena.

**Recall Questions:**
1. What year did Napoleon crown himself emperor?
2. Where was Napoleon exiled after his defeat at Waterloo?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand Napoleon Bonaparte's rise and fall.
- Identify key events in his life.
- Recognize his impact on Europe.

**Key Concepts:**
- Napoleon was born in Corsica in 1769.
- He became a military leader during the French Revolution.
- He crowned himself emperor of France in 1804.
- His invasion of Russia in 1812 led to his downfall.
- He was exiled to Elba and then to Saint Helena.

**Recall Questions:**
1. What year did Napoleon crown himself emperor?
2. Where was Napoleon exiled after his defeat at Waterloo?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand Napoleon Bonaparte's life and achievements.
- Recognize key events in his military career.
- Identify the impact of his leadership on Europe.

**Key Concepts:**
- Napoleon was born in Corsica in 1769.
- He became a military leader during the French Revolution.
- He seized power in a coup in 1799.
- He was crowned emperor in 1804.
- His invasion of Russia in 1812 failed.
- He was exiled twice, first to Elba and then to Saint Helena.

**Recall Questions:**
1. What year did Napoleon become emperor of France?
2. What was the outcome of Napoleon's invasion of Russia?

### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 11.8105       | 19.2                | 96                   | 20%              |
| 2        | 14.4129       | 23.4                | 117                  | 20%              |
| 3        | 14.108        | 23.2                | 116                  | 20%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 7.6168        | 7.9167              | 15.8333              | 100%             |
| 2        | 7.553         | 8                   | 16                   | 100%             |
| 3        | 7.4954        | 8.2308              | 17.8333              | 100%             |

---

## Input Case 4: Elon Musk Biography

### Source
https://www.amazon.com/Elon-Musk-Walter-Isaacson/dp/1982181281

### Original Input
When Elon Musk was a kid in South Africa, he was regularly beaten by bullies. One day a group pushed him down some concrete steps and kicked him until his face was a swollen ball of flesh. He was in the hospital for a week. But the physical scars were minor compared to the emotional ones inflicted by his father, an engineer, rogue, and charismatic fantasist. His father’s impact on his psyche would linger. He developed into a tough yet vulnerable man-child, prone to abrupt Jekyll-and-Hyde mood swings, with an exceedingly high tolerance for risk, a craving for drama, an epic sense of mission, and a maniacal intensity that was callous and at times destructive. At the beginning of 2022—after a year marked by SpaceX launching thirty-one rockets into orbit, Tesla selling a million cars, and him becoming the richest man on earth—Musk spoke ruefully about his compulsion to stir up dramas. “I need to shift my mindset away from being in crisis mode, which it has been for about fourteen years now, or arguably most of my life,” he said.

### Baseline Summary Attempt 1
Elon Musk faced severe bullying as a child in South Africa, culminating in a hospitalization after a brutal attack. The emotional scars from this experience, combined with the influence of his father—who was an engineer with a complex personality—shaped Musk into a man with a mix of toughness and vulnerability. He exhibited extreme mood swings, a high tolerance for risk, a desire for drama, and a strong sense of mission, often leading to destructive behavior. By early 2022, following significant achievements with SpaceX and Tesla, Musk acknowledged his long-standing tendency to operate in "crisis mode" and expressed a desire to change this mindset.

### Baseline Summary Attempt 2
Elon Musk experienced severe bullying as a child in South Africa, including a violent incident that left him hospitalized. The emotional scars from his father's influence, a complex figure characterized by charisma and unpredictability, significantly shaped Musk's personality. He developed a tough yet vulnerable demeanor, marked by mood swings, high risk tolerance, a craving for drama, and intense ambition, sometimes resulting in destructive behavior. By early 2022, after a successful year with SpaceX and Tesla, Musk acknowledged his tendency to live in "crisis mode" and expressed a desire to change this mindset.

### Baseline Summary Attempt 3
Elon Musk experienced significant bullying as a child in South Africa, including a severe incident that left him hospitalized. The emotional scars from his father's influence—a complex figure characterized as an engineer and charismatic fantasist—shaped Musk's personality, leading him to become a tough yet vulnerable individual with intense mood swings and a high tolerance for risk. By early 2022, following a successful year with SpaceX and Tesla, Musk acknowledged his tendency to create drama and expressed a desire to shift away from a crisis-oriented mindset that had dominated his life for many years.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand Elon Musk's childhood experiences.
- Recognize the impact of his father on his personality.
- Identify Musk's characteristics and mindset.

**Key Concepts:**
- Elon Musk faced severe bullying as a child.
- He was hospitalized after a serious attack by bullies.
- His father's influence shaped Musk's emotional state.
- Musk developed a mix of toughness and vulnerability.
- He has a high tolerance for risk and a craving for drama.

**Recall Questions:**
1. What traumatic experience did Elon Musk face as a child?
2. How did Musk describe his mindset in early 2022?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand Elon Musk's childhood experiences and their impact on his personality.
- Recognize the effects of bullying and family dynamics on mental health.
- Identify Musk's traits and behaviors shaped by his past.

**Key Concepts:**
- Elon Musk faced severe bullying as a child in South Africa.
- He suffered physical injuries but more significant emotional scars.
- His father influenced his personality, creating a complex character.
- Musk exhibits extreme mood swings and a high tolerance for risk.
- He acknowledges his tendency to create drama in his life.

**Recall Questions:**
1. What were some effects of bullying on Elon Musk's life?
2. How did Musk describe his mindset in early 2022?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand Elon Musk's childhood experiences and their effects.
- Learn about the emotional impact of bullying and family dynamics.
- Explore Musk's personality traits and mindset.

**Key Concepts:**
- Elon Musk faced severe bullying as a child in South Africa.
- He suffered physical injuries but more emotional scars from his father.
- Musk developed a complex personality with mood swings and high risk tolerance.
- His intense drive and need for drama shaped his life and career.
- In 2022, Musk recognized the need to change his crisis-driven mindset.

**Recall Questions:**
1. What were the effects of bullying on Elon Musk's life?
2. How did Musk describe his mindset in 2022?

### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 15.303        | 25.75               | 103                  | 20%              |
| 2        | 15.3126       | 23                  | 92                   | 20%              |
| 3        | 18.0699       | 31                  | 93                   | 20%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 8.0543        | 8.4167              | 16.8333              | 90%              |
| 2        | 8.6706        | 9.9167              | 19.8333              | 90%              |
| 3        | 7.5027        | 9.8333              | 19.6667              | 100%             |

---

## Input Case 5: Black Holes Book

### Source
https://assets.science.nasa.gov/content/dam/science/missions/hubble/multimedia/e-books/hubble-focus-black-holes-ebook.pdf?emrc=69de93ec1f175

### Original Input
An outstanding astronomical mystery is how the supermassive black holes that reside in galactic cores, weighing millions to billions of times the mass of the Sun, grew to such tremendous mass so quickly. Current theories propose that they began their lives in the dust-shrouded cores of vigorously star-forming “starburst” galaxies before expelling the surrounding gas and dust and emerging as extremely luminous quasars. While extremely rare, both these dusty starburst galaxies and luminous quasars have been detected in the early universe. But rapidly growing black holes in dusty, early star-forming galaxies had not been observed until now.


### Baseline Summary Attempt 1
The study addresses the mystery of how supermassive black holes, which can be millions to billions of times the mass of the Sun, grew so rapidly in galactic cores. Current theories suggest they originated in the dust-filled centers of starburst galaxies, later expelling gas and dust to become luminous quasars. Although both starburst galaxies and quasars have been identified in the early universe, this study marks the first observation of rapidly growing black holes within these dusty, early star-forming galaxies.

### Baseline Summary Attempt 2
The study addresses the mystery of how supermassive black holes, which can be millions to billions of times the mass of the Sun, grew so rapidly in galactic cores. Current theories suggest they originated in dust-rich, starburst galaxies, later expelling gas and dust to become luminous quasars. Although both starburst galaxies and quasars have been found in the early universe, this study marks the first observation of rapidly growing black holes in these dusty, early star-forming galaxies.

### Baseline Summary Attempt 3
The study addresses the mystery of how supermassive black holes, which can be millions to billions of times the mass of the Sun, grew so rapidly in galactic cores. Current theories suggest they originated in the dense, dust-filled centers of starburst galaxies, later expelling gas and dust to become luminous quasars. Although both starburst galaxies and quasars have been identified in the early universe, this study marks the first observation of rapidly growing black holes in these dusty, early star-forming galaxies.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand the mystery of supermassive black holes.
- Learn about their formation in early galaxies.
- Recognize the significance of quasars in astronomy.

**Key Concepts:**
- Supermassive black holes are millions to billions of times the Sun's mass.
- They likely formed in starburst galaxies with lots of star formation.
- These black holes expel gas and dust, becoming bright quasars.
- Rarely, dusty starburst galaxies and quasars are seen in the early universe.
- New observations show rapidly growing black holes in early galaxies.

**Recall Questions:**
1. What are supermassive black holes, and where do they form?
2. Why are quasars important in understanding black hole growth?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the formation of supermassive black holes.
- Learn about starburst galaxies and quasars.
- Recognize the significance of recent discoveries in astronomy.

**Key Concepts:**
- Supermassive black holes are millions to billions of times the Sun's mass.
- They likely formed in starburst galaxies with lots of star formation.
- These black holes expel gas and dust, becoming bright quasars.
- Rarely, dusty starburst galaxies and quasars are seen in the early universe.
- New observations have found rapidly growing black holes in early galaxies.

**Recall Questions:**
1. What are supermassive black holes thought to form from?
2. Why are quasars important in understanding black hole growth?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand the mystery of supermassive black holes.
- Learn about their growth in early galaxies.
- Recognize the significance of starburst galaxies and quasars.

**Key Concepts:**
- Supermassive black holes are millions to billions of times the Sun's mass.
- They likely formed in starburst galaxies with lots of star formation.
- These black holes expelled gas and dust to become luminous quasars.
- Rarely, dusty starburst galaxies and quasars have been found in the early universe.
- New observations reveal rapidly growing black holes in early galaxies.

**Recall Questions:**
1. What are supermassive black holes and where do they typically form?
2. Why are quasars important in understanding black hole growth?

### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 14.87         | 26.6667             | 80                   | 30%              |
| 2        | 14.0356       | 25.6667             | 77                   | 30%              |
| 3        | 14.7523       | 27                  | 81                   | 20%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 7.423         | 9.5                 | 19                   | 100%             |
| 2        | 7.6521        | 9.5                 | 19                   | 100%             |
| 3        | 7.5027        | 9.8333              | 18.8571              | 100%             |

---

## Input Case 6: Thinking Fast and Slow Book

### Source
https://dn790002.ca.archive.org/0/items/DanielKahnemanThinkingFastAndSlow/Daniel%20Kahneman-Thinking%2C%20Fast%20and%20Slow%20%20.pdf

### Original Input
The interaction of the two systems is a recurrent theme of the book, and a brief synopsis of the plot is in order. In the story I will tell, Systems 1 and 2 are both active whenever we are awake. System 1 runs automatically and System 2 is normally in a comfortable low-effort mode, in which only a fraction of its capacity is engaged. System 1 continuously generates suggestions for System 2: impressions, intuitions, intentions, and feelings. If endorsed by System 2, impressions and intuitions turn into beliefs, and impulses turn into voluntary actions. When all goes smoothly, which is most of the time, System 2 adopts the suggestions of System 1 with little or no modification. You generally believe your impressions and act on your desires, and that is fine—usually. When System 1 runs into difficulty, it calls on System 2 to support more detailed and specific processing that may solve the problem of the moment. System 2 is mobilized when a question arises for which System 1 does not offer an answer, as probably happened to you when you encountered the multiplication problem 17 × 24. You can also feel a surge of conscious attention whenever you are surprised. System 2 is activ">< 2 is actated when an event is detected that violates the model of the world that System 1 maintains. In that world, lamps do not jump, cats do not bark, and gorillas do not cross basketball courts. The gorilla experiment demonstrates that some attention is needed for the surprising stimulus to be detected. Surprise then activates and orients your attention: you will stare, and you will search your memory for a story that makes sense of the surprising event. System 2 is also credited with the continuous monitoring of your own behavior—the control that keeps you polite when you are angry, and alert when you are driving at night. System 2 is mobilized to increased effort when it detects an error about to be made. Remember a time when you almost blurted out an offensive remark and note how hard you worked to restore control. In summary, most of what you (your System 2) think and do originates in your System 1, but System 2 takes over when things get difficult, and it normally has the last word. The division of labor between System 1 and System 2 is highly efficient: it minimizes effort and optimizes performance. The arrangement works well most of the time because System 1 is generally very good at what it does: its models of familiar situations are accurate, its short-term predictions are usually accurate as well, and its initial reactions to challenges are swift and generally appropriate. System 1 has biases, however, systematic errors that it is prone to make in specified circumstances. As we shall see, it sometimes answers easier questions than the one it was asked, and it has little understanding of logic and statistics. One further limitation of System 1 is that it cannot be turned off. If you are shown a word on the screen in a language you know, you will read it—unless your attention is totally focused elsewhere.


### Baseline Summary Attempt 1
The study material discusses the interaction between two cognitive systems, referred to as System 1 and System 2. System 1 operates automatically and generates impressions, intuitions, and feelings, while System 2 functions in a low-effort mode, engaging more deeply when necessary. Typically, System 2 endorses the suggestions from System 1, leading to beliefs and voluntary actions. However, when System 1 encounters difficulties or surprising events, it calls on System 2 for more detailed processing and problem-solving.

System 2 is activated in situations where System 1's model of the world is challenged, such as unexpected occurrences. It also monitors behavior, helping to maintain control in social situations and during tasks requiring focus. While System 1 is efficient and effective in familiar contexts, it is prone to biases and systematic errors, particularly in logic and statistics, and cannot be easily turned off. Overall, the division of labor between the two systems optimizes cognitive performance, with System 1 handling routine tasks and System 2 stepping in when challenges arise.

### Baseline Summary Attempt 2
The study material discusses the interaction between two cognitive systems, referred to as System 1 and System 2. System 1 operates automatically and continuously generates suggestions, such as impressions and intuitions, which System 2 can endorse, turning them into beliefs and actions. Generally, System 2 remains in a low-effort mode, accepting System 1's suggestions without much modification. However, when System 1 encounters difficulties or surprises, it calls on System 2 for more detailed processing. System 2 is activated when unexpected events occur, requiring conscious attention and monitoring of behavior, such as controlling impulses or correcting potential errors.

The efficiency of this division of labor allows for optimal performance, as System 1 is adept at handling familiar situations and making quick, appropriate responses. However, System 1 has biases and systematic errors, often opting for easier questions and lacking understanding of logic and statistics. Importantly, System 1 cannot be turned off; it will respond to stimuli unless attention is fully diverted elsewhere. Overall, while System 1 handles most cognitive tasks effectively, System 2 steps in when challenges arise, ensuring a balance between automatic and deliberate thought processes.

### Baseline Summary Attempt 3
The study material discusses the interaction between two cognitive systems, referred to as System 1 and System 2. System 1 operates automatically and generates suggestions such as impressions and intuitions, while System 2 functions in a low-effort mode, engaging more deeply only when necessary. Typically, System 2 endorses System 1's suggestions, leading to beliefs and actions. However, when System 1 encounters difficulties or surprises, it activates System 2 for more detailed processing. For example, when faced with complex problems or unexpected events, System 2 helps manage attention and behavior, ensuring control in challenging situations.

The division of labor between the two systems is efficient, as System 1 is adept at handling familiar scenarios and making quick predictions. Nonetheless, System 1 is also prone to biases and systematic errors, often opting for easier questions and lacking in logical and statistical reasoning. Additionally, System 1 cannot be turned off, as it automatically processes familiar stimuli. Overall, while System 1 is generally effective, System 2 plays a crucial role in addressing complexities and maintaining control.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand the roles of System 1 and System 2.
- Recognize how these systems interact.
- Identify when System 2 is activated.

**Key Concepts:**
- System 1 operates automatically and generates suggestions.
- System 2 is low-effort and engages when needed.
- System 2 helps solve problems when System 1 struggles.
- Surprising events activate System 2 for attention and control.
- System 1 has biases and cannot be turned off.

**Recall Questions:**
1. What triggers System 2 to become active?
2. How do System 1 and System 2 work together?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the roles of System 1 and System 2.
- Recognize how these systems interact.
- Identify when System 2 is activated.

**Key Concepts:**
- System 1 runs automatically and generates suggestions.
- System 2 is low-effort and engages when needed.
- Impressions from System 1 can become beliefs in System 2.
- System 2 helps solve problems when System 1 struggles.
- System 2 monitors behavior and maintains control.

**Recall Questions:**
1. What triggers System 2 to become active?
2. How does System 1 influence our beliefs and actions?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand the roles of System 1 and System 2.
- Recognize how these systems interact during decision-making.
- Identify the limitations and strengths of each system.

**Key Concepts:**
- System 1: Operates automatically and quickly, generating impressions and feelings.
- System 2: Engages when System 1 struggles, requiring more effort and attention.
- Interaction: System 1 suggests ideas; System 2 evaluates and decides.
- Surprise: Activates System 2, prompting attention and memory search.
- Biases: System 1 can make systematic errors and cannot be turned off.

**Recall Questions:**
1. What are the main functions of System 1 and System 2?
2. How does surprise affect the activation of System 2?

### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 14.9652       | 20.75               | 83                   | 20%              |
| 2        | 16.1542       | 20.5556             | 92.5                 | 20%              |
| 3        | 15.0517       | 19.1111             | 86                   | 20%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 8.0405        | 8.0833              | 16.1667              | 90%              |
| 2        | 8.1083        | 8                   | 16                   | 90%              |
| 3        | 10.047        | 9.6667              | 19.3333              | 90%              |

---

## Input Case 7: Machine Learning Article

### Source
https://www.ibm.com/think/topics/machine-learning

### Original Input
On a high level, the inspiration for neural networks comes from the biological neurons in the human brain, which communicate through electrical signals. In 1943, Warren McCulloch and Walter Pitts proposed the first mathematical model of a neuron, showing that simple units could perform computation of a function. Later, in 1958, Frank Rosenblatt introduced the perceptron, an algorithm designed to perform pattern recognition. The perceptron is the historical ancestor of today’s networks: essentially a linear model with a constrained output. In the following section, we will dive into how neural networks borrow inspiration from the human brains to make decisions and recognize patterns. A neural network can be understood through a simple example: spam detection. An email is fed into the network, and features such as words or phrases like “prize,” “money,” “dear” or “win” are used as inputs. The early neurons in the network process the importance of each signal, while later layers combine this information into higher-level cues that capture context and tone. The final layer then computes a probability of whether the email is spam, and if that probability is high enough, the email is flagged. In essence, the network learns how to transform raw features into meaningful patterns and use them to make predictions. This process is powered by two fundamental concepts: weights and biases. Weights act like dials that control how strongly each input feature influences the decision—a word like “prize” may be given more weight than a common word like “hello.” Biases are built-in values that shift the decision threshold, allowing a neuron to activate even if the inputs themselves are weak. Together, these model parameters determine how each neuron contributes to the overall computation. By adjusting these values during training, the network gradually learns to make accurate predictions—in this case, whether an email is spam or not. Mathematically, a neural network learns a function f(X) by mapping an input vector X = (x1, x2, x3...) to a predict a response Y. What distinguishes neural networks from other traditional machine learning algorithms is their layered structure and their ability to perform nonlinear transformation.


### Baseline Summary Attempt 1
Neural networks are inspired by biological neurons in the human brain, which communicate via electrical signals. The first mathematical model of a neuron was proposed by Warren McCulloch and Walter Pitts in 1943, demonstrating that simple units can perform computations. In 1958, Frank Rosenblatt introduced the perceptron, an early algorithm for pattern recognition and the precursor to modern neural networks, functioning as a linear model with constrained output.

Neural networks process inputs, such as words in spam detection, through multiple layers. Early neurons assess the importance of features, while later layers synthesize this information into higher-level cues. The final layer computes the probability of an email being spam, flagging it if the probability exceeds a certain threshold. This learning process relies on two key parameters: weights, which determine the influence of each input feature, and biases, which adjust the decision threshold. By training, the network fine-tunes these parameters to improve prediction accuracy.

Mathematically, a neural network learns a function ( f(X) ) that maps an input vector ( X = (x_1, x_2, x_3, \ldots) ) to a predicted response ( Y ). Neural networks are distinct from traditional machine learning algorithms due to their layered structure and ability to perform nonlinear transformations.

### Baseline Summary Attempt 2
Neural networks are inspired by biological neurons in the human brain, which communicate via electrical signals. The concept began with Warren McCulloch and Walter Pitts in 1943, who created a mathematical model of a neuron, demonstrating that simple units could compute functions. In 1958, Frank Rosenblatt introduced the perceptron, an early algorithm for pattern recognition, which serves as a precursor to modern neural networks.

Neural networks, such as those used for spam detection, process inputs like specific words or phrases. Initial layers assess the significance of these inputs, while subsequent layers integrate this information to form higher-level insights. The final layer calculates the probability of an email being spam, flagging it if the probability exceeds a certain threshold.

Key components of neural networks include weights and biases. Weights determine the influence of each input feature, while biases adjust the decision threshold, allowing neurons to activate even with weak inputs. Through training, the network fine-tunes these parameters to enhance prediction accuracy. Mathematically, a neural network learns a function ( f(X) ) that maps an input vector ( X ) to a predicted response ( Y ). Their unique layered structure and capability for nonlinear transformations differentiate neural networks from traditional machine learning algorithms.

### Baseline Summary Attempt 3
Neural networks are inspired by biological neurons in the human brain, which communicate via electrical signals. The first mathematical model of a neuron was proposed by Warren McCulloch and Walter Pitts in 1943, demonstrating that simple units could perform computations. Frank Rosenblatt introduced the perceptron in 1958, a linear model for pattern recognition, which serves as the historical precursor to modern neural networks.

Neural networks function by processing inputs, such as words in spam detection. Early neurons assess the importance of each input, while later layers synthesize this information into higher-level cues. The final layer computes the probability of an email being spam, flagging it if the probability exceeds a certain threshold.

Key components of neural networks include weights and biases. Weights determine the influence of each input feature on the decision, while biases adjust the decision threshold, allowing neurons to activate even with weak inputs. During training, these parameters are adjusted to improve prediction accuracy. Mathematically, a neural network learns a function f(X) that maps an input vector X to a predicted response Y. Their layered structure and capacity for nonlinear transformations distinguish neural networks from traditional machine learning algorithms.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand the basic concept of neural networks.
- Learn how neural networks mimic human brain functions.
- Recognize key components like weights and biases.

**Key Concepts:**
- Neural networks are inspired by human brain neurons.
- The perceptron is an early model for pattern recognition.
- Inputs like words help determine if an email is spam.
- Weights adjust the influence of input features.
- Biases help activate neurons even with weak inputs. Mathematically, a neural network learns a function: f(X) = predict response Y

**Recall Questions:**
1. What are weights and biases in a neural network?
2. How does a neural network determine if an email is spam?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the basics of neural networks.
- Learn how neural networks mimic human brain functions.
- Recognize key components like weights and biases.

**Key Concepts:**
- Neural networks are inspired by human neurons.
- The first neuron model was proposed in 1943.
- The perceptron, introduced in 1958, performs pattern recognition.
- Weights control input feature influence on decisions.
- Biases shift decision thresholds for neuron activation. Mathematically, a neural network learns a function: f(X) = predict response Y

**Recall Questions:**
1. What are weights and biases in a neural network?
2. How does a neural network determine if an email is spam?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand the basics of neural networks.
- Learn how neural networks mimic human brain functions.
- Recognize key components like weights and biases.

**Key Concepts:**
- Neural networks are inspired by biological neurons in the brain.
- The perceptron is an early model for pattern recognition.
- Weights control the influence of input features on decisions.
- Biases adjust the decision threshold for neuron activation.
- Neural networks learn by adjusting weights and biases during training.

**Recall Questions:**
1. What are weights and biases in a neural network?
2. How does a neural network determine if an email is spam?


### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 14.2837       | 20.2                | 67.3333              | 20%              |
| 2        | 14.1764       | 18.3636             | 67.3333              | 20%              |
| 3        | 13.9787       | 17.3636             | 63.6667              | 30%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 8.1104        | 9.5833              | 14.375               | 90%              |
| 2        | 8.7728        | 9.0833              | 13.625               | 90%              |
| 3        | 8.6456        | 8.8333              | 17.6667              | 90%              |

---

## Input Case 8: Mongolian History Article

### Source
https://www.britannica.com/topic/Mongol

### Original Input
Among the tribes that held power in Mongolia were the Xiongnu, a confederated empire that warred with the young Chinese state for centuries before dissolving in 48 ce. The Khitan ruled in Manchuria and North China, where they established the Liao dynasty (907–1125) and formed an alliance with a little-known tribal confederacy known as All the Mongols. After the fall of the Liao, the Tatars—a Mongol people but not members of the league—appeared as allies of the Juchen, the Khitan’s successors. During this time Genghis Khan (1162–1227) came to power within the All the Mongols league and was proclaimed khan in 1206. He skillfully gained control over the Mongols outside the league. Between 1207 and 1227 he undertook military campaigns that extended Mongol domains as far west as European Russia and as far east as northern China, taking Beijing in 1215. He died on campaign against the Xi Xia in northwest China. By this time the Mongol empire stretched over an immense swath of Asia between the Caspian Sea (west) and the China Sea (east), and Siberia (north) and the Pamirs, Tibet, and central China (south). The amazing military achievements of the Mongols under Genghis Khan and his successors were largely due to their armies of mounted archers, who possessed great speed and mobility.


### Baseline Summary Attempt 1
The study material discusses the historical power dynamics in Mongolia, focusing on key tribes and leaders. The Xiongnu, a confederated empire, engaged in prolonged conflict with early China until their dissolution in 48 CE. The Khitan established the Liao dynasty (907–1125) in Manchuria and North China, forming alliances with the All the Mongols confederacy. After the Liao's fall, the Tatars allied with the Juchen, the Khitan's successors. Genghis Khan, who rose to power within the All the Mongols and was proclaimed khan in 1206, expanded Mongol territory through military campaigns from 1207 to 1227, reaching as far west as European Russia and capturing Beijing in 1215. By his death, the Mongol Empire spanned a vast region of Asia. The Mongols' military success was attributed to their mounted archers, known for their speed and mobility.

### Baseline Summary Attempt 2
The study material discusses the historical power dynamics in Mongolia, focusing on key tribes and leaders. The Xiongnu, a confederated empire, engaged in prolonged conflict with early China until their dissolution in 48 CE. The Khitan established the Liao dynasty (907–1125) in Manchuria and North China, forming alliances with the All the Mongols confederacy. After the Liao's fall, the Tatars allied with the Juchen, Khitan's successors. Genghis Khan, who rose to power within the All the Mongols and was proclaimed khan in 1206, expanded Mongol territories through military campaigns from 1207 to 1227, reaching as far as European Russia and northern China, including the capture of Beijing in 1215. By his death, the Mongol Empire spanned a vast area of Asia. The Mongols' military success was attributed to their mounted archers, known for their speed and mobility.

### Baseline Summary Attempt 3
The study material discusses the historical power dynamics in Mongolia, highlighting key tribes and their interactions. The Xiongnu were a significant confederated empire that engaged in prolonged conflict with early China until their dissolution in 48 CE. The Khitan established the Liao dynasty (907–1125) in Manchuria and North China and allied with a tribal confederacy called All the Mongols. After the Liao's fall, the Tatars allied with the Juchen, the Khitan's successors. Genghis Khan rose to power within the All the Mongols league, being proclaimed khan in 1206. He expanded Mongol territory through military campaigns from 1207 to 1227, reaching as far west as European Russia and capturing Beijing in 1215. By his death, the Mongol Empire spanned a vast region of Asia. The Mongols' military success was attributed to their mounted archers, known for their speed and mobility.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand the key tribes in Mongolia's history.
- Learn about Genghis Khan's rise to power.
- Recognize the extent of the Mongol Empire.

**Key Concepts:**
- The Xiongnu were a powerful confederated empire in Mongolia.
- The Khitan established the Liao dynasty from 907 to 1125.
- Genghis Khan united the All the Mongols and became khan in 1206.
- Mongol military success came from mounted archers' speed and mobility.
- The Mongol Empire expanded from Europe to northern China.

**Recall Questions:**
1. Who was Genghis Khan and when did he become khan?
2. What was the role of mounted archers in the Mongol military?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the key tribes in Mongolia's history.
- Learn about Genghis Khan's rise to power.
- Recognize the extent of the Mongol Empire.

**Key Concepts:**
- The Xiongnu were a powerful confederated empire in Mongolia.
- The Khitan established the Liao dynasty in Manchuria and North China.
- Genghis Khan united the All the Mongols league in 1206.
- Mongol military success came from mounted archers' speed and mobility.
- The Mongol Empire stretched from the Caspian Sea to northern China.

**Recall Questions:**
1. Who was proclaimed khan of the All the Mongols in 1206?
2. What contributed to the military success of the Mongols under Genghis Khan?

### ADHD Summary Attmept 3
**Learning Objectives:**
- Understand the key tribes in Mongolia's history.
- Learn about Genghis Khan's rise to power.
- Recognize the Mongol Empire's military strategies.

**Key Concepts:**
- The Xiongnu were a powerful confederated empire in Mongolia.
- The Khitan established the Liao dynasty in Manchuria and North China.
- Genghis Khan united the All the Mongols and became khan in 1206.
- Mongol military success relied on fast, mobile mounted archers.
- The Mongol Empire expanded greatly under Genghis Khan's leadership.

**Recall Questions:**
1. Who was proclaimed khan in 1206?
2. What was a key factor in the Mongol military's success?

### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 12.3056       | 19.1429             | 134                  | 20%              |
| 2        | 12.6283       | 19.5714             | 137                  | 20%              |
| 3        | 11.6452       | 17.375              | 139                  | 20%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 7.7795        | 9.25                | 18.5                 | 100%             |
| 2        | 8.4541        | 9.5                 | 16.2857              | 90%              |
| 3        | 9.2087        | 8.75                | 17.5                 | 90%              |

---

## Input Case 9: Parkinson's Disease Research Paper

### Source
https://www.ncbi.nlm.nih.gov/books/NBK536722/

### Original Input
Parkinson’s disease (PD) is a complex progressive neurodegenerative disease characterized by tremor, rigidity, and bradykinesia, with postural instability appearing in some patients as the disease progresses. It was first described by James Parkinson in 1817 and further characterized by Jean-Martin Charcot, and our knowledge of PD is continuing to expand. PD is the second most common neurodegenerative disease after Alzheimer’s disease (AD) (1), with a prevalence of approximately 0.5–1% among those 65–69 years of age, rising to 1–3% among persons 80 years of age and older (2, 3). With an aging population, both the prevalence and incidence of PD are expected to increase by more than 30% by 2030 (4), which will result in both direct and indirect costs on both society and the economy as a whole. PD is pathologically characterized by the loss of nigrostriatal dopaminergic innervation, although neurodegeneration is not limited to only the nigral dopaminergic neurons but also involves cells located in other regions of the neural network. Such a widespread pathology makes PD a very heterogeneous disorder, and a reliable diagnostic test is not yet available. Currently, diagnosis is based on clinical symptoms with the criteria for a diagnosis requiring the presence of two of the following clinical features: resting tremor, bradykinesia, rigidity and/or postural instability. Clinical criteria, however, can only lead to a diagnosis of probable PD, while a definitive diagnosis requires histopathological assessment, with the identification of α-synuclein-containing Lewy bodies (LBs) or Lewy neurites. Treatment predominantly focuses on symptomatic relief with drugs aiming to either restore the level of dopamine in the striatum or to act on striatal post-synaptic dopamine receptors. However, as dopamine is not the only neurotransmitter involved in PD, many other drugs are also being used to target specific symptoms, such as depression or dementia. Yet, further investigation on novel therapies to reduce the rate of neurodegeneration or even to replenish the loss of dopaminergic cells remains in the research setting, with some in the early stages of clinical trials. As our understanding of the pathogenesis of PD increases and more is learned about new therapeutic targets, the potential for the development of disease-modifying therapies is promising.


### Baseline Summary Attempt 1
Parkinson's disease (PD) is a progressive neurodegenerative disorder marked by tremor, rigidity, bradykinesia, and postural instability. First described by James Parkinson in 1817 and further detailed by Jean-Martin Charcot, PD is the second most common neurodegenerative disease after Alzheimer's, affecting 0.5–1% of individuals aged 65–69 and 1–3% of those 80 and older. With an aging population, PD prevalence is projected to increase by over 30% by 2030, impacting societal and economic costs.

Pathologically, PD is characterized by the loss of dopaminergic neurons in the nigrostriatal pathway, but neurodegeneration also affects other neural regions, contributing to its heterogeneity. Diagnosis relies on clinical symptoms, requiring two of the following: resting tremor, bradykinesia, rigidity, or postural instability. A definitive diagnosis necessitates histopathological confirmation through the identification of α-synuclein-containing Lewy bodies.

Current treatments primarily focus on symptomatic relief by restoring dopamine levels or targeting post-synaptic dopamine receptors, with additional medications addressing symptoms like depression or dementia. Research is ongoing for novel therapies aimed at slowing neurodegeneration or replenishing lost dopaminergic cells, with potential for developing disease-modifying treatments as understanding of PD pathogenesis improves.

### Baseline Summary Attempt 2
Parkinson’s disease (PD) is a progressive neurodegenerative disorder marked by tremor, rigidity, bradykinesia, and, in some cases, postural instability. Initially described by James Parkinson in 1817 and further defined by Jean-Martin Charcot, PD is the second most common neurodegenerative disease after Alzheimer’s, with a prevalence of 0.5–1% in those aged 65–69, increasing to 1–3% in individuals 80 and older. The incidence of PD is projected to rise by over 30% by 2030 due to an aging population, leading to significant societal and economic impacts.

Pathologically, PD is characterized by the loss of dopaminergic neurons in the nigrostriatal pathway, but neurodegeneration also affects other neural regions, contributing to its heterogeneity. Diagnosis relies on clinical symptoms, requiring at least two of the following: resting tremor, bradykinesia, rigidity, or postural instability. A definitive diagnosis necessitates histopathological evaluation for α-synuclein-containing Lewy bodies.

Current treatment focuses on symptomatic relief through medications that restore dopamine levels or target post-synaptic dopamine receptors. Other drugs address symptoms like depression or dementia. Research is ongoing for novel therapies aimed at slowing neurodegeneration or replenishing lost dopaminergic cells, with some in early clinical trials. As understanding of PD's pathogenesis improves, the potential for developing disease-modifying therapies is promising.

### Baseline Summary Attempt 3
Parkinson’s disease (PD) is a progressive neurodegenerative disorder marked by tremor, rigidity, bradykinesia, and postural instability. First described by James Parkinson in 1817 and further detailed by Jean-Martin Charcot, PD is the second most common neurodegenerative disease after Alzheimer’s, affecting about 0.5–1% of individuals aged 65–69 and 1–3% of those aged 80 and older. The prevalence of PD is expected to rise by over 30% by 2030 due to an aging population, leading to significant societal and economic costs.

Pathologically, PD is characterized by the loss of dopaminergic neurons in the nigrostriatal pathway, but it also involves neurodegeneration in other brain regions, contributing to its heterogeneity. Diagnosis is primarily clinical, requiring two of the following symptoms: resting tremor, bradykinesia, rigidity, or postural instability. A definitive diagnosis necessitates histopathological confirmation through the identification of α-synuclein-containing Lewy bodies.

Current treatments focus on alleviating symptoms, mainly by restoring dopamine levels or targeting post-synaptic dopamine receptors. Other medications address associated symptoms like depression and dementia. Research is ongoing to develop novel therapies aimed at slowing neurodegeneration or replenishing lost dopaminergic cells, with potential for disease-modifying treatments as our understanding of PD pathogenesis improves.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand what Parkinson’s disease (PD) is.
- Learn about the symptoms and diagnosis of PD.
- Explore treatment options and future research directions.

**Key Concepts:**
- Parkinson’s disease is a progressive neurodegenerative disorder.
- Common symptoms include tremor, rigidity, and bradykinesia.
- Diagnosis requires two clinical features: resting tremor, bradykinesia, rigidity, or postural instability.
- Treatment focuses on relieving symptoms and restoring dopamine levels.
- Research is ongoing for new therapies to slow neurodegeneration.

**Recall Questions:**
1. What are the main symptoms of Parkinson’s disease?
2. How is Parkinson’s disease diagnosed?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the basics of Parkinson's disease (PD).
- Recognize the symptoms and diagnosis of PD.
- Learn about current treatments and research for PD.

**Key Concepts:**
- Parkinson's disease is a neurodegenerative disorder.
- Common symptoms include tremor, rigidity, and bradykinesia.
- Diagnosis requires two clinical features: resting tremor, bradykinesia, rigidity, or postural instability.
- Treatment focuses on relieving symptoms and restoring dopamine levels.
- Research is ongoing for new therapies to slow neurodegeneration.

**Recall Questions:**
1. What are the main symptoms of Parkinson's disease?
2. How is Parkinson's disease diagnosed?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand the key features of Parkinson’s disease (PD).
- Recognize the prevalence and impact of PD.
- Identify current diagnostic criteria and treatment options.

**Key Concepts:**
- Parkinson’s disease is a progressive neurodegenerative disorder.
- Main symptoms include tremor, rigidity, and bradykinesia.
- Diagnosis requires two clinical features: resting tremor, bradykinesia, rigidity, or postural instability.
- Treatment focuses on relieving symptoms and restoring dopamine levels.
- Research is ongoing for new therapies to slow neurodegeneration.

**Recall Questions:**
1. What are the main symptoms of Parkinson’s disease?
2. How is Parkinson’s disease diagnosed?


### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 18.7991       | 20                  | 59.6667              | 30%              |
| 2        | 16.6987       | 18.0909             | 66                   | 20%              |
| 3        | 17.6286       | 19                  | 63                   | 30%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 11.7451       | 8.0833              | 16.1667              | 90%              |
| 2        | 11.8823       | 8.0833              | 16.1667              | 90%              |
| 3        | 12.3152       | 8.1667              | 16.3333              | 90%              |

---

## Input Case 10: Virtual Cells Research Paper

### Source
https://pmc.ncbi.nlm.nih.gov/articles/PMC12789685/

### Original Input
Virtual cell models also help elucidate tissue-specific differences in drug responses15. For example, integrating multi-omics data from hepatocytes and renal tubular epithelial cells enables prediction of tissue-specific toxicological responses under the same drug exposure6. This not only helps explain interindividual variability in adverse drug reactions but also offers a technical pathway to reduce animal experimentation and advance New Approach Methodologies (NAMs)6,16. The advent of virtual cell models is shifting biomedicine from a wet-lab-dependent, “validation-driven” paradigm toward a data- and prediction-driven simulation–validation closed loop1,6. In sum, AI-driven virtual cell models are becoming a key bridge between molecular-mechanism research and preclinical drug evaluation, providing data-driven support throughout the pipeline from hypothesis generation to mechanistic verification1,5. Driven by an evidence-progression framework, the narrative advances from model construction to evaluation and validation, to virtual-cell use cases, translational barriers, and forward outlook. This translational driver integrates technical capability, testability, utility, and compliance pathways into a preclinical evidence chain.


### Baseline Summary Attempt 1
Virtual cell models are instrumental in understanding tissue-specific drug responses by integrating multi-omics data from different cell types, such as hepatocytes and renal tubular epithelial cells. This integration aids in predicting toxicological responses to drugs, clarifying interindividual variability in adverse reactions, and reducing the need for animal testing through New Approach Methodologies (NAMs). The emergence of these models is transforming biomedicine from a traditional wet-lab approach to a more data-driven simulation and validation process. AI-driven virtual cell models serve as a crucial link between molecular research and preclinical drug evaluation, facilitating the progression from hypothesis generation to mechanistic verification. The framework emphasizes model construction, evaluation, validation, and practical applications, while addressing translational barriers and ensuring compliance within the preclinical evidence chain.

### Baseline Summary Attempt 2
Virtual cell models are instrumental in understanding tissue-specific drug responses by integrating multi-omics data from different cell types, such as hepatocytes and renal tubular epithelial cells. This integration aids in predicting toxicological responses to drugs, explaining variability in adverse drug reactions, and reducing reliance on animal testing through New Approach Methodologies (NAMs). The emergence of these models is transforming biomedicine from a traditional wet-lab approach to a simulation-driven framework that emphasizes data and predictions. AI-driven virtual cell models serve as a crucial link between molecular research and preclinical drug evaluation, supporting the process from hypothesis generation to mechanistic verification. The study outlines a progression from model construction to validation, highlighting the importance of technical capability, testability, utility, and compliance in building a robust preclinical evidence chain.

### Baseline Summary Attempt 3
Virtual cell models are instrumental in understanding tissue-specific drug responses by integrating multi-omics data from different cell types, such as hepatocytes and renal tubular epithelial cells. This integration aids in predicting toxicological responses to drugs, clarifying interindividual variability in adverse reactions, and reducing the need for animal testing through New Approach Methodologies (NAMs). The emergence of these models is transforming biomedicine from a reliance on wet-lab validation to a more data-driven, predictive simulation-validation approach. AI-driven virtual cell models serve as a crucial link between molecular research and preclinical drug evaluation, supporting the entire process from hypothesis generation to mechanistic verification. The study emphasizes a structured progression from model construction to validation, highlighting the integration of technical capabilities and regulatory compliance within the preclinical evidence chain.

### ADHD Summary Attempt 1
**Learning Objectives:**
- Understand how virtual cell models improve drug response predictions.
- Learn about the benefits of multi-omics data integration.
- Recognize the shift in biomedicine towards data-driven methods.

**Key Concepts:**
- Virtual cell models help explain tissue-specific drug responses.
- Multi-omics data from different cells predict toxicological responses.
- These models reduce the need for animal testing.
- AI-driven models connect research and drug evaluation.
- The process involves model construction, evaluation, and validation.

**Recall Questions:**
1. How do virtual cell models help in predicting drug responses?
2. What is the significance of integrating multi-omics data?

### ADHD Summary Attempt 2
**Learning Objectives:**
- Understand the role of virtual cell models in drug responses.
- Learn how multi-omics data improves predictions.
- Recognize the shift in biomedicine towards data-driven methods.

**Key Concepts:**
- Virtual cell models show differences in drug responses across tissues.
- Multi-omics data helps predict toxic responses in specific cells.
- These models reduce the need for animal testing.
- AI-driven models connect research to drug evaluation.
- The process includes model construction, validation, and application.

**Recall Questions:**
1. How do virtual cell models improve drug response predictions?
2. What is the significance of multi-omics data in this context?

### ADHD Summary Attempt 3
**Learning Objectives:**
- Understand the role of virtual cell models in drug responses.
- Learn about tissue-specific toxicological predictions.
- Recognize the benefits of AI in biomedicine.

**Key Concepts:**
- Virtual cell models show how different tissues respond to drugs.
- Multi-omics data helps predict toxic responses in liver and kidney cells.
- AI-driven models reduce animal testing and improve drug evaluation.
- The approach shifts from wet-lab methods to data-driven simulations.
- Evidence-progression frameworks guide model construction and validation.

**Recall Questions:**
1. How do virtual cell models help in understanding drug responses?
2. What is the benefit of using AI in drug evaluation?


### Evaluation Results

**Baseline**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 21.4463       | 24.2                | 121                  | 20%              |
| 2        | 20.9285       | 25.2                | 126                  | 20%              |
| 3        | 21.6304       | 25                  | 125                  | 20%              |

**ADHD**

| Attempts | Reading Level | Avg Sentence Length | Avg Paragraph Length | Compliance Score |
| -------- | ------------- | ------------------- | -------------------- | ---------------- |
| 1        | 11.9876       | 8.4167              | 16.8333              | 90%              |
| 2        | 10.1633       | 8.6667              | 17.3333              | 90%              |
| 3        | 11.1678       | 8.9167              | 17.8333              | 90%              |