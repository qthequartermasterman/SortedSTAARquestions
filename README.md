# SortedSTAARquestions
Scripts that sort questions from released STAAR Exam (Standardized K-12 exams in the State of Texas) sorted by the corresponding TEKS (Standards statement in Texas).

Texas teachers frequently wish to see released STAAR questions relating to the current topic they are teaching, but the Texas Education Agency sorts the questions by Exam year, and not by the content. 
They seperately release a key for each exam that lists the TEKS. 
As far as I can tell, no easily accessible resource sorts questions by their TEKS, which would let teachers avoid the tedious process of checking each year's exam manually.

This script downloads the list of TEKS by question for each Exam, and then compiles a sorted list for each TEKS statement.

## How To Use
Before sorting the questions, first run the `staar_exam_keys/download_all_files.sh` bash script which will automatically download all the Exam Keys from the Texas Education Agency(TEA)'s website.
The exam keys are not included in the repository to avoid copyright issues.

After all exam keys have been downloaded, simply run `STAARquestions.py`, which will create two files `STAAR_QUESTIONS_LIST_CONTENT.csv` and `STAAR_QUESTIONS_LIST_PROCESS.csv`. 
Each file contains the tested Content and Process TEKS, respectively, and the list of exam questions that directly test those TEKS.
Only a list of STAAR questions is given, and the STAAR questions themselves are not included, to avoid copyright issues.

## Disclaimers
1. I only teach Math, Physics, and Computer Science, so I'm not familiar enough with other subjects to identify any oddities in those TEKS or how they are formatted. 
2. I have noticed that the listed Math process TEKS for older exams (~2014) use the older numbering scheme, so they are not formatted properly in the lists.
3. These lists may be incomplete for a variety of reasons, including, but not limited to, 
    - Unavailability of a released exam
    - Unavailability of a key for a released exam
    - Improperly formatted exam keys
    - Incomplete exam keys
    - etc.
