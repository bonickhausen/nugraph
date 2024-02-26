import csv
import plotly.graph_objects as go

list = []

filename = 'nubank-2024-03.csv'

class expense:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.category = ""


class group:
    def __init__(self, name, value):
        self.name = name
        self.value = value

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count) == 0:
            print(f'Column names are {", ".join(row)}')
            print("\n")
        else:
            expName = row[2].lower()
            expPrice = row[3]
            newExp = expense(expName, expPrice)
            list.append(newExp)
        line_count += 1

cleanList = [value for value in list if value.name != "pagamento recebido"]

for item in cleanList:
    if any(x in item.name for x in ("amazon", "mercadolivre", "nivel6", "melimais")):
        item.category = "amazon/mercadolivre"
    elif any(x in item.name for x in ("top", "metro")):
        item.category = "metro"
    elif any(x in item.name for x in ("ifood", "ifd")):
        item.category = "ifood"
    elif any(x in item.name for x in ("zeenow", "petlove", "cobasi")):
        item.category = "pet"
    elif any(x in item.name for x in ("restaur", "japasfood", "pastel", "lanchonete", "mani", "paes", "sabor", "outback", "starbucks", "frutaria", "raposo tavares point", "cafe", "churrasc", "retro explorer e comer", "ibotirama")):
        item.category = "restaurante"
    elif any(x in item.name for x in ("thais", "minimart", "carrefour")):
        item.category = "mercado"
    elif any(x in item.name for x in ("uber", "99")):
        item.category = "uber"
    elif any(x in item.name for x in ("quintoandar", "quintoand")):
        item.category = "aluguel"
    elif any(x in item.name for x in ("iof", "iof de")):
        item.category = "iof"
    elif any(x in item.name for x in ("madeira", "madesa")):
        item.category = "moveis"
    elif any(x in item.name for x in ("droga", "farma")):
        item.category = "farmacia"
    elif any(x in item.name for x in ("contabi", "contabilizei", "companyhero")):
        item.category = "empresa/impostos"
    elif any(x in item.name for x in ("steam", "microsoft", "cinemark", "ingresso", "pbkids", "pichau")):
        item.category = "lazer"
    elif any(x in item.name for x in ("fluke", "sami", "vivo", "ramnode", "celular")):
        item.category = "essenciais"
    elif any(x in item.name for x in ("spotify", "hbomax")):
        item.category = "assinaturas"
    elif any(x in item.name for x in ("dess", "cabele")):
        item.category = "estetica"
    elif any(x in item.name for x in ("github", "gitlab")):
        item.category = "trabalho"
    else:
        item.category = "???"


print("The next items could not be assigned to any category. Please check them.\n")
for item in list:
    if item.category == "???":
        print(item.name)


print("\n\nDisplaying pie graph:\n")

groups = []

for item in list:
    hasMatchingGroup = False
    for g in groups:
        if g.name == item.category:
            hasMatchingGroup = True
            price = float(item.price)
            g.value += price
    if not hasMatchingGroup:
        if float(item.price) > 0:
            groups.append(group(item.category, float(item.price)))


# for g in groups:
#     print(g.name + " ||| " + str(g.value))

values = [x.value for x in groups]
names = [x.name for x in groups]

fig = go.Figure(data=[go.Pie(labels=names, values=values)])
fig.update_layout(title_text="Gastos - " + filename)
fig.show()
