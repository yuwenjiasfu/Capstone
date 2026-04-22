# Database Main

This is the structured database I use for the later stage of the project.

Unlike the earlier `database/` folder, this one was built after I decided that I needed a rule-based workflow. I selected papers in a more balanced way across different types of problems and different analysis layers so that the material would be easier to summarize, compare, and reuse during app-by-app analysis.

The key difference is that all rules in this database are meant to be used in the next step of my workflow. I use them together with my own Python search code to look for keywords, likely code locations, and possible evidence paths inside each app. After that, I manually review the search hits and build the final evidence chains.

So in short:

- `database/` is the earlier, broader literature collection that I mainly used for independent analysis and manual reasoning.
- `database_main/` is the later, more structured rule database that I use for keyword search, rule-based filtering, and evidence-oriented app review.

Main files:

- `README.md`: short overview of this database.
- `rule_catalog.txt`: readable text version of the rule database.

Folders:

- `snapshots/`: local HTML copies for source checking when needed.
- `papers/`: local PDF papers.



