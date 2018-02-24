# fgctech

### Objectives

- Make it easy to archive and find tech


### Requirements

- Multi games
- Easy to use
- No auth
- No duplicates
- Fast

### Stack

- Flask/SQLAlchemy/Graphene(GraphQL)/Postgres
- Vue

### TODOS

##### Before beta:
- Frontend
	- Test create Post 
	- Move queries out of code
- Deployement
	- Iaas
		- Docker (compose)
			- nginx1 -> reverse-proxy
			- nginx2 -> frontend
			- python-alpine-gunicorn -> backend
			- postgres -> db
		- Let's Encrypt/Certbot -> force HTTPS
		- Gandi -> redirect some seemein.gg subdomain
		- AWS/GCE/RamNode/DigitalOcean
	- PaaS
		- Heroku
		- Pythonanywhere(?)

##### Later:

- Finish search 
	- Multiple categories LATER
- Finish Submit 
	- Multiple categories LATER
- Pagination

### Issues

- search code is ugly (multiple ifs, None/[] thing)
- Bulma import is possibly ugly ?