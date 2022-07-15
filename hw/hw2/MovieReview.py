import csv

class RawMovieReview:
    def __init__(self, file_name: str = 'samples.csv'):
        self._file_name = file_name
        self.__samples = []
        with open(self._file_name, 'r') as fd:
            reader = csv.reader(fd)
            for index, sample in enumerate(reader):
                if index == 0:
                    continue
                self.__samples.append((sample[0], sample[1], int(sample[2])))
    def __getitem__(self, index):
        return self.__samples[index]
    def __len__(self):
        return len(self.__samples)

class MovieReview(RawMovieReview):
    def __init__(self, score_threadhold : int, file_name: str = 'samples.csv'):
        self.__score_threadhold = score_threadhold
        super().__init__(file_name)
    
    def __getitem__(self, index):
        sample = super().__getitem__(index)
        return (sample[1].strip(),sample[2] >= self.__score_threadhold)