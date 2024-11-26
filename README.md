# Red Scare Assignment

The 3 groups are:
- Birungtongerne:
  Turi∂, Hannah and Frederik
- Okapierne:
  Silas, Jonas and Otto
- Blobfiskene:
  Magnus, Marcus and Kristian

We have a weekly meeting with a TA on Wednesdays at 11.

## How to run

The `find_graphs.py` is used to find all graphs with 500 or more vertices.
Hence this was used to generate the file `all_graphs.txt`.
This should not be necessary to run, since we provided the file with all graphs.
This file can be run as any other python file:

```sh
python find_graphs.py
```

`ALL_graphs.txt` is a text file containing the file names of all graphs inside
the `data/` folder.

`all_graphs.txt` contains all graphs with 500 or more vertices.

To get the csv data of all graphs run on all programs, simply run the shell
script `run_graphs.sh` with the file containing the names of the files of the
graphs which is to be run.
An example of such a command can be seen below:

```sh
./run_graphs.sh all_graphs.txt
```

Make sure the shell script is runnable, but doing something like the following:

```sh
chmod +x run_graphs.sh
```
