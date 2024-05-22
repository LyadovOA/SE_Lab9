import matplotlib.pyplot as plt
import streamlit as st

def get_group_func(lines):
    male_fares = []
    female_fares = []

    for line in lines:
        data = line.strip().split(",")
        sex = data[5]
        fare_str = data[10].strip()  # Удаляем лишние пробелы
        if fare_str:  # Проверяем, что строка не пустая
            fare = float(fare_str)
            if sex == 'male':
                male_fares.append(fare)
            elif sex == 'female':
                female_fares.append(fare)

    male_avg_fare = sum(male_fares) / len(male_fares) if male_fares else 0
    female_avg_fare = sum(female_fares) / len(female_fares) if female_fares else 0

    male_min_fare = min(male_fares) if male_fares else 0
    female_min_fare = min(female_fares) if female_fares else 0

    male_max_fare = max(male_fares) if male_fares else 0
    female_max_fare = max(female_fares) if female_fares else 0

    AvgFares = {'male_avg_fare': male_avg_fare, 'female_avg_fare': female_avg_fare}
    MinFares = {'male_min_fare': male_min_fare, 'female_min_fare': female_min_fare}
    MaxFares = {'male_max_fare': male_max_fare, 'female_max_fare': female_max_fare}

    return AvgFares, MinFares, MaxFares


with open("data.csv") as file:
    next(file)
    lines = file.readlines()
    AvgFares, MinFares, MaxFares = get_group_func(lines)


def do_var10(lines=None):
    st.image('titanic.jpg')
    st.header('Данные пассажиров Титаника')
    st.write("Для просмотра данных о стоимости билетов , выберите пункт из списка ")
    selected = st.selectbox('Выберите тип стоимости', ['Средняя цена', 'Максимальная цена', 'Минимальная цена'])

    if selected == 'Средняя цена':
        averageFare = [AvgFares['male_avg_fare'], AvgFares['female_avg_fare']]
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
        maxFare = [MaxFares['male_max_fare'], MaxFares['female_max_fare']]
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
        minFare = [MinFares['male_min_fare'], MinFares['female_min_fare']]
        sex = ['Мужчины', 'Женщины']
        data = {'Пол': sex, 'Цена': minFare}
        st.table(data)

        fig = plt.figure(figsize=(10, 5))
        plt.bar(sex, minFare)
        plt.xlabel("Пол")
        plt.ylabel("Цена")
        plt.title("Минимальная стоимость билетов")
        st.pyplot(fig)
do_var10()