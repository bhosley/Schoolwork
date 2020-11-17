//Your Neo4j code goes here

CREATE (GA:Person { name: "Gomez Addams", born: 1966 }),
    (MA:Person { name: "Morticia Addams", born: 1972 }),
    (PA:Person { name: "Pugsley Addams", born: 1992}),
    (WA:Person { name: "Wednesday Addams", born: 1993}),
    (FeA:Person { name: "Fester Addams", born: 1964 }),
    (FaA:Person { name: "Father Addams", born: 1922}),
    (TA:Person { name: "That Addams", born: 1920}),
    (IA:Person { name: "Itt Addams", born: 1947})

CREATE
    (GA)-[:SPOUSE {MARRIED: 1991}]->(MA),   (MA)-[:SPOUSE {MARRIED: 1991}]->(GA),
    (MA)-[:PARENT {TYPE: "Mother"}]->(PA),    (PA)-[:CHILD {TYPE: "Son"}]->(MA),
    (GA)-[:PARENT {TYPE: "Father"}]->(PA),    (PA)-[:CHILD {TYPE: "Son"}]->(GA),
    (MA)-[:PARENT {TYPE: "Mother"}]->(WA),    (WA)-[:CHILD {TYPE: "Daughter"}]->(MA),
    (GA)-[:PARENT {TYPE: "Father"}]->(WA),    (WA)-[:CHILD {TYPE: "Daughter"}]->(GA),
    (FaA)-[:PARENT {TYPE: "Father"}]->(GA),   (GA)-[:CHILD {TYPE: "Son"}]->(FaA),
    (FaA)-[:PARENT {TYPE: "Father"}]->(FeA),  (FeA)-[:CHILD {TYPE: "Son"}]->(FaA),
    (TA)-[:PARENT {TYPE: "Father"}]->(IA),    (IA)-[:CHILD {TYPE: "Son"}]->(TA),
    (PA)-[:SIBLING {TYPE: "Brother"}]->(WA),  (WA)-[:SIBLING {TYPE: "Sister"}]->(PA),
    (GA)-[:SIBLING {TYPE: "Brother"}]->(FeA), (FeA)-[:SIBLING {TYPE: "Brother"}]->(GA),
    (FaA)-[:SIBLING {TYPE: "Brother"}]->(TA), (TA)-[:SIBLING {TYPE: "Brother"}]->(FaA)
;