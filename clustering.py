# Code to cluster professional LoL playres into their roles based on kills, deaths, assists, cs per gae averages
# Clayton Thorrez 2016
from sklearn.cluster import KMeans, SpectralClustering

class Player:
    def __init__(self, kills, deaths, assists, cs):
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.cs = cs

if __name__ == "__main__":

    players = {}
    data = []
    names = []
    data_file = open("kda_200.txt", "r")

    # Build data from file
    for line in data_file:
        fields = line.split(",")
        data.append([float(fields[1]), float(fields[3]), float(fields[4]), float(fields[4])])
        names.append(fields[0])

    # Create and fit model
    clus = SpectralClustering(n_clusters=5,eigen_solver='arpack',affinity= "nearest_neighbors")
    clus.fit(data)
    labels = clus.fit_predict(data)

    # Sort the fitted data into 5 boxes, one for each role
    boxes = [[],[],[],[],[]]
    for x in range(len(data)):
        pred = labels[x]
        name = names[x]
        # names like "Amazing (Maurice Stuckenschneider)" are too long, cut at first space
        if " " in name:
            name = name[0:name.find(" ")+1]
        
        boxes[pred].append(name.ljust(10))

    # Get size of largest cluster so you can pad the others
    sizes = [len(boxes[0]), len(boxes[1]), len(boxes[2]), len(boxes[3]), len(boxes[4])]
    biggest = max(sizes)
    # Pad the other clusters
    for box in boxes:
        while len(box) < biggest:
            box.append("            ")
    # Print the clustering results
    for x in range(biggest):
        print boxes[0][x], "\t",boxes[1][x],"\t", boxes[2][x],"\t", boxes[3][x],"\t", boxes[4][x]
