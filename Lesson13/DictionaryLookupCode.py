"""
Write a program that can get the value associated
with the key "Kenya"
"""

def main():
    my_dict = {
        "Kenya":"Nairobi", 
        "Malaysia":"Kuala Lumpur",
        "Spain":"Madrid"
    }
    value = my_dict['Kenya']
    print(value)

if __name__ == '__main__':
    main()