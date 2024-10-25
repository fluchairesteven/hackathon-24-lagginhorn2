"Which cantons are being represented by parliamentarians?"

MATCH (person:Person)-[:REPRESENTS]-(canton:Canton)
RETURN person.first_name, person.last_name, canton.name
LIMIT 10

╒═════════════════╤══════════════════╤═══════════╕
│person.first_name│person.last_name  │canton.name│
╞═════════════════╪══════════════════╪═══════════╡
│"Karl"           │"Kümin"           │"Schwyz"   │
├─────────────────┼──────────────────┼───────────┤
│"Dominik"        │"Blunschy"        │"Schwyz"   │
├─────────────────┼──────────────────┼───────────┤
│"Elisabeth"      │"Blunschy-Steiner"│"Schwyz"   │
...

"Which bills did a specific person propose, by status?"

MATCH (person:Person {first_name: 'Balthasar', last_name: 'Glättli'})-[:ACTING_AS]-(bill:Bill)
RETURN bill.title_de, bill.status 
LIMIT 10

╒══════════════════════════════════════════════════════════════════════╤═════════════════════════════════╕
│bill.title_de                                                         │bill.status                      │
╞══════════════════════════════════════════════════════════════════════╪═════════════════════════════════╡
│"Gleichstellung der eingetragenen Partnerschaft und der Ehe im Einbürg│"Resolved"                       │

"Which politicians were born in the last decade of the 20th century?"

MATCH (person:Person) 
WHERE person.date_birth >= date("1990-01-01") AND person.date_birth < date("2000-01-01") 
RETURN person LIMIT 10

╒══════════════════════════════════════════════════════════════════════╕
│person                                                                │
╞══════════════════════════════════════════════════════════════════════╡
│(:Person:Unique Person {date_birth: "1996-12-26",uid: 10830,gender: "f│
...

"Which people have authored which bills?"

MATCH (bill:Bill)-[:ACTING_AS]-(person:Person)
RETURN bill, person
LIMIT 250

╒═══════════════════════════════════════════╤══════════════════════════════════════════════════════════════════════╕
│bill                                       │person                                                                │
╞═══════════════════════════════════════════╪══════════════════════════════════════════════════════════════════════╡
│(:Bill:Interpellation {title_de: "Stopp ...│(:Person:Unique Person {date_birth: "1958-11-26",uid: 3867,gender: "m"│
...

"What is the full text of the bills in parliament?"

MATCH (person:Person)-[:ACTING_AS]-(bill:Bill)-[:CONTAINS]-(text:BillText)
RETURN bill.title_de, bill.status, text.text
LIMIT 10

╒════════════════════════════════════════════╤═══════════╤══════════════════════════════════════════════════════════════════════╕
│bill.title_de                               │bill.status│text.text                                                             │
╞════════════════════════════════════════════╪═══════════╪══════════════════════════════════════════════════════════════════════╡
│"Stopp der Unterwanderung der direkten De...│"Resolved" │"<p>Die Paketvorlage zur Personenfreizügigkeit mit der EU ist der neue│
...
