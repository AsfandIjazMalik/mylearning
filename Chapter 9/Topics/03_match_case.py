name = 'Asfand Ijaz Malik'

match name:
    
    case 'Asfand':
        print('case 0 is matched and name is:',name)

    case 'Asfand Ijaz Malik':
        print('case 1 is matched and name is:',name)

    case 'Asfand Ijaz':
        print('case 2 is matched and name is:',name)

    case _:
        print('All cases is not match default case is excecuted',name)
