
For Math3315/CSE3365 Project 1:

(1) You do not and should not modify the code that are used for verification, such as 
    the functions constructed with 'def verify()' or 'def verification()'  etc


(2) The driver code below the line "if __name__=='__main__':" should not be touched either. 
    The only exception may be Problem 5, for which you may need to reduce 10**8 to 10**7;
    or, if you are able to construct and implement the fast method, you remove the # sign 
    on the line 
    #FAST_METHOD_DONE=True
    and let the driver code test your fast method.


(3) If these tests are too difficult for your code, you'll need to first construct some
    easier test problems and debug your code so that it can solve the easier test problems.


(4) As mentioned in class, in order not to reveal the solutions in the test scripts, the
    instructor resorted to using random numbers etc and put very few comments on what the test 
    code tried to do.  So, it is normal if you find it hard to understand the test driver code.
    (You do not need to understand these test driver code.)    


(5) When your code runs correctly, it shoudl produce logs similar to those listed below:
    (The numbers may change since many of the tests are constructed using random numbers/signs.)

----------------------------------------------------------------------
Problem 1:

	Congratulations, you have passed the tests for Problem 1!

----------------------------------------------------------------------
Problem 2:

Run test 29,  pass is True
	your min is -26.45020,  np_min is -26.4502
	your id_min=[89, 151],  np id_min=[ 88 150]
	your max is 31.18517,  np_max is 31.18517
	your id_max=[63, 105, 175],  np id_max=[ 62 104 174]

Congratulations, you passed all 30 tests for Problem 2!

----------------------------------------------------------------------
Problem 3:

s=    -/ 20l2M9>5o7z1s1(0t9Y5f7p3B4{8@8e6u4@0(
s=       27\4l5v5o1e8,6]9&6)2T2c3}3{2b7_3?6d
s=    -/ -8|7I1i6z6}7E0z5[2/6c8|9g5D3m1z1^3h6^
s=       -6'9p6E3T2S3*7/8P5f3K5"7=3v0;9_6)9w6Y
s=    -/ -1z0 6@0 4.2:0%8^3&0&4e1q7^7W3l2V0A0F

  Great, you passed 200 tests for Problem 3!


----------------------------------------------------------------------
Problem 4:

    num=-570183663792593105
 revnum=-501395297366381075
    num=598747345136660294
 revnum=492066631543747895

  Congratulations, you have passed all 100 tests for Problem 4.

the reverse of 1234500007890000 is 0000987000054321
Passed
the reverse of -50329320407933661000000 is -00000016633970402392305
Passed
the reverse of 66154332782429707000 is 00070792428723345166
Passed


----------------------------------------------------------------------
Problem 5:

 n1=-32768, pn1=-15;   n2=64, pn2=6
power_of_2 for this test: [-32768, -16384, -8192, -4096, -2048, -1024, -512, -256, -128, -64, -32, -16, -8, -4, -2, -1, 1, 2, 4, 8, 16, 32, 64]
Both end-points are power_of_2 case: Passed!
Left end-point is power_of_2 case: Passed!
Right end-points is power_of_2 case: Passed!
Neither end-points are power_of_2 case: Passed!

====== For all 120 tests,  failcount=0,  total_failcount=0 ======
Congratulations for passing all tests for Problem 5!


----------------------------------------------------------------------
Problem 6:

...
exp( 28.50)=2.3844747848e+12,  your_exp=2.3844747848e+12,  abs_err=9.76562e-04,  rel_err=4.0955035726e-16
exp( 29.00)=3.9313342971e+12,  your_exp=3.9313342971e+12,  abs_err=1.95312e-03,  rel_err=4.9680969675e-16
exp( 29.50)=6.4816744779e+12,  your_exp=6.4816744779e+12,  abs_err=9.76562e-04,  rel_err=1.5066515656e-16

...
exp(-30.00)=9.3576229688e-14  exp1=9.3576229688e-14, exp2=6.1030421638e-06, exp3=-9.7656250000e-04
err1=2.5243548967e-29, err2=6.1030420702e-06, err3=9.7656250009e-04

exp(-28.00)=6.9144001069e-13  exp1=6.9144001069e-13, exp2=-4.9723779009e-06, exp3=2.4414062500e-04
err1=5.0487097934e-28, err2=4.9723785923e-06, err3=2.4414062431e-04

exp(-26.00)=5.1090890281e-12  exp1=5.1090890281e-12, exp2=-3.4866282098e-07, exp3=-3.0517578125e-05
err1=0.0000000000e+00, err2=3.4866793007e-07, err3=3.0517583234e-05
...


----------------------------------------------------------------------
Problem 7:

...

mean = 2600,  deviation=16.2245154965971
xbar=2599.312106268033, xbarv=2599.3121062680334, xbar_diff=-4.547474e-13
sd11=16.27561709458037, sd12=16.27561709452315,  sd1_diff=5.722000651e-11
sd21=16.27561709449084, sd22=16.27561709449084, sd2_diff=0.000000000e+00

Test passed

mean = 2800,  deviation=16.833200530681513
xbar=2800.7461926420265, xbarv=2800.7461926420247, xbar_diff=1.818989e-12
sd11=17.00662931861079, sd12=17.006629318939368,  sd1_diff=-3.285762773e-10
sd21=17.006629318948796, sd22=17.006629318948786, sd2_diff=1.065814104e-14

Test passed

  Total 15 test:  Passed 15
  Congratulations, you passed all tests for Problem 7.

----------------------------------------------------------------------