import os
import json

import flask
import subprocess

from api.decorators import render_view
from modern_paste import app
from uri.misc import *


@app.route(APIDocumentationInterfaceURI.path, methods=['GET'])
@render_view
def api_documentation_interface():
    """
    Documentation for all publicly exposed API endpoints.
    """
    api_documentation = open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '../templates/misc/api_documentation.json',
    ))
    api_documentation_data = json.loads(api_documentation.read())
    api_documentation.close()
    return 'misc/api_documentation.html', {
        'api_endpoints': api_documentation_data['api_endpoints'],
        'generic_error_responses': api_documentation_data['generic_error_responses'],
    }


@app.route(VersionURI.path, methods=['GET', 'POST'])
def version():
    """
    Show the currently-deployed version of the app.
    """
    branch_name = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True).stdout.replace('\n', '')
    commit_sha = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.replace('\n', '')
    commit_date = subprocess.run(['git', 'log', '-1', '--format=%cd'], capture_output=True, text=True).stdout.replace('\n', '')
    remote_url = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], capture_output=True, text=True).stdout.replace('\n', '')

    version_string = '{branch}\n{sha}\n{date}\n{url}'.format(
        branch=branch_name,
        sha=commit_sha,
        date=commit_date,
        url=remote_url,
    )

    return flask.Response(version_string, mimetype='text/plain')
