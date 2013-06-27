# clear screen
clear

# source the virtual environment
# source venv/bin/activate

# make sure any new requirements have been installed
pip install -r requirements.txt

# clear install info if desired
clear

#if [-f /tmp/test.db ]
#then
    #rm /tmp/test.db
#fi

export DATABASE_URL="sqlite:////tmp/test.db"

# setup database inside of project
python -c "from app import db; db.create_all()"

# run app
python run.py
