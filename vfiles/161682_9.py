nums1=input("Enter coordinates of point P (p1, p2,...,qn): ")
nums2=input("Enter coordinates of point Q (q1, q2,..., qn): ")
nums1=nums1.split(",")
nums2=nums2.split(",")
euc=0
for i in range(len(nums1)):
    nums1[i]=int(nums1[i])
for i in range(len(nums2)):
    nums2[i]=int(nums2[i])
for i in range(len(nums1)):
    d=0
    d=(nums1[i]-nums2[i])**2
    euc= euc + d
    
euc=euc**1/2
print("Euclidean distance between point P and point Q: ",euc)