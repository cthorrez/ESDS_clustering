from sklearn.cluster import KMeans, SpectralClustering
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import AffinityPropagation
from sklearn.datasets.samples_generator import make_blobs



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
    data_file = open("kda_50.txt", "r")
    for line in data_file:
        fields = line.split(",")
        data.append([float(fields[1]), float(fields[3]), float(fields[4]), float(fields[4])])
        names.append(fields[0])
        

    
    

    #clus = MeanShift(bin_seeding=True)
    #clus = KMeans(init='k-means++', n_clusters=5, n_init=100)
    clus = SpectralClustering(n_clusters=5,eigen_solver='arpack',affinity= "nearest_neighbors")
    

    clus.fit(data)

    labels = clus.fit_predict(data)

    print len(labels)
    boxes = [[],[],[],[],[]]
    for x in range(len(data)):
        pred = labels[x]
        name = names[x]
        if " " in name:
            name = name[0:name.find("(")]
        boxes[pred].append(name.ljust(10))

    print len(boxes[0]), len(boxes[1]), len(boxes[2]), len(boxes[3]), len(boxes[4])
    sizes = [len(boxes[0]), len(boxes[1]), len(boxes[2]), len(boxes[3]), len(boxes[4])]
    biggest = max(sizes)
    for box in boxes:
        while len(box) < biggest:
            box.append("            ")
            


    for x in range(biggest):
        print boxes[0][x], "|",boxes[1][x],"|", boxes[2][x],"|", boxes[3][x],"|", boxes[4][x]
