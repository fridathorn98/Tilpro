%% Del 1
clear, close all, clc
N = [250000 500000 999992]; %antal element
linsok_osort= [4.5598 9.5566 19.4858]; %Linjärsökning efter nästsista elementet i osorterad lista 
medel= [2.213289128385993 4.2809509653840045 8.646174122120007]; %Linjärsökningen i osorterad lista, genomsnitt
linsok_sort= [8.1555 17.3735 36.3129]; %Linjärsökning efter nästsista elementet i sorterad lista 
mergesort= [155.9309 330.1293 740.489]; %Sortering med mergesort
quicksort= [144.6254 310.5222 690.4224]; %Sortering med quicksort
heapsort= [255.6937 534.8917 1141.9597]; %Sortering med heapsort
binsok= [0.782 2.0061 4.193]; %Binärsökningen i sorterad lista
dic= [0.0001 0.0001 0.0001]; %Sökning i dictionar

A=[N',linsok_osort',linsok_sort',mergesort',quicksort',heapsort',medel',binsok',dic']'; %för tabell
figure(1)
plot(N,linsok_osort), hold on
plot(N,linsok_sort), plot(N,medel)
plot(N,N*0.8e-5,'*'), plot(N,N*1.9e-5,'*'), plot(N,N*3.5e-5,'*')
legend('linsok osort','linsok sort','linsok osort medel','O(N)','O(N)','O(N)')
xlabel('N'), ylabel('time'), title('Linjärsökning')
figure(2)
plot(N,binsok),hold on, plot(N,4e-2*log2(N),'*')
legend('binsok','O(log_2(N))')
xlabel('N'), ylabel('time'), title('Binärsökning')
figure(3)
plot(N,mergesort), hold on
plot(N,quicksort), plot(N,heapsort), plot(N,N.*log(N)*5e-5,'*')
legend('mergesort','quicksort','heapsort','O(N*log(N))')
xlabel('N'), ylabel('time'), title('Sorteringsmetoder')

%% Del 2
k=[1;3;5;7;9;11;13;15;17;19;21;23;25;27;29];
metod1=[0.373593363000000;1.12198907200000;1.96830239300000;2.75906720300000;3.57919855200000;4.73065186500000;5.40181906200000;6.39320874999999;7.21188290300000;7.63137598400000;9.29459459399999;9.70441979799999;10.6259308200000;11.6881280250000;12.5214340080000];
metod2=[7.04412195900000;5.20363485700000;5.07624954000000;5.02554145300000;5.16478657700000;5.24173498800001;5.35491793100000;5.32107413000000;5.13428814700001;4.95661716500000;5.20177221500001;5.23093413100000;5.20492068600001;5.41245779500000;5.02825192300000];
n=258207; log(n)
figure(4)
plot(k,metod1), hold on
plot(k,metod2)
plot(k,ones(size(k))*5,'*'), plot(k,k/2,'*')
legend('metod\_1','metod\_2','O(1)','O(k)')
xlabel('k'), ylabel('time')
