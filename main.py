import pandas

payops_team = [
    "Memory M",
    "Tsoanelo B",
    "Jane B",
    "MphoM",
    "Lehlomela",
    "Rose K",
    "Denzel M",
    "Wina Y",
    "Zione B",
    "WalterK",
    "Petronella K",
    "SibongileP",
    "Matshidiso M",
    "Mirriam N",
    "Penina M",
    "Pontsho H"
]

try:
    data = pandas.read_csv("Openchannel By Agent Samuel-iaPq.csv")
    # data.to_csv
except FileNotFoundError:
    print('Sorry! File name not found!\nPlease check the "File Name"(it needs to be the same with the one in the '
          'database) or \n"File Format"(only csv accepted) and retry!')

try:
    for name in payops_team:
        if name in data.Agent.to_list():
            new_data = data[data.Agent == name]
            print(f'{new_data.Agent.to_list()[0]}: {sum(new_data["Total Interactions"].to_list())}')
except NameError:
    pass
