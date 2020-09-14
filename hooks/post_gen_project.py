import os
import os.path as osp
import subprocess

COOKIECUTTER_REPO_NAME = 'cookiecutter-pypackage'

par_dir_path = osp.normpath(osp.join(osp.abspath(osp.curdir), osp.pardir))
if osp.basename(par_dir_path) == COOKIECUTTER_REPO_NAME:
    # This was most likely called `cookiecutter .`
    cookiecutter_repo_path = par_dir_path
else:
    # This was most likely called as `cookeicutter git@bitbucket.org:geomagical/labtech-wrapper.git`
    # This is the canonical location for the cached cookiecutter template
    cookiecutter_repo_path = osp.join(os.environ['HOME'], '.cookiecutters', COOKIECUTTER_REPO_NAME)

# Obtain Cookiecutter repo path
cookiecutter_hash = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=cookiecutter_repo_path)
cookiecutter_hash = cookiecutter_hash.strip().decode('utf-8')

cookiecutter_uri = subprocess.check_output(["git", "config", "--get", "remote.origin.url"], cwd=cookiecutter_repo_path)
cookiecutter_uri = cookiecutter_uri.strip().decode('uft-8')


#######################
# Setting up git repo #
#######################
shell_cmds = [
        """git init""",
        """git remote add origin git@github.com:{{cookiecutter.github_username}}/{{project_slug}}.git""",
        """git add *""",
        """git add .gitignore""",
        f'''git commit -m "Initial commit from cookiecutter {cookiecutter_uri} commit {cookiecutter_hash}"''',
        ]

for cmd in shell_cmds:
    subprocess.call(cmd, shell=True)


print("=======================================================================")
print("Project setup complete. If you are happy with the setup, run:")
print("        git push origin master")
