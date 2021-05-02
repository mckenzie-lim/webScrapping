import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w", encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    if job is not None:
      temp = list(job.values())
      writer.writerow(temp)
  return 

