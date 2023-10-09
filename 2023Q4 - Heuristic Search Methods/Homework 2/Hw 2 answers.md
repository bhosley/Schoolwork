(a)
In the hospital-resident matching problem the goal is to match medical residents' choices 
for training probgrams with the hospitals hat offer those programs. Simultaneously we seek to match
the hospitals' preferences with their preferred applicants.

The resulting matches are considered to be stable if the following conditions are met:
1. No candidate is unmatched *or*
2. No candidate is matched to a program when a more prefered program has an opening
3. Some program has an open slot *or*
4. A program would prefer some other applicant over the ones assigned to it


(d)
The military application of this problem is that it is essentially a perfect similitude
for several problems faced by AFPC.
One may consider that during accessions each cadet/candidate will be assigned an AFSC;
in the process of doing so, a CFM (career field manager) will have a target number of 
personell to meet the needs of the Air Force. For a number of reasons it is desirable
to make these assignments with respect to the cadet/candidate's desired field.
Ideally this will be a stable match.

Another iteration of this problem occurs during movement cycles where vulnerable movers are
assigned to open billets. The movers have an opportunity to provide an ordered list of their preferences, and the hiring billet owner can likewise provide a ranked list of preferred candidates.
Once again, it is preferable to maximize the utility of all involved parties.


(b)
This problem was shown to be NP-complete, not by extending a previously determined NP-complete problem,
but through extensions of more basic versions of the problem. 
Gale and Shapley proved that in the case of one-to-one matching a stable output alway exists and
can be found algorithmically, an O(n^2) time. 
One weakness of this algorithm in application is that among all possible stable solutions the one 
produced by the Shapley-Gale algorithm is the best for the candidate and worst for the program.

Gusfield describes a number of extensions of this problem in which stable solutions (if they exist) 
can be found and confirmed in polynomial time, and methods for doing so.

Extensions of interest include cases where there are more open slots than candidates, some candidates occur as pairs (akin to the join spouse program), coalition forming (on either side of selection), and other strategies labelled 'Machiavellian'. 


(c)

In his 249 page book, Gusfield outlines a number of algorithms to solve this problem and its variations. 
Additionally, he provides proofs in which certain aspects of different versions of the problem can or
cannot be ignored.
For example, Gusfield proves that in the case of a coalition, it is impossible for all members of the
coalition to achieve a more preferred result than what they would have gotten otherwise.
For this reason he argues that, assuming rational agents, the problem solver will not need to 
worry about making their algorithm coalition-proof.




-Summary of 2 to 3 journal references (include links in blog) which pertain to the selected problem



(e)
In practical terms it seems fairly likely that stability does not exist, 
what alternatives might you recommend?
Often the answer to this is considered from a game theoretic perspective where
we may wish to maximize overall happiness or minimize the maximum unhappiness. 




References:
