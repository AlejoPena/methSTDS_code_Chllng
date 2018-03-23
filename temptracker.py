
class TempTracker:
    def __init__(self):
        self.temperatures = []
        self.tempRecords = 0
        self.max = None
        self.min = None ##max assumed
        self.mean = None  ## using only two arbitrary decimals places to report mean
        self.temp_sum= 0


    def insert(self, record):
        #insert function will keep track of min max and get_mean
        #for simplicity and optimal calculation of parameters


        #only imput data acepted is integers
        if type(record) != type(1):
            print ("different type than int")
            return

        ##input data has to be in range 0..110
        if record < 0 or record > 110:
            print ("input out of range")
            return

        self.temperatures.append(record)
        self.tempRecords+=1
        self.temp_sum+=record
        if self.max is None or self.max < record:
            self.max = record
        if self.min is None or self.min > record:
            self.min = record
        self.mean = format(self.temp_sum / self.tempRecords, '.2f')
        return

        ##returns maximum valid temperature record imputed
    def get_max(self):
        print("something")
        return self.max

        ##returns minimum valid temperature record imputed
    def get_min(self):
        return self.min

        ##returns mean  temperature from valid imputed records
    def get_mean(self):
        return self.mean


        ##Function used for testing pourposes
    def printall(self):
        lista=[self.tempRecords, self.min, self.max]
        return lista
