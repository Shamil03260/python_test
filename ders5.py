#  dict() luget
# keys() values()
# tekrar keysleri qebul etmir
# mutable
#  Açarlar hashable olmalıdır int, float, str, bool, bytes , ancaq  data tipler keys ola biler
# index yoxdur


# my_dict = {"ad" : "Nasib",
#            "soyad" : "Nasibov" ,
#            "email": "nasiboffdevfgmail.com"}

# print(my_dict["ad"])
# print(my_dict["soyad"])
# print(my_dict["email"])

# nested
# api_movie = {'adult': False, 'backdrop_path': '/vcrgU0KaNj5mKUCIQSUdiQwTE9y.jpg',
#              'belongs_to_collection': {'id': 1241, 'name': 'Harry Potter Collection',
#             'poster_path': '/eVPs2Y0LyvTLZn6AP5Z6O2rtiGB.jpg', 'backdrop_path': '/4gV0rKUjB1nLUdZB4zIltLvNZZr.jpg'}, 
#              'budget': 250000000, 'genres': [{'id': 13, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}], 
#              'homepage': 'https://www.warnerbros.com/movies/harry-potter-and-deathly-hallows-part-1/', 
#              'id': 12444, 'imdb_id': 'tt0926084', 'original_language': 'en', 
#              'original_title': 'Harry Potter and the Deathly Hallows: Part 1', 
#              'overview': "Harry, Ron and Hermione walk away from their last year at Hogwarts to find and destroy the remaining Horcruxes, putting an end to Voldemort's bid for immortality. But with Harry's beloved Dumbledore dead and Voldemort's unscrupulous Death Eaters on the loose, the world is more dangerous than ever.", 
#              'popularity': 233.894, 'poster_path': '/iGoXIpQb7Pot00EEdwpwPajheZ5.jpg', 
#              'production_companies': [{'id': 174, 
#                 'logo_path': '/IuAlhI9eVC9Z8UQWOIDdWRKSEJ.png', 
#                 'name': 'Warner Bros. Pictures', 'origin_country': 'US'}, 
#             {'id': 437, 'logo_path': '/nu20mtwbEIhUNnQ5NXVhHsNknZj.png', 
#              'name': 'Heyday Films', 'origin_country': 'GB'}], 
#              'production_countries': [{'iso_3166_1': 'GB', 'name': 'United Kingdom'}, 
#                                       {'iso_3166_1': 'US', 'name': 'United States of America'}], 
#              'release_date': '2010-10-06', 'revenue': 954305868, 'runtime': 146, 
#              'spoken_languages': [{'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}], 
#              'status': 'Released', 'tagline': 'One Way… One Fate… One Hero.', 
#              'title': 'Harry Potter and the Deathly Hallows: Part 1', 'video': False, 
#              'vote_average': 7.774, 'vote_count': 16625}

# print(api_movie["belongs_to_collection"]["name"])

# print(api_movie["overview"])


# hashed
# 12345!
# pbkdf2_sha256$1200000$D5i21CYAHWyo1PQej4CMiY$VZ6lcU/PzEP5PqoMin9/rfeOnQlGdmZZ4Hy6zTlnSPU=

# my_dict = {"ad" : "Nasib",
#            "soyad" : "Nasibov" ,
#            "email": "nasiboffdevfgmail.com",
#            "ad" :"test",
#         "emails": "nasiboffdevfgmail.com",

           
#            }

# my_dict["company"] = "test"

# print(my_dict["ada"])
# print(my_dict.get("ada"))

# print(my_dict.keys())

# print(my_dict.values())


# print(my_dict.items())

# my_dict.update({"test":"test"})


# my_dict.pop("email")

# my_dict = {"ad" : "Nasib",
#            "soyad" : "Nasibov" ,
#            "email": "nasiboffdevfgmail.com",
#            "ad" :"test",
#         "emails": "nasiboffdevfgmail.com",

           
#            }




# print(my_dict)


# api_movie = {'adult': False, 'backdrop_path': '/vcrgU0KaNj5mKUCIQSUdiQwTE9y.jpg',
#              'belongs_to_collection': {'id': 1241, 'name': 'Harry Potter Collection',
#             'poster_path': '/eVPs2Y0LyvTLZn6AP5Z6O2rtiGB.jpg', 'backdrop_path': '/4gV0rKUjB1nLUdZB4zIltLvNZZr.jpg'}, 
#              'budget': 250000000, 'genres': [{'id': 13, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}], 
#              'homepage': 'https://www.warnerbros.com/movies/harry-potter-and-deathly-hallows-part-1/', 
#              'id': 12444, 'imdb_id': 'tt0926084', 'original_language': 'en', 
#              'original_title': 'Harry Potter and the Deathly Hallows: Part 1', 
#              'overview': "Harry, Ron and Hermione walk away from their last year at Hogwarts to find and destroy the remaining Horcruxes, putting an end to Voldemort's bid for immortality. But with Harry's beloved Dumbledore dead and Voldemort's unscrupulous Death Eaters on the loose, the world is more dangerous than ever.", 
#              'popularity': 233.894, 'poster_path': '/iGoXIpQb7Pot00EEdwpwPajheZ5.jpg', 
#              'production_companies': [{'id': 174, 
#                 'logo_path': '/IuAlhI9eVC9Z8UQWOIDdWRKSEJ.png', 
#                 'name': 'Warner Bros. Pictures', 'origin_country': 'US'}, 
#             {'id': 437, 'logo_path': '/nu20mtwbEIhUNnQ5NXVhHsNknZj.png', 
#              'name': 'Heyday Films', 'origin_country': 'GB'}], 
#              'production_countries': [{'iso_3166_1': 'GB', 'name': 'United Kingdom'}, 
#                                       {'iso_3166_1': 'US', 'name': 'United States of America'}], 
#              'release_date': '2010-10-06', 'revenue': 954305868, 'runtime': 146, 
#              'spoken_languages': [{'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}], 
#              'status': 'Released', 'tagline': 'One Way… One Fate… One Hero.', 
#              'title': 'Harry Potter and the Deathly Hallows: Part 1', 'video': False, 
#              'vote_average': 7.774, 'vote_count': 16625}


# print(api_movie["genres"][1]["id"])