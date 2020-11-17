# Automation Team - Programming Challenge

---

## Instructions

- Fork this repository into your github account. All the work must be done on your forked repository.

- Create a branch from `master` (e.g. `develop`) and do your job on this created branch.

- Code (and document) up

- When finished, create a Pull Request from the created branch to master.

- Send an email to us with the Pull Request link (from your forked repository). These way we can request access to review it and provide you feedback.

---

## The Challenge

- As a business requirement, choose a fashion-related resource. E.g. shoes, pants, shirts, etc...

- Create a RESTful JSON API to expose CRUD (Create/Retrieve/Update/Delete) operations on this resource.

- Create an endpoint to populate data into the model/table using a CSV file. One of the fields of the model/table must pass through a calculation to provide its' value.

- Create a frontend that has a list of all resources.

- Provide a way to us run your application locally with all of its requirements (python and infrastructure-wide)

---

## What will be taken into account

- Your understanding of the requirements

- Your development workflow

- How you architecture the solution using python

- Data sanitization and validation

- API documentation

- Project documentation: the fashion-related resource you chose, how you structured the project and instructions to run your solution locally on a Ubuntu 18.04+ machine (backend and frontend). Feel free to add any information you think relevant beside that.

---

## **You will stand out from the crowd if**:

- You handle the documentation with love and care (attention to details is a HUGE seller here)

- The frontend consumes the API you developed as a backend, and even more if it provides ways to search for contents.

- You use Docker - so we can run you application locally.

- If you deploy the application somewhere remotely where we can interact with it (although we will still try to run it locally ;).

---

## Frameworks, databases and other tooling

On our team we architecture applications with microservices in mind. All new applications (and nowadays the majority of them) are developed on python 3.8+, django or flask, postgres as the database, redis as cache and celery/rabbitmq when we need to deal with processing/flows too long to finish on a request-response cycle. We package our applications as docker images and deploy with kubernetes using helm charts. But feel free to use frameworks, databases and tooling your are the most familiar with.


