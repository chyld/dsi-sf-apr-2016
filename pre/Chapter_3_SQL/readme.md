# Chapter 3: SQL
<br>
## Instructions
In this chapter you will be using SQL to answer the questions in the assignment.txt using the data provided.  Please fill in the `assignment.txt` with your own answers.  Each answer should be the SQL query you wrote, and the result it returned.



## The Data To Use
This directory contains New York State's
[nursing home weekly bed census](https://health.data.ny.gov/Health/Nursing-Home-Weekly-Bed-Census-Beginning-2009/uhyy-xp9s?)
in a few different formats.

* `beds.csv` is a comma-delimited file
* `beds.json` is JSON
* `beds.tsv` is tab-delimeted
* `beds.sqlite` is a SQLite3 database.

(The first two of these came directly from the data portal,
and we converted the CSV to the other two formats.)

## Assignment
Choose a nursing home ("Facility"), and subset the data by that nursing home.  Answer the following using SQL.  

**Fill your answers in the provided assignment.txt file.**

* The count of how many censuses were reported
* The earliest census date
* The latest census date
* The ten census dates with the highest number of available beds for that nursing home
* The ten census dates with the lowest number of available beds for that nursing home

<br>

# If you are new to SQL...
Structured Query Language (SQL) is used to interact with data stored in
relational databases.

There are many relational databases (PostgreSQL, MySQL, etc.) but they all share
SQL as a query language. We'll be using SQLite.

## Install SQLite
If you are running Mac or GNU/Linux, you probably already have SQLite3 installed.
Try running it in the terminal.

```
sqlite3
```

If it's not installed, check your package manager; it might be called "sqlite" or "sqlite3".

If you're on Windows, download the Windows binaries from [here](http://www.sqlite.org/download.html).

More directions are [here](http://mislav.uniqpath.com/rails/install-sqlite3/).

## Basic commands

```sh
$ sqlite3 beds.sqlite
```

Display headers
```
>> .header on
```
A single SQLite3 database can contain many tables. List the tables.
```
>> .tables
```
Show a table schema
```
>> .schema beds
```
Get the whole table. (This will take a while.)

```sql
SELECT * FROM beds;
```

Get the first ten records.

```sql
SELECT * FROM beds LIMIT 10;
```

Count how many records there are.

```sql
SELECT count(*) FROM beds;
```

Count how many rows are XXX

```sql
SELECT count(*) FROM beds WHERE Facility_ID = 28321;
```

Order

```sql
SELECT * FROM beds ORDER BY Bed_Census_Date;
```
<br>

## Additonal Resources
* I highly recommend [SQL Zoo](http://sqlzoo.net/wiki/Main_Page): tutorials 1-7  

* [Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/).



## Extra credit

* Do the project exclusively with UNIX shell commands
