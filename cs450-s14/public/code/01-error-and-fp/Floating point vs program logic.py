
# In[1]:

from time import sleep

x = 0.0

while x != 1.0:
    x += 0.1
    print repr(x)
    
    sleep(0.1)


# Out[1]:

#     0.1
#     0.2
#     0.30000000000000004
#     0.4
#     0.5
#     0.6
#     0.7
#     0.7999999999999999
#     0.8999999999999999
#     0.9999999999999999
#     1.0999999999999999
#     1.2
#     1.3
#     1.4000000000000001
#     1.5000000000000002
#     1.6000000000000003
#     1.7000000000000004
#     1.8000000000000005
#     1.9000000000000006
#     2.0000000000000004
#     2.1000000000000005
#     2.2000000000000006
#     2.3000000000000007
#     2.400000000000001
#     2.500000000000001
#     2.600000000000001
#     2.700000000000001
#     2.800000000000001
#     2.9000000000000012
#     3.0000000000000013
#     3.1000000000000014
#     3.2000000000000015
#     3.3000000000000016
#     3.4000000000000017
#     3.5000000000000018
#     3.600000000000002


    ---------------------------------------------------------------------------
    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-1-83e244af505a> in <module>()
          7     print repr(x)
          8 
    ----> 9     sleep(0.1)
    

    KeyboardInterrupt: 


#     
# 

# In[ ]:


