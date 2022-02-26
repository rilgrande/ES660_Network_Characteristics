# ES660_Network_Characteristics

Number of nodes: 1000
Number of links: 2991
Average Degree: 5.982
See code output for (node, degree) pairs

There were several network layout algorithms available, some are clearer than others:
Fruchterman Reingold, Circular, Random, Spectral, and Spring

All algorithms are included in this program, and the user can select which plot they would like to see.

The network density (the ratio of actual edges in the network to all possible edges in the network) is 0.005987987987987988, which is relatively low. A network density of 1 would mean that all possible edges are present in a perfectly connected network. The low density in this example can be attributed to most nodes having a low degree. The nodes of this network do not have directions, so this network is undirected. The average degree in this network is 5.982, meaning each node has an average 5.982 links originating from it. There are some nodes with many more links than average, for example one node has a degree of 98 and another node has a degree of 90.

From the network drawings, this high degree is reflected with the apparent crowding of links which all connect to a common node that has a higher degree than average. There are 1,000 total nodes in this network, so one node connecting to approximately 100 nodes in a couple of cases will produce a proportionally large number of links in the drawing. In the circular drawing, for example, if there are nodes with degrees 98, 90, and 55, it is logical that the black links cross so densely. Those three nodes do not necessarily connect to the same nodes, so it is theoretically possible that these three nodes connect to approximately 250 other unique nodes.
