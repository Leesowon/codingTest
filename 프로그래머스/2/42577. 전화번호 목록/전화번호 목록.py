# https://mainkey.tistory.com/20

def solution(phone_book):
    answer = True
    
    hash_map = {}
    for nums in phone_book :
        hash_map[nums] = 1
    
    for nums in phone_book :
        arr = ""
        for num in nums :
            arr += num
            
            if arr in hash_map and arr != nums :
                return False
    
    return True