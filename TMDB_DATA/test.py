# import json

# with open('movie_data_credits_test.json', 'r', encoding='UTF8') as f:

#     json_data = json.load(f)
# print(json_data)
# print(type(json_data))
# genreset=set()
# for i in json_data:
#     # print(i.get('genre_ids'))
#     genreset.update(tuple(i.get('genre_ids')))
#     print()
# print(genreset)
aaaa=dict()

sample_dict = {
    '수학':80,
    '국어':90, 
    '영어':95
}
aaaa['fields']=sample_dict
print(aaaa)
# print(sample_dict)
 
# del sample_dict['영어']
# print(sample_dict)
