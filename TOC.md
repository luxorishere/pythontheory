# Notes for TOC 

## Unit 2

### Regular expressoins 

R1∅ = ∅R1 = ∅  
R1ϵ = ϵR1 = R1  
R1 ∪ ∅ = ∅ ∪ R1 = R1 <br> 
R1 ∪ R1 = R1  <br>
R1 ∪ R2 = R2 ∪ R1  <br>
R1(R2 ∪ R3) = R1R2 ∪ R1R3  <br>
(R1 ∪ R2)R3 = R1R3 ∪ R2R3  <br>
R1(R2R3) = (R1R2)R3  <br>
∅* = ϵ  <br>
ϵ* = ϵ  <br>
(ϵ ∪ R1)* = R1*  <br>
(ϵ ∪ R1)(ϵ ∪ R1)* = R1*  <br> 
R1*(ϵ ∪ R1) = (ϵ ∪ R1)R1*=R1*  <br>
R1*R2 ∪ R2 = R1*R2  <br>
R1(R2R1)* = (R1R2)*R1  <br>
(R1 ∪ R2)*= (R1*R2)*R1* = (R2*R1)*R2*  <br>

--- 
The image lists closure properties for formal languages. Here is the transcribed content:

**Closure Properties:**
1. Union \((L_1 \cup L_2)\)
2. Concatenation \((L_1 L_2)\)
3. Closure (Kleene Star) \((L^*)\)
4. Complementation \(\overline{L} = \Sigma^* - L\)
5. Intersection \((L_1 \cap L_2) = \overline{\overline{L_1} \cup \overline{L_2}}\)
6. Difference \((L_1 - L_2) = L_1 \cap \overline{L_2}\)
7. Reversal \((L^R)\)
8. Homomorphism
9. Reverse Homomorphism
10. Quotient Operation
11. INIT
12. Substitution
13. Infinite Union