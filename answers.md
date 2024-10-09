# Answers
## Q1
**Q1.** What are the five most similar segments to segment "267:476"  
**Input:** "that if we were to meet alien life at some point"  
**SQL Query**:  
```sql
SELECT i.title as "Podcast name", i.id as "Segment ID", 
        i.content as "Segment raw text", i.start_time as "Start time", 
        i.end_time as "Stop time", i.dist as "Embedding distance"
FROM 
    (
    SELECT p.title, ps.id, ps.content, ps.start_time, ps.end_time, 
        ps.embedding <->
            (SELECT embedding FROM podcast_segment 
            WHERE id='267:476') as dist
    FROM 
        (
        SELECT *
        FROM podcast_segment
        WHERE id != '267:476'
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    ) as i
ORDER BY i.dist ASC
LIMIT 5;
```
**Output**:  
> ('Podcast: Ryan Graves: UFOs, Fighter Jets, and Aliens | Lex Fridman Podcast #308', '113:2792', ' encounters, human beings, if we were to meet another alien', 6725.62, 6729.86, 0.6483450674336982)  
> ('Podcast: Richard Dawkins: Evolution, Intelligence, Simulation, and Memes | Lex Fridman Podcast #87', '268:1019', ' Suppose we did meet an alien from outer space', 2900.04, 2903.0800000000004, 0.6558106859320757)  
> ('Podcast: Jeffrey Shainline: Neuromorphic Computing and Optoelectronic Intelligence | Lex Fridman Podcast #225', '305:3600', ' but if we think of alien civilizations out there', 9479.960000000001, 9484.04, 0.6595433115268592)  
> ('Podcast: Michio Kaku: Future of Humans, Aliens, Space Travel & Physics | Lex Fridman Podcast #45', '18:464', ' So I think when we meet alien life from outer space,', 1316.8600000000001, 1319.5800000000002, 0.6662026419636159)  
> ('Podcast: Alien Debate: Sara Walker and Lee Cronin | Lex Fridman Podcast #279', '71:989', ' because if aliens come to us', 2342.34, 2343.6200000000003, 0.6742942635162208)

**Readable Result:**
| Podcast name | Segment ID | Segment raw text | Start time | Stop time | Embedding distance |
|  --- | --- | --- | --- | --- | --- |
| Podcast: Ryan Graves: UFOs, Fighter Jets, and Aliens &#124; Lex Fridman Podcast #308 | 113:2792 |  encounters, human beings, if we were to meet another alien | 6725.620 | 6729.860 | 0.648 |
| Podcast: Richard Dawkins: Evolution, Intelligence, Simulation, and Memes &#124; Lex Fridman Podcast #87 | 268:1019 |  Suppose we did meet an alien from outer space | 2900.040 | 2903.080 | 0.656 |
| Podcast: Jeffrey Shainline: Neuromorphic Computing and Optoelectronic Intelligence &#124; Lex Fridman Podcast #225 | 305:3600 |  but if we think of alien civilizations out there | 9479.960 | 9484.040 | 0.660 |
| Podcast: Michio Kaku: Future of Humans, Aliens, Space Travel & Physics &#124; Lex Fridman Podcast #45 | 18:464 |  So I think when we meet alien life from outer space, | 1316.860 | 1319.580 | 0.666 |
| Podcast: Alien Debate: Sara Walker and Lee Cronin &#124; Lex Fridman Podcast #279 | 71:989 |  because if aliens come to us | 2342.340 | 2343.620 | 0.674 |

## Q2
**Q2.** What are the five most dissimilar segments to segment "267:476"  
**Input:** "that if we were to meet alien life at some point"  
**SQL Query**:  
```sql
SELECT i.title as "Podcast name", i.id as "Segment ID", 
        i.content as "Segment raw text", i.start_time as "Start time", 
        i.end_time as "Stop time", i.dist as "Embedding distance"
FROM 
    (
    SELECT p.title, ps.id, ps.content, ps.start_time, ps.end_time, 
        ps.embedding <->
            (SELECT embedding FROM podcast_segment 
            WHERE id='267:476') as dist
    FROM 
        (
        SELECT *
        FROM podcast_segment
        WHERE id != '267:476'
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    ) as i
ORDER BY i.dist DESC
LIMIT 5;
```
**Output**:  
> ('Podcast: Jason Calacanis: Startups, Angel Investing, Capitalism, and Friendship | Lex Fridman Podcast #161', '119:218', ' a 73 Mustang Grande in gold?', 519.96, 523.8000000000001, 1.6157687685840119)
('Podcast: Rana el Kaliouby: Emotion AI, Social Robots, and Self-Driving Cars | Lex Fridman Podcast #322', '133:2006', ' for 94 car models.', 5818.62, 5820.82, 1.5863359073014982)  
> ('Podcast: Travis Stevens: Judo, Olympics, and Mental Toughness | Lex Fridman Podcast #223', '283:1488', ' when I called down to get the sauna.', 3709.34, 3711.1000000000004, 1.572552805197421)  
> ('Podcast: Jeremy Howard: fast.ai Deep Learning Courses and Research | Lex Fridman Podcast #35', '241:1436', ' which has all the courses pre-installed.', 4068.9, 4071.1400000000003, 1.5663319710412156)  
> ('Podcast: Joscha Bach: Nature of Reality, Dreams, and Consciousness | Lex Fridman Podcast #212', '307:3933', ' and very few are first class and some are budget.', 10648.64, 10650.960000000001, 1.5616341289820461)

**Readable Result:**
| Podcast name | Segment ID | Segment raw text | Start time | Stop time | Embedding distance |
|  --- | --- | --- | --- | --- | --- |
| Podcast: Jason Calacanis: Startups, Angel Investing, Capitalism, and Friendship &#124; Lex Fridman Podcast #161 | 119:218 |  a 73 Mustang Grande in gold? | 519.960 | 523.800 | 1.616 |
| Podcast: Rana el Kaliouby: Emotion AI, Social Robots, and Self-Driving Cars &#124; Lex Fridman Podcast #322 | 133:2006 |  for 94 car models. | 5818.620 | 5820.820 | 1.586 |
| Podcast: Travis Stevens: Judo, Olympics, and Mental Toughness &#124; Lex Fridman Podcast #223 | 283:1488 |  when I called down to get the sauna. | 3709.340 | 3711.100 | 1.573 |
| Podcast: Jeremy Howard: fast.ai Deep Learning Courses and Research &#124; Lex Fridman Podcast #35 | 241:1436 |  which has all the courses pre-installed. | 4068.900 | 4071.140 | 1.566 |
| Podcast: Joscha Bach: Nature of Reality, Dreams, and Consciousness &#124; Lex Fridman Podcast #212 | 307:3933 |  and very few are first class and some are budget. | 10648.640 | 10650.960 | 1.562 |

## Q3
**Q3.** What are the five most similar segments to segment '48:511'  
**Input:** "Is it is there something especially interesting and profound to you in terms of our current deep learning neural network, artificial neural network approaches and the whatever we do understand about the biological neural network."  
**SQL Query**:  
```sql
SELECT i.title as "Podcast name", i.id as "Segment ID", 
        i.content as "Segment raw text", i.start_time as "Start time", 
        i.end_time as "Stop time", i.dist as "Embedding distance"
FROM 
    (
    SELECT p.title, ps.id, ps.content, ps.start_time, ps.end_time, 
        ps.embedding <->
            (SELECT embedding FROM podcast_segment 
            WHERE id='48:511') as dist
    FROM 
        (
        SELECT *
        FROM podcast_segment
        WHERE id != '48:511'
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    ) as i
ORDER BY i.dist ASC
LIMIT 5;
```
**Output**:  
> ('Podcast: Andrew Huberman: Neuroscience of Optimal Performance | Lex Fridman Podcast #139', '155:648', ' Is there something interesting to you or fundamental to you about the circuitry of the brain', 3798.48, 3805.84, 0.652299685331962)  
> ('Podcast: Cal Newport: Deep Work, Focus, Productivity, Email, and Social Media | Lex Fridman Podcast #166', '61:3707', ' of what we might discover about neural networks?', 8498.02, 8500.1, 0.7121050124628524)  
> ('Podcast: Matt Botvinick: Neuroscience, Psychology, and AI at DeepMind | Lex Fridman Podcast #106', '48:512', " And our brain is there. There's some there's quite a few differences. Are some of them to you either interesting or perhaps profound in terms of in terms of the gap we might want to try to close in trying to create a human level intelligence.", 1846.84, 1865.84, 0.7195603322334674)  
> ('Podcast: Yann LeCun: Dark Matter of Intelligence and Self-Supervised Learning | Lex Fridman Podcast #258', '276:2642', ' Have these, I mean, small pockets of beautiful complexity. Does that, do cellular automata, do these kinds of emergence and complex systems give you some intuition or guide your understanding of machine learning systems and neural networks and so on?', 8628.16, 8646.16, 0.7357217735737499)  
> ('Podcast: Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe | Lex Fridman Podcast #124', '2:152', ' So is there something like that with physics where so deep learning neural networks have been around for a long time?', 610.86, 618.86, 0.7366969553372291)

**Readable Result:**
| Podcast name | Segment ID | Segment raw text | Start time | Stop time | Embedding distance |
|  --- | --- | --- | --- | --- | --- |
| Podcast: Andrew Huberman: Neuroscience of Optimal Performance &#124; Lex Fridman Podcast #139 | 155:648 |  Is there something interesting to you or fundamental to you about the circuitry of the brain | 3798.480 | 3805.840 | 0.652 |
| Podcast: Cal Newport: Deep Work, Focus, Productivity, Email, and Social Media &#124; Lex Fridman Podcast #166 | 61:3707 |  of what we might discover about neural networks? | 8498.020 | 8500.100 | 0.712 |
| Podcast: Matt Botvinick: Neuroscience, Psychology, and AI at DeepMind &#124; Lex Fridman Podcast #106 | 48:512 |  And our brain is there. There's some there's quite a few differences. Are some of them to you either interesting or perhaps profound in terms of in terms of the gap we might want to try to close in trying to create a human level intelligence. | 1846.840 | 1865.840 | 0.720 |
| Podcast: Yann LeCun: Dark Matter of Intelligence and Self-Supervised Learning &#124; Lex Fridman Podcast #258 | 276:2642 |  Have these, I mean, small pockets of beautiful complexity. Does that, do cellular automata, do these kinds of emergence and complex systems give you some intuition or guide your understanding of machine learning systems and neural networks and so on? | 8628.160 | 8646.160 | 0.736 |
| Podcast: Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe &#124; Lex Fridman Podcast #124 | 2:152 |  So is there something like that with physics where so deep learning neural networks have been around for a long time? | 610.860 | 618.860 | 0.737 |

## Q4
**Q4.** What are the five most similar segments to segment '51:56'  
**Input:** "But what about like the fundamental physics of dark energy? Is there any understanding of what the heck it is?"  
**SQL Query**:  
```sql
SELECT i.title as "Podcast name", i.id as "Segment ID", 
        i.content as "Segment raw text", i.start_time as "Start time", 
        i.end_time as "Stop time", i.dist as "Embedding distance"
FROM 
    (
    SELECT p.title, ps.id, ps.content, ps.start_time, ps.end_time, 
        ps.embedding <->
            (SELECT embedding FROM podcast_segment 
            WHERE id='51:56') as dist
    FROM 
        (
        SELECT *
        FROM podcast_segment
        WHERE id != '51:56'
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    ) as i
ORDER BY i.dist ASC
LIMIT 5;
```
**Output**:  
> ('Podcast: George Hotz: Hacking the Simulation & Learning to Drive with Neural Nets | Lex Fridman Podcast #132', '308:144', " I mean, we don't understand dark energy, right?", 500.44, 502.6, 0.6681965222094363)  
> ('Podcast: Lex Fridman: Ask Me Anything - AMA January 2021 | Lex Fridman Podcast', '243:273', " Like, what's up with this dark matter and dark energy stuff?", 946.22, 950.12, 0.7355511762966292)  
> ('Podcast: Katherine de Kleer: Planets, Moons, Asteroids & Life in Our Solar System | Lex Fridman Podcast #184', '196:685', ' being like, what the hell is dark matter and dark energy?', 2591.72, 2595.9599999999996, 0.7631141596843518)  
> ('Podcast: Alex Filippenko: Supernovae, Dark Energy, Aliens & the Expanding Universe | Lex Fridman Podcast #137', '51:36', ' Do we have any understanding of what the heck that thing is?', 216.0, 219.0, 0.7922019445543276)  
> ('Podcast: Leonard Susskind: Quantum Mechanics, String Theory and Black Holes | Lex Fridman Podcast #41', '122:831', ' That is a big question in physics right now.', 2374.9, 2377.6200000000003, 0.8022704628640559)

**Readable Result:**
| Podcast name | Segment ID | Segment raw text | Start time | Stop time | Embedding distance |
|  --- | --- | --- | --- | --- | --- |
| Podcast: George Hotz: Hacking the Simulation & Learning to Drive with Neural Nets &#124; Lex Fridman Podcast #132 | 308:144 |  I mean, we don't understand dark energy, right? | 500.440 | 502.600 | 0.668 |
| Podcast: Lex Fridman: Ask Me Anything - AMA January 2021 &#124; Lex Fridman Podcast | 243:273 |  Like, what's up with this dark matter and dark energy stuff? | 946.220 | 950.120 | 0.736 |
| Podcast: Katherine de Kleer: Planets, Moons, Asteroids & Life in Our Solar System &#124; Lex Fridman Podcast #184 | 196:685 |  being like, what the hell is dark matter and dark energy? | 2591.720 | 2595.960 | 0.763 |
| Podcast: Alex Filippenko: Supernovae, Dark Energy, Aliens & the Expanding Universe &#124; Lex Fridman Podcast #137 | 51:36 |  Do we have any understanding of what the heck that thing is? | 216.000 | 219.000 | 0.792 |
| Podcast: Leonard Susskind: Quantum Mechanics, String Theory and Black Holes &#124; Lex Fridman Podcast #41 | 122:831 |  That is a big question in physics right now. | 2374.900 | 2377.620 | 0.802 |

## Q5
**Q5.** For each of the following podcast segments, find the five most similar podcast episodes. *Hint: You can do this by averaging over the embedding vectors within a podcast episode.*

<ol type="a">
<li>Segment "267:476"</li>
<li>Segment '48:511'</li>
<li>Segment '51:56'</li>
</ol>

### Q5.a
**Q5.a**: Find the five most similar podcast episodes to Segment "267:476".  
**Input:** "that if we were to meet alien life at some point"  
**SQL Query**:  
```sql
SELECT i.title as "Podcast title", i.dist as "Embedding Distance"
FROM
    (SELECT p.title, AVG(embedding) <->
        (SELECT embedding FROM podcast_segment
        WHERE id='267:476') as dist
    FROM 
        (SELECT * FROM podcast_segment
        WHERE podcast_id !=
            (SELECT podcast_id
            FROM podcast_segment
            WHERE id = '267:476')
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    GROUP BY p.title
    ) as i
ORDER BY i.dist
LIMIT 5;
```
**Output**:  
> ('Podcast: Sara Walker: The Origin of Life on Earth and Alien Worlds | Lex Fridman Podcast #198', 0.7828978136062058)  
> ('Podcast: Martin Rees: Black Holes, Alien Life, Dark Matter, and the Big Bang | Lex Fridman Podcast #305', 0.7879499391348677)  
> ('Podcast: Max Tegmark: Life 3.0 | Lex Fridman Podcast #1', 0.7886899314049058)  
> ('Podcast: Sean Carroll: The Nature of the Universe, Life, and Intelligence | Lex Fridman Podcast #26', 0.7890653704600481)  
> ('Podcast: Nick Bostrom: Simulation and Superintelligence | Lex Fridman Podcast #83', 0.7911210354871258)

**Readable Result:**
| Podcast title | Embedding Distance |
|  --- | --- |
| Podcast: Sara Walker: The Origin of Life on Earth and Alien Worlds &#124; Lex Fridman Podcast #198 | 0.783 |
| Podcast: Martin Rees: Black Holes, Alien Life, Dark Matter, and the Big Bang &#124; Lex Fridman Podcast #305 | 0.788 |
| Podcast: Max Tegmark: Life 3.0 &#124; Lex Fridman Podcast #1 | 0.789 |
| Podcast: Sean Carroll: The Nature of the Universe, Life, and Intelligence &#124; Lex Fridman Podcast #26 | 0.789 |
| Podcast: Nick Bostrom: Simulation and Superintelligence &#124; Lex Fridman Podcast #83 | 0.791 |

### Q5.b
**Q5.b**: Find the five most similar podcast episodes to Segment '48:511'.  
**Input:** "Is it is there something especially interesting and profound to you in terms of our current deep learning neural network, artificial neural network approaches and the whatever we do understand about the biological neural network."  
**SQL Query**:  
```sql
SELECT i.title as "Podcast title", i.dist as "Embedding Distance"
FROM
    (SELECT p.title, AVG(embedding) <->
        (SELECT embedding FROM podcast_segment
        WHERE id='48:511') as dist
    FROM 
        (SELECT * FROM podcast_segment
        WHERE podcast_id !=
            (SELECT podcast_id
            FROM podcast_segment
            WHERE id = '48:511')
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    GROUP BY p.title
    ) as i
ORDER BY i.dist
LIMIT 5;
```
**Output**:  
> ('Podcast: Christof Koch: Consciousness | Lex Fridman Podcast #2', 0.7537802160985114)  
> ('Podcast: Dileep George: Brain-Inspired AI | Lex Fridman Podcast #115', 0.7605152893560989)  
> ('Podcast: Tomaso Poggio: Brains, Minds, and Machines | Lex Fridman Podcast #13', 0.7615547981858913)  
> ('Podcast: Elon Musk: Neuralink, AI, Autopilot, and the Pale Blue Dot | Lex Fridman Podcast #49', 0.7761520759503151)  
> ('Podcast: Philip Goff: Consciousness, Panpsychism, and the Philosophy of Mind | Lex Fridman Podcast #261', 0.7872055032874042)

**Readable Result:**
| Podcast title | Embedding Distance |
|  --- | --- |
| Podcast: Christof Koch: Consciousness &#124; Lex Fridman Podcast #2 | 0.754 |
| Podcast: Dileep George: Brain-Inspired AI &#124; Lex Fridman Podcast #115 | 0.761 |
| Podcast: Tomaso Poggio: Brains, Minds, and Machines &#124; Lex Fridman Podcast #13 | 0.762 |
| Podcast: Elon Musk: Neuralink, AI, Autopilot, and the Pale Blue Dot &#124; Lex Fridman Podcast #49 | 0.776 |
| Podcast: Philip Goff: Consciousness, Panpsychism, and the Philosophy of Mind &#124; Lex Fridman Podcast #261 | 0.787 |

### Q5.c
**Q5.c**: Find the five most similar podcast episodes to Segment '51:56'.  
**Input**: "But what about like the fundamental physics of dark energy? Is there any understanding of what the heck it is?"   
**SQL Query**:  
```sql
SELECT i.title as "Podcast title", i.dist as "Embedding Distance"
FROM
    (SELECT p.title, AVG(embedding) <->
        (SELECT embedding FROM podcast_segment
        WHERE id='51:56') as dist
    FROM 
        (SELECT * FROM podcast_segment
        WHERE podcast_id !=
            (SELECT podcast_id
            FROM podcast_segment
            WHERE id = '51:56')
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    GROUP BY p.title
    ) as i
ORDER BY i.dist
LIMIT 5;
```
**Output**:  
> ('Podcast: Sean Carroll: Quantum Mechanics and the Many-Worlds Interpretation | Lex Fridman Podcast #47', 0.7767144344304333)  
> ('Podcast: Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe | Lex Fridman Podcast #124', 0.8080714284866961)  
> ('Podcast: Donald Hoffman: Reality is an Illusion - How Evolution Hid the Truth | Lex Fridman Podcast #293', 0.8165829480979995)  
> ('Podcast: Cumrun Vafa: String Theory | Lex Fridman Podcast #204', 0.8173474448880219)  
> ('Podcast: Avi Loeb: Aliens, Black Holes, and the Mystery of the Oumuamua | Lex Fridman Podcast #154', 0.8254520536023432)

**Readable Result:**
| Podcast title | Embedding Distance |
|  --- | --- |
| Podcast: Sean Carroll: Quantum Mechanics and the Many-Worlds Interpretation &#124; Lex Fridman Podcast #47 | 0.777 |
| Podcast: Stephen Wolfram: Fundamental Theory of Physics, Life, and the Universe &#124; Lex Fridman Podcast #124 | 0.808 |
| Podcast: Donald Hoffman: Reality is an Illusion - How Evolution Hid the Truth &#124; Lex Fridman Podcast #293 | 0.817 |
| Podcast: Cumrun Vafa: String Theory &#124; Lex Fridman Podcast #204 | 0.817 |
| Podcast: Avi Loeb: Aliens, Black Holes, and the Mystery of the Oumuamua &#124; Lex Fridman Podcast #154 | 0.825 |

## Q6
**Q6.** For podcast episode id = VeH7qKZr0WI, find the five most similar podcast episodes. *Hint: you can do a similar averaging procedure as Q5*  
**Input**: Podcast: Balaji Srinivasan: How to Fix Government, Twitter, Science, and the FDA | Lex Fridman Podcast #331  
**SQL Query**:  
```sql
SELECT i.title as "Podcast title", i.dist as "Embedding Distance"
FROM
    (SELECT p.title, AVG(embedding) <->
        (SELECT AVG(embedding)
        FROM podcast_segment
        INNER JOIN podcast
        ON podcast_id = podcast.id
        WHERE podcast_id='VeH7qKZr0WI'
        GROUP BY podcast_id) as dist
    FROM 
        (SELECT * FROM podcast_segment
        WHERE podcast_id != 'VeH7qKZr0WI'
        ) as ps
    INNER JOIN podcast as p
    ON p.id = ps.podcast_id
    GROUP BY p.title
    ) as i
ORDER BY i.dist
LIMIT 5;
```
**Output**:  
> ('Podcast: Tyler Cowen: Economic Growth & the Fight Against Conformity & Mediocrity | Lex Fridman Podcast #174', 0.11950103776872197)  
> ('Podcast: Eric Weinstein: Difficult Conversations, Freedom of Speech, and Physics | Lex Fridman Podcast #163', 0.1257139025632404)  
> ('Podcast: Michael Malice and Yaron Brook: Ayn Rand, Human Nature, and Anarchy | Lex Fridman Podcast #178', 0.12842690324343972)  
> ('Podcast: Steve Keen: Marxism, Capitalism, and Economics | Lex Fridman Podcast #303', 0.12916269225753493)  
> ('Podcast: Michael Malice: The White Pill, Freedom, Hope, and Happiness Amidst Chaos | Lex Fridman Podcast #150', 0.13040864953585687)

**Readable Result:**
| Podcast title | Embedding Distance |
|  --- | --- |
| Podcast: Tyler Cowen: Economic Growth & the Fight Against Conformity & Mediocrity &#124; Lex Fridman Podcast #174 | 0.120 |
| Podcast: Eric Weinstein: Difficult Conversations, Freedom of Speech, and Physics &#124; Lex Fridman Podcast #163 | 0.126 |
| Podcast: Michael Malice and Yaron Brook: Ayn Rand, Human Nature, and Anarchy &#124; Lex Fridman Podcast #178 | 0.128 |
| Podcast: Steve Keen: Marxism, Capitalism, and Economics &#124; Lex Fridman Podcast #303 | 0.129 |
| Podcast: Michael Malice: The White Pill, Freedom, Hope, and Happiness Amidst Chaos &#124; Lex Fridman Podcast #150 | 0.130 |
