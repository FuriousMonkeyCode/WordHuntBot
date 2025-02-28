print([(dr, dc) for dr in (-2,-1,1,-2) for dc in (-2, -1, 1 , 2) if not (abs(dr)==abs(dc))]
          )