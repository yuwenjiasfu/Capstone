# Database

This was the first paper database I built for the project.

At that stage, I had not yet decided how to split the literature into concrete app-checkable rules. Because of that, I collected a wider mix of papers, including papers from different directions, different levels of abstraction, and papers that were useful for building background understanding even if they were not easy to convert into fixed rule items.

Later, this database was mainly used for independent analysis. In practice, that means I would first look through the important code paths of an app, then use my understanding of these papers to manually identify possible problems, risks, and evidence chains.

This database is therefore broader and less structured. It is useful for background understanding, independent reasoning, and manually guided code review.

Main files:

- `paper_catalog.tsv`: paper index for the earlier collection.
- `rule_catalog.txt`: readable text version of the rule catalog.

