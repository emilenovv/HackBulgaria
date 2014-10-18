def reduce_file_path(path):
    path = path.split("/")
    path_copy = path
    print(path_copy)
    for i in range(len(path_copy)):
        if path_copy[i] == '..':
            path.remove(path[i])
            path.remove(path[i - 1])
            
        #if path_copy[i] == '.':
            #print(i)
            #path.remove(path[i])
        print(len(path_copy))
            

reduce_file_path("/srv/www/../htdocs/wtf/..")