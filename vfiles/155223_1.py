XF= input("Enter a series of numbers separated by commas: ")
XR = XF.split(",")
XMI = min(XR)
XM = max(XR)


XM = int(XM)
XMI = int(XMI)
nums0 = int(XR[0])
nums1 = int(XR[1])
nums2 = int(XR[2])
nums3 = int(XR[3])
nums4 = int(XR[4])

d = (nums0 - XMI)/(XM-XMI),(nums1 - XMI)/(XM-XMI),(nums2 - XMI)/(XM-XMI),(nums3 - XMI)/(XM-XMI),(nums4 - XMI)/(XM-XMI)

print("Normalized values:\n",d[0],"\n",d[1],"\n",d[2],"\n",d[3],"\n",d[4],sep = "")



# print(QS1)


# min_x = min(nums)
# max_x = max(nums)
# print(min_x,max_x)
# r0 = nums[0] - min_x
# r1 = nums[1] - min_x
# r2 = nums[2] - min_x
# r3 = nums[3] - min_x