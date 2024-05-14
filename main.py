import matplotlib.pyplot as plt
import streamlit as st
def process_data(lines):
    male_fares = []
    female_fares = []

    for line in lines:
        data = line.strip().split(",")
        sex = data[5]
        fare = float(data[10])
        if sex == 'male':
            male_fares.append(fare)
        elif sex == 'female':
            female_fares.append(fare)

    male_stats = {
        'min_fare': min(male_fares),
        'max_fare': max(male_fares),
        'avg_fare': sum(male_fares) / len(male_fares) if male_fares else None
    }

    female_stats = {
        'min_fare': min(female_fares),
        'max_fare': max(female_fares),
        'avg_fare': sum(female_fares) / len(female_fares) if female_fares else None
    }

    return male_stats, female_stats

with open("data.csv") as file:
    next(file)
    male_stats, female_stats = process_data(file.readlines())

st.image('titanic.jpg')
st.header('Данные пассажиров Титаника')
st.write("Для просмотра данных о стоимости билетов , выберите пункт из списка ")
selected = st.selectbox('Выберите тип стоимости', ['Средняя цена', 'Максимальная цена', 'Минимальная цена'])

if selected == 'Средняя цена':
    averageFare = [male_stats['avg_fare'], female_stats['avg_fare']]
    sex = ['Мужчины', 'Женщины']
    data = {'Пол': sex, 'Цена': averageFare}
    st.table(data)

    fig = plt.figure(figsize=(10, 5))
    plt.bar(sex, averageFare)
    plt.xlabel("Пол")
    plt.ylabel("Цена")
    plt.title("Средняя стоимость билетов")
    st.pyplot(fig)

elif selected == 'Максимальная цена':
    maxFare = [male_stats['max_fare'], female_stats['max_fare']]
    sex = ['Мужчины', 'Женщины']
    data = {'Пол': sex, 'Цена': maxFare}
    st.table(data)

    fig = plt.figure(figsize=(10, 5))
    plt.bar(sex, maxFare)
    plt.xlabel("Пол")
    plt.ylabel("Цена")
    plt.title("Максимальная стоимость билетов")
    st.pyplot(fig)

elif selected == 'Минимальная цена':
    minFare = [male_stats['min_fare'], female_stats['min_fare']]
    sex = ['Мужчины', 'Женщины']
    data = {'Пол': sex, 'Цена': minFare}
    st.table(data)

    fig = plt.figure(figsize=(10, 5))
    plt.bar(sex, minFare)
    plt.xlabel("Пол")
    plt.ylabel("Цена")
    plt.title("Минимальная стоимость билетов")
    st.pyplot(fig)