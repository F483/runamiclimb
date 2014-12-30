# Trainless

# Installation for development

Trainless is made with python/django.

### Dependencies for ubuntu

    # install apt packages
    sudo apt-get -qy install gettext libjpeg-dev libfreetype6-dev

### Project Setup

    # Clone repository
    cd where/you/keep/your/repos
    git clone https://github.com/F483/trainlessmagazine.com
    cd trainlessmagazine.com

    # python virtualenv
    virtualenv -p /usr/bin/python2 env  # create virtualenv
    source env/bin/activate             # activate virtualenv

    # Install python packages
    pip install --upgrade -r packages.txt

    # Setup development database
    python manage.py syncdb

    # Start development server
    python manage.py runserver

