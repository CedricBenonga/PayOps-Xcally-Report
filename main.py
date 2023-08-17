import pandas

payops_team = [
    "Memory M",
    "Zione B",
    "WalterK",
    "Petronella K",
    "SibongileP",
    "Tsoanelo B",
    "Jane B",
    "Mirriam N",
    "Matshidiso M",
    "MphoM",
    "Lehlomela",
    "Rose K",
    "Denzel M",
    "Penina M",
    "Wina Y",
    "Pontsho H"
]

data = pandas.read_csv("Openchannel By Agent Samuel-iaPq.csv")

for name in payops_team:
    if name in data.Agent.to_list():
        new_data = data[data.Agent == name]
        print(f'{new_data.Agent.to_list()[0]}: {sum(new_data["Total Interactions"].to_list())}')
