from rospy import Rospy



r = Rospy("https://10.1.1.254/", "admin", "rospy")
i = r.log

print(i)
