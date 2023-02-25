cd;
cd /home/testsarkari/SarkaariWebsite;
source /home/testsarkari/.virtualenvs/sarkarivigyaapan/bin/activate;
python manage.py dumpdata --indent 4 --exclude=contenttypes --natural-foreign --natural-primary > backup/db_backup.json;
deactivate;
