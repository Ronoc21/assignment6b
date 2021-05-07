#Name: Conor Smith
#Date: 04/05/21
#Description: Takes a list of first names, and returns a list that contains only names that start with a K. Adds surname "Kardashian" to each one

#add a space between k name and Kardashian
last_name = "Kardashian"

def add_surname(string_list, target_string):
    """takes a list of names, filters out all names that don't start with K. The ones that do, adds the surname Kardashian"""
    return [i for i in string_list if i[0] == target_string] + [" "] + ["Kardashian"] #couldn't get it to put the space and the Kardashian on each iteration that met the criteria

#add_surname(["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"], 'K')
#print(add_surname(["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"],'K'))
