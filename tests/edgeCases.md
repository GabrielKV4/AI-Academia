<h1 align="center">Edge Case Testing</h1>
Test Case 1: Oversimplified Content<br>
- Purpose: Test if summaries become too vague when enforcing short sentences<br>
- Conflict: Sentence length vs. content depth<br>
- Input: Dense academic text
<pre>
-Expected outcome:
    - Sentence length passes
    - Content may lack critical detail
    - System should not crash
</pre>
<br>
Test Case 2: Detailed but Long Sentences<br>
- Purpose: Ensure system flags long sentences even when content is strong<br>
- Conflict: Detail vs. sentence length
- Input: Complex explanatory material
<pre>
- Expected Outcome:
    - Sentence length fails
    - Other rules might pass
    - Error handling activated
</pre>
<br>
Test Case 3: Paragraph Overflow<br>
- Purpose: Validate Section completeness<br>
- Conflict: Structural presence vs. meaningful content<br>
- Input: Complex explanatory material
<pre>
- Expected Outcome:
    - Paragraph rule fails
    - Structure otherwise intact
</pre><br>
Test Case 4: Empty or Weak Sections<br>
- Purpose: Validate section completeness<br>
- Conflict: Structural presence vs. meaningful content<br>
- Input: Prompt with correct headers but minimal content
<pre>
- Expected Outcome:
    - Required rules pass
    - Content quality is weak
</pre><br>
Test Case 5: Too Few Bullet Points<br>
- Purpose: Test minimum bullet enforcement<br>
- Conflict: Formatting completeness<br>
- Input: 1-2 bullet points<br>
<pre>
- Expected Outcome: 
    - Bullet format passes
    - Minimum bullet rule fails
</pre><br>
Test Case 6: Too Many Bullets<br>
- Purpose: Prevent an overwhelming prompt
- Conflict: Detail vs conciseness
- Input: 7+ bullet points
<pre>
- Expected Outcome:
    - Bullet format passes
    - Bullet max rule fails
</pre><br>
Test Case 7: Week Recall Questions<br>
- Purpose: Validate question quality<br>
- Conflict: Rule satisfaction vs. educational value<br>
- Input: Superficial or vague question
<pre>
- Expected Outcome:
    - Recall question count passes
    - Quality may be poor
</pre><br>
Test Case 8: Over-Simplified Reading Level<br>
- Purpose: Test reading-level constraint effects<br>
- Conflict: Simplicity vs. accuracy<br>
- Input: Technical Academic content
<pre>
- Expected Outcome:
    - Reading level passes
    - Concepts may lose precision
</pre><br>
Test Case 9: Inline Formula Violation<br>
- Purpose: Enforce formula formatting rule<br>
- Conflict: Natural writing vs formatting rules<br>
- Input: Sentence with embedded formula
<pre>
- Expected Outcome:
    -Formula seperation fails
</pre><br>
Test Case 10: Proper Formula with Weak Explanation<br>
- Purpose: Ensure formulas are explained correctly<br>
- Conflict: Structure vs. comprehension<br>
- Input: Separate formula with minimal context
<pre>
- Expected Outcome:
    - Formula rule passes
    - Output quality suffers
</pre><br>
Test Case 11: Section Spacing Issue<br>
- Purpose: Test formatting enforcement<br>
- Conflict: Content vs visual clarity<br>
- Input: Missing blank lines between sections
<pre>
- Expected Outcome:
    - Section spacing fails
</pre><br>
Test Case 12: Minimal Input Case<br>
- Purpose: Test system behavior with small inputs<br>
- Conflict: Rule requirements vs input limitations<br>
- Input: Very short academic test
<pre>
- Expected Outcome:
    - Rule length violated
    - Error handling initiated
</pre><br>
Test Cases 13: Technical English with Formulas<br>
- Purpose: Validate formula-friendly input handling<br>
- Conflict: English validation vs. Symbolic Content<br>
- Input: Academic text with formula/equation
<pre>
- Expected Outcome:
    - Input accepted
    - Output structured correctly
</pre><br>
Test Case 14: Non-English Structured Correctly<br>
- Purpose: Test language validation works<br>
- Conflict: Formatting bs. language validation<br>
- Input: Structure text but not in English
<pre>
- Expected Outcome:
    - Rejected before processing begins
</pre><br>
Test Case 15: Gibberish with Structure<br>
- Purpose: Detect fake compliance patterns<br>
- Conflict: Structure vs. semantic validity<br>
- Input type: Random text with headers and bullets
<pre>
- Expected Outcome:
    - Input rejected before processing
</pre>