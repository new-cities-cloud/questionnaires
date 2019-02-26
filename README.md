# Instructions

1. Clone the repository
```$ git clone https://github.com/new-cities-cloud/project-plans.git questionnaires```

2. To make changes to the questionnaire, edit it directly in YAML. Do not submit CSV files to this repository.

3. To build a CSV file that can be used in Excel or Google sheets:
Edit the yaml_to_csv.py file to point to ```my_questionnaire.yaml```. Then, run:
```$ python3 yaml_to_csv.py```
