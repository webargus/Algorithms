
"""

    E. Kropniczki
    jan/2020
    Find set intersection and set differences between two sets;
    the purpose of this script is to sync some server-hosted db table content with
    some client table mirror in some client device;
    here are the steps to accomplish this in time complexity O(m+n), where m and n are the sizes of the tables at
    the server and at the client, respectively:
    - read primary keys in ascending order from db table hosted in server;
    - read primary keys in ascending order from db table embedded in client device;
    - take the set difference between the client keys and the server keys as the set to DELETE from the client table, 
      i.e., all the keys that do not belong neither to the intersection of both nor to the server set;
    - take the set difference between the server keys and the client keys as the set to INSERT into the client table,
      i.e., all server-side keys that are not in the client table;
    - take the intersection set between the server keys and the client keys as the set to UPDATE in the client table,
      i.e., all entries that belong simultaneously to both the server and the client table;
    the script avoids nested 'for' loops by reading both sets simutaneously,
    thereby doing the job in O(m+n), instead of (n**2);
    if we want to accomplish the opposite task, i.e., if we wish to sync the server-side table anchored on the client-side
    one (using the server-side table as just a back-up, a mirror), we just use the delete set to INSERT data into 
    the server table and take the insert table to DELETE data from the server table;
"""
import Tools

server = []
client = []
Tools.fill_random_array(server, 10)
Tools.fill_random_array(client, 10)
server.sort()
client.sort()
print("server=", server)
print("client=", client)
print("_"*100)

clt_del = []
update = []
insert = []
i = j = 0
while((i < len(client)) and (j < len(server))):
    if(client[i] < server[j]):
        clt_del.append(client[i])
        i += 1
    elif(client[i] > server[j]):
        insert.append(server[j])
        j += 1
    else:
        update.append(client[i])
        i += 1
        j += 1

if(i < len(client)):
    for k in range(i, len(client)):
        clt_del.append(client[k])
elif(j < len(server)):
    for k in range(j, len(server)):
        insert.append(server[k])

print("delete=", clt_del)
print("insert=", insert)
print("update=", update)

