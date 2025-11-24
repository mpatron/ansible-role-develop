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
