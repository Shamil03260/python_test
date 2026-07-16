# set() 
# unikal elementler qebul
# mutable
# index yoxdur



# my_set = {10, 2, 3, 3, 4 , 8 , 7, 8, -5}

# print(type(my_set))
# print(my_set)

# my_set.add(9)

# my_set.update([9, 10, 11])

# element yoxdursa xeta verir
# my_set.remove(0)

# element yoxdursa xeta vermir
# my_set.discard(0)

# my_set.pop()

# my_set.clear()


# my_set1 = {1, 2, 5}
# my_set2 = {3, 4, 1, 5}

# print(my_set1.union(my_set2))

# İzah: Ortaq elementləri qaytarır.
# a={1,2,3}
# b={2,3,4}
# print(a.intersection(b))


# İzah: Birinci set-də olub ikinci set-də olmayanları qaytarır.
# a={1,2,3}
# b={2,3}
# print(a.difference(b))





# print(my_set2)



# Dict və Set fərqləri
# Xüsusiyyət	Dict	Set
# Məlumat növü	Açar:Dəyər	Tək element
# Təkrarlanan element	Açar təkrarlanmır	Element təkrarlanmır
# Dəyər saxlayır	✅	❌
# Key var	✅	❌
# Ordered	✅ (Python 3.7+)	❌
# Mutable	✅	✅
# Hash Table	✅	✅
# İndeks	❌	❌
# Nested ola bilər	✅	Məhdud
# JSON-də istifadə	✅	❌
# API-lərdə istifadə	Çox	Az
# Django Model-lərdə	Çox	Nadir