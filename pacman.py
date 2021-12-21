def bfs(edges,goal):
    



def movegen(edges,m,n,goal,bdd):  
    if bdd==0 :
        #bfs
        print("bfs")
        path = bfs(edges,goal)


    elif bdd==1:
        #dfs
        print("dije")
    else:
        #dfid
        print("soije")
    
















bdd= int(input())
m= 11

graph_input= []
for i in range(m):
    graph_input.append(list(input()))
print(len(graph_input[0]),len(graph_input[1]))

n=len(graph_input[0])

edges= {
    (0,0):[1,0]

}




for i in range(0,m-1):
    for j in range(0,n):
        templist= []
        if(graph_input[i][j]=='*'):
            goal= (i,j)
        if(graph_input[i][j]==' '):
            if(i<n-1):
                if(graph_input[i+1][j]==' '):
                    templist.append((i+1,j))
            if(i>0):
                if(graph_input[i-1][j]==' '):
                    templist.append((i-1,j))
            if(j<n-1):
                if(graph_input[i][j+1]==' '):
                    templist.append((i,j+1))
            if(j>0):
                if(graph_input[i][j-1]==' '):
                    templist.append((i,j-1))
            
        edges[(i,j)]= templist
       
print(edges[(3,4)],goal)




current_position=[0,0]



    
