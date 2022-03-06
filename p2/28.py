import sys #för att kunna ta input

def get_file_content(file_name): #hämta många lösenord
    #print("IN = ",file_name)
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("Fel")
        sys.exit()

    file_content = infil.readlines()
    #print("OUT = ",file_content)
    return file_content

def main(): #jämför en input med alla kombinationer i p2_comb.txt
    out=get_file_content('p2_comb.txt')
    output=[]
    for line in out:
        output=output+line.split('\n') #ta bort \n i varje rad
    #print(output)

    if len( sys.argv ) > 1:
        word_to_test = sys.argv[1]
        if word_to_test in output:
            print("Olämpligt som lösenord")
    else:
        print("Usage: argv[0] <ord>") # ingen input


main()
