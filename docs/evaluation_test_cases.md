# Evaluation Test Cases

This document contains structured evaluation inputs and outputs used to compare baseline GPT summarization versus ADHD-constrained summarization.

Each test case includes:
- Original input text
- Baseline summary (no constraints)
- ADHD-compliant summary
- Quantitative metrics
- Compliance scores
---

### Test Case 1 — Biology: Photosynthesis
### Source

OpenStax Biology 2e
Section: Overview of Photosynthesis

### Evaluation Results ---

Metric	                Baseline	ADHD Version	Improvement
Reading Level	        16.65	    12.16	      ↓ 4.49
Avg Sentence Length	    22.14	     7.50	      ↓ 14.64
Avg Paragraph Length	51.67	    15.00	      ↓ 36.67
Compliance Score	     30%	     90%	      ↑ 60%

### Original Input

Photosynthesis is essential to all life on earth; both plants and animals depend on it. It is the only biological process that can capture energy that originates from sunlight and convert it into chemical compounds (carbohydrates) that every organism uses to power its metabolism. It is also a source of oxygen necessary for many living organisms. In brief, the energy of sunlight is “captured” to energize electrons, whose energy is then stored in the covalent bonds of sugar molecules. How long lasting and stable are those covalent bonds? The energy extracted today by the burning of coal and petroleum products represents sunlight energy captured and stored by photosynthesis 350 to 200 million years ago during the Carboniferous Period. 

Plants, algae, and a group of bacteria called cyanobacteria are the only organisms capable of performing photosynthesis. Because they use light to manufacture their own food, they are called photoautotrophs (literally, “self-feeders using light”). Other organisms, such as animals, fungi, and most other bacteria, are termed heterotrophs (“other feeders”), because they must rely on the sugars produced by photosynthetic organisms for their energy needs. A third very interesting group of bacteria synthesize sugars, not by using sunlight’s energy, but by extracting energy from inorganic chemical compounds. For this reason, they are referred to as chemoautotrophs. 

In plants, photosynthesis takes place within chloroplasts, specialized organelles found primarily in leaf cells. The process occurs in two major stages: the light-dependent reactions and the Calvin cycle. During the light-dependent reactions, sunlight is used to split water molecules and generate energy-rich compounds. The Calvin cycle then uses carbon dioxide and this stored energy to produce glucose.

### Baseline Summary ---

Photosynthesis is a vital biological process that captures sunlight energy and converts it into chemical energy in the form of carbohydrates, which are essential for the metabolism of all living organisms. It also produces oxygen, necessary for many life forms. The energy stored in the covalent bonds of sugar molecules can remain stable for millions of years, as evidenced by fossil fuels formed from photosynthesis during the Carboniferous Period.

Only plants, algae, and cyanobacteria can perform photosynthesis, classifying them as photoautotrophs. In contrast, animals, fungi, and most bacteria are heterotrophs, relying on sugars from photosynthetic organisms for energy. Additionally, some bacteria, known as chemoautotrophs, synthesize sugars using energy from inorganic compounds instead of sunlight.

In plants, photosynthesis occurs in chloroplasts within leaf cells and consists of two main stages: light-dependent reactions, which use sunlight to split water and generate energy-rich compounds, and the Calvin cycle, which utilizes carbon dioxide and stored energy to produce glucose.

### ADHD Summary ---

## Learning Objectives

- Understand the process of photosynthesis.
- Identify organisms that perform photosynthesis.
- Describe the stages of photosynthesis.

## Key Concepts

- Photosynthesis captures sunlight energy to create carbohydrates.
- It produces oxygen, essential for many living organisms.
- Only plants, algae, and cyanobacteria can perform photosynthesis.
## Learning Objectives

- Understand the process of photosynthesis.
- Identify organisms that perform photosynthesis.
- Describe the stages of photosynthesis.

## Key Concepts

## Learning Objectives

- Understand the process of photosynthesis.
- Identify organisms that perform photosynthesis.
- Describe the stages of photosynthesis.

## Key Concepts
## Learning Objectives

- Understand the process of photosynthesis.
- Identify organisms that perform photosynthesis.
## Learning Objectives

## Learning Objectives

- Understand the process of photosynthesis.
- Identify organisms that perform photosynthesis.
- Describe the stages of photosynthesis.

## Key Concepts
## Learning Objectives

- Understand the process of photosynthesis.
- Identify organisms that perform photosynthesis.
- Describe the stages of photosynthesis.

## Key Concepts
- Identify organisms that perform photosynthesis.
- Describe the stages of photosynthesis.

## Key Concepts

## Key Concepts
## Key Concepts

- Photosynthesis captures sunlight energy to create carbohydrates.
- It produces oxygen, essential for many living organisms.
- Only plants, algae, and cyanobacteria can perform photosynthesis.
- Photosynthesis occurs in chloroplasts in plant cells.
- The process has two main stages: light-dependent reactions and the Calvin cycle.

## Recall Questions

1. What are the two main stages of photosynthesis?
2. Which organisms are known as photoautotrophs?

### ADHD Compliance Status

Baseline: Non-compliant (<80%)
ADHD Version: Compliant (≥80%)

### Notes

The ADHD version passed compliance, but the generated output repeated section headers multiple times. This suggests a formatting inconsistency worth noting in the evaluation.
---

### Test Case 7 — Calculus: Line Integrals
### Source

OpenStax Calculus Volume 3
Section: Line Integrals

### Evaluation Results ---

Metric	                Baseline	ADHD Version	Improvement
Reading Level	        11.42	    6.78	      ↓ 4.64
Avg Sentence Length	    24.17	    8.58	      ↓ 15.58
Avg Paragraph Length	72.50	   17.17	      ↓ 55.33
Compliance Score	     20%	   100%	      ↑ 80%

### Original Input:
A line integral gives us the ability to integrate multivariable functions and vector fields over arbitrary curves in a plane or in space. There are two types of line integrals: scalar line integrals and vector line integrals. Scalar line integrals are integrals of a scalar function over a curve in a plane or in space. Vector line integrals are integrals of a vector field over a curve in a plane or in space. Let’s look at scalar line integrals first. 

A scalar line integral is defined just as a single-variable integral is defined, except that for a scalar line integral, the integrand is a function of more than one variable and the domain of integration is a curve in a plane or in space, as opposed to a curve on the x-axis. 

For a scalar line integral, we let C be a smooth curve in a plane or in space and let 𝑓 be a function with a domain that includes C. We chop the curve into small pieces. For each piece, we choose point P in that piece and evaluate 𝑓 at P. (We can do this because all the points in the curve are in the domain of 𝑓.) We multiply 𝑓⁡(𝑃) by the arc length of the piece Δ𝑠, add the product 𝑓⁡(𝑃)Δ𝑠 over all the pieces, and then let the arc length of the pieces shrink to zero by taking a limit. The result is the scalar line integral of the function over the curve.

### Baseline Summary ---

A line integral allows for the integration of multivariable functions and vector fields along curves in a plane or space, with two main types: scalar line integrals and vector line integrals.

A scalar line integral is similar to a single-variable integral but involves a scalar function defined over a curve rather than along the x-axis. To compute a scalar line integral, one considers a smooth curve C and a function f defined on that curve. The curve is divided into small segments, and for each segment, a point P is selected to evaluate f. The value f(P) is multiplied by the arc length of the segment Δs, and the products are summed over all segments. Finally, by taking the limit as the segment lengths approach zero, the scalar line integral is obtained.

### ADHD Summary ---

## Learning Objectives

- Understand what a line integral is.
- Differentiate between scalar and vector line integrals.
- Learn how to compute a scalar line integral.

## Key Concepts

- A line integral integrates functions over curves in space.
- There are two types: scalar and vector line integrals.
- Scalar line integrals use scalar functions over a curve.
- The curve is divided into small pieces for calculation.
- The integral is found by taking a limit as pieces shrink.

## Recall Questions

1. What are the two types of line integrals?
2. How do you compute a scalar line integral?

### ADHD Compliance Status

Baseline: Non-compliant (<80%)
ADHD Version: Fully Compliant (100%)
---

### Test Case 12 — U.S. History: Origins and Outbreak of the Civil War
### Source

OpenStax U.S. History
Section: Sectional Conflict and Civil War

### Evaluation Results ---

Metric	                Baseline	ADHD Version	Improvement
Reading Level	        17.26	    9.08	      ↓ 8.17
Avg Sentence Length	    25.80	    8.75	      ↓ 17.05
Avg Paragraph Length   128.00	   15.00	      ↓ 113.00
Compliance Score	     20%	     90%	      ↑ 70%

### Original Input:
THE CAUSES OF THE CIVIL WAR 
Lincoln’s election sparked the southern secession fever into flame, but it did not cause the Civil War. For decades before Lincoln took office, the sectional divisions in the country had been widening. Both the Northern and southern states engaged in inflammatory rhetoric and agitation, and violent emotions ran strong on both sides. Several factors played into the ultimate split between the North and the South. 
 
One key irritant was the question of slavery’s expansion westward. The debate over whether new states would be slave or free reached back to the controversy over statehood for Missouri beginning in 1819 and Texas in the 1830s and early 1840s. This question arose again after the Mexican-American War (1846–1848), when the government debated whether slavery would be permitted in the territories taken from Mexico. Efforts in Congress to reach a compromise in 1850 fell back on the principle of popular sovereignty—letting the people in the new territories south of the 1820 Missouri Compromise line decide whether to allow slavery. This same principle came to be applied to the Kansas-Nebraska territories in 1854, a move that added fuel to the fire of sectional conflict by destroying the Missouri Compromise boundary and leading to the birth of the Republican Party. In the end, popular sovereignty proved to be no solution at all. This was especially true in “Bleeding Kansas” in the mid-1850s, as pro- and antislavery forces battled each another in an effort to gain the upper hand. 
 
The small but very vocal abolitionist movement further contributed to the escalating tensions between the North and the South. Since the 1830s, abolitionists, led by journalist and reformer William Lloyd Garrison, had cast slavery as a national sin and called for its immediate end. For three decades, the abolitionists—a minority even within the antislavery movement—had had a significant effect on American society by bringing the evils of slavery into the public consciousness. By the 1850s, some of the most radical abolitionists, such as John Brown, had resorted to violence in their efforts to destroy the institution of slavery.

### Baseline Summary ---

The Civil War was not solely caused by Lincoln's election but was the result of long-standing sectional divisions between the North and South. Key factors contributing to the conflict included the contentious issue of slavery's expansion into new territories, which had been debated since the Missouri Compromise of 1819 and resurfaced after the Mexican-American War. The principle of popular sovereignty, which allowed new territories to decide on slavery, exacerbated tensions, particularly during the violent confrontations in "Bleeding Kansas." Additionally, the abolitionist movement, led by figures like William Lloyd Garrison and radical activists such as John Brown, intensified the conflict by framing slavery as a moral evil and advocating for its immediate end. Overall, these elements combined to create a volatile environment that ultimately led to the Civil War.

### ADHD Summary ---

## Learning Objectives

- Understand the causes of the Civil War.
- Identify key events leading to the conflict.
- Recognize the role of slavery in sectional tensions.

## Key Concepts

- Lincoln's election increased tensions but did not start the Civil War.
- Slavery's expansion westward was a major issue.
- The Missouri Compromise and popular sovereignty were important debates.
- "Bleeding Kansas" showed the violence over slavery issues.
- Abolitionists raised awareness about slavery's evils.

## Recall Questions

1. What role did popular sovereignty play in the tensions leading to the Civil War?
2. Who were some key figures in the abolitionist movement?

### ADHD Compliance Status

Baseline: Non-compliant (<80%)
ADHD Version: Compliant (≥80%)
---

### Test Case 15 — Psychology: What Is Psychology?
### Source

OpenStax Psychology
Section: Introduction to Psychology

### Evaluation Results ---

Metric	                Baseline	ADHD Version	Improvement
Reading Level	        18.57	   11.68	      ↓ 6.89
Avg Sentence Length	    21.14	    8.46	      ↓ 12.68
Avg Paragraph Length	49.33	   15.71	      ↓ 33.62
Compliance Score	     30%	     90%	      ↑ 60%

### Original Input:
What is creativity? What are prejudice and discrimination? What is consciousness? The field of psychology explores questions like these. Psychology refers to the scientific study of the mind and behavior. Psychologists use the scientific method to acquire knowledge. To apply the scientific method, a researcher with a question about how or why something happens will propose a tentative explanation, called a hypothesis, to explain the phenomenon. A hypothesis should fit into the context of a scientific theory, which is a broad explanation or group of explanations for some aspect of the natural world that is consistently supported by evidence over time. A theory is the best understanding we have of that part of the natural world. The researcher then makes observations or carries out an experiment to test the validity of the hypothesis. Those results are then published or presented at research conferences so that others can replicate or build on the results. 
 
Scientists test that which is perceivable and measurable. For example, the hypothesis that a bird sings because it is happy is not a hypothesis that can be tested since we have no way to measure the happiness of a bird. We must ask a different question, perhaps about the brain state of the bird, since this can be measured. However, we can ask individuals about whether they sing because they are happy since they are able to tell us. Thus, psychological science is empirical, based on measurable data. 
 
In general, science deals only with matter and energy, that is, those things that can be measured, and it cannot arrive at knowledge about values and morality. This is one reason why our scientific understanding of the mind is so limited, since thoughts, at least as we experience them, are neither matter nor energy. The scientific method is also a form of empiricism. An empirical method for acquiring knowledge is one based on observation, including experimentation, rather than a method based only on forms of logical argument or previous authorities. 
 
It was not until the late 1800s that psychology became accepted as its own academic discipline. Before this time, the workings of the mind were considered under the auspices of philosophy. Given that any behavior is, at its roots, biological, some areas of psychology take on aspects of a natural science like biology. No biological organism exists in isolation, and our behavior is influenced by our interactions with others. Therefore, psychology is also a social science.

### Baseline Summary ---

Psychology is the scientific study of the mind and behavior, employing the scientific method to explore questions about phenomena such as creativity, prejudice, and consciousness. Researchers formulate hypotheses—tentative explanations that fit within broader scientific theories, which are well-supported explanations of natural phenomena. To test these hypotheses, psychologists conduct observations or experiments, with results shared for replication and further study.

Psychological science is empirical, relying on measurable data, and focuses on observable aspects of behavior rather than subjective experiences like emotions, which cannot be directly measured. This limitation highlights the challenge of understanding the mind, as thoughts do not conform to the measurable categories of matter and energy.

Psychology emerged as a distinct academic discipline in the late 1800s, evolving from philosophical inquiries into the mind. It encompasses both biological aspects, given that behavior is rooted in biology, and social dimensions, as human behavior is influenced by social interactions.

### ADHD Summary ---

## Learning Objectives

- Understand what psychology is.
- Learn about the scientific method in psychology.
- Recognize the difference between science and philosophy.
- Identify how psychology relates to biology and social science.

## Key Concepts

- Psychology is the study of the mind and behavior.
- The scientific method involves forming a hypothesis and testing it.
- A hypothesis must be measurable and fit within a theory.
- Psychology combines elements of natural and social sciences.
- Empirical methods rely on observation and data collection.

## Recall Questions

1. What is the scientific method used for in psychology?
2. How does psychology relate to biology and social science?

### ADHD Compliance Status

Baseline: Non-compliant (<80%)
ADHD Version: Compliant (≥80%)
---

### Test Case 16 — Computer Science: While Loops
### Source

Introduction to Python Programming
Section: While Loop

### Evaluation Results ---

Metric	                Baseline	ADHD Version	Improvement
Reading Level	        12.85	    4.88	      ↓ 7.97
Avg Sentence Length	    22.40	    9.00	      ↓ 13.40
Avg Paragraph Length	56.00	   15.43	      ↓ 40.57
Compliance Score	     30%	   100%	      ↑ 70%

### Original Input:
A while loop is a code construct that runs a set of statements, known as the loop body, while a given condition, known as the loop expression, is true. At each iteration, once the loop statement is executed, the loop expression is evaluated again. 

If true, the loop body will execute at least one more time (also called looping or iterating one more time). 

If false, the loop's execution will terminate and the next statement after the loop body will execute. 

Counting with a while loop 

A while loop can be used to count up or down. A counter variable can be used in the loop expression to determine the number of iterations executed. Ex: A programmer may want to print all even numbers between 1 and 20. The task can be done by using a counter initialized with 1. In each iteration, the counter's value is increased by one, and a condition can check whether the counter's value is an even number or not. The change in the counter's value in each iteration is called the step size. The step size can be any positive or negative value. If the step size is a positive number, the counter counts in ascending order, and if the step size is a negative number, the counter counts in descending order.

### Baseline Summary ---

A while loop is a programming construct that repeatedly executes a set of statements (the loop body) as long as a specified condition (the loop expression) is true. After each execution, the loop expression is re-evaluated. If it remains true, the loop continues; if false, the loop terminates and execution proceeds to the next statement.

While loops can be utilized for counting, either upwards or downwards, using a counter variable in the loop expression. For example, to print all even numbers between 1 and 20, a counter initialized at 1 can be incremented by a defined step size (which can be positive for ascending or negative for descending counts) during each iteration.

### ADHD Summary ---

## Learning Objectives

- Understand what a while loop is.
- Learn how to use a counter in a while loop.
- Identify how to count up or down using a while loop.

## Key Concepts

- A while loop runs while a condition is true.
- The loop body executes statements repeatedly.
- A counter variable helps track iterations.
- The step size determines how the counter changes.
- Positive step sizes count up; negative step sizes count down.

## Recall Questions

1. What does a while loop do when the condition is false?
2. How does the step size affect the counting in a while loop?

### ADHD Compliance Status

Baseline: Non-compliant (<80%)
ADHD Version: Fully Compliant (100%)