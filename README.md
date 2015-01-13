# Universal Multi-game AIE Membership Interface (UMAMI)

This is the rewrite of the membership management tool for the Alea Iacta Est gaming community.  The focus of the development is to improve reusability and minimize unnecessary complexity.

The current plan for the project is to develop a web-based tool that is easy to deploy on a PaaS infrastructure and which incorporates the following functional modules.

- Django core user and group management.
- Synchronization of the user and group data with an external LDAP service.
- Support for membership applications for MMORPGs that use character or account membership models.
- An extensible platform for the development of other guild management tools.
 
## Installation

1. Clone the Git repository.

```shell
git clone git@github.com:AIE-Guild/umami.git
cd umami
```

2. Configure the virtualenv environment.

```shell
virtualenv env
source env/bin/activate
pip install -r 
requirements.txt
```

## Running the test server locally

1. Copy the default environment configuration script.

```shell
cp umami/scripts/local_config.sh.example local_config.sh
```

2. Edit `local_config.sh`.

3. Configure the environment.

```shell
source local_config.sh
```

4. Initialize the database.

```shell
python manage.py syncdb
```

5. Start the test server.

```shell
foreman start
```



