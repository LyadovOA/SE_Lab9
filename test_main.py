import pytest
from main import get_group_func
# №1 Тест для проверки корректного подсчета средней цены для мужчин и женщин
def test_avgFares():
    lines = [
        "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S\n",
        "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',female,38,1,0,PC 17599,71.2833,C85,C\n",
        "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S\n"
    ]
    avg_fares, min_fares, max_fares = get_group_func(lines)
    assert avg_fares == {'male_avg_fare': 7.25, 'female_avg_fare': 39.60415}

# №2 Тест для проверки корректного подсчета максимальной цены для мужчин и женщин
def test_maxFares():
    lines = [
        "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S\n",
        "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',female,38,1,0,PC 17599,71.2833,C85,C\n",
        "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S\n"
    ]
    avg_fares, min_fares, max_fares = get_group_func(lines)
    assert max_fares == {'male_max_fare': 7.25, 'female_max_fare': 71.2833}

# №3 Тест для проверки корректного подсчета минимальной цены для мужчин и женщин

def test_minFares():
    lines = [
        "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S\n",
        "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',female,38,1,0,PC 17599,71.2833,C85,C\n",
        "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S\n"
    ]
    avg_fares, min_fares, max_fares = get_group_func(lines)
    assert min_fares == {'male_min_fare': 7.25, 'female_min_fare': 7.925}

# №4 Тест для данных с отсутствием информации о ценах билетов для мужчин

def test_noFires():
    lines = ["1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,,S\n",
        "2,1,1,'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',female,38,1,0,PC 17599,71.2833,C85,C\n",
        "3,1,3,'Heikkinen, Miss. Laina',female,26,0,0,STON/O2. 3101282,7.925,,S\n"
    ]
    avg_fares, min_fares, max_fares = get_group_func(lines)
    assert min_fares == {'female_min_fare': 7.925, 'male_min_fare': 0}

# №5 Тест с полным отсутствием информации
def test_noData():
    lines = []
    avg_fares, min_fares, max_fares = get_group_func(lines)
    assert avg_fares  == {'male_avg_fare': 0, 'female_avg_fare': 0}