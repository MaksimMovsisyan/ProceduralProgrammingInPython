# TODO Напишите функцию find_common_participants
def find_common_participants(group1_, group2_, separator = ','):
    list1_, list2_ = group1_.split(separator), group2_.split(separator)
    set1_, set2_ = set(list1_), set(list2_)
    return sorted(set1_.intersection(set2_))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')