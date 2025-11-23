https://docs.ansible.com/projects/molecule/getting-started-playbooks/#linux-container-testing-scenario


molecule test --scenario-name runinpodman --report --command-borders

# Test the complete lifecycle
molecule test --scenario-name runinpodman --report --command-borders

# Run specific actions
molecule create --scenario-name runinpodman --report --command-borders
molecule converge --scenario-name runinpodman --report --command-borders
molecule verify --scenario-name runinpodman --report --command-borders
