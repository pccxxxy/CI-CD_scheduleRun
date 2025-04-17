# scheduleRun

## Introduction: 
A CI/CD pipeline template automatically triggers a program to regularlly run at scheduled time.


## Tools used: 
GitHub Actions, YAML, Python


## Use case: 
* Automaticaly run the job at specified time
* Can be modified to fit for the purpose of automated testing - Automatically run the testing scrtipt on the dataset that you would like to test on a regular basis
* Can be integrated in Azure

## How to use
1. Replace the code in main.py with your own test script. Similarlly, change the packages in requirements.txt to the ones your code used.

2.
Change the
```
- cron: '5 * * * *'
```
in actions.yml to your ideal frequency of running the job

For example,
```
- cron: '0 22 * * 1-5' 
```

3. (optional) If you have multiple test scripts or other components need to run sequentially, add them in one by one in the code block under 
```
    steps:
```
in actions.yml.

The way of adding them into YAML code is similar to how the below code is written.

```
     - name: execute py script # run anotherjob.py
        env:
          SOME_SECRET: ${{ secrets.SOME_SECRET }}
        run: python anotherjob.py
```
