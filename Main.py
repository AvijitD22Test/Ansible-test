from os import system
system("ansible-playbook Main.yaml")
system("ansible-playbook Namenode.yaml")
system("ansible-playbook Datanode.yaml")
