import pytest
from main import process_data
# Тест для проверки корректной обработки данных о мужчинах
def test_process_data_male():
    lines = [
        "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S\n",
        "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',female,38,1,0,PC 17599,71.2833,C85,C\n",
        "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S\n"
    ]
    male_stats, female_stats = process_data(lines)
    assert male_stats['min_fare'] == 7.25
    assert male_stats['max_fare'] == 7.25
    assert male_stats['avg_fare'] == 7.25

# Тест для проверки корректной обработки данных о женщинах
def test_process_data_female():
    lines = [
        "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S\n",
        "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',female,38,1,0,PC 17599,71.2833,C85,C\n",
        "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S\n"
    ]
    male_stats, female_stats = process_data(lines)
    assert female_stats['min_fare'] == 7.925
    assert female_stats['max_fare'] == 71.2833
    assert female_stats['avg_fare'] == 39.60415

# Этот тест проверяет, что функция корректно обрабатывает случаи, когда для некоторых пассажиров отсутствует информация о поле.
def test_process_data_missing_gender():
    lines = [
        "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,S\n",
        "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',,38,1,0,PC 17599,71.2833,C85,C\n",
        "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S\n"
    ]
    male_stats, female_stats = process_data(lines)
    assert male_stats['min_fare'] == 7.25
    assert male_stats['max_fare'] == 7.25
    assert male_stats['avg_fare'] == 7.25
    assert female_stats['min_fare'] == 7.925
    assert female_stats['max_fare'] == 7.925
    assert female_stats['avg_fare'] == 7.925