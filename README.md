# GDS-OA

## How to run this code locally

This is assuming you are on a **windows computer**.

It is preferable to run this code in a python `venv` by running:

```
py -m venv .venv
```

Thereafter, please install the dependencis using (basically only the `pandas` and `openpyxl` library):

```
pip install -r requirements.txt
```

Run the main script using:

```
py main.py
```

It will output the **Rating Thresholds for Task 3 in stdout** and create 2 files: `restaurant_events.csv` and `restaurants.csv` in the **same folder**.

## Deploying Solution on Cloud Services

One possible way to run this script is to upload the data files to an `AWS S3` and then run it with `AWS Lambda` 

Alternatively, the files could be directly downloaded during the `AWS Lambda` run-time.

## Architecture Diagram

![](Architecture%20Diagram.png)