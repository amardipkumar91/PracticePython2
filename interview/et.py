import glob
class Pipeline(object):
    def __init__(self, dir):
        self.dir = dir

    def get_all_file(self):
        file_list = glob.glob(self.dir+'*.txt')
        return file_list

    def processfile(self, f):
        file_obj = open(f, 'r')
        data = file_obj.readlines()
        index_pos = []
        for i in data:
            split_data = i.split(',')
            l_index = []
            for index, m in enumerate(split_data):
                
                if not m or m == "''" or m == 'NA':
                    l_index.append(index)
            index_pos.append(l_index)
        return index_pos
    def write_output(self, index_pos):
        result = []
        for index, i in enumerate(index_pos):
            result.append({index: i})
        print (result)
    
if __name__ == '__main__':
    obj = Pipeline('/Users/amardip.kumar/Documents/PracticePython/interview/')
    file_list = obj.get_all_file()
    for f in file_list:
        index_pos = obj.processfile(f)
        obj.write_output(index_pos)


