import time
'''
    USED BFS TO SEARCH PATH
'''

#For four-path
def bfs_four(matrix,start,end):
     V = [0,1]
     queue = []
     visited = set([start])
     queue.append([start])
     while queue:
          path = queue.pop()
          x,y = path[-1]
          if x == end[0] and y == end[1]:
               return path
          for x1, y1 in ((x + 1), y), ((x - 1), y), (x, (y + 1)), (x, (y - 1)):
               if 0 <= x1 < width and 0 <= y1 < length and matrix[x1][y1] in V and (x1, y1) not in visited:
                    queue.append(path + [(x1,y1)])
                    visited.add((x1,y1))
#For eight-path
def bfs_eight(matrix,start,end):
     V = [0, 1]
     queue = []
     visited = set([start])
     queue.append([start])
     while queue:
          path = queue.pop()
          x, y = path[-1]
          if x == end[0] and y == end[1]:
               return path
          for x1, y1 in ((x + 1), y), ((x - 1), y), (x, (y + 1)), (x, (y - 1)), ((x+1),(y+1)), ((x-1),(y+1)), ((x+1),(y-1)), ((x-1),(y-1)):
               if 0 <= x1 < width and 0 <= y1 < length and matrix[x1][y1] in V and (x1, y1) not in visited:
                    queue.append(path + [(x1, y1)])
                    visited.add((x1, y1))
#For m-path
def bfs_m(matrix, start, end):
     V = [0, 1]
     queue = []
     visited = set([start])
     queue.append([start])
     while queue:
          path = queue.pop()
          x, y = path[-1]
          if x == end[0] and y == end[1]:
               return path

          for x1,y1 in ((x + 1), y), ((x - 1), y), (x, (y + 1)), (x, (y - 1)):
               if 0 <= x1 < width and 0 <= y1 < length:
                    if matrix[x1][y1] in V:
                         if (x1, y1) not in visited:
                              queue.append(path + [(x1, y1)])
                              visited.add((x1, y1))
                              break
                    else:
                         for x2, y2 in ((x+1, y + 1), (x-1, y - 1), (x + 1, y-1), (x - 1, y+1)):
                              if 0 <= x2 < width and 0 <= y2 < length and matrix[x2][y2] in V and (
                              x2, y2) not in visited:
                                   queue.append(path + [(x2, y2)])
                                   visited.add((x2, y2))
                                   break

C = [[3,1,2,1],
     [2,2,0,2],
     [1,2,1,1],
     [1,0,1,2]]

B = [[0,1,3,4],
     [3,1,0,2],
     [1,0,2,0],
     [0,1,2,3]]

A= [[0,2,2,3],
     [2,1,0,1],
     [0,3,1,0],
     [1,1,0,4]]

#Ran on Matrix A
length = len(A)
width = len(A[0])

print("matrix \n", A)

x = int(input("Enter start location x ")) #enter x-coordinate of start
y = int(input("Enter start location y ")) #enter y-coordinate of start
start = (x,y)

#To take input from the user
x = int(input("Enter end location x ")) #enter x-coordinate of end
y = int((input("Enter end location y "))) #enter y-coordinate of end
end = (x,y)
type = input("Enter path type: four, eight or m ") #type of path search

if type == 'four':
    time_start = time.process_time() #to note time of start
     path = bfs_four(A,start,end)
     time_end = time.process_time() - time_start #end time
     if path == None:
          print("no path")
     else:
          print("Path using BFS is ",path)
          print("time: ",time_end)
          print("path length ",len(path))
elif type == 'eight':
     time_start = time.process_time()
     path = bfs_eight(A,start,end)
     time_end = time.process_time() - time_start
     if path == None:
          print("no path")
     else:
          print("Path using BFS is ",path)
          print("time: ",time_end)
          print("path length ",len(path))
elif type == 'm':
     time_start = time.process_time()
     path = bfs_m(A,start,end)
     time_end = time.process_time() - time_start
     if path == None:
          print("no path")
     else:
          print("Path using BFS is ",path)
          print("time: ",time_end)
          print("path length ",len(path))















