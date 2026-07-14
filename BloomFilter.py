from BitHash import BitHash
from BitVector import BitVector

class BloomFilter(object):
    
    def __bitsNeeded(self, numKeys, numHashes, maxFalsePositive):
        n = numKeys
        d = numHashes
        p = maxFalsePositive
        # equation B
        self.__phi = (1 - (p ** (1/d)))
        # equation D
        N = int(((d) // (1 - (self.__phi ** (1/n)))))
        return N
        
    
    
   
    def __init__(self, numKeys, numHashes, maxFalsePositive):
        self.__numKeys = numKeys
        self.__numHashes = numHashes
        self.__maxFalsePositive = maxFalsePositive
        # Keep track of the number of bits set
        self.__bitsSet = 0
        # get the size from bitsNeeded
        self.__size = self.__bitsNeeded(numKeys, numHashes, maxFalsePositive) 
        # use __bitsNeeded to figure out how big of a BitVector will be needed
        self.__bv = BitVector(size = self.__size)
    
    
    def insert(self, key):
        # Hash the word according to each hash function and set it in the bitvector
        for i in range(1, self.__numHashes+1):
            index = BitHash(key, i) % self.__size
            # Increment the amount of bits set
            if self.__bv[index] == 0: self.__bitsSet = +1
            self.__bv[index] = 1
    
   
    def find(self, key):
        count = 0
        # Hash the word by each hash function and check if that bit is set
        for i in range(1, self.__numHashes+1):
            index = BitHash(key, i) % self.__size
            if self.__bv[index] == 0:
                return False
        return True
            
            
    
    def falsePositiveRate(self):
        phi = (( 1- self.__numHashes / self.__size) **self.__numKeys)
        p = ((1-phi) ** self.__numHashes)
        return p
        
       
    
    def numBitsSet(self):
        return self.__bitsSet     

       

def __main():
    numKeys = 100000
    numHashes = 4
    maxFalse = .05
    
    # create the Bloom Filter
    b = BloomFilter(numKeys, numHashes, maxFalse)
    
    
    
    # read the first numKeys words from the file and insert them 
    fin = open("wordlist.txt")
    count = 0
    while count < numKeys:
        line = fin.readline()
        b.insert(line)
        count += 1
    
    #Close the input file.
    fin.close()
    

    fp = b.falsePositiveRate()
    print("False Positive rate:", fp)
    
    
    fin = open("wordlist.txt")
    count = 0
    total = 0
    while count < numKeys:
        line = fin.readline()
        if b.find(line) is False:
            total += 1
        count += 1
    print("Missing:", total)
    
     
    
   
    total2 = 0
    while count < numKeys*2:
        line = fin.readline()
        if b.find(line) is True:
            total2 += 1              
        count += 1
    
    fin.close()
            
        
        
        
    
    
    print("Actual False Positive Rate:", total2 / numKeys)
    
if __name__ == '__main__':
    __main()       

