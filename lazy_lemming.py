# go over the holes
# for each hole, go over cafe
# keep track of distance

def max_distance(num_holes, cafes):

    worst = 0
    dist_list = []

    for hole in range(num_holes):

        for cafe in cafes:

            dist = abs(hole - cafe)
            dist_list.append(dist)

        worst = max(worst, min(dist_list))
        
    print(min(dist_list))
    return worst

print(max_distance(6, [2,5]))