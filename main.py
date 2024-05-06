s = 0
fare = 0
averageFare = 0
fareSum = 0
count = 0
listForCells = []
fareBool = True
sex = 'male'
for i in range(0, 2):
    with open("data.csv") as file:
        for line in file:
            if line.count("Sex") == 1:
                continue
            data = line.split(",")
            if data[5] != sex:
                continue
            else:
                if fareBool:
                    minFare = float(data[10])
                    maxFare = float(data[10])
                    fareBool = False
                fare = float(data[10])
                fareSum = fareSum + fare
                count += 1
                if fare < minFare:
                    minFare = fare
                if fare > maxFare:
                    maxFare = fare
        averageFare = fareSum / count

        listForCells.append(averageFare)
        listForCells.append(maxFare)
        listForCells.append(minFare)

        fareBool = True
        print("Средняя цена для " + sex + ": " + str(averageFare) + "\nМаксимальная цена: " + str(maxFare) + "\nМинимальная цена: " + str(minFare))
        sex = 'female'

import matplotlib.pyplot as plt
import streamlit as st

st.image ('titanic.jpg')
st.header ('Данные пассажиров Титаника')
st.write ("Для просмотра данных о стоимости билетов , выберите пункт из списка ")
selected = st.selectbox ('Выберите пол', ['Мужской','Женский'])
if repr(selected) == "'Мужской'":
    pclass = ['Средняя цена', 'Максимальная цена', 'Минимальная цена']
    costs = [listForCells[0], listForCells[1], listForCells[2]]
    fig = plt.figure(figsize=(8, 3))
    sex = 'мужчин'
    plt.xlabel('Значения цен')
else:
    pclass = ['Средняя цена', 'Максимальная цена', 'Минимальная цена']
    costs = [listForCells[3], listForCells[4], listForCells[5]]
    fig = plt.figure(figsize=(8, 3))
    sex = 'женщин'
    plt.xlabel('Значение цен')
data = {'билет': pclass, 'цена':costs}
st.table(data)
plt.bar(pclass, costs)
plt.ylabel('Значение поля: Стоимость')
plt.title('Показания по билету для: ' + sex)
st.pyplot(fig)
