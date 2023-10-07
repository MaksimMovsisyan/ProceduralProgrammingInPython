# TODO Найдите количество книг, которое можно разместить на дискете
V_Mb = 1.44
V_bites = V_Mb*1024*1024
NumberOfPagesPerOneBook = 100
NumberOfLinesPerPage = 50
NumberOfSymbolsPerLine = 25
SymbolWeight_bites = 4
WeightOfOneBook_bites = NumberOfPagesPerOneBook*NumberOfLinesPerPage*NumberOfSymbolsPerLine*SymbolWeight_bites
print("Количество книг, помещающихся на дискету:", int(V_bites//WeightOfOneBook_bites))
