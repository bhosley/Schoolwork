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

Generically, extensions of interest include cases where there are more open slots than candidates, some candidates occur as pairs (akin to the join spouse program), coalition forming (on either side of selection), and other strategies labelled 'Machiavellian'. 


(b)
Gale and Shapley proved that in the case of one-to-one matching a stable output alway exists and
can be found algorithmically, an O(n^2) time, thus is NP. 
One weakness of this algorithm in application is that among all possible stable solutions the one 
produced by the Shapley-Gale algorithm is the best for the candidate and worst for the program.

Four variants of the problem; the marriage problem, the roommate problem, the intern assignment problem, and the intern assignment problem with couples; are shown to be NP complete by Ronn, et al. in their 1990 paper.
In these proofs Ronn, et al. demonstrates that these four problems can be represented as
instances of the 3SAT problem.

In his 249 page book, Gusfield outlines a number of algorithms to solve this problem and its variations. 
Additionally, he provides proofs in which certain aspects of different versions of the problem can or
cannot be ignored. For example, Gusfield proves that in the case of a one-to-one problem, 
it is impossible to form a coalition where all members of the
coalition achieve a more preferred result than what they would have gotten otherwise.
For this reason he argues that, assuming rational agents, the problem solver will not need to 
worry about making their algorithm coalition-proof.

This is expanded upon by Sotomayor (1998) where they consider a many-to-many situation.
The objective in their paper was to examine subset stability.
Subsets are defined as stable if none of its members can benefit from defection
(or being transferred) to another subset, and thus represents a coalition proof result.

A result that I found particularly interesting in the Sotomayor paper is that 'setwise stability
is strictly stronger than pairwise stability'. By that they mean that if a setwise stable 
solution exists there will always exist a pairwise stable solution, 
and even a many-to-one solution if the version of the problem allows for that.


(e)
In practical terms it seems fairly likely that stability does not exist, 
what alternatives might you recommend?
Often the answer to this is considered from a game theoretic perspective where
we may wish to maximize overall happiness or minimize the maximum unhappiness. 




References:
