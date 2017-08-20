pip3 uninstall -y django_toolbox &&

# Packing new version
cd package/django_toolbox/ &&
python3 setup.py sdist &&

#Install new version
pip3 install --user dist/django_toolbox-0.0.3.tar.gz &&
cd ../../
