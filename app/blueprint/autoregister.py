import os
import importlib
import logging

#//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
#\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//

def blueprint(app, sub_dir=None):

    # Current directory of this file
    logging.info('_______________________________________________')
    logging.info('Registered routes:')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    url_prefix = '/'
    if sub_dir:
        sub_dir = sub_dir.strip('/')
        dir_path = os.path.join(dir_path, sub_dir)
        url_prefix += sub_dir + '/'
    search_blueprint(app, dir_path, url_prefix)
    logging.info('_______________________________________________')

#------------------------------------------------------------------------------------------------------------

def search_blueprint(app, dir_path, url_prefix):

    # Loop into the files of that directory
    for f in sorted(os.listdir(dir_path)):

        # Select file if it is a directory
        blueprint_path = os.path.join(dir_path, f)
        if os.path.isfile(blueprint_path):
            continue

        # Perform a recursive search
        next_url_prefix = '{}{}/'.format(url_prefix, f)
        search_blueprint(app, blueprint_path, next_url_prefix)

        # Find the python file inside the directory with the same name
        blueprint_file = os.path.join(blueprint_path, f + '.py')
        if not os.path.isfile(blueprint_file):
            continue

        # Try to register that blueprint
        register_blueprint(app, f, url_prefix)

#------------------------------------------------------------------------------------------------------------

def register_blueprint(app, route_name, url_prefix):

    module_prefix = url_prefix[:-1].replace('/', '.')
    module_name = '{}{}.{}.{}'.format('blueprint', module_prefix, route_name, route_name)
    module = importlib.import_module(module_name)

    try:
        route = getattr(module, route_name + '_route')
        app.register_blueprint(route, url_prefix=url_prefix + route_name)
        logging.info(f"- {url_prefix}{route_name}")

    except:
        pass # No route found in the module
