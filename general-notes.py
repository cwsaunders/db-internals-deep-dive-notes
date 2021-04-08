'''
Databases are modular systems with multiple parts:
1. A transport layer accepting requests
2. Query processor determining the most efficient way to run queries
3. Execution engine carrying out operations
4. Storage engine



The storage engine is a software component of the DMS (database management system) responsible for storing, retrieving, and managing data in memory and and on disk.
It is designed to capture a persistent long term memory of each node.


mySQL storage systems -- InnoDB, MyISAM, and multiple others.
MongoDB storage systems -- WiredTiger, MMAPv1 (now deprecated)


How to compare DBs:
1. Schema and record sizes
2. Number of clients
3. Types of quieries
4. Rates of the read and write queries
5. Expected changes in any of these variables

Questions:
1. Does the DB support requires queries
2. Is the DB able to handle the amount of data
3. How many read/write operations can a single node handle
4. how many nodes should the system have
5. How can we expand the cluster given the expected growth rates
6. what is the maintenance process

Popular benchmarking tool:
https://databass.dev/links/104 (YCSB -- Yahoo! Cloud Serving Benchmarking)







'''