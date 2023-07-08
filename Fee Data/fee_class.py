from dict_class import fee,data
from fee_dict_avg import avg_value
from cube_input import cube

class Fee:
    def fee_details(self):
        fee_detail=fee
        for i, (key,value) in enumerate(fee_detail.items(),start=1):
            print(f'{i}. {key:17s}: {value}')
        avg=avg_value()
        print('Avarage of Fee particulars is :',avg)
    
    def cube_value(self):
        cube(fee=fee)
class Data:
    def data_details(self):
        data_detail=data
        for i, (key,value) in enumerate(data_detail.items(),start=1):
            print(f"{i}. {key.title().replace('_',' '):17s}: {value}")
    
class Main(Fee,Data):
    def show_details(self):
        print('Data Details:')
        self.data_details()
        print('Fee Details:')
        self.fee_details()
        self.cube_value()
        
if __name__ == '__main__':
    main_instance=Main().show_details()

    

    

