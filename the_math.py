import math

class Converter():
    def __init__(self):
        self.num = 0
        self.den = 0
        self.the_Qs_Integer = 0
        self.first_mapping=0
        self.second_mapping_step = 0

        self.nat=0


    def set_rational_number(self, num,den):
        self.num=num
        self.den=den

    def convert_Q_to_N(self):
        #this function takes a positive rational number and maps it to a natural number

        #step one  - separate out the integer portion and minimize the numerator
        self.the_Qs_Integer=math.floor(self.num/self.den)
        self.num=int(self.num-self.the_Qs_Integer*self.den)

        #step two - reduce the fraction if possible
        the_gcd = math.gcd(self.den, self.num)
        self.den = int(self.den/the_gcd)
        self.num = int(self.num/the_gcd)

        #step three - map the fraction to a natural number
        #there will be a second mapping after this.
        self.first_mapping = 0

        if self.num>0:

            all_reduced_fractions=[]
            for one_value in range(1,self.den):
                all_reduced_fractions.append({'den':one_value, 'nums':self.reduced_fractions(one_value)})

            for one_den in all_reduced_fractions:
                self.first_mapping += len(one_den['nums'])

            self.first_mapping += self.reduced_fractions(self.den).index(self.num)

        #step four - the final mapping
        #this is done by dividing the natural numbers in to a countable number of sequences
        #the first sequence is the odd numbers
        #the second sequence is multiples of 4 plus 2
        #the third sequence is multples of 8 plus 4

        #and so on
        #we choose the sequence based on the integer portion of the number
        #if the integer portion is zero use the first sequence
        #if the integer portion is one use the second sequence
        #and so on

        #we then map the value from the first mapping above to the coresponding sequence
        
        self.second_mapping_starting_point = 2**self.the_Qs_Integer
        self.second_mapping_step = 2**(self.the_Qs_Integer+1)

        self.nat = self.second_mapping_starting_point + self.second_mapping_step*self.first_mapping

        pass

    def reduced_fractions(self, this_den):

        return_value = [1]

        for index in range(2,this_den):
            if math.gcd(index,this_den)==1:
                return_value.append(index)

        return return_value
    
    def set_natural_number(self, nat):
        self.nat=nat

    def convert_N_to_Q(self):
        
        #step 1 - find the integer portion

        self.the_Qs_Integer = 0
        if self.nat==0:

            return
        
        temp_nat = self.nat
        
        while self.is_even(temp_nat):
            temp_nat /=2
            self.the_Qs_Integer += 1

        self.second_mapping_starting_point = 2**self.the_Qs_Integer
        self.second_mapping_step = 2**(self.the_Qs_Integer+1)

        self.first_mapping = int((self.nat-self.second_mapping_starting_point)/self.second_mapping_step)

        if self.first_mapping==0:
            self.num = self.the_Qs_Integer
            self.den = 1
        else:
            
            self.den=2
            
            reduced_fractions_sum = 1
            this_reduced_fraction_list = self.reduced_fractions(self.den)
            while self.first_mapping > reduced_fractions_sum:
                self.den += 1
                this_reduced_fraction_list = self.reduced_fractions(self.den)
                reduced_fractions_sum += len(this_reduced_fraction_list)
                

            reduced_fractions_sum -= len(this_reduced_fraction_list)
            self.num = this_reduced_fraction_list[self.first_mapping-reduced_fractions_sum-1] + self.the_Qs_Integer *self.den

            pass
        
    def is_even(self,value):

        x=math.floor(value/2)
        return value == x*2
            
        

    def get_answer(self):
        
        return {'final_N': str(self.nat),
                'final_den': str(self.den),
                'final_num':str(self.num),
                'first_mapping':str(self.first_mapping),
                'second_mapping_start':str(self.second_mapping_starting_point),
                'second_mapping_step':str(self.second_mapping_step)}