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

### Evaluation Results 

Metric	                   Baseline	  ADHD Version	  Improvement
Reading Level (FK Grade)	16.53	     15.29          ↓ 1.24
Avg Sentence Length	        21.5	     7.5	        ↓ 14.0
Avg Paragraph Length	    57.33	     15.0	        ↓ 42.33
Compliance Score	         30%	     90%	        ↑ 60%

### Original Input

Photosynthesis is essential to all life on earth; both plants and animals depend on it. It is the only biological process that can capture energy that originates from sunlight and convert it into chemical compounds (carbohydrates) that every organism uses to power its metabolism. It is also a source of oxygen necessary for many living organisms. In brief, the energy of sunlight is “captured” to energize electrons, whose energy is then stored in the covalent bonds of sugar molecules. How long lasting and stable are those covalent bonds? The energy extracted today by the burning of coal and petroleum products represents sunlight energy captured and stored by photosynthesis 350 to 200 million years ago during the Carboniferous Period. 

Plants, algae, and a group of bacteria called cyanobacteria are the only organisms capable of performing photosynthesis. Because they use light to manufacture their own food, they are called photoautotrophs (literally, “self-feeders using light”). Other organisms, such as animals, fungi, and most other bacteria, are termed heterotrophs (“other feeders”), because they must rely on the sugars produced by photosynthetic organisms for their energy needs. A third very interesting group of bacteria synthesize sugars, not by using sunlight’s energy, but by extracting energy from inorganic chemical compounds. For this reason, they are referred to as chemoautotrophs. 

In plants, photosynthesis takes place within chloroplasts, specialized organelles found primarily in leaf cells. The process occurs in two major stages: the light-dependent reactions and the Calvin cycle. During the light-dependent reactions, sunlight is used to split water molecules and generate energy-rich compounds. The Calvin cycle then uses carbon dioxide and this stored energy to produce glucose. 

### Baseline Summary

Photosynthesis is a crucial biological process that captures sunlight energy and converts it into chemical energy stored in carbohydrates, which are essential for the metabolism of all organisms. It also produces oxygen, vital for many life forms. The energy stored in the covalent bonds of sugar molecules during photosynthesis can last for millions of years, as evidenced by fossil fuels formed from ancient photosynthetic activity.

Only plants, algae, and cyanobacteria can perform photosynthesis, classifying them as photoautotrophs. In contrast, animals, fungi, and most bacteria are heterotrophs, relying on the sugars produced by photoautotrophs for energy. Additionally, some bacteria, known as chemoautotrophs, synthesize sugars using energy from inorganic compounds instead of sunlight.

Photosynthesis is significant not only for energy capture but also for its role in storing solar energy in carbohydrate bonds, which heterotrophs use to produce ATP through respiration. This process underpins 99 percent of Earth's ecosystems, illustrating the interconnected energy flow from sunlight to various trophic levels, exemplified by the energy transfer from vegetation to herbivores and then to top predators.

### ADHD-Constrained Summary
Learning Objectives

Understand the process of photosynthesis.

Identify organisms that perform photosynthesis.

Recognize the importance of photosynthesis in ecosystems.

### Key Concepts

Photosynthesis captures sunlight and converts it into chemical energy.

Only plants, algae, and cyanobacteria can perform photosynthesis.

Organisms that cannot perform photosynthesis are called heterotrophs.

Photosynthesis powers 99% of Earth's ecosystems.

Carbohydrates produced by photosynthesis are energy sources for other organisms.

### Recall Questions

What organisms are capable of performing photosynthesis?

Why is photosynthesis important for ecosystems?

### ADHD Compliance Status

Baseline: Non-compliant (<80%)
ADHD Version: Compliant (≥80%)

---

### Test Case 2 — Physics: Introduction to Dynamics
### Source

OpenStax College Physics 2e
Section: Introduction to Dynamics

### Evaluation Results
Metric	                  Baseline   ADHD Version	Improvement
Reading Level (FK Grade)	17.86	    12.62	      ↓ 5.24
Avg Sentence Length	        24.0	    8.33          ↓ 15.67
Avg Paragraph Length	    120.0       16.67         ↓ 103.33
Compliance Score	         20%	     90%	      ↑ 70%

### Original Input 

Motion draws our attention. Motion itself can be beautiful, causing us to marvel at the forces needed to achieve spectacular motion, such as that of a dolphin jumping out of the water, or a pole vaulter, or the flight of a bird, or the orbit of a satellite. The study of motion is kinematics, but kinematics only describes the way objects move—their velocity and their acceleration. Dynamics considers the forces that affect the motion of moving objects and systems. Newton’s laws of motion are the foundation of dynamics. These laws provide an example of the breadth and simplicity of principles under which nature functions. They are also universal laws in that they apply to similar situations on Earth as well as in space. 

Isaac Newton’s (1642–1727) laws of motion were just one part of the monumental work that has made him legendary. The development of Newton’s laws marks the transition from the Renaissance into the modern era. This transition was characterized by a revolutionary change in the way people thought about the physical universe. For many centuries natural philosophers had debated the nature of the universe based largely on certain rules of logic with great weight given to the thoughts of earlier classical philosophers such as Aristotle (384–322 BC). Among the many great thinkers who contributed to this change were Newton and Galileo. 

Galileo was instrumental in establishing observation as the absolute determinant of truth, rather than “logical” argument. Galileo’s use of the telescope was his most notable achievement in demonstrating the importance of observation. He discovered moons orbiting Jupiter and made other observations that were inconsistent with certain ancient ideas and religious dogma. For this reason, and because of the manner in which he dealt with those in authority, Galileo was tried by the Inquisition and punished. He spent the final years of his life under a form of house arrest. Because others before Galileo had also made discoveries by observing the nature of the universe, and because repeated observations verified those of Galileo, his work could not be suppressed or denied. After his death, his work was verified by others, and his ideas were eventually accepted by the church and scientific communities. 

### Baseline Summary

The study of motion, known as kinematics, focuses on how objects move, including their velocity and acceleration. In contrast, dynamics examines the forces influencing motion, grounded in Newton's laws of motion, which are universal principles applicable both on Earth and in space. Isaac Newton's contributions, alongside those of Galileo, marked a pivotal shift from Renaissance thought to modern scientific understanding. Galileo emphasized observation over logical reasoning, using the telescope to make groundbreaking discoveries, such as the moons of Jupiter, which challenged established beliefs. His conflict with authority led to his trial and house arrest, but his observations were eventually validated and accepted by both the church and the scientific community, solidifying the importance of empirical evidence in understanding the universe.

### ADHD-Constrained Summary
### Learning Objectives

Understand the concepts of motion, kinematics, and dynamics.

Learn about Newton's laws of motion.

Recognize Galileo's contributions to science and observation.

### Key Concepts

Motion captures our attention and can be beautiful.

Kinematics describes how objects move.

Dynamics studies the forces affecting motion.

Newton's laws are fundamental to physics.

Galileo emphasized observation in science.

### Recall Questions

What is the difference between kinematics and dynamics?

Why was Galileo's work significant?

### ADHD Compliance Status

Baseline: Non-compliant
ADHD Version: Compliant

---

### Test Case 3 — Physics: Newton’s First Law (Inertia)
### Source

OpenStax College Physics 2e
Section: Newton’s First Law of Motion

### Evaluation Results
Metric	                   Baseline	 ADHD Version	Improvement
Reading Level (FK Grade)	15.34	     7.65	      ↓ 7.69
Avg Sentence Length	        23.33	     11.25	      ↓ 12.08
Avg Paragraph Length	    70.0	     19.29	      ↓ 50.71
Compliance Score	         30%	      90%	      ↑ 60%

### Original Input
Newton’s first law is completely general and can be applied to anything from an object sliding on a table to a satellite in orbit to blood pumped from the heart. Experiments have thoroughly verified that any change in velocity (speed or direction) must be caused by an external force. The idea of generally applicable or universal laws is important not only here—it is a basic feature of all laws of physics. Identifying these laws is like recognizing patterns in nature from which further patterns can be discovered. The genius of Galileo, who first developed the idea for the first law, and Newton, who clarified it, was to ask the fundamental question, “What is the cause?” Thinking in terms of cause and effect is a worldview fundamentally different from the typical ancient Greek approach when questions such as “Why does a tiger have stripes?” would have been answered in Aristotelian fashion, “That is the nature of the beast.” True perhaps, but not a useful insight. 

The property of a body to remain at rest or to remain in motion with constant velocity is called inertia. Newton’s first law is often called the law of inertia. As we know from experience, some objects have more inertia than others. It is obviously more difficult to change the motion of a large boulder than that of a basketball, for example. The inertia of an object is measured by its mass. Roughly speaking, mass is a measure of the amount of “stuff” (or matter) in something. The quantity or amount of matter in an object is determined by the numbers of atoms and molecules of various types it contains. Unlike weight, mass does not vary with location. The mass of an object is the same on Earth, in orbit, or on the surface of the Moon. In practice, it is very difficult to count and identify all of the atoms and molecules in an object, so masses are not often determined in this manner. Operationally, the masses of objects are determined by comparison with the standard kilogram. 

### Baseline Summary

Newton's first law, also known as the law of inertia, states that an object will remain at rest or in uniform motion unless acted upon by an external force. This principle applies universally across contexts. Inertia, the tendency of an object to resist changes in motion, depends on mass. Larger masses exhibit more inertia than smaller ones. Mass is constant regardless of location and is measured by comparison to a standard kilogram.

### ADHD-Constrained Summary
Learning Objectives

Understand Newton's first law.

Learn about inertia.

Connect mass to motion.

### Key Concepts

An object stays at rest or constant motion unless a force acts on it.

Inertia resists changes in motion.

Larger mass means greater inertia.

Mass is constant everywhere.

Mass is measured using a standard kilogram.

### Recall Questions

What is inertia?

How does mass relate to inertia?


### ADHD Compliance Status

Baseline: Non-compliant
ADHD Version: Compliant

--- 

### Test Case 4 — Chemistry: Atomic Structure & Symbolism
### Source

OpenStax Chemistry
Section: Atomic Structure

### Evaluation Results
Metric	                  Baseline	ADHD Version	Improvement
Reading Level (FK Grade)	9.62	    5.46	      ↓ 4.16
Avg Sentence Length	        18.93	    7.93	      ↓ 11.00
Avg Paragraph Length	    87.0	    19.33	      ↓ 67.67
Compliance Score	         20%	    100%	      ↑ 80%

### Original Input:
The development of modern atomic theory revealed much about the inner structure of atoms. It was learned that an atom contains a very small nucleus composed of positively charged protons and uncharged neutrons, surrounded by a much larger volume of space containing negatively charged electrons. The nucleus contains the majority of an atom’s mass because protons and neutrons are much heavier than electrons, whereas electrons occupy almost all of an atom’s volume. The diameter of an atom is on the order of 10−10 m, whereas the diameter of the nucleus is roughly 10−15 m—about 100,000 times smaller. For a perspective about their relative sizes, consider this: If the nucleus were the size of a blueberry, the atom would be about the size of a football stadium. 

Atoms—and the protons, neutrons, and electrons that compose them—are extremely small. For example, a carbon atom weighs less than 2 × 10−23 g, and an electron has a charge of less than 2 × 10−19 C (coulomb). When describing the properties of tiny objects such as atoms, we use appropriately small units of measure, such as the unified atomic mass unit (u) and the fundamental unit of charge (e). The unified atomic mass unit is defined as exactly 1/12 of the mass of a single atom of the carbon-12 isotope (more on isotopes is provided later in this section) and is equal to 1.6605 × 10−24 g. The dalton (Da) is an alternative mass unit that is equivalent to the u. Many literature resources, including this text, use the older term atomic mass unit (amu) when referring to the u or the Da. The fundamental unit of charge (also called the elementary charge) equals the magnitude of the charge of an electron (e) with e = 1.602 × 10−19 C. 

A proton has a mass of 1.0073 amu and a charge of 1+. A neutron is a slightly heavier particle with a mass 1.0087 amu and a charge of zero; as its name suggests, it is neutral. The electron has a charge of 1− and is a much lighter particle with a mass of about 0.00055 amu (it would take about 1800 electrons to equal the mass of one proton). The properties of these fundamental particles are summarized in Table 2.2. (An observant student might notice that the sum of an atom’s subatomic particles does not equal the atom’s actual mass: The total mass of six protons, six neutrons, and six electrons is 12.0993 amu, slightly larger than 12.00 amu. This “missing” mass is known as the mass defect, and you will learn about it in the chapter on nuclear chemistry.) 

### Baseline Summary

The modern atomic theory describes the structure of atoms, which consist of a small nucleus made up of positively charged protons and neutral neutrons, surrounded by a larger volume of space occupied by negatively charged electrons. The nucleus contains most of the atom's mass, while electrons occupy nearly all of its volume. Atoms have a diameter of about 10^-10 meters, with the nucleus being roughly 10^-15 meters in diameter—about 100,000 times smaller. For perspective, if the nucleus were the size of a blueberry, the entire atom would be the size of a football stadium. 

Atoms are extremely small; for instance, a carbon atom weighs less than 2 × 10^-23 grams, and an electron has a charge of less than 2 × 10^-19 coulombs. Small units of measure, such as the unified atomic mass unit (u) and the fundamental unit of charge (e), are used to describe these properties. The unified atomic mass unit is defined as 1/12 of the mass of a carbon-12 atom, equivalent to 1.6605 × 10^-24 grams. The equivalent mass unit, the dalton (Da), is often referred to as the atomic mass unit (amu).

The mass and charge of subatomic particles are as follows: a proton has a mass of 1.0073 amu and a charge of +1, a neutron has a mass of 1.0087 amu and no charge, and an electron has a mass of about 0.00055 amu and a charge of -1. Notably, the total mass of an atom's subatomic particles does not equal the atom's actual mass due to a phenomenon known as the mass defect. 

### ADHD-Constrained Summary
Learning Objectives

- Understand the structure of atoms. 

- Identify the components of atomic mass. 

- Learn about atomic measurements and units. 

### Key Concepts

- Atoms have a small nucleus with protons and neutrons. 

- Electrons surround the nucleus and occupy most of the atom's space. 

- The size of an atom is about 10−10 m; the nucleus is 10−15 m. 

- The unified atomic mass unit (u) is 1.6605 × 10−24 g. 

- A proton has a mass of 1.0073 amu; a neutron is 1.0087 amu. 

### Recall Questions

1. What are the three main particles that make up an atom?

2. How does the size of an atom compare to its nucleus? 

### ADHD Compliance Status

Baseline: Non-compliant
ADHD Version: Fully Compliant

---

### Test Case 5 — Chemistry: Ionic Bonding
### Source

OpenStax Chemistry
Section: Ionic Compounds

### Evaluation Results
Metric	                  Baseline	 ADHD Version	Improvement
Reading Level (FK Grade)	13.90	    10.00	      ↓ 3.89
Avg Sentence Length	        20.75	     7.92	      ↓ 12.83
Avg Paragraph Length	    55.33	    13.57	      ↓ 41.76
Compliance Score	         30%	     90%	      ↑ 60%

### Original Input:
Binary ionic compounds are composed of just two elements: a metal (which forms the cations) and a nonmetal (which forms the anions). For example, NaCl is a binary ionic compound. We can think about the formation of such compounds in terms of the periodic properties of the elements. Many metallic elements have relatively low ionization potentials and lose electrons easily. These elements lie to the left in a period or near the bottom of a group on the periodic table. Nonmetal atoms have relatively high electron affinities and thus readily gain electrons lost by metal atoms, thereby filling their valence shells. Nonmetallic elements are found in the upper-right corner of the periodic table. 

As all substances must be electrically neutral, the total number of positive charges on the cations of an ionic compound must equal the total number of negative charges on its anions. The formula of an ionic compound represents the simplest ratio of the numbers of ions necessary to give identical numbers of positive and negative charges. For example, the formula for aluminum oxide, Al2O3, indicates that this ionic compound contains two aluminum cations, Al3+, for every three oxide anions, O2− [thus, (2 × +3) + (3 × –2) = 0]. 

It is important to note, however, that the formula for an ionic compound does not represent the physical arrangement of its ions. It is incorrect to refer to a sodium chloride (NaCl) “molecule” because there is not a single ionic bond, per se, between any specific pair of sodium and chloride ions. The attractive forces between ions are isotropic—the same in all directions—meaning that any particular ion is equally attracted to all of the nearby ions of opposite charge. This results in the ions arranging themselves into a tightly bound, three-dimensional lattice structure. Sodium chloride, for example, consists of a regular arrangement of equal numbers of Na+ cations and Cl– anions (Figure 7.3). 

### Baseline Summary

Binary ionic compounds consist of two elements: a metal that forms cations and a nonmetal that forms anions, such as sodium chloride (NaCl). Metals, typically located on the left side or bottom of the periodic table, have low ionization potentials and easily lose electrons. In contrast, nonmetals, found in the upper-right corner, have high electron affinities and readily gain electrons, filling their valence shells. 

For an ionic compound to be electrically neutral, the total positive charges from cations must equal the total negative charges from anions. The formula of an ionic compound reflects the simplest ratio of these ions. For example, aluminum oxide (Al2O3) contains two Al3+ cations for every three O2− anions, balancing the charges.

It's crucial to understand that the formula does not indicate the physical arrangement of ions. Ionic compounds like NaCl do not exist as discrete molecules; instead, they form a three-dimensional lattice structure where each ion is equally attracted to surrounding ions of opposite charge, resulting in a tightly bound arrangement. 

### ADHD-Constrained Summary
## Learning Objectives 

- Understand what binary ionic compounds are. 

- Learn how to write formulas for ionic compounds. 

- Recognize the structure of ionic compounds. 

  

## Key Concepts 

- Binary ionic compounds have two elements: a metal and a nonmetal. 

- Metals form cations; nonmetals form anions. 

- Ionic compounds must be electrically neutral overall. 

- The formula shows the simplest ratio of ions. 

- Ionic compounds form a three-dimensional lattice structure. 


## Recall Questions 

1. What two types of elements make up binary ionic compounds?

2. Why must ionic compounds be electrically neutral? 


---

### Test Case 6 — Algebra & Trigonometry: Verifying Trigonometric Identities
### Source

OpenStax Algebra & Trigonometry
Section: Even–Odd Trigonometric Identities

### Evaluation Results --- 

Metric	                  Baseline	 ADHD Version	Improvement
Reading Level (FK Grade)	9.2	         9.78	    ↑ 0.58 
Avg Sentence Length	        9.08	     17.5	    ↑ 8.42 
Avg Paragraph Length	    39.33	     8.75	    ↓ 30.58
Compliance Score	         30%	      80%	    ↑ 50%

### Original Input:
For all 𝜃 in the domain of the sine and cosine functions, respectively, we can state the following: 

Since sin⁡(−𝜃)=−sin⁡𝜃, sine is an odd function. 

Since, cos⁡(−𝜃)=cos⁡𝜃, cosine is an even function. 

The other even-odd identities follow from the even and odd nature of the sine and cosine functions. For example, consider the tangent identity, tan⁡(−𝜃)=−tan𝜃. We can interpret the tangent of a negative angle as tan⁡(−𝜃)=sin⁡(−𝜃)cos⁡(−𝜃)=−sin⁡𝜃cos⁡𝜃=−tan⁡𝜃. Tangent is therefore an odd function, which means that tan⁡(−𝜃)=−tan⁡(𝜃) for all 𝜃 in the domain of the tangent function. 

The cotangent identity, cot⁡(−𝜃)=−cot⁡𝜃, also follows from the sine and cosine identities. We can interpret the cotangent of a negative angle as cot⁡(−𝜃)=cos⁡(−𝜃)sin⁡(−𝜃)=cos⁡𝜃−sin⁡𝜃=−cot⁡𝜃. Cotangent is therefore an odd function, which means that cot⁡(−𝜃)=−cot⁡(𝜃) for all 𝜃 in the domain of the cotangent function. 

The cosecant function is the reciprocal of the sine function, which means that the cosecant of a negative angle will be interpreted as csc⁡(−𝜃)=1sin⁡(−𝜃)=1−sin⁡𝜃=−csc⁡𝜃. The cosecant function is therefore odd. 

Finally, the secant function is the reciprocal of the cosine function, and the secant of a negative angle is interpreted as sec⁡(−𝜃)=1cos⁡(−𝜃)=1cos⁡𝜃=sec⁡𝜃. The secant function is therefore even. 

To sum up, only two of the trigonometric functions, cosine and secant, are even. The other four functions are odd, verifying the even-odd identities. 

### Baseline Summary --- 

This study material discusses the even-odd properties of trigonometric functions based on their behavior with negative angles: 

Sine Function: ( \sin(-\theta) = -\sin(\theta) ) - Sine is an odd function. 

Cosine Function: ( \cos(-\theta) = \cos(\theta) ) - Cosine is an even function. 

Tangent Function: ( \tan(-\theta) = -\tan(\theta) ) - Tangent is an odd function. 

Cotangent Function: ( \cot(-\theta) = -\cot(\theta) ) - Cotangent is an odd function. 

Cosecant Function: ( \csc(-\theta) = -\csc(\theta) ) - Cosecant is an odd function. 

Secant Function: ( \sec(-\theta) = \sec(\theta) ) - Secant is an even function. 

In summary, cosine and secant are even functions, while sine, tangent, cotangent, and cosecant are odd functions. 

### ADHD Summary --- 

Learning Objectives 

Understand the even and odd properties of trigonometric functions. 

Identify the relationships between sine, cosine, tangent, cotangent, cosecant, and secant. 

### Key Concepts 

Sine is an odd function: 

sin(−𝜃) = −sin(𝜃) 

Cosine is an even function: 

cos(−𝜃) = cos(𝜃) 

Tangent is an odd function: 

tan(−𝜃) = −tan(𝜃) 

Cotangent is an odd function: 

cot(−𝜃) = −cot(𝜃) 

Cosecant is an odd function: 

csc(−𝜃) = −csc(𝜃) 

Secant is an even function: 

sec(−𝜃) = sec(𝜃) 

### Recall Questions 

What type of function is cosine?  

How is the tangent function classified in terms of even or odd?


---

### Test Case 7 — Calculus: Line Integrals
### Source

OpenStax Calculus Volume 3
Section: Line Integrals

### Evaluation Results
Metric	           Baseline	  ADHD Version	Improvement
Reading Level	     9.95	      6.74	      ↓ 3.21
Avg Sentence Length	 19.38	      8.67	      ↓ 10.71
Avg Paragraph Length 77.50	      17.33	      ↓ 60.17
Compliance Score	  20%	       100%	      ↑ 80%

### Original Input:
A line integral gives us the ability to integrate multivariable functions and vector fields over arbitrary curves in a plane or in space. There are two types of line integrals: scalar line integrals and vector line integrals. Scalar line integrals are integrals of a scalar function over a curve in a plane or in space. Vector line integrals are integrals of a vector field over a curve in a plane or in space. Let’s look at scalar line integrals first. 

A scalar line integral is defined just as a single-variable integral is defined, except that for a scalar line integral, the integrand is a function of more than one variable and the domain of integration is a curve in a plane or in space, as opposed to a curve on the x-axis. 

For a scalar line integral, we let C be a smooth curve in a plane or in space and let 𝑓 be a function with a domain that includes C. We chop the curve into small pieces. For each piece, we choose point P in that piece and evaluate 𝑓 at P. (We can do this because all the points in the curve are in the domain of 𝑓.) We multiply 𝑓⁡(𝑃) by the arc length of the piece Δ𝑠, add the product 𝑓⁡(𝑃)Δ𝑠 over all the pieces, and then let the arc length of the pieces shrink to zero by taking a limit. The result is the scalar line integral of the function over the curve. 

### Baseline Summary ---

A line integral allows for the integration of multivariable functions and vector fields over curves in a plane or space. There are two types: scalar line integrals and vector line integrals.  

A scalar line integral involves integrating a scalar function over a curve. It is defined similarly to a single-variable integral but applies to functions of multiple variables along a curve. To compute a scalar line integral, one considers a smooth curve \( C \) and a function \( f \) defined on \( C \). The curve is divided into small segments, and for each segment, a point \( P \) is chosen to evaluate \( f \). The product \( f(P) \) is multiplied by the arc length of the segment \( \Delta s \), and these products are summed over all segments. Finally, as the segment lengths approach zero, the limit gives the scalar line integral of the function over the curve. 

### ADHD Summary ---
## Learning Objectives 

- Understand what a line integral is. 

- Differentiate between scalar and vector line integrals. 

- Learn how to compute a scalar line integral.

## Key Concepts 

- Line integrals integrate functions over curves in space. 

- There are two types: scalar and vector line integrals. 

- Scalar line integrals use a scalar function over a curve. 

- The curve is divided into small pieces for calculation. 

- The integral is found by taking a limit as the pieces shrink. 

## Recall Questions 

1. What are the two types of line integrals? 

2. How do you compute a scalar line integral?

### ADHD Compliance Status
Baseline: Non-compliant
ADHD Version: Fully Compliant

Strong case. Clear improvement across all metrics.

---

### Test Case 8 — Biology: DNA Structure and Sequencing
### Source

OpenStax Biology
Section: DNA Structure

### Evaluation Results ---

Quantitative Metrics
Metric	              Baseline	ADHD Version	Improvement
Reading Level	        10.55	    8.38	      ↓ 2.17
Avg Sentence Length	    19.90	    8.50	      ↓ 11.40
Avg Paragraph Length	66.33	    17.00	      ↓ 49.33
Compliance Score	     30%	     90%       	  ↑ 60%

### Original Input:
The building blocks of DNA are nucleotides. The important components of the nucleotide are a nitrogenous (nitrogen-bearing) base, a 5-carbon sugar (pentose), and a phosphate group (Figure 14.5). The nucleotide is named depending on the nitrogenous base. The nitrogenous base can be a purine such as adenine (A) and guanine (G), or a pyrimidine such as cytosine (C) and thymine (T). 

The purines have a double ring structure with a six-membered ring fused to a five-membered ring. Pyrimidines are smaller in size; they have a single six-membered ring structure. 

The sugar is deoxyribose in DNA and ribose in RNA. The carbon atoms of the five-carbon sugar are numbered 1', 2', 3', 4', and 5' (1' is read as “one prime”). The phosphate, which makes DNA and RNA acidic, is connected to the 5' carbon of the sugar by the formation of an ester linkage between phosphoric acid and the 5'-OH group (an ester is an acid + an alcohol). In DNA nucleotides, the 3' carbon of the sugar deoxyribose is attached to a hydroxyl (OH) group. In RNA nucleotides, the 2' carbon of the sugar ribose also contains a hydroxyl group. The base is attached to the 1'carbon of the sugar. 

The nucleotides combine with each other to produce phosphodiester bonds. The phosphate residue attached to the 5' carbon of the sugar of one nucleotide forms a second ester linkage with the hydroxyl group of the 3' carbon of the sugar of the next nucleotide, thereby forming a 5'-3' phosphodiester bond. In a polynucleotide, one end of the chain has a free 5' phosphate, and the other end has a free 3'-OH. These are called the 5' and 3' ends of the chain. A base attached to a five-carbon sugar represents a nucleoside. A nucleotide is composed of one, two, or three phosphate groups attached to a nucleoside. 

### Baseline Summary --- 

DNA is composed of nucleotides, which consist of three key components: a nitrogenous base, a 5-carbon sugar (pentose), and a phosphate group. The nitrogenous bases are categorized into purines (adenine and guanine) and pyrimidines (cytosine and thymine). Purines have a double-ring structure, while pyrimidines have a single-ring structure. 

In DNA, the sugar is deoxyribose, whereas in RNA, it is ribose. The sugar's carbon atoms are numbered from 1' to 5', with the phosphate group linked to the 5' carbon through an ester bond. In DNA, the 3' carbon of deoxyribose has a hydroxyl (OH) group, while in RNA, the 2' carbon of ribose also has a hydroxyl group. The nitrogenous base is attached to the 1' carbon of the sugar.

Nucleotides connect via phosphodiester bonds, where the phosphate group of one nucleotide forms a bond with the 3' hydroxyl group of the next nucleotide, creating a 5'-3' directionality in the polynucleotide chain. The ends of the chain are referred to as the 5' end (with a free phosphate) and the 3' end (with a free hydroxyl). A base attached to a sugar is called a nucleoside, while a nucleotide includes one to three phosphate groups attached to a nucleoside. 

  

--- ADHD Summary --- 

## Learning Objectives 

- Understand the structure of DNA and its building blocks. 

- Identify the components of nucleotides. 

- Recognize the differences between purines and pyrimidines. 


## Key Concepts 

- Nucleotides are the building blocks of DNA. 

- Each nucleotide has a nitrogenous base, a sugar, and a phosphate group. 

- Purines (adenine, guanine) have a double ring structure. 

- Pyrimidines (cytosine, thymine) have a single ring structure. 

- DNA contains deoxyribose sugar; RNA contains ribose sugar. 


## Recall Questions

1. What are the two types of nitrogenous bases in nucleotides? 

2. How are nucleotides linked together in a polynucleotide chain? 

---

### Test Case 9 — U.S. History: Spanish Exploration and Colonial Society
### Source

OpenStax U.S. History
Section: Spanish Colonial Society

### Evaluation Results ---

Metric	            Baseline	ADHD Version	Improvement
Reading Level	      16.52	        10.51	      ↓ 6.01
Avg Sentence Length	  22.50	         9.38	      ↓ 13.12
Avg Paragraph Length  67.50	        20.33	      ↓ 47.17
Compliance Score	   20%	         90%	      ↑ 70%

### Original Input:
During the 1500s, Spain expanded its colonial empire to the Philippines in the Far East and to areas in the Americas that later became the United States. The Spanish dreamed of mountains of gold and silver and imagined converting thousands of eager Native Americans to Catholicism. In their vision of colonial society, everyone would know his or her place. Patriarchy (the rule of men over family, society, and government) shaped the Spanish colonial world. Women occupied a lower status. In all matters, the Spanish held themselves to be atop the social pyramid, with Native peoples and Africans beneath them. Both Africans and native peoples, however, contested Spanish claims to dominance. Everywhere the Spanish settled, they brought devastating diseases, such as smallpox, that led to a horrific loss of life among native peoples. European diseases killed far more native inhabitants than did Spanish swords. 

The world Native peoples had known before the coming of the Spanish was further upset by Spanish colonial practices. The Spanish imposed the encomienda system in the areas they controlled. Under this system, authorities assigned Native workers to mine and plantation owners with the understanding that the recipients would defend the colony and teach the workers the tenets of Christianity. In reality, the encomienda system exploited native workers. It was eventually replaced by another colonial labor system, the repartimiento, which required Native towns to supply a pool of labor for Spanish overlords. 

### Baseline Summary ---

In the 1500s, Spain expanded its colonial empire to the Philippines and parts of the Americas, driven by the desire for wealth and the conversion of Native Americans to Catholicism. Spanish colonial society was characterized by a strict social hierarchy, with men in power and women in subordinate roles. Spaniards viewed themselves as superior to Native peoples and Africans, who resisted this dominance. The arrival of the Spanish brought devastating diseases, such as smallpox, which caused significant mortality among Native populations, far exceeding deaths from conflict.

Spanish colonial practices disrupted Native societies, particularly through the encomienda system, which assigned Native workers to Spanish landowners under the pretense of protection and religious instruction. This system exploited Native labor and was later replaced by the repartimiento system, which mandated that Native towns provide labor for Spanish authorities.

### ADHD Summary ---

## Learning Objectives 

- Understand Spain's colonial expansion in the 1500s. 

- Recognize the impact of Spanish rule on Native peoples. 

- Learn about the encomienda and repartimiento systems.

## Key Concepts

- Spain expanded its empire to the Philippines and the Americas. 

- Spanish colonizers sought gold, silver, and to convert Native Americans to Catholicism. 

- Patriarchy defined Spanish society, placing men in power and women in lower status. 

- Native peoples and Africans resisted Spanish dominance. 

- The encomienda system exploited Native workers for labor. 

- The repartimiento system replaced encomienda, requiring labor from Native towns. 

## Recall Questions

1. What were the main goals of Spanish colonization in the 1500s? 

2. How did the encomienda system affect Native workers? 

---

### Test Case 10 — U.S. History: Political and Cultural Fusions
### Source

OpenStax U.S. History
Section: Reagan Era Conservatism

### Evaluation Results ---
  
Metric	                Baseline	ADHD Version	Improvement
Reading Level	         17.27	        12.74	      ↓ 4.53
Avg Sentence Length	     22.75	         8.83	      ↓ 13.92
Avg Paragraph Length	 91.00	        15.14	      ↓ 75.86
Compliance Score	      20%	         90%	      ↑ 70%

### Original Input:
Ronald Reagan’s victory in 1980 suggested to conservatives that the days of liberalism were over and the liberal establishment might be dismantled. Many looked forward to the discontinuation of policies like affirmative action. Conservative Christians sought to outlaw abortion and stop the movement for gay and lesbian rights. Republicans, and some moderate Democrats, demanded a return to “traditional” family values, a rhetorical ploy to suggest that male authority over women and children constituted a natural order that women’s rights and the New Left had subverted since the 1960s. As the conservative message regarding the evils of government permeated society, distrust of the federal government grew, inspiring some to form organizations and communities that sought complete freedom from government control. 

CREATING CONSERVATIVE POLICY 

Ronald Reagan’s popularity and effectiveness as a leader drew from his reputation as a man who fought for what he believed in. He was a very articulate spokesperson for a variety of political ideas based on conservative principles and perspectives. Much of the intellectual meat of the Reagan Revolution came from conservative think tanks (policy or advocacy groups) that specifically sought to shape American political and social dialogues. The Heritage Foundation, one such group, soon became the intellectual arm of the conservative movement. 

Launched in 1973 with a $250,000 contribution from Joseph Coors (of Coors Brewing Company) and support from a variety of corporations and conservative foundations, the Heritage Foundation sought to counteract what conservatives believed to be Richard Nixon’s acceptance of a liberal consensus on too many issues. In producing its policy position papers and political recommendations to conservative candidates and politicians, it helped contribute to a sanitization of U.S. history and a nostalgic glorification of what it deemed to be traditional values, seemingly threatened by the expansion of political and personal freedoms. The foundation had lent considerable support and encouragement to the conservative dialogues that helped carry Ronald Reagan into office in 1980. Just a year later, it produced a document entitled Mandate for Leadership that catalogued some two thousand specific recommendations on how to shrink the size and reach of the federal government and implement a more consistent conservative agenda. The newly elected Reagan administration looked favorably on the recommendations and recruited several of the paper’s authors to serve in the White House. 

### Baseline Summary ---

Ronald Reagan's 1980 election victory signaled a shift toward conservatism, leading many to believe liberalism's influence was waning. Conservatives anticipated the end of policies like affirmative action, while conservative Christians aimed to outlaw abortion and curb gay and lesbian rights. The call for a return to "traditional" family values was framed as a restoration of a natural order disrupted by women's rights and the New Left since the 1960s. This growing distrust of federal government prompted the formation of groups seeking autonomy from government control.

Reagan's leadership was bolstered by his strong advocacy for conservative principles, with significant intellectual support from conservative think tanks, notably the Heritage Foundation. Founded in 1973 with backing from Joseph Coors and various corporations, the Heritage Foundation aimed to counteract what it viewed as a liberal consensus established during Nixon's presidency. It produced policy papers that romanticized traditional values and provided strategic recommendations to conservative politicians. Its 1981 document, "Mandate for Leadership," outlined around 2,000 proposals to reduce federal government size and promote a conservative agenda, which the Reagan administration embraced, incorporating several authors into its ranks.

### ADHD Summary ---

## Learning Objectives 

- Understand the impact of Ronald Reagan's presidency on conservatism. 

- Identify key conservative organizations and their roles. 

- Recognize the shift in political values during the 1980s.

## Key Concepts 

- Reagan's victory in 1980 marked a conservative shift in American politics. 

- Conservative Christians aimed to restrict abortion and LGBTQ+ rights. 

- The Heritage Foundation shaped conservative policies and ideas. 

- Reagan's administration embraced recommendations to reduce government size. 

- Distrust of the federal government grew among conservatives.

## Recall Questions

1. What were some goals of conservative Christians during Reagan's presidency?

2. How did the Heritage Foundation influence conservative policies? 

---

### Test Case 11 — Philosophy: What Is Philosophy?
### Source

OpenStax Introduction to Philosophy
Section: Defining Philosophy

### Evaluation Results --- 


Metric	               Baseline  	ADHD Version	Improvement
Reading Level	         17.23	        9.79	      ↓ 7.44
Avg Sentence Length	     20.71	        8.25	      ↓ 12.46
Avg Paragraph Length	 72.50	        16.50	      ↓ 56.00
Compliance Score	      20%	         90%	      ↑ 70%

### Original Input: 

It is difficult to define philosophy. In fact, to do so is itself a philosophical activity, since philosophers are attempting to gain the broadest and most fundamental conception of the world as it exists. The world includes nature, consciousness, morality, beauty, and social organizations. So the content available for philosophy is both broad and deep. Because of its very nature, philosophy considers a range of subjects, and philosophers cannot automatically rule anything out. Whereas other disciplines allow for basic assumptions, philosophers cannot be bound by such assumptions. This open-endedness makes philosophy a somewhat awkward and confusing subject for students. There are no easy answers to the questions of what philosophy studies or how one does philosophy. Nevertheless, in this chapter, we can make some progress on these questions by (1) looking at past examples of philosophers, (2) considering one compelling definition of philosophy, and (3) looking at the way academic philosophers today actually practice philosophy. 

Historical Origins of Philosophy 

One way to begin to understand philosophy is to look at its history. The historical origins of philosophical thinking and exploration vary around the globe. The word philosophy derives from ancient Greek, in which the philosopher is a lover or pursuer (philia) of wisdom (sophia). But the earliest Greek philosophers were not known as philosophers; they were simply known as sages. The sage tradition provides an early glimpse of philosophical thought in action. Sages are sometimes associated with mathematical and scientific discoveries and at other times with their political impact. What unites these figures is that they demonstrate a willingness to be skeptical of traditions, a curiosity about the natural world and our place in it, and a commitment to applying reason to understand nature, human nature, and society better. The overview of the sage tradition that follows will give you a taste of philosophy’s broad ambitions as well as its focus on complex relations between different areas of human knowledge. There are some examples of women who made contributions to philosophy and the sage tradition in Greece, India, and China, but these were patriarchal societies that did not provide many opportunities for women to participate in philosophical and political discussions. 

### Baseline Summary --- 

Defining philosophy is challenging, as it encompasses a wide range of subjects, including nature, consciousness, morality, beauty, and social organizations. Unlike other disciplines, philosophy does not operate on fixed assumptions, leading to its complexity and confusion for students. This chapter aims to clarify philosophy by examining historical examples, proposing a compelling definition, and exploring contemporary philosophical practices. 

The origins of philosophy can be traced back to ancient Greece, where the term derives from the Greek words for love (philia) and wisdom (sophia). Early Greek thinkers, known as sages rather than philosophers, exemplified philosophical inquiry through skepticism of traditions and a commitment to reason in understanding the natural world and human society. While some women contributed to philosophical thought in various cultures, patriarchal structures limited their participation in these discussions. The sage tradition highlights philosophy's broad ambitions and its intricate connections across different fields of knowledge. 

### ADHD Summary --- 

Learning Objectives 

Understand what philosophy is and its significance. 

Learn about the historical origins of philosophy. 

Recognize key figures in the sage tradition. 

### Key Concepts 

Philosophy seeks to understand the world deeply and broadly. 

The term "philosophy" means love of wisdom in Greek. 

Early philosophers were known as sages, not philosophers. 

Sages questioned traditions and explored nature and society. 

Women had limited roles in early philosophical discussions. 

### Recall Questions 

What does the term "philosophy" mean in Greek? 

How did sages contribute to the development of philosophy? 

---

### Test Case 12 — U.S. History: Origins and Outbreak of the Civil War
### Source

OpenStax U.S. History
Section: Sectional Conflict and Civil War

### Evaluation Results --- 

Metric	                Baseline	ADHD Version	Improvement
Reading Level	         18.64	        9.02	      ↓ 9.62
Avg Sentence Length	     27.50	        8.83	      ↓ 18.67
Avg Paragraph Length	 109.00	        17.67	      ↓ 91.33
Compliance Score	       20%	         90%	      ↑ 70%

### Original Input:
THE CAUSES OF THE CIVIL WAR 
Lincoln’s election sparked the southern secession fever into flame, but it did not cause the Civil War. For decades before Lincoln took office, the sectional divisions in the country had been widening. Both the Northern and southern states engaged in inflammatory rhetoric and agitation, and violent emotions ran strong on both sides. Several factors played into the ultimate split between the North and the South. 
 
One key irritant was the question of slavery’s expansion westward. The debate over whether new states would be slave or free reached back to the controversy over statehood for Missouri beginning in 1819 and Texas in the 1830s and early 1840s. This question arose again after the Mexican-American War (1846–1848), when the government debated whether slavery would be permitted in the territories taken from Mexico. Efforts in Congress to reach a compromise in 1850 fell back on the principle of popular sovereignty—letting the people in the new territories south of the 1820 Missouri Compromise line decide whether to allow slavery. This same principle came to be applied to the Kansas-Nebraska territories in 1854, a move that added fuel to the fire of sectional conflict by destroying the Missouri Compromise boundary and leading to the birth of the Republican Party. In the end, popular sovereignty proved to be no solution at all. This was especially true in “Bleeding Kansas” in the mid-1850s, as pro- and antislavery forces battled each another in an effort to gain the upper hand. 
 
The small but very vocal abolitionist movement further contributed to the escalating tensions between the North and the South. Since the 1830s, abolitionists, led by journalist and reformer William Lloyd Garrison, had cast slavery as a national sin and called for its immediate end. For three decades, the abolitionists—a minority even within the antislavery movement—had had a significant effect on American society by bringing the evils of slavery into the public consciousness. By the 1850s, some of the most radical abolitionists, such as John Brown, had resorted to violence in their efforts to destroy the institution of slavery. 

### Baseline Summary --- 

The Civil War was not solely caused by Lincoln's election but was the culmination of long-standing sectional divisions between the North and South. Key factors contributing to the conflict included the contentious issue of slavery's expansion into new territories, which had been debated since the Missouri Compromise of 1819 and intensified after the Mexican-American War. The principle of popular sovereignty, introduced to resolve these debates, ultimately failed, leading to violent confrontations in "Bleeding Kansas." Additionally, the abolitionist movement, particularly figures like William Lloyd Garrison and radical activists like John Brown, heightened tensions by framing slavery as a moral crisis and advocating for its immediate abolition, often resorting to violence. 

### ADHD Summary --- 
Learning Objectives 

Understand the main causes of the Civil War. 

Identify key events leading to the conflict. 

Recognize the role of slavery in the sectional divide. 

### Key Concepts 

Lincoln's election increased tensions but did not start the Civil War. 

Slavery's expansion was a major issue for new states. 

The Missouri Compromise and popular sovereignty were key concepts. 

"Bleeding Kansas" highlighted violent conflicts over slavery. 

Abolitionists raised awareness about the evils of slavery. 

### Recall Questions 

What role did popular sovereignty play in the Civil War? 

Who was a prominent figure in the abolitionist movement? 

---

### Test Case 13 — Economics: Monopoly and Barriers to Entry
### Source

OpenStax Principles of Economics
Section: Monopoly and Market Power

### Evaluation Results --- 

Metric	                Baseline	ADHD Version	Improvement
Reading Level	         14.04	        10.37	      ↓ 3.67
Avg Sentence Length	     18.91	         8.33	      ↓ 10.58
Avg Paragraph Length	 68.67	        16.67	      ↓ 52.00
Compliance Score	      20%	         90%	      ↑ 70%

### Original Input:
Because of the lack of competition, monopolies tend to earn significant economic profits. These profits should attract vigorous competition as we described in Perfect Competition, and yet, because of one particular characteristic of monopoly, they do not. Barriers to entry are the legal, technological, or market forces that discourage or prevent potential competitors from entering a market. Barriers to entry can range from the simple and easily surmountable, such as the cost of renting retail space, to the extremely restrictive. For example, there are a finite number of radio frequencies available for broadcasting. Once an entrepreneur or firm has purchased the rights to all of them, no new competitors can enter the market. 
 
In some cases, barriers to entry may lead to monopoly. In other cases, they may limit competition to a few firms. Barriers may block entry even if the firm or firms currently in the market are earning profits. Thus, in markets with significant barriers to entry, it is not necessarily true that abnormally high profits will attract new firms, and that this entry of new firms will eventually cause the price to decline so that surviving firms earn only a normal level of profit in the long run. 
 
There are five types of monopoly, based on the types of barriers to entry they exploit. 
 
Natural Monopoly 
Economies of scale can combine with the size of the market to limit competition. (We introduced this theme in Production, Cost and Industry Structure). Figure 9.2 presents a long-run average cost curve for the airplane manufacturing industry. It shows economies of scale up to an output of 8,000 planes per year and a price of P0, then constant returns to scale from 8,000 to 20,000 planes per year, and diseconomies of scale at a quantity of production greater than 20,000 planes per year. 
 
Now consider the market demand curve in the diagram, which intersects the long-run average cost (LRAC) curve at an output level of 5,000 planes per year and at a price P1, which is higher than P0. In this situation, the market has room for only one producer. If a second firm attempts to enter the market at a smaller size, say by producing a quantity of 4,000 planes, then its average costs will be higher than those of the existing firm, and it will be unable to compete. If the second firm attempts to enter the market at a larger size, like 8,000 planes per year, then it could produce at a lower average cost—but it could not sell all 8,000 planes that it produced because of insufficient demand in the market. 

### Baseline Summary --- 

Monopolies can earn significant economic profits due to a lack of competition, primarily because of barriers to entry that prevent potential competitors from entering the market. These barriers can be legal, technological, or market-based and vary in severity. For instance, while some barriers, like renting retail space, are easily overcome, others, such as limited radio frequencies, are much more restrictive. 

Barriers to entry can lead to monopolies or limit competition to a few firms, meaning that high profits do not necessarily attract new entrants to the market. This situation can result in sustained high profits for existing firms without the expected market adjustments that would normally occur in competitive environments. 

There are five types of monopoly based on the barriers they exploit. One type is the natural monopoly, where economies of scale and market size limit competition. For example, in the airplane manufacturing industry, a single producer can operate efficiently at a certain output level (e.g., 5,000 planes per year) due to lower average costs compared to any potential new entrant. If a new firm tries to enter the market at a smaller scale, it will face higher costs, while entering at a larger scale would lead to overproduction relative to market demand, making competition unfeasible. 

### ADHD Summary --- 

Learning Objectives 

Understand what monopolies are and how they work. 

Identify barriers to entry in markets. 

Recognize different types of monopolies. 

### Key Concepts 

Monopolies earn high profits due to lack of competition. 

Barriers to entry prevent new competitors from joining the market. 

Types of barriers include legal, technological, and market forces. 

Natural monopolies occur when economies of scale limit competition. 

A market can only support one producer if demand is low. 

### Recall Questions 

What are barriers to entry in a market? 

How do natural monopolies affect competition? 

---

### Test Case 14 — Accounting: Service Companies and Operating Cycles
### Source

OpenStax Financial Accounting
Section: Service vs. Merchandising Companies

### Evaluation Results --- 

Metric	                Baseline	ADHD Version	Improvement
Reading Level	         16.34	       12.71	      ↓ 3.63
Avg Sentence Length	     18.00	        9.17	      ↓ 8.83
Avg Paragraph Length	 45.00	       18.33	      ↓ 26.67
Compliance Score	      30%	        90%	          ↑ 60%

### Original Input:
Comparison of Merchandising Transactions versus Service Transactions 

Some of the biggest differences between a service company and a merchandising company are what they sell, their typical financial transactions, their operating cycles, and how these translate to financial statements. 

A service company provides intangible services to customers and does not have inventory. Some examples of service companies include lawyers, doctors, consultants, and accountants. Service companies often have simple financial transactions that involve taking customer deposits, billing clients after services have been provided, providing the service, and processing payments. These activities may occur frequently within a company’s accounting cycle and make up a portion of the service company’s operating cycle. 

An operating cycle is the amount of time it takes a company to use its cash to provide a product or service and collect payment from the customer. Completing this cycle faster puts the company in a more stable financial position. A typical operating cycle for a service company begins with having cash available, providing service to a customer, and then receiving cash from the customer for the service (Figure 6.2). 

### Baseline Summary --- 

The study material outlines key differences between service companies and merchandising companies. Service companies, such as lawyers and doctors, offer intangible services and do not maintain inventory. Their financial transactions are generally straightforward, involving customer deposits, billing after service delivery, and payment processing.  

The operating cycle for service companies is defined as the time taken to convert cash into services and collect payment, which typically starts with cash availability, followed by service provision, and concludes with cash receipt from the customer. A faster operating cycle enhances the company's financial stability. 

### ADHD Summary --- 

Learning Objectives 

Understand the differences between service and merchandising companies. 

Identify the components of a service company’s operating cycle. 

Recognize the financial transactions typical for service companies. 

### Key Concepts 

Service companies sell intangible services, not physical products. 

Examples of service companies include lawyers, doctors, and consultants. 

Service transactions involve customer deposits and billing after service. 

An operating cycle measures how quickly cash is used and collected. 

Faster operating cycles lead to better financial stability. 

### Recall Questions 

What do service companies sell compared to merchandising companies? 

What is an operating cycle in the context of a service company? 

---

### Test Case 15 — Psychology: What Is Psychology?
### Source

OpenStax Psychology
Section: Introduction to Psychology

### Evaluation Results --- 

Metric	                Baseline	ADHD Version	Improvement
Reading Level	          18.53	        13.18	      ↓ 5.34
Avg Sentence Length	      19.00	         8.00	      ↓ 11.00
Avg Paragraph Length	  50.67	        14.86	      ↓ 35.81
Compliance Score	       30%	         90%	      ↑ 60%

### Original Input:
What is creativity? What are prejudice and discrimination? What is consciousness? The field of psychology explores questions like these. Psychology refers to the scientific study of the mind and behavior. Psychologists use the scientific method to acquire knowledge. To apply the scientific method, a researcher with a question about how or why something happens will propose a tentative explanation, called a hypothesis, to explain the phenomenon. A hypothesis should fit into the context of a scientific theory, which is a broad explanation or group of explanations for some aspect of the natural world that is consistently supported by evidence over time. A theory is the best understanding we have of that part of the natural world. The researcher then makes observations or carries out an experiment to test the validity of the hypothesis. Those results are then published or presented at research conferences so that others can replicate or build on the results. 
 
Scientists test that which is perceivable and measurable. For example, the hypothesis that a bird sings because it is happy is not a hypothesis that can be tested since we have no way to measure the happiness of a bird. We must ask a different question, perhaps about the brain state of the bird, since this can be measured. However, we can ask individuals about whether they sing because they are happy since they are able to tell us. Thus, psychological science is empirical, based on measurable data. 
 
In general, science deals only with matter and energy, that is, those things that can be measured, and it cannot arrive at knowledge about values and morality. This is one reason why our scientific understanding of the mind is so limited, since thoughts, at least as we experience them, are neither matter nor energy. The scientific method is also a form of empiricism. An empirical method for acquiring knowledge is one based on observation, including experimentation, rather than a method based only on forms of logical argument or previous authorities. 
 
It was not until the late 1800s that psychology became accepted as its own academic discipline. Before this time, the workings of the mind were considered under the auspices of philosophy. Given that any behavior is, at its roots, biological, some areas of psychology take on aspects of a natural science like biology. No biological organism exists in isolation, and our behavior is influenced by our interactions with others. Therefore, psychology is also a social science. 

### Baseline Summary --- 

Psychology is the scientific study of the mind and behavior, utilizing the scientific method to explore questions about phenomena such as creativity, prejudice, discrimination, and consciousness. Researchers formulate hypotheses—tentative explanations that fit within broader scientific theories, which are well-supported explanations of natural phenomena. These hypotheses are tested through observations and experiments, with results shared for replication and further exploration. 

Psychological science focuses on measurable and observable aspects of behavior, as it cannot assess values or morality. For instance, while we cannot measure a bird's happiness, we can study its brain states or ask individuals about their feelings. This empirical approach emphasizes observation and experimentation over purely logical reasoning. 

Psychology gained recognition as a distinct academic discipline in the late 1800s, evolving from philosophical inquiries into the mind. It intersects with biology, as behavior is rooted in biological processes, and it also encompasses social science, acknowledging the influence of interpersonal interactions on behavior. 

### ADHD Summary --- 

Learning Objectives 

Understand what psychology is and its purpose. 

Learn about the scientific method in psychology. 

Recognize the difference between science and philosophy. 

Identify the relationship between biology and behavior. 

### Key Concepts 

Psychology studies the mind and behavior scientifically. 

A hypothesis is a testable explanation for a phenomenon. 

The scientific method involves observation and experimentation. 

Psychology combines aspects of natural and social sciences. 

Empirical methods rely on measurable data, not just logic. 

### Recall Questions 

What is a hypothesis in psychology?  

How does psychology relate to both natural and social sciences? 

---

### Test Case 16 — Computer Science: While Loops
### Source

Introduction to Python Programming
Section: While Loop

### Evaluation Results --- 

Metric	             Baseline	ADHD Version	Improvement
Reading Level	      12.52	        4.97	      ↓ 7.56
Avg Sentence Length	  22.83	        9.83	      ↓ 13.00
Avg Paragraph Length  68.50	       16.86	      ↓ 51.64
Compliance Score	   30%	        100%	      ↑ 70%

### Original Input:
A while loop is a code construct that runs a set of statements, known as the loop body, while a given condition, known as the loop expression, is true. At each iteration, once the loop statement is executed, the loop expression is evaluated again. 

If true, the loop body will execute at least one more time (also called looping or iterating one more time). 

If false, the loop's execution will terminate and the next statement after the loop body will execute. 

Counting with a while loop 

A while loop can be used to count up or down. A counter variable can be used in the loop expression to determine the number of iterations executed. Ex: A programmer may want to print all even numbers between 1 and 20. The task can be done by using a counter initialized with 1. In each iteration, the counter's value is increased by one, and a condition can check whether the counter's value is an even number or not. The change in the counter's value in each iteration is called the step size. The step size can be any positive or negative value. If the step size is a positive number, the counter counts in ascending order, and if the step size is a negative number, the counter counts in descending order. 

### Baseline Summary --- 

A while loop is a programming construct that repeatedly executes a set of statements, known as the loop body, as long as a specified condition (the loop expression) remains true. After each iteration, the loop expression is re-evaluated. If the expression is true, the loop continues; if false, the loop terminates, and execution proceeds to the next statement after the loop. 

While loops can be utilized for counting, either upwards or downwards, using a counter variable in the loop expression to track iterations. For example, to print all even numbers between 1 and 20, a programmer might initialize a counter at 1 and increment it by one in each iteration, checking if the counter is even. The increment amount is known as the step size, which can be positive (for ascending counts) or negative (for descending counts). 

### ADHD Summary --- 

Learning Objectives 

Understand how a while loop works. 

Learn how to use a counter in a while loop. 

Identify how to count up or down using a while loop. 

### Key Concepts 

A while loop runs while a condition is true. 

The loop body executes repeatedly until the condition is false. 

A counter variable helps track the number of iterations. 

Step size determines how much the counter changes each time. 

Positive step size counts up; negative step size counts down. 

### Recall Questions 

What happens when the loop expression in a while loop is false?  

How does the step size affect the counting in a while loop? 

---

### Test Case 17 — Computer Science: Functions
### Source

Introduction to Python Programming
Section: Functions

### Evaluation Results --- 

Metric	             Baseline	ADHD Version	Improvement
Reading Level	       12.78	    6.12	      ↓ 6.66
Avg Sentence Length	   19.40	    7.83	      ↓ 11.57
Avg Paragraph Length   48.50	   15.67	      ↓ 32.83
Compliance Score	    30%	        100%	      ↑ 70%

### Original Input:
Calling a function 

Throughout the book, functions have been called to perform tasks. Ex: print() prints values, and sqrt() calculates the square root. A function is a named, reusable block of code that performs a task when called. 

A function is defined using the def keyword. The first line contains def followed by the function name (in snake case), parentheses (with any parameters—discussed later), and a colon. The indented body begins with a documentation string describing the function's task and contains the function statements. A function must be defined before the function is called. 

Benefits of functions 

A function promotes modularity by putting code statements related to a single task in a separate group. The body of a function can be executed repeatedly with multiple function calls, so a function promotes reusability. Modular, reusable code is easier to modify and is shareable among programmers to avoid reinventing the wheel. 

### Baseline Summary --- 

Functions are named, reusable blocks of code that perform specific tasks when called, such as print() for printing values and sqrt() for calculating square roots. They are defined using the def keyword, followed by the function name in snake case, parentheses (which may include parameters), and a colon. The function's body begins with a documentation string and contains the executable statements. Functions must be defined before they can be called. 

The benefits of using functions include promoting modularity by grouping related code, enabling reusability through multiple calls, and facilitating easier modification and sharing of code among programmers. 

### ADHD Summary --- 

Learning Objectives 

Understand what a function is. 

Learn how to define a function. 

Recognize the benefits of using functions. 

### Key Concepts 

A function is a named block of code that performs a task. 

Functions are defined using the def keyword. 

The first line includes the function name and parameters. 

Functions promote modularity and reusability in code. 

Code in a function can be reused multiple times. 

### Recall Questions 

What keyword is used to define a function? 

Why are functions beneficial in programming? 

---

### Test Case 18 — Nursing: Health Promotion and the Health Belief Model
### Source

Open Nursing Text
Section: Health Promotion

### Evaluation Results --- 

Metric	             Baseline	ADHD Version	Improvement
Reading Level	      17.29	        9.91	      ↓ 7.39
Avg Sentence Length	  27.57	        8.25	      ↓ 19.32
Avg Paragraph Length  64.33	       22.00	      ↓ 42.33
Compliance Score	   30%	        80%	          ↑ 50%

### Original Input:
Health promotion and preventive health measures are foundational nursing interventions, and they are becoming more and more important as the climate of the health-care industry shifts from a reactive to a proactive (preventive) model. Nurses need to understand why people value being healthy, what motivates them to make choices related to their health, what can convince them to make lifestyle changes for better health outcomes, and, of course, what health means. Nurses also need to understand that the concept of health has changed over time and varies according to culture and across the lifespan. Health was previously considered to be the absence of disease or similar problems. But current conceptions establish that health is a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity (World Health Organization, 1946). 

People may receive health information, but it does not always result in changes in lifestyle or health-related behaviors. The Health Belief Model (Rosenstock, 1974) suggests that even though people recognize the consequences of poor health behaviors, they will not take action to change their behaviors unless: 

they believe that they are susceptible to (at risk for) the health condition; 

the health condition poses serious consequences; 

behavior change will result in decreased risk; 

the benefits of change will outweigh the costs of change; 

they believe they can change their behaviors and the changes will pay off (Paul, 2020). 

For nurses to positively affect people’s health through health promotion, according to the Health Belief Model, the information presented to patients must be individualized, relevant to their current lifestyle, and provide enough facts for the patients to make behavior changes. Consider the use of pamphlets; if a nurse determines that a patient is at risk for a sexually transmitted infection (STI), the nurse would typically provide the patient with a pamphlet to read regarding prevention of STIs. Evidence reveals, however, that providing pamphlets without additional educational interventions is ineffective (Bhattad & Pacifico, 2022). A written pamphlet may not include all the information needed for the patient to believe they can make the needed lifestyle change. The nurse should explain why the patient is susceptible to an STI, explain the consequences of contracting an STI, and provide the patient with education on safe sex practices. 

### Baseline Summary --- 

Health promotion and preventive health measures are essential nursing interventions, increasingly important as healthcare shifts from reactive to proactive models. Nurses must understand the value of health, motivations for health-related choices, and the evolving definitions of health, which now encompass complete physical, mental, and social well-being, rather than merely the absence of disease (World Health Organization, 1946). 

The Health Belief Model (Rosenstock, 1974) outlines that awareness of health risks alone does not lead to behavior change. Individuals are more likely to change their health behaviors if they believe they are at risk, recognize serious consequences, perceive that change will reduce their risk, find the benefits of change outweigh the costs, and feel capable of making those changes (Paul, 2020). 

For effective health promotion, nurses must provide individualized and relevant information that empowers patients to make lifestyle changes. Simply distributing pamphlets is insufficient; nurses should also explain the patient's specific risks, the consequences of health issues, and offer education on preventive practices. For instance, when addressing the risk of sexually transmitted infections (STIs), nurses should accompany pamphlets with thorough explanations and discussions to enhance understanding and motivation for behavior change (Bhattad & Pacifico, 2022). 

### ADHD Summary --- 

Learning Objectives 

Understand the importance of health promotion in nursing. 

Recognize factors that motivate health-related behavior changes. 

Learn about the Health Belief Model and its components. 

### Key Concepts 

Health promotion is essential in nursing today. 

Health is more than just the absence of disease. 

The Health Belief Model outlines reasons for behavior change: 

Belief in susceptibility to health issues. 

Awareness of serious consequences. 

Understanding that change reduces risk. 

Weighing benefits against costs. 

Confidence in ability to change behaviors. 

Individualized education is crucial for effective health promotion. 

Pamphlets alone may not lead to behavior change. 

### Recall Questions 

What are the key components of the Health Belief Model? 

Why is individualized education important in health promotion? 

---

### Test Case 19 — Political Science: Empirical Political Science
### Source

Introduction to Political Science
Section: Empirical Political Science

### Evaluation Results --- 

Metric	                Baseline	ADHD Version	Improvement
Reading Level	          16.51	        12.52	       ↓ 3.99
Avg Sentence Length	      22.00	         8.92	       ↓ 13.08
Avg Paragraph Length	  51.33	        17.83	       ↓ 33.50
Compliance Score	       30%	         90%	       ↑ 60%

### Original Input:
Unlike normative political science, empirical political science is based not on what should be, but on what is. It seeks to describe the real world of politics, distinguishing between what is predictable and what is idiosyncratic. Empirical political science attempts to explain and predict.32 
 
Empirical political science assumes that facts exist: actual, genuine, verifiable facts. Empirical questions are ones that can be answered by factual evidence. The number of votes a candidate receives is an empirical matter: votes can be counted. Counting votes accurately so that each candidate receives the actual number of votes that were cast for them can be difficult. Different ways of counting can lead to slightly different counts, but a correct number actually exists. 
 
A fact may be disputed. There may be genuine uncertainty as to what the facts really are—what the evidence really shows. Sometimes it is extremely difficult to gather the facts. Do space aliens exist? That is an empirical question. Either space aliens exist, or they do not. Some researchers claim to have evidence that space aliens are real, but their evidence is not universally, or even broadly, accepted. One side of this argument is correct, however, and the other is not. Evidence has not yet conclusively determined which is correct.35 
 
Does the Russian government seek to interfere with American elections, and if so, does its interference affect the outcome? The first part of the question is difficult (but not impossible) to answer because when a country interferes in another country’s domestic affairs it tries to do so in secret. It is difficult to uncover secrets.36 But the second part of the question, does the interference affect the outcome, is almost impossible to answer. Because so many factors influence election outcomes, it is extremely challenging to determine which individual factors made any consequential difference.37 
 
There are thus empirical debates in which people of good faith disagree about what the facts are. In many cases, however, people do not want to acknowledge what the evidence shows, and because they do not want to believe what the facts demonstrate, they insist the evidence cannot be true. Humans often use motivated reasoning, first deciding what is true—for example, “Gun control makes us safer” or “Gun control makes us less safe”—and then finding evidence that supports this belief while rejecting data that contradicts it. 


### Baseline Summary --- 

Empirical political science focuses on describing and analyzing the actual state of politics rather than prescribing what it should be. It aims to explain and predict political phenomena based on verifiable facts. Empirical questions can be answered through factual evidence, such as counting votes, although the process can be complicated by different counting methods. 

Disputes over facts can arise, as seen in debates about the existence of space aliens, where evidence is contested but one side must ultimately be correct. Similarly, questions about foreign interference in elections, like that of the Russian government in American elections, present challenges in determining both the occurrence of interference and its impact on outcomes due to the complexity of influencing factors. 

Empirical debates often see individuals of good faith disagreeing on facts, sometimes influenced by motivated reasoning, where personal beliefs shape the interpretation of evidence. People may selectively accept data that supports their views while dismissing contradictory information. 

### ADHD Summary --- 

Learning Objectives 

Understand the difference between normative and empirical political science. 

Recognize the importance of facts in empirical research. 

Identify challenges in gathering and interpreting empirical evidence. 

### Key Concepts 

Empirical political science focuses on what is, not what should be. 

It relies on verifiable facts and evidence to answer questions. 

Counting votes accurately is a key empirical challenge. 

Disputed facts can lead to differing opinions and beliefs. 

Motivated reasoning affects how people interpret evidence. 

### Recall Questions 

What is the main focus of empirical political science? 

How does motivated reasoning influence people's beliefs about facts?

---

### Test Case 20 — Data Science: Web Scraping and Social Media Data Collection
### Source

Principles of Data Science
Section: Web Scraping and Social Media Data Collection

### Evaluation Results --- 

Metric	             Baseline	ADHD Version	Improvement
Reading Level	       17.41	    8.59	      ↓ 8.82
Avg Sentence Length	   21.71	    9.08	      ↓ 12.63
Avg Paragraph Length   38.00	   18.17	      ↓ 19.83
Compliance Score	    30%	        90%	          ↑ 60%

### Original Input:
Web scraping and social media data collection are two approaches used to gather data from the internet. Web scraping involves pulling information and data from websites using a web data extraction tool, often known as a web scraper. One example would be a travel company looking to gather information about hotel prices and availability from different booking websites. Web scraping can be used to automatically gather this data from the various websites and create a comprehensive list for the company to use in its business strategy without the need for manual work. 

Social media data collection involves gathering information from various platforms like Twitter and Instagram using application programming interface or monitoring tools. An application programming interface (API) is a set of protocols, tools, and definitions for building software applications allowing different software systems to communicate and interact with each other and enabling developers to access data and services from other applications, operating systems, or platforms. Both web scraping and social media data collection require determining the data to be collected and analyzing it for accuracy and relevance. 

Web Scraping 

There are several techniques and approaches for scraping data from websites. See Table 2.2 for some of the common techniques used. (Note: The techniques used for web scraping will vary depending on the website and the type of data being collected. It may require a combination of different techniques to effectively scrape data from a website.) 

### Baseline Summary --- 

The study material discusses two primary methods for data collection from the internet: web scraping and social media data collection.  

Web Scraping involves using web data extraction tools, known as web scrapers, to automatically gather information from websites. For instance, a travel company might scrape data on hotel prices and availability from various booking sites to compile a comprehensive list for strategic use, eliminating the need for manual data collection. 

Social Media Data Collection entails gathering information from platforms like Twitter and Instagram through application programming interfaces (APIs) or monitoring tools. APIs facilitate communication between different software systems, allowing developers to access and utilize data from various applications. 

Both methods require careful consideration of the data to be collected and necessitate analysis for accuracy and relevance. Various techniques for web scraping exist, which may differ based on the website and data type, often requiring a combination of approaches for effective data extraction. 

### ADHD Summary --- 

Learning Objectives 

Understand web scraping and social media data collection. 

Learn how to gather data from the internet. 

Identify techniques for web scraping. 

### Key Concepts 

Web scraping pulls data from websites using tools called web scrapers. 

Social media data collection gathers information from platforms like Twitter and Instagram. 

An API allows different software systems to communicate and share data. 

Techniques for web scraping vary based on the website and data type. 

Analyzing collected data is essential for accuracy and relevance. 

### Recall Questions 

What is web scraping used for? 

How does an API help in data collection? 