# Universal Multi-game AIE Membership Interface (UMAMI)

This is the rewrite of the membership management tool for the Alea Iacta Est gaming community.  The focus of the development is to improve reusability and minimize unnecessary complexity.

The current plan for the project is to develop a web-based tool that is easy to deploy on a PaaS infrastructure and which incorporates the following functional modules.

- Django core user and group management.
- Synchronization of the user and group data with an external LDAP service.
- Support for membership applications for MMORPGs that use character or account membership models.
- An extensible platform for the development of other guild management tools.
 
## Installation

- Clone the Git repository.

```shell
git clone git@github.com:AIE-Guild/umami.git
cd umami
```

- Configure the virtualenv environment.

```shell
virtualenv env
source env/bin/activate
pip install -r 
requirements.txt
```

## Running the test server locally

- Copy the default environment configuration script.

```shell
cp umami/scripts/local_config.sh.example local_config.sh
```

- Edit `local_config.sh`.

- Configure the environment.

```shell
source local_config.sh
```

- Initialize the database.

```shell
python manage.py syncdb
```

- Start the test server.

```shell
foreman start
```



