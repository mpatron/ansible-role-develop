# Run in podman

[https://docs.ansible.com/projects/molecule/getting-started-playbooks/#linux-container-testing-scenario](https://docs.ansible.com/projects/molecule/getting-started-playbooks/#linux-container-testing-scenario)

~~~bash
# Test the complete lifecycle
clear && molecule reset && molecule test --scenario-name runinpodman --report --command-borders

# Run specific actions
molecule create --scenario-name runinpodman --report --command-borders
molecule converge --scenario-name runinpodman --report --command-borders
molecule verify --scenario-name runinpodman --report --command-borders
~~~

On doit voir ceci

~~~bash
WARNING  Driver podman does not provide a schema.
WARNING  Driver podman does not provide a schema.
INFO     default ➜ discovery: scenario test matrix: 
INFO     default ➜ prerun: Performing prerun with role_name_check=0...
INFO     default ➜ reset: Removing /home/mickael/.ansible/tmp/molecule.d0Go.default
WARNING  Driver podman does not provide a schema.
WARNING  Driver podman does not provide a schema.
INFO     runinpodman ➜ discovery: scenario test matrix: dependency, destroy, create, converge, idempotence, verify, cleanup, destroy
INFO     runinpodman ➜ prerun: Performing prerun with role_name_check=0...
INFO     runinpodman ➜ dependency: Executing
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-galaxy install
  │   --role-file /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/requirements.yml
  │ 
  │ Starting galaxy collection install process
  │ Nothing to do. All requested collections are already installed. If you want to reinstall them, consider using `--force`.
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
INFO     runinpodman ➜ dependency: Dependency completed successfully.
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-galaxy collection
  │   install
  │   --requirements-file /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/requirements.yml
  │ 
  │ Starting galaxy collection install process
  │ Nothing to do. All requested collections are already installed. If you want to reinstall them, consider using `--force`.
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
INFO     runinpodman ➜ dependency: Dependency completed successfully.
INFO     runinpodman ➜ dependency: Executed: Successful
INFO     runinpodman ➜ destroy: Executing
INFO     Sanity checks: 'podman'
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-playbook --inventory /home/mickael/.ansible/tmp/molecule.d0Go.runinpodman/inventory
  │   --skip-tags molecule-notest,notest
  │   --inventory=inventory/ /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/destroy.yml
  │ 
  │ 
  │ PLAY [Destroy container instances] *********************************************
  │ 
  │ TASK [Get info for all containers] *********************************************
  │ ok: [localhost] => (item=molecule-fedora)
  │ 
  │ TASK [Kill container if running] ***********************************************
  │ skipping: [localhost] => (item=molecule-fedora) 
  │ skipping: [localhost]
  │ 
  │ PLAY RECAP *********************************************************************
  │ localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
  │ 
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
INFO     runinpodman ➜ destroy: Executed: Successful
INFO     runinpodman ➜ create: Executing
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-playbook --inventory /home/mickael/.ansible/tmp/molecule.d0Go.runinpodman/inventory
  │   --skip-tags molecule-notest,notest
  │   --inventory=inventory/ /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/create.yml
  │ 
  │ 
  │ PLAY [Create container instances] **********************************************
  │ 
  │ TASK [Create containers from inventory] ****************************************
  │ changed: [localhost] => (item=molecule-fedora)
  │ 
  │ TASK [Verify containers are running in error state] ****************************
  │ skipping: [localhost] => (item=molecule-fedora) 
  │ skipping: [localhost]
  │ 
  │ TASK [Wait for containers to be ready] *****************************************
  │ [WARNING]: Reset is not implemented for this connection
  │ ok: [localhost -> molecule-fedora] => (item=molecule-fedora)
  │ 
  │ PLAY RECAP *********************************************************************
  │ localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
  │ 
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
INFO     runinpodman ➜ create: Executed: Successful
INFO     runinpodman ➜ converge: Executing
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-playbook --inventory /home/mickael/.ansible/tmp/molecule.d0Go.runinpodman/inventory
  │   --skip-tags molecule-notest,notest
  │   --inventory=inventory/ /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/converge.yml
  │ 
  │ 
  │ PLAY [Converge] ****************************************************************
  │ 
  │ TASK [Gathering Facts] *********************************************************
  │ ok: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ skipping: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ included: /home/mickael/Documents/ansible-role-develop/tasks/setup-Fedora.yml for molecule-fedora
  │ 
  │ TASK [mpatron.ansible_role_develop : == Fedora == Ensure all packages are installed] ***
  │ ok: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : == Fedora == Déinstaller vim-enhanced pour le remplacer par vim sur Fedora] ***
  │ changed: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : == Fedora == Installer vim] ***************
  │ changed: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ skipping: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ skipping: [molecule-fedora]
  │ 
  │ TASK [Read OS release information] *********************************************
  │ ok: [molecule-fedora]
  │ 
  │ TASK [Write OS info to file] ***************************************************
  │ changed: [molecule-fedora]
  │ 
  │ PLAY RECAP *********************************************************************
  │ molecule-fedora            : ok=7    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
  │ 
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
INFO     runinpodman ➜ converge: Executed: Successful
INFO     runinpodman ➜ idempotence: Executing
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-playbook --inventory /home/mickael/.ansible/tmp/molecule.d0Go.runinpodman/inventory
  │   --skip-tags molecule-notest,notest,molecule-idempotence-notest
  │   --inventory=inventory/ /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/converge.yml
  │ 
  │ 
  │ PLAY [Converge] ****************************************************************
  │ 
  │ TASK [Gathering Facts] *********************************************************
  │ ok: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ skipping: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ included: /home/mickael/Documents/ansible-role-develop/tasks/setup-Fedora.yml for molecule-fedora
  │ 
  │ TASK [mpatron.ansible_role_develop : == Fedora == Ensure all packages are installed] ***
  │ ok: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : == Fedora == Déinstaller vim-enhanced pour le remplacer par vim sur Fedora] ***
  │ changed: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : == Fedora == Installer vim] ***************
  │ changed: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ skipping: [molecule-fedora]
  │ 
  │ TASK [mpatron.ansible_role_develop : ansible.builtin.include_tasks] ************
  │ skipping: [molecule-fedora]
  │ 
  │ TASK [Read OS release information] *********************************************
  │ ok: [molecule-fedora]
  │ 
  │ TASK [Write OS info to file] ***************************************************
  │ ok: [molecule-fedora]
  │ 
  │ PLAY RECAP *********************************************************************
  │ molecule-fedora            : ok=7    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
  │ 
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
CRITICAL Idempotence test failed because of the following tasks:
*  => mpatron.ansible_role_develop : == Fedora == Déinstaller vim-enhanced pour le remplacer par vim sur Fedora
*  => mpatron.ansible_role_develop : == Fedora == Installer vim
ERROR    runinpodman ➜ idempotence: Executed: Failed
WARNING  runinpodman ➜ idempotence: An error occurred during the test sequence action: 'idempotence'. Cleaning up.
INFO     runinpodman ➜ cleanup: Executing
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-playbook --inventory /home/mickael/.ansible/tmp/molecule.d0Go.runinpodman/inventory
  │   --skip-tags molecule-notest,notest
  │   --inventory=inventory/ /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/cleanup.yml
  │ 
  │ 
  │ PLAY [Cleanup container instances] *********************************************
  │ 
  │ TASK [Check if container is running] *******************************************
  │ ok: [molecule-fedora -> localhost]
  │ 
  │ TASK [Remove temporary files from running containers] **************************
  │ changed: [molecule-fedora]
  │ 
  │ PLAY RECAP *********************************************************************
  │ molecule-fedora            : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  │ 
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
INFO     runinpodman ➜ cleanup: Executed: Successful
INFO     runinpodman ➜ destroy: Executing
  ┌──────────────────────────────────────────────────────────────────────────────────
  │ ansible-playbook --inventory /home/mickael/.ansible/tmp/molecule.d0Go.runinpodman/inventory
  │   --skip-tags molecule-notest,notest
  │   --inventory=inventory/ /home/mickael/Documents/ansible-role-develop/molecule/runinpodman/destroy.yml
  │ 
  │ 
  │ PLAY [Destroy container instances] *********************************************
  │ 
  │ TASK [Get info for all containers] *********************************************
  │ ok: [localhost] => (item=molecule-fedora)
  │ 
  │ TASK [Kill container if running] ***********************************************
  │ changed: [localhost] => (item=molecule-fedora)
  │ 
  │ PLAY RECAP *********************************************************************
  │ localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  │ 
  └─ Return code: 0 ─────────────────────────────────────────────────────────────────
INFO     runinpodman ➜ destroy: Executed: Successful
INFO     runinpodman ➜ scenario: Pruning extra files from scenario ephemeral directory
ERROR    Idempotence test failed because of the following tasks:
*  => mpatron.ansible_role_develop : == Fedora == Déinstaller vim-enhanced pour le remplacer par vim sur Fedora
*  => mpatron.ansible_role_develop : == Fedora == Installer vim
INFO     Molecule executed 1 scenario (1 successful)

DETAILS                                                                        
runinpodman ➜ dependency: Executed: Successful
runinpodman ➜ destroy: Executed: Successful
runinpodman ➜ create: Executed: Successful
runinpodman ➜ converge: Executed: Successful
runinpodman ➜ idempotence: Executed: Successful
runinpodman ➜ cleanup: Executed: Successful
runinpodman ➜ destroy: Executed: Successful

SCENARIO RECAP                                                                 
runinpodman               : actions=7  successful=6  disabled=0  skipped=0  missing=0  failed=0
~~~
