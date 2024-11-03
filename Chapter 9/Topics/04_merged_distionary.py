contry_code1 = {
    'Pak' : 50200,
    'US' : 100,
    'Uk' : 600
}
contry_code2 = {
    'Ireland' : 502,
    'Ban' : 102,
    'NZ' : 605
}

merge = contry_code1 | contry_code2
print (merge)
print(type(merge))