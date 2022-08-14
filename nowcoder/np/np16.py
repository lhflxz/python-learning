# https://www.nowcoder.com/practice/66969869634b4142ac371684fcf89764
# NP16 发送offer
offer_list=['Allen','Tom']
for u in offer_list:
    print("%s, you have passed our interview and will soon become a member of our company."%u)
offer_list[1]='Andy'
for u in offer_list:
    print("%s, welcome to join us!"%u)