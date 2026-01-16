from practice_data_define import Record
import json
class FileReader:
    def read_data(self)-> list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    #rewrite
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list: list[Record]=[]

        for line in f.readlines():
            line = line.strip() # delete/n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        
        f.close()
        return record_list
    
class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list: list[Record]=[]
        
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list

if __name__ == '__main__':
    textfile = TextFileReader("/Users/huangchuning/Desktop/python/Day05/data01.txt")
    jsonfile = JsonFileReader("/Users/huangchuning/Desktop/python/Day05/data02.txt")
    list1 = textfile.read_data()
    list2 = jsonfile.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
    

